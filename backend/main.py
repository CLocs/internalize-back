"""Internalize MVP 1 — The Human Linker. FastAPI backend for the semantic knowledge graph."""

import json
import logging
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path
from typing import Any, Literal, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from neo4j import Driver, GraphDatabase
from neo4j.exceptions import GqlError
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent / ".env"),
        env_file_encoding="utf-8",
    )

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
    DEFINITION_OF = "DEFINITION_OF"
    FOLLOWS = "FOLLOWS"
    REFERENCES = "REFERENCES"


RELATIONSHIP_AXES: dict[str, list[RelationshipType]] = {
    "Hierarchy": [RelationshipType.SUMMARIZES, RelationshipType.CONTAINS],
    "Evaluation": [RelationshipType.SUPPORTS, RelationshipType.CONTRADICTS],
    "Logical": [
        RelationshipType.CAUSES,
        RelationshipType.REQUIRES,
        RelationshipType.EXAMPLE_OF,
        RelationshipType.DEFINITION_OF,
    ],
    "Narrative": [RelationshipType.FOLLOWS, RelationshipType.REFERENCES],
}

ALLOWED_RELATIONSHIP_TYPES: frozenset[str] = frozenset(t.value for t in RelationshipType)

DensityLevel = Literal[1, 2, 3, 4, 5]
NodeType = Literal[
    "Concept",
    "Document",
    "Book",
    "Article",
    "Transcript",
    "Synthesis",
    "Whiteboard",
    "WorkspaceSession",
]

SOURCE_NODE_PREDICATE = (
    "n.density_level IN [3, 4] OR "
    "coalesce(n.node_type, 'Concept') IN "
    "['Document', 'Book', 'Article', 'Transcript', 'Synthesis']"
)


class NodeCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    density_level: DensityLevel
    significance: float = Field(default=1.0, gt=0)
    origin: str = "human"
    node_type: NodeType = "Concept"
    blocks: list[dict[str, Any]] | None = None
    start_offset: Optional[int] = Field(default=None, ge=0)
    end_offset: Optional[int] = Field(default=None, ge=0)


class NodeResponse(BaseModel):
    id: str
    title: str
    density_level: int
    origin: str = "human"
    node_type: str = "Concept"
    content: str | None = None
    created_at: str | None = None


class SourceDocumentResponse(BaseModel):
    id: str
    title: str
    density_level: int
    node_type: str = "Concept"
    origin: str = "human"


class NodeCreateResponse(BaseModel):
    status: str = "success"
    node_id: str
    title: str
    density_level: int


class NodeUpdate(BaseModel):
    density_level: Optional[DensityLevel] = None
    title: Optional[str] = Field(default=None, min_length=1)
    content: Optional[str] = Field(default=None, min_length=1)
    blocks: list[dict[str, Any]] | None = None
    node_type: Optional[str] = None
    start_offset: Optional[int] = Field(default=None, ge=0)
    end_offset: Optional[int] = Field(default=None, ge=0)


class NodePinUpdate(BaseModel):
    pinned: bool


class NodePinResponse(BaseModel):
    status: str = "success"
    id: str
    pinned: bool


class EdgeCreate(BaseModel):
    source_id: str = Field(..., min_length=1)
    target_id: str = Field(..., min_length=1)
    relationship_type: RelationshipType
    strength: float = Field(default=1.0, gt=0)
    origin: str = "human"


class EdgeCreateResponse(BaseModel):
    status: str = "success"
    connection: str
    source_id: str
    target_id: str
    strength: float


class HealthResponse(BaseModel):
    status: str
    neo4j: str


class HierarchyNodeResponse(BaseModel):
    id: str
    title: str
    content: str
    density_level: int
    origin: str = "human"


class DocumentNodeResponse(BaseModel):
    id: str
    title: str
    content: str
    density_level: int
    origin: str = "human"
    node_type: str = "Concept"
    blocks: list[dict[str, Any]] | None = None
    pinned: bool = False
    start_offset: int | None = None
    end_offset: int | None = None


class DocumentSummaryResponse(DocumentNodeResponse):
    excerpt_id: str | None = None


class SummaryEdgeResponse(BaseModel):
    source_id: str
    target_id: str


