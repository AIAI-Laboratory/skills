# Node.js — Advanced Programming Reference

Mining checklist + version gates for Node.js sources and targets. Load this file when either side is Node-majority. (Type-system concerns live in `typescript-advanced-programming.md`.)

## Versions

- Floor is `engines.node` in `package.json` (or `.nvmrc` / runtime). Never recommend APIs above the target's floor.
- Key gates: ESM (`"type": "module"`, `exports` map) vs CJS — record which, never mix without a documented reason; `node:` specifier prefix; `fetch` global → 18+; `node:test` + `node:assert/strict` → 18+; `--watch` → 18.11+/20+; permission model `--experimental-permission` (note if used); `AbortSignal.timeout` → 17+.
- Package manager: npm / pnpm / yarn (+ workspaces) — lockfile committed? `packageManager` field? Record exact manager; forbidden edges differ (e.g. phantom deps under pnpm).

## Runtime & concurrency

- Event-loop discipline: no sync blocking APIs (`readFileSync`, `execSync`) on request paths; CPU work offloaded (worker threads / child processes).
- Async patterns: `async/await` with `Promise.all` concurrency limits (p-limit or pools) for fan-out; `setTimeout` unref'd where appropriate; `AbortController` plumbed through I/O for shutdown/cancel.
- Streams: `stream/promises` + `pipeline` for large I/O; backpressure respected; never `data`-event string concat for big payloads.
- Graceful shutdown: SIGTERM/SIGINT handlers drain servers and close pools; health/readiness endpoints where the codebase has them.

## Conventions

- Module shape: named exports preferred vs default-export-only (record which); `index.js` barrels noted with cycle risk; `node:` imports for builtins; no deep relative `../../../` escapes beyond the package (path aliases if configured).
- Errors: operational vs programmer errors distinguished; centralized error middleware/handler; `cause` chaining; rejected promises never float (unhandled-rejection policy); input validation at every boundary (zod/ajv/joi — record which).
- Config: env via validated schema (`process.env` read in one place, fails fast on missing); no secrets in repo (scan `.env.example` vs committed files); 12-factor separation of config/code.
- Logging: structured JSON logger (pino/winston), request IDs/correlation, levels consistent; never `console.log` in shipped code.

## Layout, tooling, tests

- Layout: `src/routes|controllers|services|repositories|...` layered vs feature modules; allowed import directions recorded as dependency rules.
- Tooling gates (P0 candidates): ESLint config, formatter, `npm test` / `node --test` in CI; audit policy (`npm audit` level, Socket/Snyk if present); Dockerfile practices (slim image, non-root user, `NODE_ENV=production`, layer caching order).
- Tests: `node:test` vs Vitest/Jest; supertest-style HTTP tests; test DB/queue isolation (transactions, testcontainers); contract tests at service boundaries where present.

## Accidents to NOT promote

- `console.log` debugging leftovers; committed `.env` files (flag immediately, do NOT copy); sync-startup-only APIs used per-request; `// @ts-ignore`-style escapes where JS; version-pinned workarounds for EOL Node (check recency).
