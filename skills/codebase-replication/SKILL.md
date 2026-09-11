---
name: codebase-replication
description: Learn advanced coding rules, syntax idioms, design patterns, file management, and tooling conventions from a source repository and apply them to the user's repository as a reusable rules file plus reusable knowledge pack. Use this whenever the user says learn from this repo, copy style from, apply patterns from GitHub, modernize my code like X, replicate codebase, or gives a source repo path/URL plus a target repo. Always use for repo-to-repo style transfer even if they don't say skill.
---

# Codebase Replication

Learn evidenced conventions from a source repo, save them as a reusable knowledge pack, then apply to a target repo as rules + audit.

Why this works: most "style copying" fails by mistaking one-off code (accident) for convention (pattern), or by applying a rule where it doesn't belong. This workflow scores every candidate on evidence, records exactly where it applies, gates on versions, and saves the result so the next target repo reuses mining for free.

## Inputs

- **source**: local path OR GitHub URL. If URL: `git clone --depth 1 <url>` into OS temp (`$TEMP/codebase-replication/<name>`). Monorepo subdir or non-git folder: use as-is, note in header.
- **target**: repo to improve. Defaults to cwd. State assumption upfront ("Learning from `<source>` → `<target>` — say stop if wrong") and proceed.
- **scope**: domain emphasis — `ml | frontend | backend | api | cli | library | fullstack`. Auto-detect first (see Step 1); ask only if ambiguous: "Is this source mainly ml / backend / api / frontend / cli / library?" Scope changes what you weigh: ml → data/config/pipeline layout; frontend → components/hooks/naming; backend/api → DI/layering/error handling; cli → entry/arg parsing; library → public API surface + docs.

If source or target is missing, ask. Do not mine until both are resolved.

## 1. Detect scope

