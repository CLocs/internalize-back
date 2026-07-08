"""Node pin PATCH tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_patch_pin_true_and_false(client, neo4j_required, test_source_node):
    node_id = test_source_node["node_id"]

    pin_res = client.patch(f"/api/nodes/{node_id}", json={"pinned": True})
    assert pin_res.status_code == 200
    pin_body = pin_res.json()
    assert pin_body["id"] == node_id
    assert pin_body["pinned"] is True
    assert pin_body.get("status") == "success"

    unpin_res = client.patch(f"/api/nodes/{node_id}", json={"pinned": False})
    assert unpin_res.status_code == 200
    assert unpin_res.json()["pinned"] is False


@pytest.mark.integration
def test_patch_pin_not_found(client, neo4j_required):
    response = client.patch(
        "/api/nodes/00000000-0000-0000-0000-000000000000",
        json={"pinned": True},
    )
    assert response.status_code == 404
