# Bug Authoring

A workflow bug records wrong, missing, regressed, or inconsistent behavior as a **spec**: what is broken, how to reproduce it, and what "done" means. It does not prescribe the fix approach.

When reproduction is unknown and the work is mostly discovery, use `spike` or `research` until the defect is pinned down.

## Required sections

- Description — observed vs expected behavior.

## Optional sections

The body shape is yours to choose: use the sections below only when they carry
weight, and add other sections when the bug needs them. These commonly help:

- Context — where it surfaces, triggering conditions, relevant anchors, and why it matters.
- Reproduction — steps, command, data, or conditions that reproduce the bug.
- Acceptance Criteria — independently checkable done conditions, including regression coverage or a manual verification path with the reason automation is not feasible.

When behavior is observed, prefer explicit `Actual Behavior`, `Expected Behavior`, or `Environment` sections over generic prose. One optional section carries a bug-specific rule:

- Root Cause — include only when already diagnosed and evidence-backed. Do not assert an undiagnosed hypothesis as the cause; leave diagnosis to implementation time. If a suspected trigger is useful, label it as a non-exhaustive hypothesis or investigation note.

Do not record the fix approach or a step sequence in the body — those are worked out against the current code at implementation time.

## Evidence-readiness

Before treating a bug as ready for fix, capture enough to reproduce, diagnose, fix, and confirm: reproduction, observed/expected behavior, relevant environment/data conditions, and the regression behavior the fix must pin.

## Backlog mode

A backlog bug captures the defect to triage and fix later; record at least Description and add Context, Reproduction, and Acceptance Criteria to whatever level of detail is useful now.