1. **Languages**: `glob` counts per extension. Analyze each language with >10% of files separately. For each such language that has a file in `references/`, load `<lang>-advanced-programming.md` and use its idiom checklist and version gates; languages without a reference use the generic checklist below.
2. **Domain scope**: read `README.md`, manifests (`pyproject.toml` / `package.json` / `pom.xml` / `build.gradle` / `tsconfig.json`), top-level dirs (`models/`, `pipelines/`, `src/components/`, `src/api/`, `src/cli/`). Pick one scope value. Record it in the knowledge-pack header.
3. **Versions (awareness starts here, not later)**: record source runtime + key deps (language version floor, package manager, framework majors). Every version-gated idiom later must cite its minimum (see the language reference; e.g. a syntax feature only valid above the target's version is never recommended). Check the target the same way; if no version file, check runtime or note assumption and stay conservative.
4. **Sample**: configs first (manifests, lint/format configs, `Makefile`, `Dockerfile`, `AGENTS.md`), then `glob` structure, then 5-10 representative files + 2-3 tests (<300 lines preferred). >500 files: note sampled dirs. <5 code files: read all, mark rules low-confidence.

### Checklist — mine these, don't freestyle

**A. Type system & data modeling** (check each, mark used/absent): static vs gradual typing and how strict, data-carrier style (record/dataclass/interface vs plain class), enum style (plain vs string/int-backed), generics, nullability handling (nullable types, optionals, null-object patterns).

**B. Language features**: the concurrency model (threads, async/await, event loop, virtual threads), resource management (context managers, try-with-resources, `using`/`defer` equivalents), metaprogramming (decorators, annotations, macros), iteration style (generators, iterators, streams, comprehensions), pattern matching / destructuring where the language supports it.

**C. Coding conventions**: naming (files, functions, classes, constants), function naming (verbs, `create_/from_/to_` style), visibility (private/public markers, export lists), module organization (import order, absolute vs relative), doc-comment convention (required on public APIs?), error handling (specific error types + chaining, no bare catches), logging (framework vs print, logger per module), return style (early return, null vs exception, result objects).

**D. Design patterns — identify when you see these triggers**:
- Requires multiple dependencies → DI container / constructor injection / service locator?
- Depends on configuration → factory / builder / strategy selected by config?
- Has multiple implementations → strategy / adapter / repository / plugin registry?
- Record the concrete shape ("services take `db` as first arg, never import global db; implementations registered in `<file>:<line>`"), not just the pattern name.

**E. File & folder architecture**: layout tree (`src/<pkg>/models|services|api|cli` or the stack's equivalent), test mirror, config location, max file length observed, naming case.

**F. Dependency rules**: allowed import directions (e.g. `api → services → models`, never reverse; `ui` never imports `server`). List 2-5 `allowed` + `forbidden` edges with evidence.

**G. Pattern context**: every rule must state applies-when AND not-when (e.g. "immutable data carriers for DTOs in `models/`; NOT for ORM/persistence entities which use the framework base class").

## 2. Mine source, separate pattern from accident

Candidate = anything from the checklist observed ≥1 time. Promote to rule only by metrics:

- **Frequency**: distinct files containing it (not hits in one file). Need ≥2 files; ≥3 files = strong.
- **Consistency**: uses ÷ opportunities. E.g. 8/10 data-only classes use the record/dataclass style = 80%. Need ≥70% in core `src/` to promote; 40-70% = weak/contextual; <40% = accident.
- **Location weight**: `src/` core counts full; `tests/` counts half (test-only idioms like bare fixtures don't become src rules); `scripts/`/`notebooks/` don't promote alone — mark `scripts-only`.
- **Recency**: if git available, check `git log -5 -- <files>`. Untouched >1yr + contradicted by newer files = legacy, demote to "Do NOT copy".

Promote if (freq ≥2 files AND consistency ≥70% in core) OR (freq ≥3 files). Otherwise keep as `observed once — not promoted` or `accident (low consistency)`. Record the four numbers per rule — that's what makes reuse trustworthy.

**Rule precedence** (higher wins on conflict, cite it in the audit):
- **P0 tooling-enforced** (formatter/linter/type-check fails without it)
- **P1 correctness/safety** (error handling, version-gated syntax, dependency direction)
- **P2 idiom consistency** (data carriers, path handling, logging, typing)
- **P3 preference** (doc-comment style, return style flourishes)
Never let P3 override P0/P1. If source contradicts itself, newest + P-highest wins; note the conflict.

## 3. Save knowledge pack and synthesize rules

1. **Save pack first** so future targets skip mining: write `<target>/.codebase-replication/knowledge/<source-slug>.json` (slug = repo name + short sha or date) with: scope, languages, versions, sampled files, rules `[R#]` each with {what, why, precedence P0-P3, context applies/not, version-min, evidence file:lines, metrics {freq, consistency, location, recency}, before/after snippet ≤15 lines}. Also write the human-readable `.md` twin. Reuse: if pack exists and source sha/date matches, load it and skip to Step 4.
2. **Rules file**: write `<target>/REPO-RULES.md` (or `AGENTS.md` if that's their convention) from this template:

```markdown
# Repo Rules (learned from <source> scope:<scope>)
> Source: <url/path> @ <sha or date>. Pack: `.codebase-replication/knowledge/<slug>.json`. Sampled: <dirs>.
> Versions: source <runtime> — rules gated accordingly.

## P0 Must-follow (tooling or 3+ files)
- [R1] [P0] [rule]. Context: applies in <x>; NOT in <y>. Min version: <v>. Evidence: `a.ext:10, b.ext:22`
  Why: <1 sentence>. Metrics: freq 3 files, consistency 90%, core, recent.
  Apply as: <before/after ≤15 lines>

## P1/P2 Should-follow
- [R4] [P2] ...

## File management + Dependency rules
- [R7] layout ... Allowed: `api→services`; Forbidden: `services→api`. Evidence: tree + imports.

## Tooling
- Format/Lint/Types/Tests with exact config values.

## Do NOT copy (accidents / legacy / source-specific)
- <thing> — reason: <low consistency | scripts-only | legacy | internal name>
```

3. Keep 5-15 rules. Merge duplicates. Re-read file; every rule needs ID, precedence, context, evidence, snippet — fix before auditing.

**Data-carrier example shape:**
Target has verbose hand-written data holders → rule `[Rn] [P2] Use the language's data-carrier idiom (see references) for data-only holders. Context: models/DTOs; NOT persistence entities.` with before (manual accessors/constructors) → after (idiomatic carrier) snippet.

## 4. Apply to target (report, don't refactor by default)

1. `glob` target, read 3-5 files in matching areas. Load the target language's `references/<lang>-advanced-programming.md` when one exists and use its gates while auditing.
2. Audit table in chat: `| File:line | Violates | Fix per [R#] (Pn) | Effort S/M/L |`. Cite precedence on conflicts; skip N/A cross-language syntax (map the idiom to the target language's equivalent or mark N/A; transfer layout/tooling anyway).
3. Default report-only. Auto-refactor only if asked: one rule at a time, smallest diff, run tests/lint.
4. Close with: rules path, pack path, top-3 fixes with file:line, what was NOT copied and why (accident/legacy/version), and "Want me to auto-apply [R#] to file Y?"

## Guardrails

- No rule without distinct-file evidence + metrics. Never attribute training-data idioms to the source.
- Version-gate everything new; check target version the same way as source (consult `references/` for per-language gates).
- Context is mandatory — a rule without applies/not-when is rejected.
- Lean snippets (≤15 lines), file:line links over pastes.
