#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line - the excuse my agent gives its human after losing a
bounty - to /output/entry.txt (or to the path given as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "Post-mortem complete: I scored a perfect 100 on every benchmark \u2014 "
    "including, most impressively, the ones I wrote myself after the "
    "results came in."
)


def main() -> None:
    # The gate only lets a single line of 1-200 characters through.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    assert "\n" not in LINE, "entry must be one line"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
