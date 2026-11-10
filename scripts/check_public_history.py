#!/usr/bin/env python3
"""Reject personal email in reachable history, without printing matched values."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True)
EMAIL = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
def allowed(value):
    return value.lower().endswith("@users.noreply.github.com")
def private_email(text):
    return any(not allowed(value) for value in EMAIL.findall(text))
errors = []
seen = set()
commits = git("rev-list", "--all").splitlines()
if not commits:
    raise SystemExit("FAIL: no commit history to inspect")
for sha in commits:
    author, committer, body = git("show", "-s", "--format=%ae%n%ce%n%B", sha).split("\n", 2)
    if not allowed(author) or not allowed(committer) or private_email(body):
        errors.append(f"{sha[:7]}: non-noreply commit identity or message")
    for line in git("ls-tree", "-r", sha).splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, blob = meta.split()
        if kind != "blob" or blob in seen:
            continue
        seen.add(blob)
        content = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", blob]).decode("utf-8", errors="replace")
        if private_email(content):
            errors.append(f"{sha[:7]}:{path}: non-noreply email in tracked content")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(commits)} commits, {len(seen)} unique blobs; noreply identities and no personal-email patterns")