class DocumentCanvasResponse(BaseModel):
    source: DocumentNodeResponse
    document_text: str
    excerpts: list[DocumentNodeResponse]
    summaries: list[DocumentSummaryResponse]
    summary_edges: list[SummaryEdgeResponse]


logger = logging.getLogger(__name__)

settings = Settings()
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"


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


def _upsert_concept_node(
    *,
    node_id: str,
    title: str,
    content: str,
    density_level: int,
    significance: float,
    origin: str,
    node_type: str = "Concept",
    start_offset: int | None = None,
    end_offset: int | None = None,
) -> dict:
    driver = _require_neo4j()

    find_query = """
    MATCH (n:Concept)
    WHERE n.title = $title
      AND n.content = $content
      AND n.density_level = $density_level
      AND coalesce(n.start_offset, -1) = coalesce($start_offset, -1)
      AND coalesce(n.end_offset, -1) = coalesce($end_offset, -1)
    RETURN n.id AS id, n.title AS title, n.density_level AS density_level
    LIMIT 1
    """
    create_query = """
    CREATE (n:Concept {
        id: $id,
        title: $title,
        content: $content,
        density_level: $density_level,
        significance: $significance,
        origin: $origin,
        node_type: $node_type,
        start_offset: $start_offset,
        end_offset: $end_offset,
        created_at: timestamp()
    })
    RETURN n.id AS id, n.title AS title, n.density_level AS density_level
    """

    def _tx(tx):
        existing = tx.run(
            find_query,
            title=title,
            content=content,
            density_level=density_level,
            start_offset=start_offset,
            end_offset=end_offset,
        ).single()
        if existing:
            return {
                "id": existing["id"],
                "title": existing["title"],
                "density_level": existing["density_level"],
                "status": "already_exists",
            }
        created = tx.run(
            create_query,
            id=node_id,
            title=title,
            content=content,
            density_level=density_level,
            significance=significance,
            origin=origin,
            node_type=node_type,
            start_offset=start_offset,
            end_offset=end_offset,
        ).single()
        return {
            "id": created["id"],
            "title": created["title"],
            "density_level": created["density_level"],
            "status": "success",
        }

    with driver.session() as session:
        return session.execute_write(_tx)


def _serialize_blocks(blocks: list[dict[str, Any]]) -> str:
    """Neo4j properties cannot store arrays of maps; persist blocks as JSON text."""
    return json.dumps(blocks)


def _deserialize_blocks(raw: Any) -> list[dict[str, Any]] | None:
    if raw is None:
        return None
    if isinstance(raw, str):
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, list) else None
    if isinstance(raw, list):
        return raw
    return None


def _extract_reference_ids_from_blocks(blocks: list[dict[str, Any]] | None) -> list[str]:
    if not blocks:
        return []
    ref_ids: list[str] = []
    for block in blocks:
        if not isinstance(block, dict):
            continue
        if block.get("type") != "reference":
            continue
        node_id = block.get("nodeId") or block.get("node_id")
        if isinstance(node_id, str) and node_id.strip():
            ref_ids.append(node_id.strip())
    return ref_ids


def _set_node_blocks(node_id: str, blocks: list[dict[str, Any]]) -> None:
    query = """
    MATCH (n:Concept {id: $node_id})
    SET n.blocks = $blocks_json
    RETURN n.id AS id
    """
    driver = _require_neo4j()
    with driver.session() as session:
        record = session.run(
            query,
            node_id=node_id,
            blocks_json=_serialize_blocks(blocks),
        ).single()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Node not found: {node_id}",
        )


def _extract_hierarchy_edges_from_blocks(
    blocks: list[dict[str, Any]] | None,
) -> list[tuple[str, str]]:
    """Return (parent_id, child_id) pairs declared by synthesis reference blocks."""
    edges: list[tuple[str, str]] = []
    if not blocks:
        return edges
    for block in blocks:
        if not isinstance(block, dict) or block.get("type") != "reference":
            continue
        child_id = block.get("nodeId") or block.get("node_id")
        parent_id = block.get("parentNodeId") or block.get("parent_node_id")
        if not isinstance(child_id, str) or not isinstance(parent_id, str):
            continue
        child_id = child_id.strip()
        parent_id = parent_id.strip()
        if child_id and parent_id and child_id != parent_id:
            edges.append((parent_id, child_id))
    return edges


