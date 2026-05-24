# Workflow Use Case Authoring — Knowledge Side

This file covers the **knowledge side** of `usecase`: the curated knowledge page that carries the stable, citable use case content.

Common rules that apply across both sides (definition, dual-role overview, abstraction discipline) live in `./usecase-authoring.md`. Read that file in addition to this one.

Companion contracts:

- `./knowledge-body.md`
- Use case rules common to both sides: `./usecase-authoring.md`

## Storage role (knowledge side)

The curated page lives on the configured knowledge backend. Purpose: stable use case content used by implementation and testing. The curated page should link back to the workflow issue once published, and the workflow issue's `Current Draft` section should link to the curated page in turn.

## Curated page body

The curated use case page should contain the stable user-facing content.

Place a metadata line immediately under the page title that points back to the paired workflow issue, in the provider's link form. The metadata line should read `source: <link to paired workflow issue>`.

Required body sections:

- `Goal` — what the actor wants to accomplish.
- `Actors` — every actor that participates in this use case, with each actor's role.
- `Situation` — trigger and context.
- `Flow` — ordered list of user-visible steps and responses.
- `Expected Outcome` — observable successful outcome.

List every actor that participates in this use case under the `Actors` section. Use the same actor name across use cases when referring to the same role, so the actor catalog can be read off the curated pages.

Optional sections:

- `Validation` — user-visible input constraints, limits, or required formats.
- `Error Handling` — what the actor sees when things fail.
- `Related Work` — workflow issues, tasks, specs, or research.
- `Supersedes` — prior use case page when replacing one.
- `Change Log` — required for material updates. See `./knowledge-body.md`.

Do not include raw discovery discussion in the curated page; it belongs in the workflow issue or its comments.

## Publishing rule

Publish or update the curated page when:

- The actor and goal are clear.
- The flow is stable enough to guide tasks.
- Expected outcome is explicit.
- Blocking open questions are resolved or intentionally deferred.
- User-visible validation and error handling are known or explicitly out of scope.

The first publication should add a `Change Log` entry linking to the workflow issue.

## Splitting a use case (knowledge side)

When a use case splits, the knowledge-side follow-up is:

1. Publish or update curated pages when each child is stable.
2. Cross-link the new curated pages to one another via `Related Work`.
3. Do not use `Supersedes` unless an older published use case is being replaced wholesale.

## Common mistakes (knowledge side)

- Publishing a curated page before the user-visible flow is stable.
- Putting long discovery discussion into the curated page.
- Leaving the curated page without a `source:` link back to the workflow issue.

## Do not (knowledge side)

- Do not create the curated page before the workflow issue unless importing existing documents.
- Do not store use case discussion only in the knowledge page — discussion belongs on the workflow issue.
