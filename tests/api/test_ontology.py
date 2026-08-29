"""Ontology endpoint tests."""

from __future__ import annotations


def test_relationship_types_include_definition_of(client):
    response = client.get("/api/ontology/relationship-types")
    assert response.status_code == 200
    data = response.json()
    assert "DEFINITION_OF" in data["allowed_types"]
    assert "DEFINITION_OF" in data["axes"]["Logical"]
