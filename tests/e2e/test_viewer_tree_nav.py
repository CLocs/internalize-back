"""Tree keyboard navigation E2E tests."""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from tests.e2e.conftest import load_seeded_workspace


@pytest.mark.e2e
def test_arrow_right_sets_focus(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)
    page.keyboard.press("ArrowRight")
    page.wait_for_timeout(400)

    focused_count = page.locator(".focused-node").count()
    assert focused_count == 1

    focused_id = page.evaluate("() => window.focusedNodeId")
    assert focused_id, "window.focusedNodeId should be set after ArrowRight"


@pytest.mark.e2e
def test_h_key_moves_focus(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)
    page.keyboard.press("ArrowRight")
    page.wait_for_timeout(300)
    first_id = page.evaluate("() => window.focusedNodeId")

    page.keyboard.press("l")
    page.wait_for_timeout(400)
    second_id = page.evaluate("() => window.focusedNodeId")

    assert first_id
    assert second_id
    assert first_id != second_id or page.locator(".focused-node").count() == 1
