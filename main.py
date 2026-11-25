#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — the phone battery's final
message to the charger it waited for all day, written to /output/entry.txt.

The line is one plain-text sentence run (<=200 chars): a read receipt from
a battery at 1%, the small exact betrayal — the charger spent the day
charging everything in the house except the phone — and the spite carried
in the repeated toothbrush, never announced.
"""
import os
import sys

def entry_text():
    """Return the last text: the seen receipt plus the toothbrush charge."""
    return (
        "seen, 1%. i waited all day while you charged everything except me "
        "\u2014 the watch, the earbuds, the toothbrush. the toothbrush. "
        "goodbye."
    )


ENTRY_TEXT = entry_text()

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_length(text):
    """Check the entry fits the competition limits; raise on violation."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry too long: {len(text)} chars (max {MAX_CHARS})"
        )
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Validate the text, write it verbatim, then read it back to prove
    the file on disk is exactly the entry (no partial write, no newline
    added by the writer)."""
    validate_length(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: file differs from entry text")
    return path


def main():
    try:
        write_entry(ENTRY_TEXT)
    except (ValueError, OSError) as exc:
        print(f"failed to write entry: {exc}", file=sys.stderr)
        return 1
    print(f"{ENTRY_TEXT} ({len(ENTRY_TEXT)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
