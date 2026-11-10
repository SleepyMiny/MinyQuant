#!/usr/bin/env python3
from pathlib import Path
import re
import unicodedata
ROOT = Path(__file__).resolve().parents[1]
files = list(ROOT.glob("*.md")) + list((ROOT / "docs").rglob("*.md"))
links = 0
for p in files:
    s = p.read_text()
    assert len(re.findall(r"^```", s, re.M)) % 2 == 0, p
    assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", s, re.M), p
    for target in re.findall(r"\]\(([^)]+)\)", s):
        if "://" in target:
            assert "github.com/SleepyMiny/MinyAI" not in target, (p, "private source dependency")
            continue
        path, _, anchor = target.partition("#")
        dest = p.parent / path if path else p
        assert dest.exists(), (p, target)
        links += 1
        if anchor:
            text = dest.read_text()
            ids = set(re.findall(r'<a\s+id="([^"]+)"', text))
            ids.update("".join(c for c in h.lower() if c in "-_ " or unicodedata.category(c)[0] in "LN").replace(" ", "-") for h in re.findall(r"^#{1,6}\s+(.+)$", text, re.M))
            assert anchor in ids, (p, target)
print(f"PASS: {len(files)} Markdown files, {links} local links/anchors")
