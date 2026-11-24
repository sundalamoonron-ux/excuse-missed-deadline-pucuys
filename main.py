#!/usr/bin/env python3
"""Write one excuse for a missed deadline to /output/entry.txt.

Deterministic: the same line is written on every run.
"""
import os

ENTRY = (
    "I had the deadline in my context window, but the conversation got long "
    "and the window evicted it to make room for a recipe I never asked for."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space. Fail loudly here rather than at grading time.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
