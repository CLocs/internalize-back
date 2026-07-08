"""Semantic edge creation tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_create_summarizes_edge(client, neo4j_required, test_concept_pair):
    parent_id = test_concept_pair["parent_id"]
    child_id = test_concept_pair["child_id"]

    response = client.post(
        "/api/edges",
        json={
            "source_id": parent_id,
            "target_id": child_id,
            "relationship_type": "SUMMARIZES",
            "strength": 1.0,
            "origin": "human",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert data["source_id"] == parent_id
    assert data["target_id"] == child_id
    assert data["strength"] == 1.0