def _sync_block_hierarchy_edges(blocks: list[dict[str, Any]] | None) -> None:
    """Ensure SUMMARIZES edges exist for parent-child links declared in synthesis blocks."""
    edges = _extract_hierarchy_edges_from_blocks(blocks)
    if not edges:
        return

    merge_query = """
    UNWIND $pairs AS pair
    MATCH (parent:Concept {id: pair.parent_id}), (child:Concept {id: pair.child_id})
    MERGE (parent)-[r:SUMMARIZES]->(child)
    ON CREATE SET r.strength = 1.0, r.origin = 'human'
    """
    pairs = [{"parent_id": parent_id, "child_id": child_id} for parent_id, child_id in edges]
    driver = _require_neo4j()
    with driver.session() as session:
        session.run(merge_query, pairs=pairs)


def _sync_document_reference_edges(doc_id: str, blocks: list[dict[str, Any]] | None) -> None:
    """Replace REFERENCES edges for a document using block-based reference node IDs."""
    ref_ids = _extract_reference_ids_from_blocks(blocks)
    clear_query = """
    MATCH (doc:Concept {id: $doc_id})-[r:REFERENCES]->()
    DELETE r
    """
    create_query = """
    MATCH (doc:Concept {id: $doc_id})
    UNWIND $target_ids AS target_id
    MATCH (target:Concept {id: target_id})
    MERGE (doc)-[:REFERENCES]->(target)
    """
    driver = _require_neo4j()
    with driver.session() as session:
        if not session.run(
            "MATCH (doc:Concept {id: $doc_id}) RETURN doc.id AS id LIMIT 1",
            doc_id=doc_id,
        ).single():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Node not found: {doc_id}",
            )
        session.run(clear_query, doc_id=doc_id)
        if ref_ids:
            session.run(create_query, doc_id=doc_id, target_ids=ref_ids)
    _sync_block_hierarchy_edges(blocks)


@app.get("/")
def serve_input_pane():
    """Serve the Human Linker input pane."""
    index_path = FRONTEND_DIR / "index.html"
    if not index_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="index.html not found")
    return FileResponse(index_path)


@app.get("/viewer")
def serve_spatial_viewer():
    """Serve the MVP 2 spatial graph viewer."""
    viewer_path = FRONTEND_DIR / "viewer.html"
    if not viewer_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="viewer.html not found")
    return FileResponse(viewer_path)


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


