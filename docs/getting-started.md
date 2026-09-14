# Getting Started

## Install all skills

```bash
npx skills add AIAI-Laboratory/aiai-skills
```

## Install one skill

```bash
npx skills add AIAI-Laboratory/aiai-skills --skill <skill-name>
```

## Install manually

Clone the repo, then copy `skills/<name>/` into your agent's skill directory:

```bash
git clone https://github.com/AIAI-Laboratory/aiai-skills.git
```

- Claude Code: `~/.claude/skills/`
- OpenCode: `.opencode/skills/` or `~/.config/opencode/skills/`
- Cursor: `.cursor/skills/`
- Codex: `~/.codex/skills/`
- Antigravity: install as native plugin instead — `agy plugin install https://github.com/AIAI-Laboratory/aiai-skills.git`

## Use a skill

Point the agent at the skill (`SKILL.md` is the entry point) or let it discover the folder. Follow the skill's Process section and provide the Verification evidence it asks for.
