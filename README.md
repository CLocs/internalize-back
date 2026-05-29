# Internalize Backend

Local-first semantic knowledge graph API for **MVP 1: The Human Linker**. You paste excerpts, write summaries, and link concepts in Neo4j using a strict relationship ontology—no generic tags.

## Stack

- **Python** · [FastAPI](https://fastapi.tiangolo.com/) · Pydantic
- **Neo4j** (local Desktop instance)
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **UI:** `index.html` (vanilla JS, dark-themed Input Pane)

## Prerequisites

1. [Neo4j Desktop](https://neo4j.com/download/) running locally (default bolt port `7687`)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

```powershell
# Install uv (Windows)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Quick start

```powershell
cd internalize-back

# Install dependencies and create .venv
uv sync

# Configure Neo4j credentials
copy .env.example .env
# Edit .env with your Neo4j username and password

# Run the API + Input Pane (hot reload)
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open **http://127.0.0.1:8000/** for the Human Linker UI. API docs: **http://127.0.0.1:8000/docs**.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `NEO4J_URI` | `bolt://127.0.0.1:7687` | Bolt connection URI (use `127.0.0.1`, not `localhost`, on Windows) |
| `NEO4J_USER` | `neo4j` | Database username |
| `NEO4J_PASSWORD` | `password` | Database password |

Copy `.env.example` to `.env` and set your Neo4j Desktop credentials.

### Neo4j not running?

The API **starts even if Neo4j is down** — you'll see a warning in the terminal. The Input Pane loads, but create/list endpoints return **503** until the database is up.

1. Open **Neo4j Desktop** and start your local DB instance (green "Running" status).
2. Confirm the Bolt port in Desktop matches `NEO4J_URI` (usually `7687`).
3. Set `NEO4J_PASSWORD` in `.env` to the password you chose when creating the DB.
4. Restart uvicorn, or hit **Refresh** in the UI after starting Neo4j.

Check connectivity: `GET http://127.0.0.1:8000/health` → `{"status":"ok","neo4j":"connected"}`.

## Semantic ontology

Nodes are **Concepts** with `id`, `title`, `excerpt`, `summary`, `source_metadata`, and `created_at`.

Edges must be one of these types (enforced by the API):

| Type | Axis | Meaning |
|------|------|---------|
| `SUMMARY_EXPANSION` | Vertical | Drill down from concept to raw evidence |
| `SUPPORTS` | Evaluation (+) | Agreement or reinforcing evidence |
| `CONTRADICTS` | Evaluation (−) | Conflicting theories |
| `AGREES_WITH` | Evaluation (=) | Identical concepts |
| `CAUSE_REQUIRE` | Logical | Functional dependencies |
| `TYPE_EXAMPLE` | Logical (+Ex) | Instantiation of a category |

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Input Pane (`index.html`) |
| `GET` | `/health` | Neo4j connectivity check |
| `GET` | `/api/nodes` | List all concepts |
| `POST` | `/api/nodes` | Create a concept |
| `POST` | `/api/edges` | Create a semantic edge |
| `GET` | `/api/ontology/relationship-types` | Allowed edge types + descriptions |

### Example: create a node

```bash
curl -X POST http://127.0.0.1:8000/api/nodes \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"System 1\", \"excerpt\": \"...\", \"summary\": \"Fast, automatic thinking.\", \"source_metadata\": \"Kahneman\"}"
```

### Example: create an edge

```bash
curl -X POST http://127.0.0.1:8000/api/edges \
  -H "Content-Type: application/json" \
  -d "{\"source_id\": \"<uuid>\", \"target_id\": \"<uuid>\", \"relationship_type\": \"SUPPORTS\"}"
```

## uv commands

| Command | Description |
|---------|-------------|
| `uv sync` | Install / update dependencies from lockfile |
| `uv run uvicorn main:app --reload` | Start server with hot reload |
| `uv run uvicorn main:app` | Start server (no reload) |
| `uv lock` | Refresh `uv.lock` after changing `pyproject.toml` |
| `uv add <package>` | Add a dependency |

## Project layout

```
internalize-back/
├── main.py           # FastAPI app + Neo4j queries
├── index.html        # Human Linker Input Pane
├── pyproject.toml    # Project metadata & dependencies
├── uv.lock           # Locked dependency versions
├── .env.example      # Environment template
└── .cursorrules      # Architecture & ontology reference
```

## Development notes

- The app logs a warning on startup if Neo4j is unreachable; data endpoints return 503 until it connects.
- Node IDs are generated in Python (`uuid4`); no APOC plugin required.
- Serve the UI through FastAPI (`GET /`) so API calls stay same-origin. Opening `index.html` from disk still works—it falls back to `http://localhost:8000`.
