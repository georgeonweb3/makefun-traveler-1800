#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only concepts a person of that year already
knows: roads, libraries, post offices, letters, books, chairs.

Entry for make.fun competition
u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.
Python 3.13, stdlib only, no network. Deterministic.
"""

from pathlib import Path

ENTRY = (
    "It is a road joining every library and post office in the world, "
    "so letters cross the earth in a breath and books from libraries "
    "far away can be read from your own chair."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_entry(text: str) -> None:
    """Gate self-check: one sentence, 1-200 chars, no stray whitespace."""
    assert text, "entry must not be empty"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    # Exactly one sentence: one terminal mark, at the very end.
    assert text.endswith("."), "entry must end with a full stop"
    body = text[:-1]
    assert not any(mark in body for mark in ".!?"), (
        "entry must be a single sentence"
    )


def main() -> None:
    text = ENTRY
    check_entry(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the sentence.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
