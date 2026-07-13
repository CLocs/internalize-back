"""Document canvas API tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_document_canvas_for_source(client, neo4j_required, test_source_node):
    source_id = test_source_node["node_id"]
    response = client.get("/api/document-canvas", params={"source_id": source_id})
    assert response.status_code == 200
    data = response.json()

    assert data["source"]["id"] == source_id
    assert data["source"]["title"] == test_source_node["title"]
    assert isinstance(data["document_text"], str)
    assert isinstance(data["excerpts"], list)
    assert isinstance(data["summaries"], list)
    assert isinstance(data["summary_edges"], list)


@pytest.mark.integration
def test_create_excerpt_with_text_offsets(client, neo4j_required, test_source_node):
    source_id = test_source_node["node_id"]
    create_res = client.post(
        "/api/nodes",
        json={
            "title": "Chapter 2 body",
            "content": "Chapter 2",
            "density_level": 2,
            "significance": 1.0,
            "origin": "human",
            "start_offset": 120,
            "end_offset": 129,
        },
    )
    assert create_res.status_code in (200, 201)
    excerpt_id = create_res.json()["node_id"]

    edge_res = client.post(
        "/api/edges",
        json={
            "source_id": source_id,
            "target_id": excerpt_id,
            "relationship_type": "CONTAINS",
            "strength": 1.0,
            "origin": "human",
        },
    )
    assert edge_res.status_code == 201

    canvas_res = client.get("/api/document-canvas", params={"source_id": source_id})
    assert canvas_res.status_code == 200
    excerpts = canvas_res.json()["excerpts"]
    matched = next((e for e in excerpts if e["id"] == excerpt_id), None)
    assert matched is not None
    assert matched["start_offset"] == 120
    assert matched["end_offset"] == 129

    client.delete(f"/api/nodes/{excerpt_id}")


@pytest.mark.integration
def test_synthesis_blocks_sync_hierarchy_edges(client, neo4j_required):
    parent_res = client.post(
        "/api/nodes",
        json={
            "title": "Parent summary",
            "content": "Parent summary text",
            "density_level": 1,
            "significance": 1.0,
            "origin": "human",
        },
    )
    child_res = client.post(
        "/api/nodes",
        json={
            "title": "Child excerpt",
            "content": "Child excerpt text",
            "density_level": 2,
            "significance": 1.0,
            "origin": "human",
        },
    )
    assert parent_res.status_code in (200, 201)
    assert child_res.status_code in (200, 201)
    parent_id = parent_res.json()["node_id"]
    child_id = child_res.json()["node_id"]

    blocks = [
        {"type": "reference", "nodeId": parent_id, "order": 0, "indentLevel": 0},
        {
            "type": "reference",
            "nodeId": child_id,
            "order": 1,
            "indentLevel": 1,
            "parentNodeId": parent_id,
        },
    ]

    doc_res = client.post(
        "/api/nodes",
        json={
            "title": "Synthesis with hierarchy",
            "content": "Synthesis body",
            "density_level": 4,
            "node_type": "Document",
            "significance": 1.0,
            "origin": "human",
            "blocks": blocks,
        },
    )
    assert doc_res.status_code in (200, 201)
    doc_id = doc_res.json()["node_id"]

    canvas_res = client.get("/api/document-canvas", params={"source_id": doc_id})
    assert canvas_res.status_code == 200
    edge_pairs = {
        (edge["source_id"], edge["target_id"]) for edge in canvas_res.json()["summary_edges"]
    }
    assert (parent_id, child_id) in edge_pairs

    client.delete(f"/api/nodes/{doc_id}")
    client.delete(f"/api/nodes/{parent_id}")
    client.delete(f"/api/nodes/{child_id}")


@pytest.mark.integration
def test_document_canvas_unknown_source(client, neo4j_required):
    response = client.get(
        "/api/document-canvas",
        params={"source_id": "00000000-0000-0000-0000-000000000000"},
    )
    assert response.status_code == 404
