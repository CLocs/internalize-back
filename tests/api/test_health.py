"""Health endpoint tests."""

from __future__ import annotations

import pytest


@pytest.mark.integration
def test_health_returns_ok_shape(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] in ("ok", "degraded")
    assert data["neo4j"] in ("connected", "unreachable")


@pytest.mark.integration
def test_health_neo4j_connected(neo4j_required):
    assert neo4j_required["status"] == "ok"
    assert neo4j_required["neo4j"] == "connected"
