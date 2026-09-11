# TypeScript — Advanced Programming Reference

Mining checklist + version gates for TypeScript sources and targets. Load this file when either side is TypeScript-majority. (Node.js runtime concerns live in `nodejs-advanced-programming.md`; Next.js app concerns in `nextjs-advanced-programming.md`.)

## Versions

- Floor is `compilerOptions.target` + `lib` + `module` in `tsconfig.json`, plus the TS version in `package.json`. Never recommend syntax/lib APIs above the target's floor.
- Key gates: `strict` family (`strictNullChecks`, `noUncheckedIndexedAccess`) — record which flags are actually on; `satisfies` → 4.9+; `const` type params → 5.0+; decorators: legacy `experimentalDecorators` vs TC39 standard (5.x+) — never mix; `verbatimModuleSyntax` / `moduleResolution: bundler` vs `node16`.
- `target` below ES2020 with modern APIs used = missing `lib` entries or polyfill policy; note which.

## Type system & data modeling

- Strictness posture: full `strict` vs partial flags; `any` ban policy (`no-explicit-any`?), `unknown` preferred at boundaries with narrowing.
- Data shapes: `type` vs `interface` (record which the codebase prefers and where); discriminated unions for state machines; string-literal unions vs enums (enums only where reverse-mapping or framework requires).
- Generics: constraints (`extends`), defaults, inference-friendly signatures; utility types (`Pick`, `Omit`, `Partial` for construction, `Required`, `Awaited`, `ReturnType`) vs hand-rolled equivalents.
- Nullability: `strictNullChecks` discipline, optional chaining / nullish coalescing over `||` defaults (0/"" bugs), exhaustive narrowing (`never` checks in `default` branches).
- Validation at runtime boundaries: zod/valibot/io-ts schemas where external data enters; types alone are not validation (P1 for API inputs).

## Language features

- `async/await` throughout; no floating promises (`no-floating-promises` if enforced); `Promise.all` vs `allSettled` chosen deliberately; `AbortSignal` for cancellation.
- Destructuring + rest/spread for immutable updates; never mutate function params; `readonly` arrays/tuples at boundaries where codebase does it.
- Iterators/generators for lazy pipelines; `Map`/`Set` over object-as-map; `structuredClone` vs manual deep-copy.
- Modules: ESM `import`/`export` with `type` imports (`import type`) separated; no `require` in TS sources; barrel files (`index.ts`) only where the codebase uses them — note circular-import risk.

## Conventions

- Naming: files `kebab-case` (record actual case!), types `PascalCase`, functions/vars `camelCase`, constants `UPPER_SNAKE`; boolean `is/has/should` prefixes.
- Errors: typed error taxonomy (custom `Error` subclasses or result unions) vs `throw new Error(string)`; `unknown` in `catch`, narrowed before use; error chaining via `cause`.
- Logging: structured logger, never `console.log` in shipped code; log levels used consistently.
- Doc comments: TSDoc on exported APIs? Return style: early returns, guard clauses; function size discipline observed.

## Layout, tooling, tests

- Layout: feature folders vs technical layers; `src/` vs root; path aliases (`@/*`) in tsconfig — allowed directions follow folder structure.
- Tooling gates (P0 candidates): `tsc --noEmit` clean, ESLint (typescript-eslint strict?), formatter (Prettier/dprint), knip/unused-exports if present.
- Tests: Vitest/Jest conventions (describe/it vs test), `testing-library` patterns for UI, MSW for network boundaries; type-level tests (`expectTypeOf`) where present.

## Accidents to NOT promote

- `as any` / `@ts-ignore` escapes (legacy, demote); compiled `dist/` idioms; test-only mocks as src rules; pre-strict code in untouched files (check recency).
