"""Internalize MVP 1 — The Human Linker. FastAPI backend for the semantic knowledge graph."""

import logging
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from neo4j import Driver, GraphDatabase
from neo4j.exceptions import GqlError
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    neo4j_uri: str = "bolt://127.0.0.1:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"


class RelationshipType(str, Enum):
    """Strict semantic edge ontology from the Internalize pitch deck."""

    SUMMARY_EXPANSION = "SUMMARY_EXPANSION"
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    AGREES_WITH = "AGREES_WITH"
    CAUSE_REQUIRE = "CAUSE_REQUIRE"
    TYPE_EXAMPLE = "TYPE_EXAMPLE"


ALLOWED_RELATIONSHIP_TYPES: frozenset[str] = frozenset(t.value for t in RelationshipType)


class NodeCreate(BaseModel):
    title: str = Field(..., min_length=1)
    excerpt: str = ""
    summary: str = Field(..., min_length=1)
    source_metadata: str = ""


class NodeResponse(BaseModel):
    id: str
    title: str
    excerpt: str
    summary: str
    source_metadata: str
    created_at: int


class NodeCreateResponse(BaseModel):
    status: str = "success"
    node_id: str
    title: str


class EdgeCreate(BaseModel):
    source_id: str = Field(..., min_length=1)
    target_id: str = Field(..., min_length=1)
    relationship_type: RelationshipType


class EdgeCreateResponse(BaseModel):
    status: str = "success"
    connection: str
    source_id: str
    target_id: str


class HealthResponse(BaseModel):
    status: str
    neo4j: str


logger = logging.getLogger(__name__)

settings = Settings()
BASE_DIR = Path(__file__).resolve().parent


def get_driver() -> Driver:
    return GraphDatabase.driver(
        settings.neo4j_uri,
        auth=(settings.neo4j_user, settings.neo4j_password),
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    driver = get_driver()
    app.state.db_driver = driver
    app.state.neo4j_connected = False
    try:
        driver.verify_connectivity()
        app.state.neo4j_connected = True
        logger.info("Connected to Neo4j at %s", settings.neo4j_uri)
    except GqlError as exc:
        logger.warning(
            "Neo4j unavailable at %s — API will start but data endpoints return 503 until "
            "Neo4j Desktop is running. (%s)",
            settings.neo4j_uri,
            exc,
        )
    yield
    driver.close()


app = FastAPI(
    title="Internalize Backend",
    description="MVP 1: The Human Linker — semantic knowledge graph API",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _require_neo4j() -> Driver:
    driver: Driver = app.state.db_driver
    try:
        driver.verify_connectivity()
        app.state.neo4j_connected = True
    except GqlError as exc:
        app.state.neo4j_connected = False
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Neo4j is unreachable. Start your database in Neo4j Desktop, "
                f"then confirm NEO4J_URI ({settings.neo4j_uri}) and credentials in .env."
            ),
        ) from exc
    return driver


def _run_write(query: str, **params):
    driver = _require_neo4j()
    with driver.session() as session:
        return session.execute_write(lambda tx: tx.run(query, **params).single())


@app.get("/")
def serve_input_pane():
    """Serve the Human Linker input pane."""
    index_path = BASE_DIR / "index.html"
    if not index_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="index.html not found")
    return FileResponse(index_path)


@app.get("/health", response_model=HealthResponse)
def health_check():
    try:
        driver: Driver = app.state.db_driver
        driver.verify_connectivity()
        app.state.neo4j_connected = True
        return HealthResponse(status="ok", neo4j="connected")
    except GqlError:
        app.state.neo4j_connected = False
        return HealthResponse(status="degraded", neo4j="unreachable")


@app.post("/api/nodes", response_model=NodeCreateResponse, status_code=status.HTTP_201_CREATED)
def create_knowledge_node(node: NodeCreate):
    """Create a Concept node with a generated UUID."""
    node_id = str(uuid4())
    query = """
    CREATE (n:Concept {
        id: $id,
        title: $title,
        excerpt: $excerpt,
        summary: $summary,
        source_metadata: $source_metadata,
        created_at: timestamp()
    })
    RETURN n.id AS id, n.title AS title
    """
    try:
        record = _run_write(
            query,
            id=node_id,
            title=node.title,
            excerpt=node.excerpt,
            summary=node.summary,
            source_metadata=node.source_metadata,
        )
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create node",
        )

    return NodeCreateResponse(node_id=record["id"], title=record["title"])


@app.get("/api/nodes", response_model=list[NodeResponse])
def list_knowledge_nodes():
    """List all Concept nodes (for the Human Linker dropdown)."""
    query = """
    MATCH (n:Concept)
    RETURN n.id AS id,
           n.title AS title,
           n.excerpt AS excerpt,
           n.summary AS summary,
           coalesce(n.source_metadata, "") AS source_metadata,
           n.created_at AS created_at
    ORDER BY n.created_at DESC
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            records = session.run(query).data()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    return [
        NodeResponse(
            id=r["id"],
            title=r["title"],
            excerpt=r.get("excerpt") or "",
            summary=r["summary"],
            source_metadata=r.get("source_metadata") or "",
            created_at=r["created_at"],
        )
        for r in records
    ]


@app.post("/api/edges", response_model=EdgeCreateResponse, status_code=status.HTTP_201_CREATED)
def create_semantic_edge(edge: EdgeCreate):
    """Create a typed semantic edge between two existing Concept nodes."""
    rel_type = edge.relationship_type.value

    # rel_type is validated by Enum; safe to interpolate into Cypher.
    query = f"""
    MATCH (a:Concept {{id: $source_id}})
    MATCH (b:Concept {{id: $target_id}})
    CREATE (a)-[r:{rel_type}]->(b)
    RETURN type(r) AS link_type
    """
    try:
        record = _run_write(query, source_id=edge.source_id, target_id=edge.target_id)
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source or target node not found",
        )

    return EdgeCreateResponse(
        connection=record["link_type"],
        source_id=edge.source_id,
        target_id=edge.target_id,
    )


@app.get("/api/ontology/relationship-types")
def get_relationship_types():
    """Return allowed edge types for frontend dropdowns."""
    return {
        "allowed_types": sorted(ALLOWED_RELATIONSHIP_TYPES),
        "descriptions": {
            RelationshipType.SUMMARY_EXPANSION: "Vertical axis: drill down from concept to raw evidence",
            RelationshipType.SUPPORTS: "Evaluation axis: agreement or reinforcing evidence (+)",
            RelationshipType.CONTRADICTS: "Evaluation axis: conflicting theories (-)",
            RelationshipType.AGREES_WITH: "Evaluation axis: identical concepts (=)",
            RelationshipType.CAUSE_REQUIRE: "Logical axis: functional dependencies",
            RelationshipType.TYPE_EXAMPLE: "Logical axis: instantiation of a category (+Ex)",
        },
    }
