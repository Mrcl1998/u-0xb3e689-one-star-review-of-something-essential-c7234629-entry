#!/usr/bin/env python3
"""Entry generator for the One-Star Review of Something Essential bounty.

Writes the one-line review to /output/entry.txt as UTF-8 text with no
trailing newline, then sets the output file mode to 0644.
"""

import os

ENTRY = "One star. The weekend lasts two days: one for chores, one for dreading Monday."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
