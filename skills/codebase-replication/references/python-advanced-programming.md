# Python — Advanced Programming Reference

Mining checklist + version gates for Python sources and targets. Load this file when either side is Python-majority.

## Versions

- Floor is `requires-python` in `pyproject.toml` (or runtime `python --version`). Never recommend syntax above the target's floor.
- Key gates: `X | Y` unions and `match` → 3.10+; `dataclass(slots=True)` → 3.10+; `StrEnum` → 3.11+; `asyncio.TaskGroup` / exception groups → 3.11+; `tomllib` (stdlib) → 3.11+; `TypeVar` default / `type` statement → 3.12+/3.13+.
- Third-party majors that change rules: Pydantic v1 vs v2, Django vs FastAPI, SQLAlchemy 1.x vs 2.x. Record exact versions.

## Type system & data modeling

- Typing posture: strict (`mypy --strict` / pyright) vs gradual; `Any` policy; params + returns annotated?
- Data carriers: `@dataclass` (frozen for DTOs?) vs `NamedTuple` vs Pydantic models vs plain classes; `__slots__` usage.
- Enums: `Enum` / `StrEnum` / `IntEnum`; generics via `TypeVar`, `Generic[T]`, `Protocol` vs `abc.ABC`.
- `None` handling: `Optional[X]` / `X | None`, sentinel vs exception vs result objects.

## Language features

- `async/await`: plain coroutines vs task groups, cancellation (`CancelScope` / timeouts), sync/async boundary discipline.
- Context managers (`with`, custom `__enter__`/`__exit__`, `contextlib`); generators (`yield`, `yield from`, async gens); comprehensions; walrus (`:=`) only where it aids readability; structural pattern matching (`match`) for dispatch, not for simple if/else.
- Decorators: custom + stdlib (`functools.lru_cache`, `cached_property`, `wraps` — missing `wraps` is a smell).

## Conventions

- Naming: files/modules `snake_case`, classes `PascalCase`, functions `snake_case` verbs, constants `UPPER`; private `_prefix`; `__all__` in package `__init__`.
- Imports: stdlib / third-party / first-party groups, absolute vs relative; no circular imports; no `import *` outside `__init__` re-exports.
- Docstrings: Google / NumPy / Sphinx style; required on public functions? Error handling: specific exceptions + `raise ... from e`, no bare `except`; logging via `logging` (module-level logger), never `print` in library code; early returns.

## Layout, tooling, tests

- Layout: flat vs `src/`; test mirror (`tests/`); config in `pyproject.toml` (black/ruff line length, isort profile, pytest settings).
- Tooling gates (P0 candidates): formatter (black/ruff format), linter (ruff/flake8), type-check (mypy/pyright) pass rates in CI.
- Tests: pytest style (plain asserts, fixtures vs factories), coverage expectations, marker conventions (`-m "not slow"`).

## Accidents to NOT promote

- Notebook/script-only idioms (`sys.path` hacks, top-level `input()`); test-only fixtures leaking into src rules; version-pinned workarounds for EOL Pythons (check recency).
