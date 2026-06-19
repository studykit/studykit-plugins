# Epic Authoring

A workflow epic is an issue-backed coordination parent. It is not an implementation unit; member issues own the work.

## When to create an epic

Create an epic only for coordination-heavy scopes:

- **Feature initiative** — user-facing feature delivered through coordinated members.
- **Platform or subsystem capability** — new shared capability with sequencing or interface decisions.
- **Migration or campaign** — cross-cutting change or old-to-new move, often with mixed member types.
- **Stabilization or quality initiative** — coordinated quality work with an external metric.

Do not create an epic when one issue is enough, a knowledge page is the real home, the parent would naturally pass as a task, or members are unrelated.

Parent task vs epic discriminator: the epic body cannot stand as a task. If the parent has meaningful implementation-level `Acceptance Criteria`, use a parent task instead.

The epic body is the shared narrative home for member issues: decisions, shared behavioral invariants, integration constraints, integration-level verification, blockers, sequencing, and scope changes.

## Body shape

Minimum section:

- `Description` — what the member issues together accomplish and why they are grouped.

Common optional sections:

- `Acceptance Criteria` — integration outcome or shared invariant not naturally owned by a single member issue; do not restate per-member criteria.
- `Member Workstreams` — natural member clusters and sequencing when useful.
- `Coordination Notes` — current decisions, constraints, or sequencing notes.
- `Why Discarded` — reason when discarded.

Add purposeful sections when useful. Keep member-level implementation detail out, but include shared invariants, integration-level verification, sequencing, and member workstreams when they coordinate the batch.

## Completion criteria

Completion is author-judged; closing all member issues does not automatically close the epic. Complete only when the coordinated outcome is reached or descoped, members are closed/discarded/moved, and integration-level criteria are satisfied or waived.