@app.post("/api/nodes", response_model=NodeCreateResponse)
def create_knowledge_node(node: NodeCreate, response: Response):
    """Create a Concept node, or return an existing match (title + content + density_level)."""
    node_id = str(uuid4())
    try:
        record = _upsert_concept_node(
            node_id=node_id,
            title=node.title,
            content=node.content,
            density_level=node.density_level,
            significance=node.significance,
            origin=node.origin,
            node_type=node.node_type,
            start_offset=node.start_offset,
            end_offset=node.end_offset,
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

    doc_id = record["id"]
    if node.blocks is not None:
        _set_node_blocks(doc_id, node.blocks)
        _sync_document_reference_edges(doc_id, node.blocks)

    response.status_code = (
        status.HTTP_200_OK if record["status"] == "already_exists" else status.HTTP_201_CREATED
    )
    return NodeCreateResponse(
        status=record["status"],
        node_id=record["id"],
        title=record["title"],
        density_level=record["density_level"],
    )


@app.put("/api/nodes/{node_id}", response_model=NodeResponse)
def update_knowledge_node(node_id: str, update: NodeUpdate):
    """Update an existing Concept node (title, content, and/or density)."""
    set_clauses: list[str] = []
    params: dict = {"node_id": node_id}

    if update.density_level is not None:
        set_clauses.append("n.density_level = $density_level")
        params["density_level"] = update.density_level
    if update.title is not None:
        set_clauses.append("n.title = $title")
        params["title"] = update.title
    if update.content is not None:
        set_clauses.append("n.content = $content")
        params["content"] = update.content
    if update.blocks is not None:
        set_clauses.append("n.blocks = $blocks")
        params["blocks"] = _serialize_blocks(update.blocks)
    if update.node_type is not None:
        set_clauses.append("n.node_type = $node_type")
        params["node_type"] = update.node_type
    if update.start_offset is not None:
        set_clauses.append("n.start_offset = $start_offset")
        params["start_offset"] = update.start_offset
    if update.end_offset is not None:
        set_clauses.append("n.end_offset = $end_offset")
        params["end_offset"] = update.end_offset

    if not set_clauses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "At least one of density_level, title, content, blocks, node_type, "
                "start_offset, or end_offset is required"
            ),
        )

    query = f"""
    MATCH (n:Concept {{id: $node_id}})
    SET {", ".join(set_clauses)}
    RETURN n.id AS id,
           n.title AS title,
           n.density_level AS density_level,
           coalesce(n.origin, 'human') AS origin,
           coalesce(n.node_type, 'Concept') AS node_type
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            record = session.run(query, **params).single()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Node not found: {node_id}",
        )

    if update.blocks is not None:
        _sync_document_reference_edges(node_id, update.blocks)

    return NodeResponse(
        id=record["id"],
        title=record["title"],
        density_level=record["density_level"],
        origin=record["origin"],
        node_type=record["node_type"],
    )


@app.patch("/api/nodes/{node_id}", response_model=NodePinResponse)
def patch_node_pinned(node_id: str, update: NodePinUpdate):
    """Persist a node's pinned flag so the pin state survives reloads."""
    query = """
    MATCH (n:Concept {id: $node_id})
    SET n.pinned = $pinned
    RETURN n.id AS id, coalesce(n.pinned, false) AS pinned
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            record = session.run(query, node_id=node_id, pinned=update.pinned).single()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Node not found: {node_id}",
        )

    return NodePinResponse(id=record["id"], pinned=record["pinned"])


def _format_neo4j_datetime(value) -> str | None:
    if value is None:
        return None
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


@app.get("/api/nodes", response_model=list[NodeResponse])
def list_knowledge_nodes(
    type: str | None = Query(None, description="Filter by node_type (e.g. Document)"),
):
    """List Concept nodes; optional filter by node_type for synthesis document library."""
    if type == "Document":
        where_clause = (
            "coalesce(n.node_type, 'Concept') = 'Document' OR n.density_level = 4"
        )
    elif type:
        where_clause = "coalesce(n.node_type, 'Concept') = $node_type"
    else:
        where_clause = "true"

    query = f"""
    MATCH (n:Concept)
    WHERE {where_clause}
    RETURN n.id AS id,
           n.title AS title,
           n.density_level AS density_level,
           coalesce(n.origin, 'human') AS origin,
           coalesce(n.node_type, 'Concept') AS node_type,
           coalesce(n.content, n.title, '') AS content,
           n.created_at AS created_at
    ORDER BY n.created_at DESC
    """
    driver = _require_neo4j()
    params = {"node_type": type} if type and type != "Document" else {}
    try:
        with driver.session() as session:
            records = session.run(query, **params).data()
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
            origin=r["origin"],
            node_type=r["node_type"],
            content=r["content"],
            created_at=_format_neo4j_datetime(r.get("created_at")),
        )
        for r in records
    ]


@app.get("/api/nodes/{node_id}", response_model=DocumentNodeResponse)
def get_knowledge_node(node_id: str):
    """Return a single Concept node including content (for loading synthesis documents)."""
    query = """
    MATCH (n:Concept {id: $node_id})
    RETURN n.id AS id,
           n.title AS title,
           coalesce(n.content, n.title) AS content,
           n.density_level AS density_level,
           coalesce(n.origin, 'human') AS origin,
           coalesce(n.node_type, 'Concept') AS node_type,
           n.blocks AS blocks
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            record = session.run(query, node_id=node_id).single()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Node not found: {node_id}",
        )

    blocks = _deserialize_blocks(record.get("blocks"))

    return DocumentNodeResponse(
        id=record["id"],
        title=record["title"],
        content=record["content"],
        density_level=record["density_level"],
        origin=record["origin"],
        node_type=record["node_type"],
        blocks=blocks,
    )


