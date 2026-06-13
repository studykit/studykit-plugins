# Backlog Capture Authoring

A backlog item is a `task` or `bug` recorded as an **open spec** — the
not-yet-done work captured now, to be picked up for implementation later. It is
not a retroactive item (work already done). Use this contract only when the
resolver was invoked with `--mode backlog`, alongside the type spec contract
(`./task.md` or `./bug.md`), which defines the spec sections this framing tells
you how to fill.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`
- Type spec: `./task.md` or `./bug.md`

## Intent

Capture is flexible and low-commitment. Record the spec at whatever level of
detail is useful right now — from a one-line Description to a complete spec.
Both are valid; a brief capture is not an incomplete draft. Record *what* the
work is, *why* it matters, and — as far as you can usefully state it — what
"done" means. Do not work out a cause, an approach, or implementation steps in
the body; those are decided against the current code when the item is picked
up.

## Title

Short and human-readable, naming the intended change (task) or the broken
behavior (bug) and the main target area.

## Anchoring

A backlog item should still link the anchor it serves when one already exists —
the use case, requirement, spec, or epic it belongs to — so it is findable and
groupable later. Do not create new anchors solely to satisfy this; if no anchor
exists yet, capture the item anchorless and let pickup establish one.

## Body shape

The type spec contract (`./task.md` or `./bug.md`) defines the spec sections. In
backlog mode you record them at any level of detail:

- `Description` — required. What the change is (task) or what is broken (bug)
  and why it matters. Always present, even in the briefest capture.
- `Context`, `Acceptance Criteria`, and — for a bug — `Reproduction` — recorded
  to whatever level is useful now. A one-line capture may leave them thin or
  absent; a fuller capture states them completely. Their thinness here is a
  deliberate deferral to pickup, not an incomplete draft.

Do not author a cause, an approach, or a step sequence in the body — the type
spec forbids it and so does this framing. Those are decided against the current
code at implementation time.

## Audits

Skip the size audit (`task-size-auditor`) and the resolution audit
(`resolution-auditor`) at capture. They validate an implementation approach or a
landed change; a backlog spec has neither yet. They run at implementation time
when the item is picked up.

## Publish state

Publish in the backend's open / unresolved state. A backlog item is future work
waiting to be picked up, not completed work.

## Picking the item up

When the item is scheduled for implementation, the approach and concrete steps
are decided against the current code at that point, and the size and resolution
audits run then. The captured spec is the starting point, not a finished plan;
nothing in the body is re-authored into a stored plan.
