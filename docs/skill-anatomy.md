# Skill Anatomy

Format specification for `SKILL.md` of every skill. Use this when you need to understand how a skill works or when contributing a new one.

## Skill Structure

```
.
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md        # required: main guideline
│       ├── references/     # optional: supporting materials that clarify specific topics or instructions
│       ├── scripts/        # optional: execution helpers for deterministic  tasks
│       └── assets/         # optional: templates and files used in output
```

## Frontmatter (required)

```yaml
---
name: lowercase-hyphen-name
description: Guides agents through [task]. Use when [trigger].
---
```

Rules:

- `name` uses lowercase hyphens and **must equal the skill directory name** exactly.
- `description` starts with what the skill does (third person, strong verb, maximum 10 words), then includes at least one `Use when…` trigger conditions. Total word count must be less than 70 word. Agents select skills by reading descriptions — a description without triggers never gets selected. <!-- notes: description must short but intent enough to distinct  -->
- Valid YAML. No tabs, no trailing spaces.

## Recommend Sections (in order)

<!-- These standards are recommend, not must to be exactly. Heading can be different as long as the same meaning. Maximum 200 lines. Can generate supporting files, script if neccessary -->

### 1. Overview

What the skill does and why it matters, in 2–4 sentences. State the key principle (e.g. "process, not prose"). This is not a tutorial — save the how for Process.

### 2. When to Use

Bullet list of triggering conditions. Include non-triggers: one or two `Do not use for…` lines prevent the most common misapplications.

### 3. Process

Numbered steps in execution order. Each step needs:

- An imperative action ("Identify…", "Write…", "Run…"), not a vague verb ("Consider…", "Think about…").
- A checkpoint or exit criterion — how does the agent know the step is done?
- File paths and exact commands where applicable, never "appropriate handling" hand-waving.

### 4. Specific Scenarios


### 5. Verification

Evidence required before the skill counts as done: commands to run, expected outputs, file:line links. "Seems right" is never sufficient. If the skill produces files, list exactly which files must exist.

<!-- checklist -->

## Common Mistakes

- Description without trigger conditions (skill never gets selected).
- `name` that does not match the directory name.
- Process steps with no exit criteria ("Add appropriate error handling").
- Background prose burying the workflow (overview longer than process).
- Verification that cannot be executed ("make sure it looks good").
- Supporting files that no step ever references.
<!-- fallback -->

## Reference Standards
<!-- create relevant file -->
Supporting files only when they keep the main SKILL.md focused

## Script Standards

## Naming Conventions

