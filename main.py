"""Write the make.fun entry text to entry.txt."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


def output_dir() -> Path:
    """Return the destination folder.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is the fallback, then /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        raw = os.environ.get(name)
        if raw:
            return Path(raw)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
