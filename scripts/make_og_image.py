#!/usr/bin/env python3
"""Regenerate og-image.png (1200x630 link-preview image) with headless Chrome.

Usage: python3 -I scripts/make_og_image.py
Needs Google Chrome (macOS path below, or set CHROME). No Python dependencies.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
OUT = ROOT / "og-image.png"

HTML = f"""<!doctype html><meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;800&display=swap');
  html,body{{margin:0;width:1200px;height:630px}}
  body{{font-family:Inter,system-ui,sans-serif;color:#fff;display:flex;align-items:center;
    gap:64px;padding:0 90px;box-sizing:border-box;
    background:radial-gradient(circle at 20% 80%,rgba(14,165,233,.25),transparent 55%),
    linear-gradient(135deg,#0f172a 0%,#1e3a5f 55%,#0ea5e9 100%)}}
  img{{width:300px;height:300px;border-radius:50%;object-fit:cover;object-position:50% 18%;
    border:6px solid rgba(255,255,255,.85);flex:none}}
  h1{{font-size:84px;font-weight:800;letter-spacing:-3px;margin:0 0 18px}}
  p{{font-size:31px;font-weight:300;line-height:1.35;margin:0;color:rgba(255,255,255,.92)}}
  small{{display:block;margin-top:28px;font-size:26px;color:#7dd3fc}}
</style>
<img src="{(ROOT / 'fix-avatar.jpg').as_uri()}" alt="">
<div><h1>FiX Kowalski</h1>
<p>Senior Architect @ Amadeus<br>Agentic AI for self-healing cloud operations</p>
<small>github.asnowfix.fr</small></div>"""

with tempfile.TemporaryDirectory() as tmp:
    page = pathlib.Path(tmp) / "og.html"
    page.write_text(HTML, encoding="utf-8")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--virtual-time-budget=8000", "--window-size=1200,630",
        f"--screenshot={OUT}", page.as_uri(),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if not OUT.is_file():
    sys.exit("og-image.png was not created")
print(f"wrote {OUT}")
