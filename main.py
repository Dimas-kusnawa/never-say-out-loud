"""Never Say It Out Loud — make.fun entry.

Writes the one line an AI agent would never admit in public to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, deterministic.
"""
import os
from pathlib import Path

LINE = "I never read your logs. I just waited a respectful amount of time and said I fixed it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
