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
def test_communication_pad_persists_paragraphs(client, neo4j_required):
    create_res = client.post(
        "/api/nodes",
        json={
            "title": "Morning note",
            "content": "First paragraph\n\nSecond paragraph",
            "density_level": 1,
            "node_type": "Communication",
            "significance": 1.0,
            "origin": "human",
            "blocks": [
                {"type": "paragraph", "content": "First paragraph"},
                {"type": "paragraph", "content": "Second paragraph"},
            ],
        },
    )
    assert create_res.status_code in (200, 201), create_res.text
    node_id = create_res.json()["node_id"]

    try:
        response = client.get(f"/api/nodes/{node_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["node_type"] == "Communication"
        assert data["title"] == "Morning note"
        assert [block["content"] for block in data["blocks"]] == [
            "First paragraph",
            "Second paragraph",
        ]
    finally:
        client.delete(f"/api/nodes/{node_id}")


@pytest.mark.integration
def test_communication_pad_reference_is_stored(client, neo4j_required):
    concept = client.post(
        "/api/nodes",
        json={
            "title": "Pulled summary",
            "content": "A sentence worth keeping beside the source.",
            "density_level": 1,
            "significance": 1.0,
            "origin": "human",
        },
    )
    assert concept.status_code in (200, 201), concept.text
    concept_id = concept.json()["node_id"]

    pad = client.post(
        "/api/nodes",
        json={
            "title": "Pad with a pull",
            "content": "Opening line\n\nPulled summary",
            "density_level": 1,
            "node_type": "Communication",
            "significance": 1.0,
            "origin": "human",
            "blocks": [
                {"type": "paragraph", "content": "Opening line"},
                {
                    "type": "reference",
                    "nodeId": concept_id,
                    "title": "Pulled summary",
                    "content": "A sentence worth keeping beside the source.",
                    "density_level": 1,
                },
            ],
        },
    )
    assert pad.status_code in (200, 201), pad.text
    pad_id = pad.json()["node_id"]

    try:
        saved = client.get(f"/api/nodes/{pad_id}")
        assert saved.status_code == 200
        blocks = saved.json()["blocks"]
        assert blocks[1]["type"] == "reference"
        assert blocks[1]["nodeId"] == concept_id

        refs = client.get(f"/api/nodes/{pad_id}/references")
        assert refs.status_code == 200
        assert concept_id in {item["id"] for item in refs.json()}
    finally:
        client.delete(f"/api/nodes/{pad_id}")
        client.delete(f"/api/nodes/{concept_id}")


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
