#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No network, no input, deterministic.
"""

import os


JOKE = (
    "My printer finally admitted it isn't out of ink "
    "— it's out of respect for what I keep printing."
)


def main() -> None:
    # Self-check against the competition gate: 1-280 chars, one line.
    if not 1 <= len(JOKE) <= 280 or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke violates the entry gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