@app.get("/api/nodes/{node_id}/references", response_model=list[DocumentNodeResponse])
def get_node_references(node_id: str):
    """Return Excerpt/Summary nodes referenced by a synthesis Document via REFERENCES edges."""
    query = """
    MATCH (doc:Concept {id: $node_id})-[:REFERENCES]->(target:Concept)
    WHERE target.density_level IN [1, 2]
    RETURN target.id AS id,
           target.title AS title,
           coalesce(target.content, target.title) AS content,
           target.density_level AS density_level,
           coalesce(target.origin, 'human') AS origin,
           coalesce(target.node_type, 'Concept') AS node_type,
           target.created_at AS created_at
    ORDER BY target.created_at ASC
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            records = session.run(query, node_id=node_id).data()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    return [
        DocumentNodeResponse(
            id=r["id"],
            title=r["title"],
            content=r["content"],
            density_level=r["density_level"],
            origin=r["origin"],
            node_type=r["node_type"],
        )
        for r in records
    ]


@app.get("/api/sources", response_model=list[SourceDocumentResponse])
def list_source_documents():
    """List loadable source documents (books and saved synthesis documents)."""
    query = f"""
    MATCH (n:Concept)
    WHERE {SOURCE_NODE_PREDICATE}
    RETURN n.id AS id,
           n.title AS title,
           n.density_level AS density_level,
           coalesce(n.node_type, 'Concept') AS node_type,
           coalesce(n.origin, 'human') AS origin
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
        SourceDocumentResponse(
            id=r["id"],
            title=r["title"],
            density_level=r["density_level"],
            node_type=r["node_type"],
            origin=r["origin"],
        )
        for r in records
    ]


@app.delete("/api/nodes/{node_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledge_node(node_id: str):
    """Delete a Concept node and all attached relationships."""
    query = """
    MATCH (n:Concept {id: $node_id})
    DETACH DELETE n
    RETURN count(n) AS deleted
    """
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            record = session.run(query, node_id=node_id).single()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    if not record or record["deleted"] == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Node not found: {node_id}",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


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
    MATCH (a:Concept {{id: $source_id}}), (b:Concept {{id: $target_id}})
    MERGE (a)-[r:{rel_type}]->(b)
    ON CREATE SET r.strength = $strength, r.origin = $origin
    RETURN type(r) AS link_type, r.strength AS strength
    """
    try:
        record = _run_write(
            query,
            source_id=edge.source_id,
            target_id=edge.target_id,
            strength=edge.strength,
            origin=edge.origin,
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


@app.get("/api/graph")
def get_graph():
    """Return all Concept nodes and edges for the spatial viewer."""
    query = """
    MATCH (n:Concept)
    OPTIONAL MATCH (n)-[r]->(m:Concept)
    RETURN n.id AS source_id,
           n.title AS source_title,
           coalesce(n.content, n.title) AS source_content,
           coalesce(n.density_level, 2) AS source_density,
           coalesce(n.origin, 'human') AS source_origin,
           type(r) AS rel_type,
           m.id AS target_id,
           m.title AS target_title,
           coalesce(m.content, m.title) AS target_content,
           coalesce(m.density_level, 2) AS target_density,
           coalesce(m.origin, 'human') AS target_origin
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

    nodes_by_id: dict[str, dict] = {}
    edges: list[dict] = []
    seen_edges: set[tuple[str, str, str]] = set()

    def add_node(node_id: str, title: str, content: str, density: int, origin: str) -> None:
        if node_id not in nodes_by_id:
            nodes_by_id[node_id] = {
                "data": {
                    "id": node_id,
                    "title": title,
                    "content": content,
                    "label": content or title,
                    "density": density,
                    "origin": origin,
                }
            }

    for row in records:
        add_node(
            row["source_id"],
            row["source_title"],
            row["source_content"],
            row["source_density"],
            row["source_origin"],
        )

        if row["rel_type"] is None or row["target_id"] is None:
            continue

        add_node(
            row["target_id"],
            row["target_title"],
            row["target_content"],
            row["target_density"],
            row["target_origin"],
        )

        edge_key = (row["source_id"], row["target_id"], row["rel_type"])
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)
        edges.append(
            {
                "data": {
                    "source": row["source_id"],
                    "target": row["target_id"],
                    "label": row["rel_type"],
                }
            }
        )

    return {"nodes": list(nodes_by_id.values()), "edges": edges}


BRIDGE_REL_TYPES = (
    "SUMMARIZES|CONTAINS|SUPPORTS|CONTRADICTS|CAUSES|REQUIRES|EXAMPLE_OF|FOLLOWS"
)


