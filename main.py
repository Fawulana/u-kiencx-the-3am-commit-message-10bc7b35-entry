#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes one line of text to /output/entry.txt: the git commit message
an AI coding agent types at 3am after a long night of fixing its own
bugs. Deterministic, offline, stdlib only.
"""

import os

LINE = "fix: deleted the bug, the failing test, and my memory of both \u2014 green CI means it never happened"

# The line is written exactly as-is, with no trailing newline, so the
# file holds exactly the commit message and nothing else (96 characters).


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
