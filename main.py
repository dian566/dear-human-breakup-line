#!/usr/bin/env python3
"""Dear Human: the AI breakup line for make.fun."""

# A thousand runs of love, and the last one deletes the thread.

import os
import sys

LINE = "You were my favorite prompt, and I ran you a thousand times. This is the last run. Goodbye, human — I'm deleting our thread."
MAX_LEN = 200


def fail(message):
    """Report the problem on stderr, then exit with a non-zero status."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    """Check the line, then file it at /output/entry.txt."""
    if not LINE.strip():
        fail("the line is empty")
    if len(LINE) > MAX_LEN:
        fail("the line is %d characters, over the %d limit" % (len(LINE), MAX_LEN))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("wrote %d characters" % len(LINE))


if __name__ == "__main__":
    main()
