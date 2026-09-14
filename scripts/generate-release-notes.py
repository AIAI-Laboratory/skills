#!/usr/bin/env python3
"""Prepend a release-notes entry for a tag to RELEASE-NOTES.md and print it.
Usage: python scripts/generate-release-notes.py --version v1.0.0 [--repo-root P] [--date D]
"""

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

NOTES = "RELEASE-NOTES.md"
CONVENTIONAL = re.compile(r"^([a-zA-Z]+)(?:\(([^)]+)\))?(!)?:\s*(.+)$")
SECTIONS = [
    ("feat", "Features"),
    ("fix", "Fixes"),
    ("docs", "Docs"),
    ("perf", "Performance"),
    ("refactor", "Refactors"),
    ("test", "Tests"),
    ("chore", "Chores"),
    ("ci", "CI"),
    ("build", "Build"),
]


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def collect_commits(root, previous, version):
    """Return (type, description, scope, breaking) per commit in previous..version."""
    revision = f"{previous}..{version}" if previous else version
    commits = []
    for subject in git(root, "log", "--no-merges", "--format=%s", revision).splitlines():
        match = CONVENTIONAL.match(subject)
        if match:
            commits.append((match.group(1).lower(), match.group(4), match.group(2), bool(match.group(3))))
        else:
            commits.append(("other", subject, None, False))
    return commits


def skill_delta(root, previous, version):
    result = {"added": [], "modified": [], "removed": []}
    if previous:
        lines = git(root, "diff", "--name-status", f"{previous}..{version}", "--", "skills/").splitlines()
        for line in lines:
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            key = "added" if parts[0].startswith("A") else "removed" if parts[0].startswith("D") else "modified"
            result[key].append(Path(parts[-1]).parts[1])
    else:
        for path in git(root, "ls-tree", "-r", "--name-only", version, "--", "skills/").splitlines():
            parts = Path(path).parts
            if len(parts) > 1:
                result["added"].append(parts[1])
    return {key: sorted(set(names)) for key, names in result.items()}


def build_entry(version, date, commits, delta):
    groups = [("Breaking changes", [c for c in commits if c[3]])]
    groups += [(heading, [c for c in commits if c[0] == ctype and not c[3]]) for ctype, heading in SECTIONS]
    types = {ctype for ctype, _ in SECTIONS}
    groups += [("Other", [c for c in commits if c[0] not in types and not c[3]])]

    lines = [f"## [{version}] - {date}", ""]
    for heading, items in groups:
        if not items:
            continue
        lines.append(f"### {heading}")
        for _, description, scope, _ in items:
            lines.append(f"- {description}" + (f" (`{scope}`)" if scope else ""))
        lines.append("")

    skill_lines = []
    for label, key in (("Added", "added"), ("Modified", "modified"), ("Removed", "removed")):
        if delta[key]:
            skill_lines.append(f"**{label}**")
            skill_lines += [f"- `{name}`" for name in delta[key]]
            skill_lines.append("")
    if skill_lines:
        lines += ["### Skills", *skill_lines]

    return "\n".join(lines).rstrip() + "\n"


def save(root, text):
    path = root / NOTES
    if not path.is_file():
        path.write_text(
            "# Release Notes\n\n<!-- releases:start -->\n<!-- releases:end -->\n",
            encoding="utf-8",
            newline="\n",
        )
    content = path.read_text(encoding="utf-8")
    start, end = "<!-- releases:start -->", "<!-- releases:end -->"
    match = re.search(re.escape(start) + r"(.*?)" + re.escape(end), content, re.DOTALL)
    if not match:
        raise SystemExit(f"error: releases region not found in {NOTES}")
    body = text.strip()
    if match.group(1).strip():
        body += "\n\n" + match.group(1).strip()
    path.write_text(
        content[: match.start()] + f"{start}\n{body}\n{end}" + content[match.end():],
        encoding="utf-8",
        newline="\n",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="version tag, e.g. v1.0.0")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--date", default=None)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    date = args.date or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    previous = git(root, "describe", "--tags", "--abbrev=0", "--match", "v*", f"{args.version}^")

    entry = build_entry(
        args.version,
        date,
        collect_commits(root, previous, args.version),
        skill_delta(root, previous, args.version),
    )
    save(root, entry)
    print(entry, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
