# Decomposition Patterns

Provider-neutral guidance for decomposing work that is too large for a single task but still cohesive.

Read with:

- `./common.md`
- `./task.md` when the parent is task-shaped
- `./epic.md` when the parent is coordination-only

## When to decompose

A single task is too large when it spans any of:

- Unrelated code areas.
- Independent acceptance criteria with no shared invariant.
- Independent test surfaces (different test files, fixtures, or runtimes).
- Work that can be assigned or sequenced independently.

If none fire, the work is correctly sized as a single task — do not decompose. If at least one fires, pick the shape with the Decision rule below.

## Three patterns

The shapes are mutually exclusive; the choice is body-shape-driven, not size alone.

### 1. Sibling tasks (no parent)

Use when 2–3 tasks are peers with no shared coordination home.

Signals:

- Each member has its own anchor (use case, spec, or its own parent).
- No shared invariant, integration outcome, or cross-member decision links them.
- Sequencing constraints, when present, are pairwise and locally visible.

Layout: every member is a `task`; no parent issue.

### 2. Parent task with subtasks

Use when 2–3 subtasks are slices of one coherent implementation goal whose parent still passes as a `task`.

Signals (all should hold):

- Every subtask is a `task`.
- The parent body has meaningful `Description` and `Acceptance Criteria` at parent level — typically the parent AC is the integration-level observable outcome of the joined goal, each criterion operationally checkable and implying the integration scenario.
- All subtasks land in the same code area within roughly one PR cycle.
- Natural decomposition is two or three units; four or more disqualifies this pattern.

Layout: the parent is a `task`; each subtask is a `task` linked via the `parent` relationship intent. The parent `Acceptance Criteria` records the joined observable outcome including the integration-level checks (subtask AC are slices). Do not duplicate subtask details in the parent body.

Do not use when members would mix types (`bug`, `spike`, `research`), the parent body cannot stand as a task (no meaningful integration-level `Acceptance Criteria` at parent level), or the work needs four or more units.

### 3. Epic with member issues

Use when the parent is coordination-only and the work matches a recognized epic scope in `./epic.md`.

Signals:

- The work matches a canonical epic scope (feature initiative, platform/subsystem capability, migration or campaign, stabilization or quality initiative).
- Members may mix types (`task`, `bug`, `spike`, `research`).
- Integration-level outcome is owned by no single member.
- Coordination, sequencing, or cross-member decisions need a shared home.

Layout: the parent is an `epic`; each member links via the `parent` relationship intent. See `./epic.md` for parent body rules.

## Decision rule

Pick in this order:

1. Four or more units → **epic**.
2. Members would mix types, or the scope matches a recognized epic pattern → **epic**.
3. Parent body would naturally pass as a task (`Description` and integration-level `Acceptance Criteria` both meaningful at parent level) and all subtasks are tasks → **parent task with subtasks**.
4. 2–3 units share no parent-level invariant → **sibling tasks**.
5. Otherwise the work is probably a single task — do not decompose.

The body-shape check at step 3 is the key discriminator between parent-task and epic: if the parent body cannot stand as a task without inventing filler, the parent is an epic.

## Shared narrative

When a batch coordinates under a shared anchor, the shared context has a single home and member bodies do not duplicate it. The shared home holds cross-member decisions, integration constraints and integration-level outcomes, shared blockers and sequencing choices, and scope changes affecting several members. Member bodies record only the scope, acceptance criteria, and implementation notes specific to that member.

Where the shared home lives:

- **Epic with member issues**: the epic body is the coordination summary; members link to it when their approach depends on epic-level narrative.
- **Parent task with subtasks**: the parent body owns the joined `Description` and the integration-level observable `Acceptance Criteria` at parent level.
- **Sibling tasks under a shared anchor** (use case, spec, parent task, or epic): the anchor is the shared home; sibling bodies stay scoped to their slice.

Use comments — on whichever issue owns the shared narrative — for discussion. Keep bodies as the current structured summary, not transcripts.

## Sibling relationships

These apply within any pattern when describing how member issues relate.

- **Sequencing**: use the `blocked_by` relationship intent when one member must merge before another. Sequencing is provider-native, so recording it through the native relationship is required.
- **Shared anchor**: when siblings deliver toward the same use case, spec, parent task, or epic, each links to that anchor independently — the shared anchor makes them discoverable as a group.
- **Soft coupling**: use the `Related` body section for non-blocking, human-readable connections. Use sparingly.

## Common mistakes

- Using a parent task when the parent body has no meaningful integration-level Acceptance Criteria at parent level — promote to epic instead, or keep as a single task.
- Using an epic when the decomposition has only two cohesive task slices and the parent is implementation-coherent — use a parent task instead.
- Splitting into four sibling tasks without a parent — the missing coordination home is itself the signal to promote to epic.
- Duplicating subtask AC in the parent task body, or member AC in the epic body.
- Encoding sequencing only in human-readable body sections without recording the native blocking relationship.
