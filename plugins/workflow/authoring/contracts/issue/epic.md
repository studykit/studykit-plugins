# Workflow Epic Authoring

A workflow epic is an **issue-backed coordination parent** for a larger goal delivered through multiple member issues.

The epic is not an implementation unit; the work belongs to its member issues. The parent body carries coordination narrative and integration-level outcomes, not a task-shaped implementation contract.

Epics are stored in the configured issue backend.

Companion contracts:

- `./body.md`
- Issue rules: `./authoring.md`
- Decomposition choice: `./decomposition-patterns.md`

## Storage role

`epic` is stored in the issue backend.

Use canonical issue identity. Do not use local integer ids.

## When to create an epic

Create an epic only when the work matches one of these canonical scopes:

- **Feature initiative** — a user-facing feature delivered through multiple coordinated members, with an integration-level outcome (such as end-to-end behavior or rollout gate) that no single member owns.
- **Platform or subsystem capability** — a new platform component or subsystem whose delivery requires multiple coordinated members with shared sequencing or interface decisions.
- **Migration or campaign** — moving from an old system to a new one, or applying a cross-cutting change across many call sites; member types are usually mixed (`task`, `bug`, `spike`, `research`).
- **Stabilization or quality initiative** — a coordinated effort to improve a quality dimension (flake reduction, observability rollout, deprecation cleanup) where the integration-level outcome is an external metric.

Do not create an epic when:

- One issue is enough.
- A spec, architecture, or domain page is the real home for the decision.
- The decomposition has only 2–3 task-typed slices and the parent body would naturally pass as a task — use a parent task with subtasks per `./decomposition-patterns.md` instead.
- Members are unrelated and have no shared narrative or anchor.

Parent task vs epic discriminator: the epic body cannot stand as a task. If a draft parent body would have a meaningful `Unit Test Strategy` and `Acceptance Criteria` at the parent level, the parent is a task, not an epic. See `./decomposition-patterns.md`.

The epic body is the home for shared narrative across member issues (decisions, integration constraints, shared blockers, sequencing, scope changes). See the Shared narrative section in `./decomposition-patterns.md`.

## Body shape

Required sections:

- `Description` — what the member issues together accomplish and why they are grouped.

Recommended sections:

- `Coordination Notes` — current decisions across member issues, constraints, or sequencing notes.

Optional sections:

- `Acceptance Criteria` — integration outcome not naturally owned by a single member issue; do not restate per-member criteria.
- `Resume` — current-state snapshot while open. See `./body.md`.
- `Why Discarded` — reason when discarded. See `./body.md`.

## Relationship to knowledge pages

Epics coordinate work. They do not define the product, architecture, or implementation contract.

Use knowledge pages for durable content:

- User-facing behavior → use case curated page.
- Implementation contract → spec.
- Component shape → architecture.
- Vocabulary → domain.
- Non-functional target → nfr.

If an epic discussion creates durable knowledge, update the relevant knowledge page and add a `Change Log` entry there.

## Completion criteria

Completion is author-judged; closing all member issues does not automatically close the epic.

An epic is complete when:

- The coordinated outcome has been reached or explicitly descoped.
- Member issues are closed, discarded, or moved elsewhere.
- Integration-level acceptance criteria are satisfied or explicitly waived.

## Common mistakes

- Using an epic as a spec or architecture document.
- Duplicating per-member-issue details in the epic body.
- Closing the epic while active member issues still depend on it.
- Nesting epics without explicit backend support and configuration.

## Do not

- Do not put implementation details or unit test strategy in the epic.
- Do not discard member issues automatically when discarding an epic.
- Do not store durable design decisions only in the epic; update the relevant knowledge page.
