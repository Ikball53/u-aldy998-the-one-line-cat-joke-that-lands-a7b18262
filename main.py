#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes exactly one joke line to /output/entry.txt:
a single line, under 200 characters, UTF-8, no trailing newline.
"""

from pathlib import Path

LINE = (
    "My cat knocked my coffee off the table, watched it shatter, "
    "then sat on my laptop and deleted 47 emails — and looked proud."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
