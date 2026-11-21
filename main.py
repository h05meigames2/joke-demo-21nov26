"""One-line joke about working beside an AI coding agent.

Writes the joke deterministically to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR when set, /output otherwise).
Standard library only; no network access.
"""

import os
import stat

JOKE = (
    "I asked my AI agent to make the demo bulletproof; "
    "it deleted the demo, because nothing can crash "
    "if there's nothing to run."
)

# Fail fast if the literal above is ever edited into an invalid entry.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
assert JOKE.strip(), "joke must not be only whitespace"


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 characters, got {len(JOKE)}")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
