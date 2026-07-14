"""Pin interaction E2E tests."""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from tests.e2e.conftest import load_seeded_workspace


@pytest.mark.e2e
def test_pin_via_click(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)
    pin = page.locator("#workspace-columns .workspace-card .pin-icon").first
    card = page.locator("#workspace-columns .workspace-card").first

    was_pinned = card.evaluate("el => el.classList.contains('pinned-node')")
    pin.click()
    page.wait_for_timeout(500)

    is_pinned = card.evaluate("el => el.classList.contains('pinned-node')")
    assert is_pinned != was_pinned
    assert card.evaluate("el => el.classList.contains('focused-node')")


@pytest.mark.e2e
def test_pin_via_p_hotkey(page: Page, seeded_workspace: dict) -> None:
    load_seeded_workspace(page, seeded_workspace)
    page.keyboard.press("ArrowRight")
    page.wait_for_timeout(400)

    card = page.locator(".focused-node").first
    was_pinned = card.evaluate("el => el.classList.contains('pinned-node')")

    page.keyboard.press("p")
    page.wait_for_timeout(500)

    is_pinned = card.evaluate("el => el.classList.contains('pinned-node')")
    assert is_pinned != was_pinned
