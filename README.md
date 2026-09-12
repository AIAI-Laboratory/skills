# Skills

High-quality agent skills for research and engineering.

Skills encode the workflows, quality gates, and best practices senior engineers use, packaged so AI agents follow them consistently.


---

## Why Skills?

AI coding agents default to the shortest path — skipping specs, tests, and reviews. Skills give agents structured workflows with steps, checkpoints, and verification so output stays production-grade.

Each skill is process, not prose: when to act, what to check, and what evidence is required before done.

---

## Quick Start

Use with any agent that accepts Markdown instruction files.

```bash
npx skills add AIAI-Laboratory/skills                         # install all skills
npx skills add AIAI-Laboratory/skills --skill <skill-name>    # install one skill
```

Or clone and copy manually:

```bash
git clone https://github.com/AIAI-Laboratory/skills.git
```

| Agent        | Install                                                                                               |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| Claude Code  | Copy `skills/*/` to `~/.claude/skills/` or use `/plugin` with this repo URL                           |
| OpenCode     | Copy `skills/*/` to `.opencode/skills/` or `~/.config/opencode/skills/`                               |
| Cursor       | Copy `skills/*/` to `.cursor/skills/`                                                                 |
| Antigravity  | Install as native plugin: `agy plugin install https://github.com/AIAI-Laboratory/skills.git`          |
| Codex        | Copy `skills/*/` to `~/.codex/skills/`                                                                |
| Other agents | Copy the skill folder contents into your agent's instruction directory, see `docs/getting-started.md` |

---

## Skills Board

| Skill                                                        | What It Does                                                                             | Use When                                                                           |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [codebase-replication](skills/codebase-replication/SKILL.md) | Learn conventions from a source repo and apply them to a target repo as rules plus audit | Learning from a repo, copying style, modernizing code like X, replicating patterns |

---

## How Skills Work

Every skill follows a consistent anatomy:

```
┌─────────────────────────────────────────────────┐
│  SKILL.md                                       │
│                                                 │
│  ┌─ Frontmatter ─────────────────────────────┐  │
│  │ name: lowercase-hyphen-name               │  │
│  │ description: Guides agents through [task].│  │
│  │              Use when…                    │  │
│  └───────────────────────────────────────────┘  │
│  Overview         → What this skill does        │
│  When to Use      → Triggering conditions       │
│  Process          → Step-by-step workflow       │
│  Verification     → Evidence requirements       │
└─────────────────────────────────────────────────┘
```

Key design choices:

- **Process, not prose.** Workflows with steps and exit criteria, not reference docs.
- **Verification is non-negotiable.** Tests passing, build output, or runtime data. "Seems right" is never sufficient.
- **Minimal.** Only what is needed to guide the agent.
- **Progressive disclosure.** `SKILL.md` is the entry point; supporting files load only when needed.

---

## Project Structure

```
.
├── skills/
│   └── codebase-replication/
│       └── SKILL.md
├── docs/
│   ├── getting-started.md
│   └── skill-anatomy.md
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## Contributing

Skills should be **specific** (actionable steps), **verifiable** (clear exit criteria), **battle-tested** (based on real workflows), and **minimal** (only what guides the agent).

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/skill-anatomy.md](docs/skill-anatomy.md).

---

## License

MIT — see [LICENSE](LICENSE).
