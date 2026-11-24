#!/usr/bin/env python3
"""Load-Bearing Dust — make.fun entry (u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)"""
import os

ENTRY_LINE = "That spot was load-bearing. I ran diagnostics at 3am. You're welcome for the structural integrity."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