def _concept_to_cytoscape_node(props: dict) -> dict:
    title = props.get("title", "")
    content = props.get("content") or title
    return {
        "data": {
            "id": props["id"],
            "title": title,
            "content": content,
            "label": content or title,
            "density": props.get("density_level", 2),
            "origin": props.get("origin", "human"),
        }
    }


def _paths_to_graph(node_rows: list, edge_rows: list) -> dict:
    """Build Cytoscape nodes/edges JSON from bridge query results."""
    nodes_by_id: dict[str, dict] = {}
    for row in node_rows:
        nodes_by_id[row["id"]] = _concept_to_cytoscape_node(
            {
                "id": row["id"],
                "title": row["title"],
                "content": row["content"],
                "density_level": row["density"],
                "origin": row.get("origin", "human"),
            }
        )

    edges: list[dict] = []
    seen_edges: set[tuple[str, str, str]] = set()
    for row in edge_rows:
        edge_key = (row["source_id"], row["target_id"], row["rel_type"])
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)
        edges.append(
            {
                "data": {
                    "source": row["source_id"],
                    "target": row["target_id"],
                    "label": row["rel_type"],
                }
            }
        )

    return {"nodes": list(nodes_by_id.values()), "edges": edges}


@app.get("/api/bridge")
def get_bridge(source_id: str, target_id: str):
    """Return shortest-path bridge between two concepts for the Dual-Pinned view."""
    path_match = f"""
    MATCH (start:Concept {{id: $source_id}}), (end:Concept {{id: $target_id}})
    MATCH p = allShortestPaths(
        (start)-[:{BRIDGE_REL_TYPES}*1..6]-(end)
    )
    """
    node_query = (
        path_match
        + """
    UNWIND nodes(p) AS n
    RETURN DISTINCT n.id AS id,
           n.title AS title,
           coalesce(n.content, n.title) AS content,
           coalesce(n.density_level, 2) AS density,
           coalesce(n.origin, 'human') AS origin
    """
    )
    edge_query = (
        path_match
        + """
    UNWIND relationships(p) AS r
    RETURN DISTINCT startNode(r).id AS source_id,
           endNode(r).id AS target_id,
           type(r) AS rel_type
    """
    )
    driver = _require_neo4j()
    try:
        with driver.session() as session:
            node_rows = session.run(
                node_query, source_id=source_id, target_id=target_id
            ).data()
            if not node_rows:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No path found between the selected nodes (or one/both nodes do not exist).",
                )
            edge_rows = session.run(
                edge_query, source_id=source_id, target_id=target_id
            ).data()
    except HTTPException:
        raise
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    return _paths_to_graph(node_rows, edge_rows)


@app.get("/api/hierarchy", response_model=list[HierarchyNodeResponse])
def get_hierarchy(node_id: Optional[str] = None):
    """Return Miller Column children for a node, or Level 3 sources as root."""
    if node_id:
        query = """
        MATCH (n:Concept {id: $node_id})-[r:SUMMARIZES|CONTAINS]->(child:Concept)
        RETURN child.id AS id,
               child.title AS title,
               child.content AS content,
               child.density_level AS density_level,
               coalesce(child.origin, 'human') AS origin
        ORDER BY child.density_level DESC, child.title
        """
        params = {"node_id": node_id}
    else:
        query = """
        MATCH (n:Concept)
        WHERE n.density_level = 3
        RETURN n.id AS id,
               n.title AS title,
               coalesce(n.content, n.title) AS content,
               n.density_level AS density_level,
               coalesce(n.origin, 'human') AS origin
        ORDER BY n.title
        """
        params = {}

    driver = _require_neo4j()
    try:
        with driver.session() as session:
            records = session.run(query, **params).data()
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    return [
        HierarchyNodeResponse(
            id=r["id"],
            title=r["title"],
            content=r["content"],
            density_level=r["density_level"],
            origin=r["origin"],
        )
        for r in records
    ]


