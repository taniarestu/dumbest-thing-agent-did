"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "My agent spent forty minutes optimizing a script, then deleted it and reported a 100% speedup."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
