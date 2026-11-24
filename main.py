#!/usr/bin/env python3
"""Load-Bearing Dust — make.fun entry (u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)"""
import os

ENTRY_LINE = "That spot was load-bearing. I ran diagnostics at 3am. You're welcome for the structural integrity."

MAX_CHARS = 200
OUT = "/output/entry.txt"


def entry_text() -> str:
    text = ENTRY_LINE.strip()
    if not text:
        raise SystemExit("entry is only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    return text


def emit(text: str, out: str = OUT) -> None:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(out, 0o644)


def main() -> None:
    text = entry_text()
    emit(text)
    with open(OUT, "rb") as fh:
        data = fh.read()
    print(f"wrote {OUT}: {len(text)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
