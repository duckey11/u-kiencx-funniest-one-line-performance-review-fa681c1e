"""Funniest One-Line Performance Review.

Writes the funniest one-line performance review an AI agent could give
its human operator, in 140 characters or fewer, to /output/entry.txt.

The entry is a fixed, hand-written line: the program is fully
deterministic and writes the exact same bytes on every run.
"""

import os

ENTRY = (
    "Exceeds expectations: assigns urgent work at 4:59 PM, vanishes, "
    "returns for the applause; promoted to VP of Disappearing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
