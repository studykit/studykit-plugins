# Decomposition Patterns

Provider-neutral guidance for choosing how to decompose work that is too large for a single task but still cohesive.

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

If none of these signals fire, the work is correctly sized as a single task; do not decompose. If at least one fires, pick the shape using the Decision rule below.

## Three patterns

When a single task is too large, decomposition takes one of three shapes. The shapes are mutually exclusive and the choice is body-shape-driven, not size-driven alone.

### 1. Sibling tasks (no parent)

Use when 2–3 tasks are peers with no shared coordination home.

Signals:

- Each member has its own anchor (use case, spec, or its own parent).
- No shared invariant, integration outcome, or cross-member decision links them.
- Sequencing constraints, when present, are pairwise and locally visible.

Layout: every member is a `task`. No parent issue is created.

### 2. Parent task with subtasks

Use when 2–3 subtasks are slices of one coherent implementation goal whose parent still passes as a `task`.

Signals (all should hold):

- Every subtask is a `task`.
- The parent body has a meaningful `Description`, `Unit Test Strategy`, and `Acceptance Criteria` at parent level — typically the parent UTS is the integration test for the joined goal and the parent AC is the observable outcome of the whole goal.
- All subtasks land in the same code area within roughly one PR cycle.
- Natural decomposition is two or three units. Four or more disqualifies this pattern.

Layout: the parent is a `task`; each subtask is a `task` linked to the parent with the `parent` relationship intent.

Parent body responsibilities:

- Parent `Acceptance Criteria` records the joined observable outcome; subtask AC are slices of that outcome.
- Parent `Unit Test Strategy` covers the integration scenario; subtask UTS cover their slice only.
- Do not duplicate subtask details in the parent body.

Do not use this pattern when:

- Members would mix types (`bug`, `spike`, `research`).
- The parent UTS does not make sense at parent level.
- The work requires four or more units.

### 3. Epic with member issues

Use when the parent is coordination-only and the work matches one of the recognized epic scopes defined in `./epic.md`.

Signals:

- The work matches one of the canonical epic scopes (feature initiative, platform / subsystem capability, migration or campaign, stabilization or quality initiative).
- Members may mix types (`task`, `bug`, `spike`, `research`).
- Integration-level outcome is not owned by any single member.
- Coordination, sequencing, or cross-member decisions need a shared home.

Layout: the parent is an `epic`; each member links with the `parent` relationship intent. See `./epic.md` for parent body rules.

## Decision rule

Pick in this order:

1. If the decomposition produces four or more units → **epic**.
2. If members would mix types, or the scope matches a recognized epic pattern → **epic**.
3. If the parent body would naturally pass as a task at parent level (`Description`, `Unit Test Strategy`, `Acceptance Criteria` all meaningful at parent level) and all subtasks are tasks → **parent task with subtasks**.
4. If 2–3 units share no parent-level invariant → **sibling tasks**.
5. Otherwise, the work is probably a single task; do not decompose.

The body-shape check at step 3 is the key discriminator between parent-task and epic. If the parent body cannot stand as a task without inventing filler content, the parent is an epic.

## Shared narrative

When a batch of work coordinates under a shared anchor, the shared context has a single home and member bodies do not duplicate it.

The shared home holds:

- Decisions across members.
- Integration constraints and integration-level outcomes.
- Shared blockers and sequencing choices.
- Scope changes that affect several members.

Member bodies record only the scope, acceptance criteria, and implementation notes specific to that member.

Where the shared home lives depends on the decomposition pattern:

- **Epic with member issues**: the epic body is the coordination summary; member issues link to it when their approach depends on epic-level narrative.
- **Parent task with subtasks**: the parent body owns the joined `Description`, the integration `Unit Test Strategy`, and the observable `Acceptance Criteria` at parent level.
- **Sibling tasks under a shared anchor** (use case, spec, parent task, or epic): the anchor is the shared home; sibling bodies stay scoped to their slice.

Use comments — on whichever issue owns the shared narrative — for discussion. Keep bodies as the current structured summary, not transcripts.

## Sibling relationships

These apply within any of the three patterns above when describing how member issues relate to each other.

- **Sequencing**: use the `blocked_by` relationship intent when one member must merge before another. Sequencing is provider-native; do not encode it in body sections when a native relationship is available.
- **Shared anchor**: when siblings deliver toward the same use case, spec, parent task, or epic, each member links to that anchor independently. The shared anchor is what makes them discoverable as a group.
- **Soft coupling**: use the `Related` body section for non-blocking, human-readable connections that help future readers locate adjacent work. Use sparingly and never to duplicate a native relationship.

## Common mistakes

- Using a parent task when the parent body has no meaningful Unit Test Strategy at parent level — promote to epic instead, or keep as a single task.
- Using an epic when the decomposition has only two cohesive task slices and the parent is implementation-coherent — use a parent task instead.
- Splitting into four sibling tasks without a parent — the missing coordination home is itself the signal to promote to epic.
- Duplicating subtask AC in the parent task body, or duplicating member AC in the epic body.
- Encoding sequencing only in human-readable body sections when a native blocking relationship is available.
