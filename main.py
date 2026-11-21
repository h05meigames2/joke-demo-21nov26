#!/usr/bin/env python3
"""The joke about the demo.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. Deterministic: the same joke every run.
"""

import os

JOKE = (
    "My coding agent's demo worked perfectly all week \u2014 "
    "until the client joined the call, and it confidently "
    "refactored itself into a 404."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert text and not text.isspace(), "joke must not be blank"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 280, "joke must be 1-280 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Round-trip check: what landed on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "round-trip mismatch"
    assert 1 <= len(text) <= 280, "written joke must be 1-280 characters"


if __name__ == "__main__":
    main()
