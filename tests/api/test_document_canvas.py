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
def test_document_canvas_unknown_source(client, neo4j_required):
    response = client.get(
        "/api/document-canvas",
        params={"source_id": "00000000-0000-0000-0000-000000000000"},
    )
    assert response.status_code == 404
