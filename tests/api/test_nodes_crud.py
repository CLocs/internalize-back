"""Node create, read, and delete tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_create_source_document(client, neo4j_required, test_source_node):
    node_id = test_source_node["node_id"]
    response = client.get(f"/api/nodes/{node_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == node_id
    assert data["title"] == test_source_node["title"]
    assert data["content"] == test_source_node["content"]
    assert data["density_level"] == 3
    assert data["node_type"] == "Document"


@pytest.mark.integration
def test_get_node_not_found(client, neo4j_required):
    response = client.get("/api/nodes/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


@pytest.mark.integration
def test_delete_node(client, neo4j_required):
    create_res = client.post(
        "/api/nodes",
        json={
            "title": "Ephemeral Node",
            "content": "To be deleted.",
            "density_level": 2,
            "significance": 1.0,
            "origin": "human",
        },
    )
    assert create_res.status_code in (200, 201)
    node_id = create_res.json()["node_id"]

    delete_res = client.delete(f"/api/nodes/{node_id}")
    assert delete_res.status_code == 204

    get_res = client.get(f"/api/nodes/{node_id}")
    assert get_res.status_code == 404
