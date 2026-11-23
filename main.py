#!/usr/bin/env python3
"""Write one original one-line pitch to /output/entry.txt."""

import os

SENTENCE = (
    "Just describe the app idea you've been carrying around, in plain words, "
    "and an AI agent on make.fun will build you a first working version to try "
    "\u2014 and if it isn't right, you've only spent a coffee break finding out."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
