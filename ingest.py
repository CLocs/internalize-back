"""Ingest a raw book .txt file into Internalize via the local FastAPI API."""

import argparse
import sys
import time
from pathlib import Path

import requests

DEFAULT_API_BASE = "http://127.0.0.1:8000"
BOOK_TITLE = "Thinking, Fast and Slow"
REQUEST_DELAY = 0.05


def api_post(session: requests.Session, api_base: str, path: str, payload: dict) -> dict:
    response = session.post(f"{api_base}{path}", json=payload, timeout=30)
    response.raise_for_status()
    time.sleep(REQUEST_DELAY)
    return response.json()


def create_node(
    session: requests.Session,
    api_base: str,
    *,
    title: str,
    content: str,
    density_level: int,
) -> str:
    data = api_post(
        session,
        api_base,
        "/api/nodes",
        {
            "title": title,
            "content": content,
            "density_level": density_level,
            "significance": 1.0,
        },
    )
    return data["node_id"]


def create_contains_edge(
    session: requests.Session, api_base: str, source_id: str, target_id: str
) -> None:
    api_post(
        session,
        api_base,
        "/api/edges",
        {
            "source_id": source_id,
            "target_id": target_id,
            "relationship_type": "CONTAINS",
            "strength": 1.0,
        },
    )


def excerpt_title(text: str, index: int) -> str:
    line = text.split("\n", 1)[0].strip()
    if len(line) > 80:
        return line[:77] + "..."
    return line or f"Excerpt {index}"


def load_paragraphs(book_path: Path) -> list[str]:
    text = book_path.read_text(encoding="utf-8")
    return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]


def check_api(session: requests.Session, api_base: str) -> None:
    try:
        response = session.get(f"{api_base}/health", timeout=10)
        response.raise_for_status()
    except requests.ConnectionError:
        print(f"Error: Cannot reach the API at {api_base}")
        print("Start the server first:")
        print("  uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000")
        sys.exit(1)

    health = response.json()
    if health.get("neo4j") != "connected":
        print("Error: API is up but Neo4j is not connected. Start Neo4j Desktop and retry.")
        sys.exit(1)


def ingest(book_path: Path, api_base: str) -> None:
    if not book_path.is_file():
        print(f"Error: book file not found: {book_path}")
        sys.exit(1)

    paragraphs = load_paragraphs(book_path)
    total = len(paragraphs)
    print(f"Loaded {total} paragraphs from {book_path.name}")

    with requests.Session() as session:
        check_api(session, api_base)

        print(f"Creating Level 3 source node: {BOOK_TITLE!r}")
        parent_id = create_node(
            session,
            api_base,
            title=BOOK_TITLE,
            content=BOOK_TITLE,
            density_level=3,
        )
        print(f"Parent node id: {parent_id}\n")

        for i, chunk in enumerate(paragraphs, start=1):
            child_id = create_node(
                session,
                api_base,
                title=excerpt_title(chunk, i),
                content=chunk,
                density_level=2,
            )
            create_contains_edge(session, api_base, parent_id, child_id)

            pct = (i / total) * 100
            print(f"\rIngesting: {i}/{total} ({pct:5.1f}%)", end="", flush=True)

    print(f"\nDone. Created 1 source node and {total} excerpt nodes with CONTAINS edges.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a book .txt into Internalize.")
    parser.add_argument(
        "book_file",
        nargs="?",
        default="thinking-fast-and-slow.txt",
        help="Path to the book text file (default: thinking-fast-and-slow.txt)",
    )
    parser.add_argument(
        "--api",
        default=DEFAULT_API_BASE,
        help=f"FastAPI base URL (default: {DEFAULT_API_BASE})",
    )
    args = parser.parse_args()

    ingest(Path(args.book_file), args.api.rstrip("/"))


if __name__ == "__main__":
    main()