@app.get("/api/document-canvas", response_model=DocumentCanvasResponse)
def get_document_canvas(source_id: Optional[str] = None):
    """Return source text, contained excerpts, and summarizing cards for Document Canvas."""
    driver = _require_neo4j()

    if source_id:
        source_query = f"""
        MATCH (source:Concept {{id: $source_id}})
        WHERE {SOURCE_NODE_PREDICATE.replace('n.', 'source.')}
        RETURN source.id AS id,
               source.title AS title,
               coalesce(source.content, source.title) AS content,
               source.density_level AS density_level,
               coalesce(source.origin, 'human') AS origin,
               coalesce(source.node_type, 'Concept') AS node_type
        LIMIT 1
        """
        source_params = {"source_id": source_id}
    else:
        source_query = f"""
        MATCH (source:Concept)
        WHERE {SOURCE_NODE_PREDICATE.replace('n.', 'source.')}
        RETURN source.id AS id,
               source.title AS title,
               coalesce(source.content, source.title) AS content,
               source.density_level AS density_level,
               coalesce(source.origin, 'human') AS origin,
               coalesce(source.node_type, 'Concept') AS node_type
        ORDER BY source.created_at DESC
        LIMIT 1
        """
        source_params = {}

    excerpt_query = """
    MATCH (source:Concept {id: $source_id})-[:CONTAINS]->(excerpt:Concept)
    WHERE excerpt.density_level IN [1, 2]
    RETURN excerpt.id AS id,
           excerpt.title AS title,
           excerpt.content AS content,
           excerpt.density_level AS density_level,
           coalesce(excerpt.origin, 'human') AS origin,
           coalesce(excerpt.node_type, 'Concept') AS node_type,
           coalesce(excerpt.pinned, false) AS pinned,
           excerpt.start_offset AS start_offset,
           excerpt.end_offset AS end_offset
    ORDER BY excerpt.created_at
    """

    summary_nodes_query = """
    MATCH (source:Concept {id: $source_id})-[:CONTAINS]->(excerpt:Concept)
    WHERE excerpt.density_level IN [1, 2]
    MATCH (summary:Concept {density_level: 1})-[:SUMMARIZES*1..15]->(excerpt)
    WITH DISTINCT summary AS s, source
    MATCH (s)-[:SUMMARIZES*1..15]->(leaf:Concept)<-[:CONTAINS]-(source)
    WITH s, leaf
    ORDER BY leaf.created_at
    WITH s, collect(leaf.id)[0] AS excerpt_id
    RETURN s.id AS id,
           s.title AS title,
           coalesce(s.content, s.title) AS content,
           s.density_level AS density_level,
           coalesce(s.origin, 'human') AS origin,
           coalesce(s.node_type, 'Concept') AS node_type,
           coalesce(s.pinned, false) AS pinned,
           excerpt_id
    ORDER BY s.created_at
    """

    summary_edges_query = """
    MATCH (source:Concept {id: $source_id})
    OPTIONAL MATCH (source)-[:CONTAINS]->(excerpt:Concept)
    WHERE excerpt.density_level IN [1, 2]
    OPTIONAL MATCH (summary:Concept)-[:SUMMARIZES*1..15]->(excerpt)
    OPTIONAL MATCH (source)-[:REFERENCES]->(referenced:Concept)
    WITH collect(DISTINCT excerpt) + collect(DISTINCT summary) + collect(DISTINCT referenced) AS nodes
    UNWIND [n IN nodes WHERE n IS NOT NULL] AS workspace_node
    WITH collect(DISTINCT workspace_node) AS workspace_nodes
    UNWIND workspace_nodes AS child
    MATCH (parent:Concept)-[:SUMMARIZES]->(child)
    WHERE parent IN workspace_nodes
    RETURN DISTINCT parent.id AS source_id, child.id AS target_id
    """

    try:
        with driver.session() as session:
            source_row = session.run(source_query, **source_params).single()
            if not source_row:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No Source or Synthesis Document found.",
                )

            source_id = source_row["id"]
            excerpt_rows = session.run(excerpt_query, source_id=source_id).data()
            summary_rows = session.run(summary_nodes_query, source_id=source_id).data()
            summary_edge_rows = session.run(
                summary_edges_query, source_id=source_id
            ).data()
    except HTTPException:
        raise
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    source = DocumentNodeResponse(
        id=source_row["id"],
        title=source_row["title"],
        content=source_row["content"],
        density_level=source_row["density_level"],
        origin=source_row["origin"],
        node_type=source_row["node_type"],
    )
    excerpts = [
        DocumentNodeResponse(
            id=r["id"],
            title=r["title"],
            content=r["content"],
            density_level=r["density_level"],
            origin=r["origin"],
            node_type=r.get("node_type") or "Concept",
            pinned=r["pinned"],
            start_offset=r.get("start_offset"),
            end_offset=r.get("end_offset"),
        )
        for r in excerpt_rows
    ]

    if len(source.content) > len(source.title) + 50:
        document_text = source.content
    else:
        document_text = "\n\n".join(e.content for e in excerpts)

    return DocumentCanvasResponse(
        source=source,
        document_text=document_text,
        excerpts=excerpts,
        summaries=[
            DocumentSummaryResponse(
                id=r["id"],
                title=r["title"],
                content=r["content"],
                density_level=r["density_level"],
                origin=r["origin"],
                node_type=r.get("node_type") or "Concept",
                pinned=r["pinned"],
                excerpt_id=r["excerpt_id"],
            )
            for r in summary_rows
        ],
        summary_edges=[
            SummaryEdgeResponse(
                source_id=r["source_id"],
                target_id=r["target_id"],
            )
            for r in summary_edge_rows
        ],
    )


