#!/usr/bin/env python3
"""Pre-PR check: forbidden strings in the public site files, and asset presence.

Run with: python3 -I scripts/check_site.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Patterns are deliberately generic: this repo is public, so the exact private
# strings (street, phone, birth date, internal names) must not be written here.
FORBIDDEN = [
    r"A3.?Tk", r"Amadeus standard", r"System Software Architect",
    r"Device & Cloud", r"Senior Software & System Architect",
    r"exfiltrat", r"\b\d{2,4},? [Cc]hemin\b", r"\+33", r"\b0[67]([ .]?\d\d){4}\b",
    r"\bBorn\b", r"\b19[67]\d-\d\d-\d\d\b", r"\bTTA\b",
]
TEXT_FILES = ["index.html", "script.js", "styles.css", "README.md"]
ASSETS = ["assets/FiX-Kowalski-Resume.pdf", "assets/FiX-Kowalski-Detailed-CV.pdf"]

bad = 0
for name in TEXT_FILES:
    path = ROOT / name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for pat in FORBIDDEN:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            print(f"FORBIDDEN {pat!r} in {name}:{line}")
            bad += 1
for name in ASSETS:
    if not (ROOT / name).is_file():
        print(f"MISSING asset {name}")
        bad += 1
if "rel=\"canonical\"" not in (ROOT / "index.html").read_text(encoding="utf-8"):
    print("MISSING canonical link in index.html")
    bad += 1
print("OK" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
