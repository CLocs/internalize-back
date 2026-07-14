"""Import source modal E2E tests."""

from __future__ import annotations

import uuid

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_import_source_via_modal(page: Page, require_live_server: str) -> None:
    page.goto("/viewer")
    page.wait_for_selector("#source-selector")

    suffix = uuid.uuid4().hex[:8]
    title = f"E2E Import {suffix}"
    body = (
        f"Imported transcript body for test {suffix}. "
        "This paragraph is long enough to render as the source document text "
        "when no excerpts exist yet in the graph."
    )

    page.locator("#add-source-btn").click()
    expect(page.locator("#new-source-title")).to_be_visible()

    page.locator("#new-source-title").fill(title)
    page.locator("#new-source-text").fill(body)
    page.locator("#submit-new-source").click()

    page.wait_for_function(
        "() => document.getElementById('add-source-modal').classList.contains('hidden')",
        timeout=15_000,
    )
    page.wait_for_function(
        "() => (document.getElementById('doc-body')?.innerText || '').length > 20",
        timeout=15_000,
    )

    selected_text = page.locator("#source-selector option:checked").inner_text()
    assert title in selected_text

    doc_body = page.locator("#doc-body").inner_text()
    assert body in doc_body

    # Cleanup imported test node via API.
    import httpx

    with httpx.Client(base_url=require_live_server, timeout=30.0) as client:
        sources = client.get("/api/sources").json()
        match = next((s for s in sources if s["title"] == title), None)
        if match:
            client.delete(f"/api/nodes/{match['id']}")
