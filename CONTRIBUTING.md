# Contributing to AIAI Skills

Thank you for your interest in contributing to AIAI Skills repository! Please ensure that your contribution follows our below guidelines.

## Adding Skills

### Before proposing a new skill

Many proposals overlap with an existing skill. Before opening one:

1. **Search the catalog.** Browse the [Skills board](./README.md#skills-board) and skim `skills/` for an existing skill that covers your idea, whole or in part.
2. **Check open PRs and issues** for proposals on the same topic. Don't add a duplicate.
3. **Read the anatomy.** Confirm your idea fits the format in `docs/skill-anatomy.md`: an actionable workflow with verification, not vague advice.
4. **Justify the gap in your PR description.** State explicitly why this isn't covered by an existing skill. If it overlaps, propose extending the existing skill instead of adding a new one.

### Creating Skill

A skill is a folder under `skills/`. The folder name is the skill name and must match
the `name` in its frontmatter.

1. Create `skills/<skill-name>/` (kebab-case).
2. Follow [skill-anatomy.md](./docs/skill-anatomy.md) to write `SKILL.md`: frontmatter, then the anatomy sections.
3. Add optional `references/`, `scripts/`, or `assets/` folders only if the skill needs them.
4. Self-review against the checklist in skill-anatomy.
5. Open a PR from a short-lived branch `skill/<name>` with a conventional commit message (`feat:`, `docs:`, `fix:`).

Do not edit the Skills board or Contributors sections in `README.md`. Both are generated
by `scripts/update-readme.py`, and the board picks up a new skill automatically once the
PR merges.

### Modifying Existing Skills

- Edit the skill in place; keep changes focused and minimal.
- Preserve the existing structure and tone.
- Keep YAML frontmatter valid after edits.
- If the change is a refinement, prefer a focused edit to that skill over a new folder.
- Open a PR from `skill/<name>`. The board refreshes automatically on merge; do not edit
  the generated sections by hand.


### Skill Quality Bar

A skill has to earn its place in an agent's context. It should be:

- **Focused**: one skill covers one kind of task. If it tries to cover two unrelated workflows, split it into two.
- **Strong constraints**: every rule states where it applies and where it does not, so the agent does not apply it blindly.
- **Safe**: the skill never invents facts and never skips verification. Destructive steps require explicit confirmation.
- **Cheap in context**: only what the agent needs to act. Move long material into `references/` so it loads on demand.

### What Not to Do

- Don't duplicate content between skills — reference other skills instead.
- Don't add skills that are vague advice instead of actionable processes.
- Don't create supporting files unless the skill content exceeds 100 lines.
- Don't put shared reference material inside skill directories — keep skill-local helpers in `skills/<name>/references/` only.

## Language

Skills, docs, and contributions should be written in English.

- Write `SKILL.md`, references, scripts output, and all documentation in English only.
- Do not submit translated copies of skills or docs. Translations drift out of sync as the originals evolve and cannot be maintained long-term.
- Code comments, identifiers, and commit messages are also in English.

## Checklist

Before opening a PR, confirm:

- [ ] Frontmatter `name` matches the directory name (kebab-case).
- [ ] Frontmatter `description` states what the skill does and when to use it.
- [ ] Every rule or step states where it applies and where it does not.
- [ ] Written entirely in English (no translated copies).
- [ ] File sizes respect the limits in [skill-anatomy.md](./docs/skill-anatomy.md).
- [ ] Skills board and Contributors sections left untouched (they are generated).
- [ ] PR comes from a short-lived feature branch with a conventional commit message.

## Submit your Contribution

1. Fork the repository.
2. Create a branch from `main`: `skill/<name>` for a skill, `docs/<topic>` for docs.
3. Add or modify the skill, then self-review against the checklist above.
4. Open a pull request targeting `main`.
5. After merge, the bot refreshes the Skills board and Contributors sections, and maintainers delete the merged branch.

Give the pull request a conventional title (`feat: add <skill-name>`, `docs: ...`) so the release notes group it correctly.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
