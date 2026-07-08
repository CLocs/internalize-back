"""Shared pytest fixtures for Internalize integration and E2E tests."""

from __future__ import annotations

import uuid

import httpx
import pytest
from starlette.testclient import TestClient

from backend.main import app

API_BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture(scope="session")
def client() -> TestClient:
    """HTTP client wired to the FastAPI app with lifespan (Neo4j driver init)."""
    with TestClient(app) as http_client:
        yield http_client


@pytest.fixture(scope="session")
def neo4j_required(client: TestClient) -> dict:
    """Skip tests when Neo4j is unreachable."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    if data.get("neo4j") != "connected":
        pytest.skip("Neo4j is not connected — start Neo4j Desktop and check .env")
    return data


@pytest.fixture
def test_source_node(client: TestClient, neo4j_required: dict) -> dict:
    """Create a Level-3 Document node for tests; delete it on teardown."""
    suffix = uuid.uuid4().hex[:8]
    payload = {
        "title": f"Test Source {suffix}",
        "content": f"Integration test document body ({suffix}).",
        "density_level": 3,
        "node_type": "Document",
        "significance": 1.0,
        "origin": "human",
    }
    response = client.post("/api/nodes", json=payload)
    assert response.status_code in (200, 201), response.text
    body = response.json()
    node_id = body["node_id"]
    yield {"node_id": node_id, "title": payload["title"], "content": payload["content"]}
    client.delete(f"/api/nodes/{node_id}")


@pytest.fixture
def test_concept_pair(client: TestClient, neo4j_required: dict) -> dict:
    """Create two Level-1 nodes linked by SUMMARIZES; delete both on teardown."""
    suffix = uuid.uuid4().hex[:8]
    parent_payload = {
        "title": f"Parent Summary {suffix}",
        "content": "Parent summary content.",
        "density_level": 1,
        "significance": 1.0,
        "origin": "human",
    }
    child_payload = {
        "title": f"Child Summary {suffix}",
        "content": "Child summary content.",
        "density_level": 1,
        "significance": 1.0,
        "origin": "human",
    }
    parent_res = client.post("/api/nodes", json=parent_payload)
    child_res = client.post("/api/nodes", json=child_payload)
    assert parent_res.status_code in (200, 201), parent_res.text
    assert child_res.status_code in (200, 201), child_res.text
    parent_id = parent_res.json()["node_id"]
    child_id = child_res.json()["node_id"]
    yield {"parent_id": parent_id, "child_id": child_id}
    client.delete(f"/api/nodes/{parent_id}")
    client.delete(f"/api/nodes/{child_id}")


@pytest.fixture(scope="session")
def live_server_url() -> str:
    return API_BASE_URL


@pytest.fixture(scope="session")
def require_live_server(live_server_url: str) -> str:
    """Skip E2E tests when the dev server is not running."""
    try:
        response = httpx.get(f"{live_server_url}/health", timeout=5.0)
        response.raise_for_status()
        if response.json().get("neo4j") != "connected":
            pytest.skip("Neo4j is not connected for E2E tests")
    except (httpx.HTTPError, OSError):
        pytest.skip(
            f"Server not running at {live_server_url} — "
            "start with: uv run uvicorn backend.main:app --host 127.0.0.1 --port 8000"
        )
    return live_server_url
