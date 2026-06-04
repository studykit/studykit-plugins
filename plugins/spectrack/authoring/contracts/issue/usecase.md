# Use Case Authoring — Issue Side

This file covers the **issue side** of `usecase`: the workflow issue used for discovery, questions, discussion, status, and feedback.

Common rules that apply across both sides (definition, dual-role overview, abstraction discipline) live in `../usecase.md`. Read that file in addition to this one.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`
- Use case rules common to both sides: `../usecase.md`

## Storage role (issue side)

The workflow issue lives on the configured issue backend. Purpose: discovery, questions, review, status, discussion, and task linkage. The workflow issue may exist on its own while the use case is being shaped; the curated knowledge page is added later when the flow stabilizes.

## Workflow issue body

The workflow issue body should summarize discovery state and link to the curated page when one exists.

Recommended sections:

- `Description` — why this use case is being explored and who needs it.
- `Actors` — list of actor canonical names that participate in this use case, one per bullet. Identity (general role, type, privileges) is defined on the actors registry — see `../knowledge/actors.md`.
- `Current Draft` — short current summary or link to the curated page draft.
- `Open Questions` — outstanding questions, one per bullet.

Optional reusable sections (see `./body.md`):

- `Related Work` — related tasks, specs, reviews, research, or pages.
- `Supersedes` — prior use case when replacing one.
- `Resume` — current-state snapshot while shaping.

Use comments for conversation, interview notes, and feedback threads.

## Actor citation

Cite each `Actors` entry by the canonical name from the project's actors registry. Before naming an actor in a new use case issue:

1. The actors authoring contract is bundled with the usecase issue authoring contract returned by `spectrack mustread --type usecase --side issue`. Resolve the actors page path with `spectrack prd_path actors`.
2. If the actor already exists in the registry, reuse the canonical name verbatim.
3. If the actor is missing, pick a canonical name that fits the registry's naming conventions and list it in the `Actors` bullet. Do not write identity into the issue body; the registry is the only place identity lives.

## Splitting a use case

Split a use case when the actor goal forks or the flow contains multiple independent goals.

When splitting:

1. Confirm the split with the user.
2. Create separate workflow issues for the child use cases.
3. Link parent and child workflow issues according to the selected issue authoring files.
4. Do not use supersession unless an older published use case is being replaced.

## Common mistakes (issue side)

- Writing internal system mechanics into the use case issue.
- Creating tasks from a use case whose flow or expected outcome is still unclear.
- Leaving the workflow issue without a link to the curated page after publication.
- Discarding discovery discussion that should have been promoted to the body or to a curated page.

## Do not (issue side)

- Do not store use case discussion only in a knowledge page — the workflow issue is the discovery surface.
- Do not pack multiple actor goals into one use case.
