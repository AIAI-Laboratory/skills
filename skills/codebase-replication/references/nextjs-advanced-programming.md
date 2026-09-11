# Next.js — Advanced Programming Reference

Mining checklist + version gates for Next.js sources and targets. Load this file when either side is Next.js-majority. (Type-system concerns in `typescript-advanced-programming.md`; server-runtime concerns in `nodejs-advanced-programming.md`.)

## Versions

- Major in `package.json` (`next`, `react`, `react-dom`) — majors change rules: App Router (13+), `metadata` API, server actions (14 stable), async `params`/`searchParams` (15+), Turbopack. Never recommend APIs above the target's major.
- Router model: App Router (`app/`) vs Pages Router (`pages/`) — record which; never mix data-fetching idioms across them.

## Rendering & data flow

- Server-first by default: React Server Components for data + static rendering; `'use client'` only at the leaves that need interactivity (record the codebase's boundary convention).
- Data fetching: `fetch` with cache options (`force-cache`, `no-store`, `revalidate`), colocated with the component that needs it; no waterfall-by-default (parallel `Promise.all`, preloading patterns); `loading.js` / `error.js` / `not-found.js` conventions where present.
- Server actions: `'use server'` placement (file vs inline), argument validation inside the action, `revalidatePath`/`revalidateTag` after mutations; never trust client-passed IDs without authorization checks (P1).
- Caching/invalidation: which cache layers the codebase relies on (Data Cache, Full Route Cache, Router Cache) and its revalidation strategy; `cookies()`/`headers()` mark dynamic — note where the codebase opts into dynamic.

## Routing & structure

- Route groups `(...)`, private folders `_...`, parallel routes `@...`, intercepting routes `(..)` — used sparingly and consistently; layouts nest shared UI, templates reset state (record which pattern where).
- `metadata` / `generateMetadata` for SEO; `viewport` export; sitemap/robots conventions.
- Middleware: auth/session gating, matcher scope kept tight; Edge vs Node runtime declared per route (`export const runtime`) where it matters.
- Env: `NEXT_PUBLIC_` only for truly public values; server secrets never prefixed; validation at boot.

## UI & performance

- `next/image` (sizes, priority for LCP, remotePatterns), `next/font` (self-hosted, no render-blocking Google Fonts link), `next/script` strategies — record which the codebase enforces.
- Bundle discipline: client components kept small; heavy libs dynamically imported (`next/dynamic`, `ssr: false` only with reason); analyze via `@next/bundle-analyzer` if present.
- Forms: controlled vs uncontrolled convention; server-action forms with `useActionState` pending/error states; accessible labels, focus management after mutations.

## Layout, tooling, tests

- Layout: `app/` colocation (component + styles + tests per route) vs shared `components/`/`lib/`; allowed import directions (`app` → `components`/`lib`, never reverse).
- Tooling gates (P0 candidates): `next lint` / ESLint `next/core-web-vitals`, `tsc --noEmit`, build (`next build`) green in CI; `next.config.js` flags recorded (strictMode, images, experimental).
- Tests: component tests (Vitest + Testing Library), E2E (Playwright/Cypress) for critical flows; MSW for API boundaries; no testing of framework internals.

## Accidents to NOT promote

- `'use client'` on whole pages out of habit (demote to leaf-level); `getServerSideProps` patterns copied into App Router; `useEffect` data fetching where RSC fetch belongs; committed `.env.local` (flag immediately, do NOT copy); version-pinned workarounds for pre-13 Next (check recency).
