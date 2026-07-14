"""Playwright E2E fixtures and helpers."""

from __future__ import annotations

import uuid

import httpx
import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def base_url(require_live_server: str) -> str:
    return require_live_server


@pytest.fixture
def seeded_workspace(require_live_server: str) -> dict:
    """Create a source + excerpt + summary linked for multi-column Tree view tests."""
    suffix = uuid.uuid4().hex[:8]
    title = f"E2E Workspace {suffix}"
    with httpx.Client(base_url=require_live_server, timeout=30.0) as client:
        source_res = client.post(
            "/api/nodes",
            json={
                "title": title,
                "content": f"Source body for E2E tests ({suffix}).",
                "density_level": 3,
                "node_type": "Document",
                "significance": 1.0,
                "origin": "human",
            },
        )
        source_res.raise_for_status()
        source_id = source_res.json()["node_id"]

        excerpt_res = client.post(
            "/api/nodes",
            json={
                "title": f"Excerpt {suffix}",
                "content": f"Excerpt content ({suffix}).",
                "density_level": 2,
                "significance": 1.0,
                "origin": "human",
            },
        )
        excerpt_res.raise_for_status()
        excerpt_id = excerpt_res.json()["node_id"]

        summary_res = client.post(
            "/api/nodes",
            json={
                "title": f"Summary {suffix}",
                "content": f"Summary content ({suffix}).",
                "density_level": 1,
                "significance": 1.0,
                "origin": "human",
            },
        )
        summary_res.raise_for_status()
        summary_id = summary_res.json()["node_id"]

        for rel in (
            {"source_id": source_id, "target_id": excerpt_id, "relationship_type": "CONTAINS"},
            {"source_id": summary_id, "target_id": excerpt_id, "relationship_type": "SUMMARIZES"},
        ):
            edge_res = client.post(
                "/api/edges",
                json={**rel, "strength": 1.0, "origin": "human"},
            )
            edge_res.raise_for_status()

        payload = {
            "title": title,
            "source_id": source_id,
            "excerpt_id": excerpt_id,
            "summary_id": summary_id,
        }
        yield payload

        for node_id in (summary_id, excerpt_id, source_id):
            client.delete(f"/api/nodes/{node_id}")


def load_seeded_workspace(page: Page, seeded_workspace: dict) -> None:
    """Open the viewer and select the seeded source so workspace cards render."""
    page.goto("/viewer")
    page.wait_for_selector("#source-selector")
    page.select_option("#source-selector", seeded_workspace["source_id"])
    page.wait_for_selector("#workspace-columns .workspace-card", timeout=30_000)
    page.wait_for_timeout(2500)
