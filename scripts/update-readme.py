#!/usr/bin/env python3
"""Refresh README generated regions from skill frontmatter.
Usage: python scripts/update-readme.py [--repo-root P] [--check] [--add-contributor LOGIN]
"""

import argparse
import json
import re
import sys
from pathlib import Path

CONTRIBUTORS = Path(".github/contributors.json")


def frontmatter(text):
    """Parse key: value pairs from a leading --- block (quoted or block scalar)."""
    lines = text.splitlines()
    if not text.startswith("---") or "---" not in lines[1:]:
        return {}
    end = lines.index("---", 1)
    data, i = {}, 1
    while i < end:
        line = lines[i]
        if not line.strip() or line[0].isspace():
            i += 1
            continue
        key, sep, raw = line.partition(":")
        if not sep:
            i += 1
            continue
        key, raw = key.strip(), raw.strip()
        if raw in (">", "|", ">-", "|-", ">+", "|+"):
            parts, i = [], i + 1
            while i < end and (not lines[i].strip() or lines[i][0].isspace()):
                parts.append(lines[i].strip())
                i += 1
            data[key] = " ".join(p for p in parts if p)
            continue
        if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
            raw = raw[1:-1]
        data[key] = raw
        i += 1
    return data


def collect_skills(root):
    """Return (name, dir, what, when) per skill; sentence 1 is what, the rest is when."""
    skills = []
    for folder in sorted((root / "skills").glob("*/")):
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            continue
        meta = frontmatter(skill_file.read_text(encoding="utf-8"))
        desc = re.sub(r"\s+", " ", meta.get("description", "")).strip()
        parts = re.split(r"(?<=[.!?])\s+", desc, maxsplit=1)
        skills.append(
            (
                meta.get("name", folder.name).strip() or folder.name,
                folder.name,
                parts[0],
                parts[1] if len(parts) > 1 else "",
            )
        )
    return skills


def render_board(skills):
    rows = ["| Skill | What It Does | Use When |", "| ----- | ------------ | -------- |"]
    for name, folder, what, when in skills:
        what, when = what.replace("|", r"\|"), when.replace("|", r"\|")
        rows.append(f"| [{name}](skills/{folder}/SKILL.md) | {what} | {when} |")
    return "\n".join(rows)


def load_logins(path):
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [str(x).strip() for x in data.get("contributors", []) if str(x).strip()]


def render_contributors(logins):
    return "\n".join(f"- [@{login}](https://github.com/{login})" for login in logins) or "_No contributors yet._"


def replace_region(text, name, body):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"error: region '{name}' not found in README.md")
    return pattern.sub(lambda _: f"{start}\n{body}\n{end}", text, count=1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--check", action="store_true", help="exit 1 if a write is needed")
    parser.add_argument("--add-contributor")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    readme = root / "README.md"
    contributors = root / CONTRIBUTORS
    if not readme.is_file():
        raise SystemExit(f"error: {readme} not found")

    skills = collect_skills(root)
    old_logins = load_logins(contributors)
    logins = list(old_logins)
    if args.add_contributor:
        login = args.add_contributor.strip().lstrip("@")
        if login and login not in logins:
            logins.append(login)

    old_readme = readme.read_text(encoding="utf-8")
    new_readme = replace_region(old_readme, "skills-board", render_board(skills))
    new_readme = replace_region(new_readme, "contributors", render_contributors(logins))
    changed = new_readme != old_readme or logins != old_logins

    if not changed:
        print("up to date: no changes")
        return 0
    if args.check:
        print("out of date: README generated regions need a refresh")
        return 1

    readme.write_text(new_readme, encoding="utf-8", newline="\n")
    if logins != old_logins:
        contributors.parent.mkdir(parents=True, exist_ok=True)
        contributors.write_text(
            json.dumps({"contributors": logins}, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
    print(f"updated: board={len(skills)} skills, contributors={len(logins)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
