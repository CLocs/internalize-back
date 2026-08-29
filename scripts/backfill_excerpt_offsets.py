"""Backfill missing start_offset/end_offset for excerpt nodes under source documents.

Uses the same disambiguation heuristics as the viewer (prefer body headings over
TOC-style matches like "CHAPTER 2 - …").

Examples:
  uv run python scripts/backfill_excerpt_offsets.py
  uv run python scripts/backfill_excerpt_offsets.py --source-id <uuid>
  uv run python scripts/backfill_excerpt_offsets.py --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass

import requests

DEFAULT_API_BASE = "http://127.0.0.1:8000"


@dataclass
class MatchResult:
    start: int
    end: int
    ambiguous: bool
    match_count: int
    score: float | None = None


def find_all_indexes(text: str, content: str) -> list[int]:
    matches: list[int] = []
    search_from = 0
    while search_from <= len(text):
        idx = text.find(content, search_from)
        if idx < 0:
            break
        matches.append(idx)
        search_from = idx + 1
    return matches


def score_match(text: str, content: str, idx: int) -> float:
    end = idx + len(content)
    after = text[end : end + 80]
    before = text[max(0, idx - 40) : idx]

    # Context-only score (no position bonus) so the first strong body hit wins.
    score = 0.0
    # TOC / ToC-list continuations: "CHAPTER 2 - …", "CHAPTER 2 A - …", "CHAPTER 2. SEVEN…"
    if re.match(r"^\s*[A-Za-z]?\s*[-–—.]", after):
        score -= 100_000
    # Body heading: content ends at a hard line break (handles \n and \r\n).
    if re.match(r"^\s*[\r\n]", after):
        score += 5_000
    if "\n\n" in before or "\r\n\r\n" in before:
        score += 2_000
    return score


def find_best_content_match(text: str, content: str) -> MatchResult | None:
    if not text or not content:
        return None

    matches = find_all_indexes(text, content)
    if not matches:
        return None
    if len(matches) == 1:
        start = matches[0]
        return MatchResult(
            start=start,
            end=start + len(content),
            ambiguous=False,
            match_count=1,
            score=None,
        )

    scored = [(score_match(text, content, idx), idx) for idx in matches]
    # Prefer higher context score; break ties with earlier occurrence.
    scored.sort(key=lambda item: (-item[0], item[1]))
    best_score, best_idx = scored[0]
    second_score = scored[1][0]

    ambiguous = abs(best_score - second_score) < 1_000

    return MatchResult(
        start=best_idx,
        end=best_idx + len(content),
        ambiguous=ambiguous,
        match_count=len(matches),
        score=best_score,
    )


def document_text_from_canvas(data: dict) -> str:
    text = data.get("document_text") or ""
    if text:
        return text
    source = data.get("source") or {}
    return source.get("content") or ""


def needs_backfill(excerpt: dict, text: str) -> bool:
    start = excerpt.get("start_offset")
    end = excerpt.get("end_offset")
    content = excerpt.get("content") or ""
    if not content:
        return False
    if not isinstance(start, int) or not isinstance(end, int):
        return True
    if end <= start or end > len(text):
        return True
    return text[start:end] != content


def process_source(
    session: requests.Session,
    api_base: str,
    source_id: str,
    *,
    apply: bool,
) -> tuple[int, int, int, int]:
    """Returns (updated, skipped_ok, skipped_ambiguous, skipped_missing)."""
    canvas_res = session.get(
        f"{api_base}/api/document-canvas",
        params={"source_id": source_id},
        timeout=120,
    )
    canvas_res.raise_for_status()
    data = canvas_res.json()
    text = document_text_from_canvas(data)
    title = (data.get("source") or {}).get("title") or source_id

    updated = skipped_ok = skipped_ambiguous = skipped_missing = 0
    print(f"\n== {title} ({source_id}) ==")
    print(f"   document_text length: {len(text):,}")

    for excerpt in data.get("excerpts") or []:
        # Only L2 excerpts are source-text anchors
        if excerpt.get("density_level") != 2:
            continue

        node_id = excerpt.get("id")
        content = excerpt.get("content") or ""
        short = (content[:48] + "…") if len(content) > 48 else content
        short = short.replace("\n", " ")

        if not needs_backfill(excerpt, text):
            skipped_ok += 1
            continue

        match = find_best_content_match(text, content)
        if match is None:
            skipped_missing += 1
            print(f"   MISS  {node_id}  {short!r}")
            continue

        if match.ambiguous:
            skipped_ambiguous += 1
            print(
                f"   AMBIG {node_id}  matches={match.match_count}  "
                f"best={match.start}  {short!r}"
            )
            continue

        action = "APPLY" if apply else "DRY"
        print(
            f"   {action} {node_id}  "
            f"{match.start}–{match.end}  (of {match.match_count})  {short!r}"
        )

        if apply:
            put_res = session.put(
                f"{api_base}/api/nodes/{node_id}",
                json={"start_offset": match.start, "end_offset": match.end},
                timeout=60,
            )
            put_res.raise_for_status()

        updated += 1

    return updated, skipped_ok, skipped_ambiguous, skipped_missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Backfill missing excerpt text offsets from document_text."
    )
    parser.add_argument(
        "--api",
        default=DEFAULT_API_BASE,
        help=f"FastAPI base URL (default: {DEFAULT_API_BASE})",
    )
    parser.add_argument(
        "--source-id",
        default=None,
        help="Only process this source document id (default: all /api/sources).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write offsets via PUT /api/nodes (default is dry-run).",
    )
    args = parser.parse_args()
    api_base = args.api.rstrip("/")

    session = requests.Session()
    try:
        health = session.get(f"{api_base}/health", timeout=10)
        health.raise_for_status()
    except requests.RequestException as exc:
        print(f"Error: cannot reach API at {api_base}: {exc}")
        print("Start the server first:")
        print("  uv run uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000")
        sys.exit(1)

    source_ids: list[str]
    if args.source_id:
        source_ids = [args.source_id]
    else:
        sources_res = session.get(f"{api_base}/api/sources", timeout=60)
        sources_res.raise_for_status()
        sources = sources_res.json()
        source_ids = [s["id"] for s in sources if s.get("id")]
        print(f"Found {len(source_ids)} source(s)")

    totals = [0, 0, 0, 0]
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Mode: {mode}")

    for source_id in source_ids:
        try:
            counts = process_source(session, api_base, source_id, apply=args.apply)
        except requests.HTTPError as exc:
            detail = exc.response.text if exc.response is not None else str(exc)
            print(f"\n!! Failed for {source_id}: {detail}")
            continue
        for i, value in enumerate(counts):
            totals[i] += value

    print("\n--- Summary ---")
    print(f"updated/would-update : {totals[0]}")
    print(f"already correct      : {totals[1]}")
    print(f"ambiguous (skipped)  : {totals[2]}")
    print(f"no match (skipped)   : {totals[3]}")
    if not args.apply and totals[0]:
        print("\nRe-run with --apply to persist offsets.")


if __name__ == "__main__":
    main()
