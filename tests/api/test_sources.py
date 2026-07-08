"""Source library listing tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_list_sources_includes_created_document(client, neo4j_required, test_source_node):
    response = client.get("/api/sources")
    assert response.status_code == 200
    sources = response.json()
    assert isinstance(sources, list)
    ids = {s["id"] for s in sources}
    assert test_source_node["node_id"] in ids

    match = next(s for s in sources if s["id"] == test_source_node["node_id"])
    assert match["title"] == test_source_node["title"]
    assert match["density_level"] == 3
    assert match["node_type"] == "Document"
