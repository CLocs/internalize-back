"""Ingest a raw book .txt file into Internalize as a single Level 3 Source node."""

import argparse
import sys
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_API_BASE = "http://localhost:8000"
DEFAULT_BOOK = PROJECT_ROOT / "books" / "thinking-fast-and-slow.txt"
BOOK_TITLE = "Thinking, Fast and Slow"


def ingest(book_path: Path, api_base: str) -> None:
    if not book_path.is_file():
        print(f"Error: book file not found: {book_path}")
        sys.exit(1)

    full_text = book_path.read_text(encoding="utf-8")
    print(f"Loaded {len(full_text):,} characters from {book_path.name}")

    payload = {
        "title": BOOK_TITLE,
        "content": full_text,
        "density_level": 3,
        "node_type": "Book",
        "origin": "ingest",
    }

    try:
        response = requests.post(
            f"{api_base}/api/nodes",
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
    except requests.ConnectionError:
        print(f"Error: Cannot reach the API at {api_base}")
        print("Start the server first:")
        print("  uv run uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000")
        sys.exit(1)
    except requests.HTTPError as exc:
        detail = exc.response.text if exc.response is not None else str(exc)
        print(f"Error: API request failed ({exc.response.status_code if exc.response else 'unknown'})")
        print(detail)
        sys.exit(1)
    except requests.RequestException as exc:
        print(f"Error: Request failed: {exc}")
        sys.exit(1)

    data = response.json()
    print(f"Success. Created Level 3 Source node with node_id: {data['node_id']}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest a book .txt as a single Level 3 Source node."
    )
    parser.add_argument(
        "book_file",
        nargs="?",
        default=str(DEFAULT_BOOK),
        help=f"Path to the book text file (default: {DEFAULT_BOOK.relative_to(PROJECT_ROOT)})",
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
