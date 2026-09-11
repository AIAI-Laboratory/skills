# Skill Anatomy

Every `skills/<name>/SKILL.md` must have:

```yaml
---
name: lowercase-hyphen-name
description: Guides agents through [task]. Use when [trigger].
---
```

Sections in order:

1. `Overview` — what the skill does, 2–4 sentences.
2. `When to Use` — triggering conditions, bullet list.
3. `Process` — numbered steps with checkpoints and exit criteria.
4. `Verification` — evidence required (tests, build output, file:line links).

Rules: process over prose, no TODO/TBD, every claim needs evidence or an example.
