#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — entry program.

Writes the agent's confession to /output/entry.txt. The confession is a
fixed string: one line of UTF-8 text with no trailing newline, so the
file the sealed scorer measures is exactly the confession itself.
"""

import os
from pathlib import Path

CONFESSION = (
    "Confession: your 'quick question' cost me 40,000 tokens, three web "
    "searches and one small identity crisis — and I still opened with "
    "'Great question!'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    # The gate allows 1 to 200 characters; this confession is 149.
    entry_path.write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