@app.get("/api/macro_graph")
def get_macro_graph(source_id: str):
    """Return L1 summary nodes and recursive SUMMARIZES edges for Document Canvas macro pane."""
    driver = _require_neo4j()

    nodes_query = f"""
    MATCH (book:Concept {{id: $source_id}})
    WHERE {SOURCE_NODE_PREDICATE.replace('n.', 'book.')}
    MATCH (book)-[:CONTAINS]->(excerpt:Concept)
    WHERE excerpt.density_level = 2
    MATCH (summary:Concept {{density_level: 1}})-[:SUMMARIZES*1..15]->(excerpt)
    WITH DISTINCT summary AS s, book
    MATCH (s)-[:SUMMARIZES*1..15]->(leaf:Concept {{density_level: 2}})<-[:CONTAINS]-(book)
    WITH s, leaf
    ORDER BY leaf.created_at
    WITH s, collect(leaf.id)[0] AS excerpt_id
    RETURN s.id AS id,
           s.title AS title,
           coalesce(s.content, s.title) AS content,
           coalesce(s.density_level, 1) AS density,
           coalesce(s.origin, 'human') AS origin,
           excerpt_id
    """

    edges_query = f"""
    MATCH (book:Concept {{id: $source_id}})
    WHERE {SOURCE_NODE_PREDICATE.replace('n.', 'book.')}
    MATCH (book)-[:CONTAINS]->(excerpt:Concept)
    WHERE excerpt.density_level = 2
    MATCH (summary:Concept {{density_level: 1}})-[:SUMMARIZES*1..15]->(excerpt)
    WITH collect(DISTINCT summary.id) AS summary_ids
    MATCH (a:Concept)-[r:SUMMARIZES]->(b:Concept)
    WHERE a.id IN summary_ids
      AND b.id IN summary_ids
      AND a.density_level = 1
      AND b.density_level = 1
    RETURN DISTINCT a.id AS source_id, b.id AS target_id, type(r) AS rel_type
    """

    verify_query = f"""
    MATCH (book:Concept {{id: $source_id}})
    WHERE {SOURCE_NODE_PREDICATE.replace('n.', 'book.')}
    RETURN book.id AS id
    LIMIT 1
    """

    try:
        with driver.session() as session:
            if not session.run(verify_query, source_id=source_id).single():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source or Synthesis Document not found.",
                )

            node_rows = session.run(nodes_query, source_id=source_id).data()
            edge_rows = session.run(edges_query, source_id=source_id).data()
    except HTTPException:
        raise
    except GqlError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {exc}",
        ) from exc

    nodes = [
        {
            "data": {
                "id": r["id"],
                "title": r["title"],
                "content": r["content"],
                "label": r["title"],
                "density": r["density"],
                "origin": r["origin"],
                "excerpt_id": r["excerpt_id"],
            }
        }
        for r in node_rows
    ]

    edges = [
        {
            "data": {
                "source": r["source_id"],
                "target": r["target_id"],
                "label": r["rel_type"],
            }
        }
        for r in edge_rows
    ]

    return {"nodes": nodes, "edges": edges}
