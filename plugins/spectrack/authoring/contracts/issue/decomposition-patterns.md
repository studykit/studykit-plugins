# Decomposition Patterns

Use only when deciding whether one task should stay single, split, become a parent task, or become an epic.

## When to decompose

A single task is too large when it spans independent code areas, acceptance criteria, test surfaces, or assignable/sequenced work. If none fire, keep one task.

## Patterns

### Sibling tasks, no parent — 2–3 peer tasks with no shared coordination home

- Each member has its own anchor (use case, spec, or its own parent).
- No shared invariant, integration outcome, or cross-member decision links them.
- Sequencing constraints, when present, are pairwise and locally visible.

Every member is a `task`; no parent issue.

### Parent task with subtasks — 2–3 task slices of one coherent implementation goal

- Parent body has meaningful `Description` and integration-level `Acceptance Criteria`.
- All subtasks land in the same code area within roughly one PR cycle.
- Members are all `task`; mixed types or four+ units disqualify this pattern.

Link subtasks via the `parent` relationship intent. The parent `Acceptance Criteria` records the joined observable outcome; do not duplicate subtask details in the parent body.

### Epic with member issues — coordination parent

- Parent is coordination-only, not a task body.
- Four+ units, mixed member types, or canonical epic scope.
- Members may mix types (`task`, `bug`, `spike`, `research`).
- Integration-level outcome, sequencing, or cross-member decisions need a shared home.

The parent is an `epic`; each member links via the `parent` relationship intent.

## Decision rule

Pick in this order:

1. Four or more units → **epic**.
2. Members would mix types or the scope matches a recognized epic pattern → **epic**.
3. Parent body would naturally pass as a task (`Description` and integration-level `Acceptance Criteria` both meaningful at parent level) and all subtasks are tasks → **parent task with subtasks**.
4. 2–3 units share no parent-level invariant → **sibling tasks**.
5. Otherwise the work is probably a single task — do not decompose.

The body-shape check at step 3 is the key discriminator between parent-task and epic: if the parent body cannot stand as a task without inventing filler, the parent is an epic.

## Shared narrative

When a batch coordinates under a shared anchor, the shared context has a single home and member bodies do not duplicate it:

- **Epic with member issues**: the epic body is the coordination summary.
- **Parent task with subtasks**: the parent body owns the joined `Description` and integration-level `Acceptance Criteria`.
- **Sibling tasks under a shared anchor** (use case, spec, parent task, or epic): the anchor is the shared home; sibling bodies stay scoped to their slice.

## Sibling relationships

- **Sequencing**: use the `blocked_by` relationship intent when one member must merge before another. Sequencing is provider-native, so recording it through the native relationship is required.
- **Shared anchor**: when siblings deliver toward the same use case, spec, parent task, or epic, each links to that anchor independently — the shared anchor makes them discoverable as a group.
- **Soft coupling**: use the `Related` body section for non-blocking, human-readable connections. Use sparingly.
