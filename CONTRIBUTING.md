# Contributing to AIAI Skills

Thank you for your interest in contributing to AIAI Skills repository! Please ensure that your contribution follows our below guidelines.

## Adding Skill

### Before proposing a new skill

Many proposals overlap with an existing skill. Before opening one:

1. **Search the catalog.** Browse the `All Skills` table in the `README.md` and skim `skills/` for an existing skill that covers your idea, whole or in part.
2. **Check open PRs and issues** for proposals on the same topic. Don't add a duplicate.
3. **Read the anatomy.** Confirm your idea fits the format in `docs/skill-anatomy.md`: an actionable workflow with verification, not vague advice.
4. **Justify the gap in your PR description.** State explicitly why this isn't covered by an existing skill. If it overlaps, propose extending the existing skill instead of adding a new one.

### Creating the skill

End to end, in order:

1. Scaffold `skills/<kebab-case-name>/` and copy the skeleton from `docs/skill-anatomy.md`.
2. Write the frontmatter (`name` equals the directory; `description` states what + `Use when` triggers).
3. Write the four anatomy sections: Overview, When to Use, Process, Verification.
4. Add optional folders (`references/`, `scripts/`, `assets/`) only if the skill needs them.
5. Self-review against the checklist in `docs/skill-anatomy.md`.
6. Add one row to the `All Skills` table in `README.md`.
7. Open a PR from a short-lived feature branch (`skill/<name>` for skills, `docs/<topic>` for docs) with a conventional commit message (`feat:`, `docs:`, `fix:`).

### Skill Quality Bar

Skills should be:

- **Specific** — Actionable steps, not vague advice.
- **Verifiable** — Clear exit criteria with evidence requirements.
- **Battle-tested** — Based on real workflows, not theoretical ideals.
- **Minimal** — Only the content needed to guide the agent correctly.

### Structure

Every new skill must have:

- `SKILL.md` in the skill directory.
- YAML frontmatter with valid `name` and `description`.
- These sections: Overview, When to Use, Process, Verification.

### What Not to Do

- Don't duplicate content between skills — reference other skills instead.
- Don't add skills that are vague advice instead of actionable processes.
- Don't create supporting files unless the skill content exceeds 100 lines.
- Don't put shared reference material inside skill directories — keep skill-local helpers in `skills/<name>/references/` only.

## Modifying Existing Skills

- Keep changes focused and minimal.
- Preserve the existing structure and tone.
- Test that YAML frontmatter remains valid after edits.
- If your idea is a refinement of an existing skill, prefer a focused edit to that skill over a new directory.

## Skill's Directory Structure

```
.
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md        # required entry point
│       ├── references/     # optional: docs loaded on demand
│       ├── scripts/        # optional: runnable helpers only
│       └── assets/         # optional: templates and files used in output

```

Rules:

- One skill = one folder, one `SKILL.md` entry point.
- Optional folders and when to use them:
  - `references/` — supporting docs the agent loads only when needed (progressive disclosure).
  - `scripts/` — runnable helpers the skill executes. Add only when the skill includes them; never an empty `scripts/` just to match another skill.
  - `assets/` — templates, boilerplate, or static files the skill uses in its output.
- Skill-local helpers go in `skills/<name>/references/`, not repo-level folders.
- Do not add repo-level `agents/`, `references/`, `commands/`, or `hooks/` without 3+ skills needing them.
- English only.

## Language

Skills, docs, and contributions must be written in English.

- Write `SKILL.md`, references, scripts output, and all documentation in English only.
- Do not submit translated copies of skills or docs. Translations drift out of sync as the originals evolve and cannot be maintained long-term.
- Code comments, identifiers, and commit messages are also in English.

## Checklist

Before opening a PR, confirm:

- [ ] Frontmatter `name` matches the directory name (kebab-case).
- [ ] Frontmatter `description` states what the skill does and when to use it.
- [ ] All four anatomy sections present: Overview, When to Use, Process, Verification.
- [ ] Every rule or step states where it applies and where it does not.
- [ ] `README.md` skills table has a row for the new skill.
- [ ] Written entirely in English (no translated copies).
- [ ] No org names, no TODO/TBD placeholders.
- [ ] File sizes respect the Quality Standards below.
- [ ] PR comes from a short-lived feature branch with a conventional commit message.

## Quality Standards

- One file must not be over 200 lines.
- Code snippets are lean (15 lines or fewer) and each rule cites evidence (`file:line`) where applicable.
- No broken links: every relative link must resolve from the repo root.

## Reporting Issues

Open an issue if you find:

- A skill that gives incorrect or outdated guidance.
- Missing coverage for a common workflow.
- Inconsistencies between skills.

Include the affected skill, the relevant excerpt, your context, and what you did instead.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
