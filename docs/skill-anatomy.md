# Skill Anatomy

Format specification for skill files. Use this when you need to understand how a skill works or when contributing a new one.

## Skill Structure

```
.
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md        # required: main guideline
│       ├── references/     # optional: supporting materials that clarify specific topics or instructions
│       ├── scripts/        # optional: execution helpers for deterministic tasks
│       └── assets/         # optional: templates and files used in output
```

## SKILL.md Format

### Frontmatter (required)

```yaml
---
name: lowercase-hyphen-name
description: Guides agents through [task]. Use when [trigger].
---
```

Rules:

- `name` uses lowercase hyphens and **must equal the skill directory name** exactly.
- `description` starts with what the skill does (third person, strong verb, maximum 10 words), then includes at least one `Use when…` trigger condition. Total word count must be under 90 words. Agents select skills by reading descriptions, so a description without triggers never gets selected.
- **Sentence convention (used by the Skills board).** The first sentence becomes the "What It Does" cell; every sentence after it becomes the "Use When" cell. Keep triggers in the sentences after the first, and keep the first sentence free of triggers, so the generated board reads cleanly.
- Valid YAML. No tabs, no trailing spaces.

### Recommended Sections (in order)

These sections are recommended, not mandatory. A heading may differ as long as it carries the same meaning. A `SKILL.md` may grow supporting files or scripts when it needs them.

#### 1. Overview

What the skill does and why it matters, in 2–4 sentences. State the key principle (for example, "process, not prose"). This is not a tutorial, so save the how for Process.

#### 2. When to Use

Bullet list of triggering conditions. Include non-triggers: one or two `Do not use for…` lines prevent the most common misapplications.

#### 3. Process

Numbered steps in execution order. Each step needs:

- An imperative action ("Identify…", "Write…", "Run…"), not a vague verb ("Consider…", "Think about…").
- A checkpoint or exit criterion: how does the agent know the step is done?
- File paths and exact commands where applicable, never "appropriate handling" hand-waving.

#### 4. Specific Scenarios

Concrete cases the agent will meet, each with the expected behavior, written as a short before/after or a worked example. This section is optional: skip it when Process is already unambiguous, and keep it when a rule is easy to misapply.

#### 5. Verification

Evidence required before the skill counts as done: commands to run, expected outputs, file:line links. "Seems right" is never sufficient. If the skill produces files, list exactly which files must exist.

#### 6. Output Format

The exact shape of what the skill produces, shown as a small template: a file, a message, or stdout. Include it when the output is a structured artifact that another step or tool consumes, and skip it when Process already shows the output.

### Self-review Checklist

- [ ] `name` equals the directory name.
- [ ] `description` has a what-sentence first, then trigger sentences.
- [ ] Recommended sections present, in order.
- [ ] Every Process step has an exit criterion.
- [ ] Verification is executable and states the expected output.
- [ ] Every relative link resolves; no orphan `references/`, `scripts/`, or `assets/`.
- [ ] `SKILL.md` stays under 300 lines; long material moved to `references/`.

## Reference Standards

`references/` holds material the agent loads only when a step asks for it.

- One topic per file, kebab-case name (for example `python-advanced-programming.md`).
- Link each file from `SKILL.md` with a relative path, and say when to load it.
- Prefer a few focused files over one large dump; split when a file passes roughly 100 lines.
- A reference file that no step links to is dead weight. Delete it.

## Script Standards

`scripts/` holds runnable helpers the skill executes, not documentation.

- Prefer zero dependencies (standard library only), one clear purpose per script.
- Take inputs as arguments, not hard-coded paths.
- Exit non-zero on failure and print a one-line usage message on bad input.
- Document usage in a short header so the agent can call the script without reading the whole file.
- Add `scripts/` only when the skill runs code; never create an empty folder to match another skill.

## Common Mistakes

- Description without trigger conditions (skill never gets selected).
- `name` that does not match the directory name.
- Process steps with no exit criteria ("Add appropriate error handling").
- Background prose burying the workflow (overview longer than process).
- Verification that cannot be executed ("make sure it looks good").
- Supporting files that no step ever references.

## Naming Conventions

- Skill folder and frontmatter `name`: kebab-case, matching each other.
- Other files: kebab-case (`python-advanced-programming.md`, `update-readme.py`).
- `SKILL.md` is the only uppercase filename, and it is required.
- Headings: one `#` title at the top, then `##` sections. Do not skip levels.

## Context Efficiency

- Keep `SKILL.md` lean so it fits in context alongside the actual task.
- Move long examples, tables, and checklists into `references/` and load them on demand.
- State each rule once, in the section where it applies. Do not restate it elsewhere.
- Prefer file:line links and short snippets (15 lines or fewer) over pasted blocks.
