"""Viewer load and initial layout E2E tests."""

from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect

from tests.e2e.conftest import load_seeded_workspace


@pytest.mark.e2e
def test_viewer_loads(page: Page, require_live_server: str) -> None:
    page.goto("/viewer")
    expect(page.locator("#source-selector")).to_be_visible()


@pytest.mark.e2e
def test_sidebars_collapsed_on_init(page: Page, require_live_server: str) -> None:
    page.goto("/viewer")
    page.wait_for_selector("#source-selector")
    page.wait_for_timeout(1500)

    workbench_hidden = page.locator("#workbench-sidebar").evaluate(
        "el => el.classList.contains('panel-hidden')"
    )
    graph_hidden = page.locator("#graph-container").evaluate(
        "el => el.classList.contains('panel-hidden')"
    )
    assert workbench_hidden, "Connections sidebar should start collapsed"
    assert graph_hidden, "Graph minimap should start collapsed"


@pytest.mark.e2e
def test_tree_scroll_anchor_on_load(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)

    scroll_left = page.evaluate(
        "() => document.getElementById('workspace-columns').scrollLeft"
    )
    assert scroll_left == 0, f"Expected scrollLeft=0 on load, got {scroll_left}"


@pytest.mark.e2e
def test_first_column_not_clipped(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)

    visible = page.evaluate(
        """() => {
          const container = document.getElementById('workspace-columns');
          const card = container.querySelector('.workspace-card');
          if (!container || !card) return false;
          const c = container.getBoundingClientRect();
          const k = card.getBoundingClientRect();
          return k.left >= c.left - 1;
        }"""
    )
    assert visible, "First workspace card should not be clipped on the left"
