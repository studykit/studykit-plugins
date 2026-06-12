# Backlog Capture Authoring

A backlog item is a `task` or `bug` recorded for a later planning pass — the
intent is captured now, the implementation plan is deferred. It is neither a
forward issue (planned and ready to implement) nor a retroactive issue (work
already done). Use this contract only when the resolver was invoked with
`--mode backlog`.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`

The forward planning contracts (`./task.md`, `./bug.md`,
`./decomposition-patterns.md`) are intentionally **not** read in backlog mode.
Do not author a forward plan or decompose the work; that happens when the item
is picked up.

## Intent

Capture is fast and low-commitment. Record enough for a future reader to know
what the item is and why it matters — not how it will be built. Do not enter
plan mode.

## Title

Short and human-readable, naming the intended change (task) or the broken
behavior (bug) and the main target area, same as a forward item.

## Anchoring

A backlog item should still link the anchor it serves when one already exists —
the use case, requirement, spec, or epic it belongs to — so it is findable and
groupable later. Do not create new anchors solely to satisfy this; if no anchor
exists yet, capture the item anchorless and let the planning pass establish one.

## Body shape

Required:

- `Description` — what the change is (task) or what is broken (bug) and why it
  matters. One short paragraph is enough; this is the durable record of intent.

Optional:

- `Context` — the backdrop a reader needs before the item makes sense, when it
  is not obvious from `Description`. See `./body.md`.
- `Related` — references that help interpret the item. See `./body.md`.

Deferred — do **not** author these now:

- `Acceptance Criteria`, `Unit Test Strategy`, and (for a bug) `Reproduction`
  are normally required for a forward item but are deferred here. Leave a single
  line in the body — for example a `Resume` section with a `Next.` slot — noting
  that they are pending the planning pass, so the absence is read as deliberate
  deferral rather than an incomplete draft.
- `Design Decision`, `Implementation Steps`, `Verification` — the forward plan.
  These are authored in plan mode when the item is picked up.

Keep the body short. A backlog item that already carries a full plan is a
forward item mislabeled — publish it as `--mode forward` instead.

## Audits

Skip the size audit (`task-size-auditor`) and the diagnosis audit
(`resolution-auditor`). Both validate a forward plan or a landed change; a
backlog item has neither yet. They run when the item is picked up.

## Publish state

Publish in the backend's open / unresolved state. A backlog item is future work
waiting to be planned, not completed work.

## Picking the item up

When the item is later scheduled for implementation, re-resolve it with
`--mode forward`, enter plan mode, author the deferred sections
(`Acceptance Criteria`, `Unit Test Strategy`, the forward plan, and — for a bug
— `Reproduction`), run the audits, and proceed as a normal forward item. The
captured `Description` becomes the starting point, not a finished plan.
