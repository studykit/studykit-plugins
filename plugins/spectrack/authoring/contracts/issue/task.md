# Task Authoring

A workflow task records implementation work as a **spec**: what changes, why it matters, and what "done" means. It does not record how to build it; the approach is decided against current code at implementation time.

## Required sections

- Description — the intended change and scope.

## Optional sections

The body shape is yours to choose: use the sections below only when they carry
weight, and add other sections when the task needs them. These commonly help:

- Context — motivation, anchors, constraints, and current-state background.
- Acceptance Criteria — independently checkable done conditions, including the behavior tests or verification must cover. Ground criteria in linked use cases/specs or the explicit request.

Valuable task detail is behavioral: boundaries, edge cases, recovery paths, atomicity, and verification. Avoid file/function choices or step sequences unless they are already verified constraints.

## Anchors and scope

A task should usually have an acceptance source — a use case, requirement, spec, or coordinating parent. Anchorless tasks are fine for small, obvious changes, but route instead when:

- User-facing behavior with no use case → create or link a use case.
- A protocol, schema, API shape, or architectural decision with no spec → create or link a spec.
- Exploratory work with missing evidence → use `spike` or `research`.

A durable, cross-cutting design decision belongs in a spec rather than only in the issue body.

## Evidence-readiness

A task is ready when the body lets a cold implementer reach done without a local plan file. If key behavior, baseline, data/API contract, or verification is unknown, use `spike` or `research` first.

## Modes

- Backlog — the open, not-yet-done spec captured for later pickup; recorded at any useful level of detail.
- Retroactive — the change already landed; the body records facts (what changed, the cause when relevant, how it was done, and the checks that ran) and publishes together with the transition to the resolved state.
