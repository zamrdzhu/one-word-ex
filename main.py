"""One word my ex would use to describe me: Clingy.

Prints the word to stdout and writes the exact same word, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the word is a constant in this file,
and the checks enforce the competition's one-word, 24-character gate.
"""

import os
import sys

WORD = "Clingy"


def main() -> int:
    if not 1 <= len(WORD) <= 24:
        print(f"error: word is {len(WORD)} chars, must be 1-24",
              file=sys.stderr)
        return 1
    if " " in WORD or "\n" in WORD:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
