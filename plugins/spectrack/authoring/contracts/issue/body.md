# Issue Body Conventions

Body-level rules for issue-backed items (`task`, `bug`, `spike`, `epic`, `review`, and the issue side of `usecase` and `research`). Covers body structure, readability, reusable sections, and references for the visible issue body. Type-specific authoring files define each type's required body shape.

Use canonical Title Case section names only; the matching rendering convention defines the literal markup for headings, lists, inline emphasis, links, code, tables, and checklists.

## Section structure

An issue body is a sequence of named sections.

- Each section has a canonical Title Case name (`Description`, `Acceptance Criteria`, `Unit Test Strategy`, etc.) and starts with a level-2 heading. Subsections use deeper heading levels.
- Do not put a top-level title heading in the body when the issue title is stored separately.
- Avoid stray content above the first section unless the type template requires a short summary block.

## Tailoring the body

Beyond the required sections, an author may add purpose-specific Title Case sections when the issue has natural structure the type-defined sections do not capture. Keep each section narrow (one named thing) and the overall body short. A custom section earns its place only when its content would otherwise fold awkwardly into an existing one; if it fits naturally, fold it back in instead.

## Reference form

Use stable, readable references in body text.

| Target | Preferred body form |
| --- | --- |
| Issue-backed item | Issue reference from the selected issue backend |
| Knowledge page | Page, document, or file reference from the selected knowledge backend |
| External source | Native link form from the rendering convention |

- Prefer the shortest reference unambiguous in the configured project; use full URLs when a short reference would be ambiguous outside its source system.
- Do not require local file paths for targets whose canonical identity is not a local file.
- Do not introduce workflow-local numeric IDs when canonical identity already exists.
- Keep one referenced item per bullet in relationship lists.

## Relationship sections

Relationship body sections are defined by the type-specific authoring file or the matching rendering convention. Do not invent new relationship sections unless the selected authoring files require them.

## Optional reusable sections

`Related`, `Resume`, `Why Discarded`, `Out of Scope`, `Alternatives Considered`, and `Risks` are optional building blocks for any issue type. Include each only when its per-section guidance applies. A type-specific authoring file may pin one as required for a type, overriding this file's optional framing.

### `Related`

References that help interpret the issue but are not stored as native backend relationships. Use the native reference form of the configured issue or knowledge backend.

### `Resume`

Current-state snapshot for a future session. Use when an item is mid-flight and its state is not obvious from the body. Rewrite in place; do not preserve history.

Record only the delta against the rest of the body: where the actual state diverges from what the other sections describe, and what a future session could not reconstruct from them. Point at sections by name instead of restating them — when the work landed as the Implementation Steps and Verification sections describe, one line saying so plus any deviations is the whole snapshot, not a past-tense retelling of those sections.

Suggested slots:

- **Approach.** Current strategy.
- **Waiting for.** External input or sequencing note.
- **Open questions.** Items left open for downstream resolution — questions awaiting input, deferred work tracked elsewhere, follow-up candidates surfaced during this work, or lateral concerns observed but not addressed within this issue's scope.
- **Next.** Next concrete step.

### `Why Discarded`

Use when an issue is intentionally abandoned and backend status alone does not explain why. One dated bullet per reason, citing the cause when relevant.

### `Out of Scope`

Name what the issue explicitly does not cover. Use when the title or `Description` could read as covering broader work, or when a related concern was deliberately deferred to a follow-up. Skip when scope is already obvious from `Description` and `Implementation Steps`, or when the only deferred item is a generic disclaimer with no concrete follow-up. One deferred item per bullet with a short reason or follow-up link.

### `Alternatives Considered`

Record evaluated-but-rejected options with the rejection reason. Use when the chosen approach is non-obvious and a reviewer is likely to suggest a rejected option. Skip when no real alternatives were considered, or when the reasoning belongs in a curated knowledge page (update that page instead). One alternative per bullet; do not re-litigate the accepted decision.

### `Risks`

Name technical risks, regression hazards, or operational concerns specific to this issue. Use when the change touches load-bearing code, migrations, contracts, or behavior with non-trivial blast radius and the risk is not already covered by `Acceptance Criteria` or the test strategy. Skip for small routine changes, or when the risk is already represented by an `Open Questions` entry or test scenario. One risk per bullet with the mitigation or detection plan when known.

## Comments versus body

Use the body for the current structured issue content. Use comments, work notes, discussions, or history for conversation, progress notes, review threads, raw investigation notes, and audit facts. Do not copy long comment threads into the body — summarize the resulting decision or current state in the relevant body section.

## Runtime-grounded claims

A *runtime-grounded claim* is an assertion about runtime behavior that a
downstream decision rests on — a measurement, the output of a command, an
observed trace or render, or a fact about a compiled artifact (e.g. a
bytecode/line attribution). These are the claims most often wrong in practice,
because they are easy to assert from reasoning and easy to get wrong.

- Record the exact command or observation that produced the claim, together with
  its captured result — not an asserted expectation. "`gradlew test` fails with
  X" backed by the actual output, not "this should fail".
- A runtime-grounded claim that was never actually run is missing evidence, not
  weak evidence. Reasoning about the code is not a substitute for running the
  premise.
- Before building on a runtime-grounded claim — **including in the same session
  that recorded it** — confirm it empirically. Re-run the command and check the
  result still holds; when no existing command exposes the fact, add temporary
  logging or instrumentation at the decisive point, run, observe the actual
  value, then remove the instrumentation. The wrong-assumption failure mode is
  epistemic, not informational: a premise nobody executed stays unverified no
  matter how much context the implementer carries, so re-grounding is required
  even when the author and the implementer are the same session.

## Filesystem projections

If workflow tooling creates local files as projections of external issues, do not treat projection paths as canonical identity.

- Do not use projection paths in commits, branches, or comments unless the local path itself is the topic.
- Do not edit projection metadata as authoring state. Use backend fields through the selected backend workflow, and keep canonical references in visible body text.

## Cross-references

- `./common.md` — issue-backed item rules.
