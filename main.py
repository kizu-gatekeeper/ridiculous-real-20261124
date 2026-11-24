#!/usr/bin/env python3
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Ridiculous at First Glance, Real by the Second" bounty: one sentence (at most 200 characters) pitching a startup so strange it sounds like a joke, yet specific enough to see the customers and the money.

The program writes exactly that text, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LINE = 'Granny-on-Demand rents real grandmothers to join your investor calls, nod proudly, and call you a clever boy; founders pay $49 a month, because a pitch a grandmother believes in closes twice as fast.'


def write_entry(out_dir: str) -> str:
    """Write the entry text to ``entry.txt`` in ``out_dir``; return its path.

    The file holds exactly the entry and nothing else: no trailing
    newline, no extra whitespace, so the gate reads the text alone.
    """
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return entry_path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
