"""Internalize MVP 1 — The Human Linker. FastAPI backend for the semantic knowledge graph."""

import logging
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path
from typing import Literal
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
    """Strict semantic edge ontology from .cursorrules."""

    SUMMARIZES = "SUMMARIZES"
    CONTAINS = "CONTAINS"
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    CAUSES = "CAUSES"
    REQUIRES = "REQUIRES"
    EXAMPLE_OF = "EXAMPLE_OF"
    FOLLOWS = "FOLLOWS"


RELATIONSHIP_AXES: dict[str, list[RelationshipType]] = {
    "Hierarchy": [RelationshipType.SUMMARIZES, RelationshipType.CONTAINS],
    "Evaluation": [RelationshipType.SUPPORTS, RelationshipType.CONTRADICTS],
    "Logical": [RelationshipType.CAUSES, RelationshipType.REQUIRES, RelationshipType.EXAMPLE_OF],
    "Narrative": [RelationshipType.FOLLOWS],
}

ALLOWED_RELATIONSHIP_TYPES: frozenset[str] = frozenset(t.value for t in RelationshipType)

DensityLevel = Literal[1, 2, 3]


class NodeCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    density_level: DensityLevel
    significance: float = Field(default=1.0, gt=0)


class NodeResponse(BaseModel):
    id: str
    title: str
    density_level: int


class NodeCreateResponse(BaseModel):
    status: str = "success"
    node_id: str
    title: str
    density_level: int


class EdgeCreate(BaseModel):
    source_id: str = Field(..., min_length=1)
    target_id: str = Field(..., min_length=1)
    relationship_type: RelationshipType
    strength: float = Field(default=1.0, gt=0)


class EdgeCreateResponse(BaseModel):
    status: str = "success"
    connection: str
    source_id: str
    target_id: str
    strength: float


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
        content: $content,
        density_level: $density_level,
        significance: $significance,
        created_at: timestamp()
    })
    RETURN n.id AS id, n.title AS title, n.density_level AS density_level
    """
    try:
        record = _run_write(
            query,
            id=node_id,
            title=node.title,
            content=node.content,
            density_level=node.density_level,
            significance=node.significance,
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

    return NodeCreateResponse(
        node_id=record["id"],
        title=record["title"],
        density_level=record["density_level"],
    )


@app.get("/api/nodes", response_model=list[NodeResponse])
def list_knowledge_nodes():
    """List all Concept nodes (for the Human Linker dropdown)."""
    query = """
    MATCH (n:Concept)
    RETURN n.id AS id, n.title AS title, n.density_level AS density_level
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
            density_level=r["density_level"],
        )
        for r in records
    ]


@app.post("/api/edges", response_model=EdgeCreateResponse, status_code=status.HTTP_201_CREATED)
def create_semantic_edge(edge: EdgeCreate):
    """Create a typed semantic edge between two existing Concept nodes."""
    rel_type = edge.relationship_type.value

    if rel_type not in ALLOWED_RELATIONSHIP_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid relationship type. Must be one of {sorted(ALLOWED_RELATIONSHIP_TYPES)}",
        )

    # rel_type is validated by Enum; safe to interpolate into Cypher.
    query = f"""
    MATCH (a:Concept {{id: $source_id}})
    MATCH (b:Concept {{id: $target_id}})
    CREATE (a)-[r:{rel_type} {{strength: $strength}}]->(b)
    RETURN type(r) AS link_type, r.strength AS strength
    """
    try:
        record = _run_write(
            query,
            source_id=edge.source_id,
            target_id=edge.target_id,
            strength=edge.strength,
        )
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
        strength=record["strength"],
    )


@app.get("/api/ontology/relationship-types")
def get_relationship_types():
    """Return allowed edge types grouped by axis for frontend dropdowns."""
    return {
        "allowed_types": sorted(ALLOWED_RELATIONSHIP_TYPES),
        "axes": {
            axis: [t.value for t in types]
            for axis, types in RELATIONSHIP_AXES.items()
        },
    }
