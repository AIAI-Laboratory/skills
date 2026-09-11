# Java — Advanced Programming Reference

Mining checklist + version gates for Java sources and targets. Load this file when either side is Java-majority.

## Versions

- Floor is `maven.compiler.release` / `sourceCompatibility` (or `--release`) in `pom.xml` / `build.gradle`. Never recommend syntax above the target's floor.
- Key gates: `var` → 10+; `switch` expressions → 14+; `record`, pattern-matching `instanceof` → 16+; sealed classes → 17+; pattern matching for `switch`, record patterns → 21+; virtual threads (`Thread.ofVirtual`), sequenced collections → 21+. Prefer LTS floors (8 / 11 / 17 / 21).
- Framework majors that change rules: Spring Boot 2 vs 3 (Jakarta namespace), JUnit 4 vs 5. Record exact versions.

## Type system & data modeling

- Data carriers: `record` for immutable DTOs vs classic POJO vs Lombok (`@Value`, `@Data` — note which the codebase chose and stay consistent); builders for many-optional-arg construction.
- Enums: rich enums with behavior vs constants; sealed hierarchies where the codebase models closed sets.
- Generics: bounded wildcards (`PECS`: producer-`extends`, consumer-`super`); no raw types (P1 finding).
- Nullability: `Optional` as return type (never fields/params), null-object vs exception; annotation-based nullness (`@NonNull`) if enforced by tooling.

## Language features

- Concurrency: `synchronized` / `Lock` vs `CompletableFuture` vs virtual threads; executor discipline (never unbounded pools in server code); `volatile`/`Atomic*` only where races were analyzed.
- Resources: try-with-resources (always for `AutoCloseable`); `var` for locals with evident types, explicit types at API boundaries.
- Streams: used for data pipelines, not for trivial loops or side-effectful iteration; collectors over manual accumulation.
- Annotations: custom vs framework; annotation processors noted in build config.

## Conventions

- Naming: packages lowercase, classes `PascalCase`, methods/fields `camelCase`, constants `UPPER_SNAKE`; getters/setters or records consistently.
- Modules: package-by-feature vs package-by-layer (record which; dependency rule follows it); no cycles between packages.
- Javadoc required on public APIs? Error handling: checked vs unchecked policy, exception translation at boundaries, never swallow (`catch (Exception e) {}` is P1); logging via SLF4J (parameterized, no string concat in hot paths), logger per class.
- Immutability default: `final` fields, unmodifiable collections at boundaries; `equals`/`hashCode`/`toString` complete for value types.

## Layout, tooling, tests

- Layout: Maven/Gradle standard (`src/main/java`, `src/test/java`) vs custom; module boundaries (`module-info.java` if JPMS).
- Tooling gates (P0 candidates): formatter (Spotless/palantir), Checkstyle/PMD/Error Prone, NullAway if present; CI gates.
- Tests: JUnit 5 style (`@DisplayName`? nested?), Mockito (strict stubs?), AssertJ vs JUnit asserts; test slices (`@WebMvcTest`, `@DataJpaTest`) vs full context; Testcontainers for integration.

## Accidents to NOT promote

- IDE-generated boilerplate committed once; `System.out.println` debugging; test-only Spring `@MockBean` patterns as src rules; pre-Java-8 idioms in files untouched for years (check recency).
