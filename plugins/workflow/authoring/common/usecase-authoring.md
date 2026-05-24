# Workflow Use Case Authoring — Common

A workflow use case describes **how an actor interacts with the system to achieve a goal in a specific situation**, with a user-visible flow and expected outcome.

Use case is a dual-role type: it has an **issue side** (discovery, questions, status, discussion, feedback) and a **knowledge side** (curated page that downstream tasks and specs cite). The workflow issue is always created first; the curated knowledge page is created or updated later when the user-visible flow is stable enough to be cited.

This file carries the rules that apply across both sides. Role-specific rules live in the companion contracts.

Companion contracts:

- Issue side: `./usecase-issue-authoring.md`
- Knowledge side: `./usecase-knowledge-authoring.md`
- Abstraction guard (conversion table + per-field obligations): `./usecase-abstraction-guard.md`

## Abstraction discipline

Use cases stay at the user level on both surfaces — the issue body and the curated page.

Write:

- What the actor does.
- What the actor sees.
- What outcome the actor expects.
- User-visible validation and error behavior.

Do not write:

- Database tables.
- Queue names.
- Service internals.
- Framework mechanics.
- Implementation algorithms.

Internal mechanics belong in `architecture`, `spec`, or implementation tasks.

For concrete before/after rewrites and the per-field abstraction obligations, see `./usecase-abstraction-guard.md`.
