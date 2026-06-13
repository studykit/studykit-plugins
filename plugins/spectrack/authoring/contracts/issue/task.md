# Task Authoring

A workflow task records a unit of implementation work — new functionality, extension, refactor, or other intended code change — as a **spec**: what the work is, why it matters, and what "done" means. It does not record *how* to build it; the approach and the concrete steps are decided against the current code at implementation time, where they would only go stale if frozen into the body. Read with `./body.md` (body conventions, runtime-grounded claims, reusable sections) and `./common.md` (issue rules, motivation, completion baseline); choose decomposition via `./decomposition-patterns.md`.

Use `spike` or `research` instead when the path is still uncertain (see Evidence-readiness).

## Required sections

- Context — the backdrop a reader who was not in the room needs before the work makes sense: the current state of the affected area, what triggered the work now, the constraints, invariants, and prior decisions or anchors it builds on. This is the durable direction a cold implementer leans on while deciding the mechanism against current code, and the home for the motivation and rationale (`./common.md`).
- Description — what the work is: the change itself and its scope.
- Acceptance Criteria — what "done" is, with each criterion stated in operational, independently checkable terms — the observation, command, or comparison that would demonstrate it. Required even when the task links to a use case or spec; ground each criterion in the linked use case flow/validation, linked spec, linked architecture/domain context, or an explicit user request when no curated page exists. Include the test coverage the work needs as a criterion (the behavior a regression or coverage test must pin); the implementer derives the test layout and confirms it.

Add any other sections the work needs and fill them in; any premise they rest on must meet the runtime-grounded-claim rule in `./body.md`. Do not record the implementation approach or a step sequence in the body — those are worked out against the current code at implementation time, and a frozen plan only goes stale and misleads.

## Anchors and scope

A task should usually have an acceptance source — a use case or requirement it delivers, a spec or knowledge page defining the contract, or an epic/parent coordinating a batch. Anchorless tasks are fine for small, obvious changes, but route instead when:

- User-facing behavior with no use case → create or link a use case.
- A protocol, schema, API shape, or architectural decision with no spec → create or link a spec.
- Exploratory work with missing evidence → use `spike` or `research`.

A durable, cross-cutting design decision likewise earns a spec rather than living only in the issue body, and is linked from the Design Decision Index (`../knowledge/decision-index.md`) when it has lasting reference value.

## Evidence-readiness

A task ready for implementation is actionable as a handoff: the body alone — with no local plan file — must let a cold implementer reach done and derive the approach and concrete edit sequence against the current code. Check the body or linked references supply: reproduction or invocation command when relevant, code coordinates or expected area, data flow or API contract when relevant, baseline behavior, and the directional constraints that bound the work (Context). Any load-bearing runtime claim must be runtime-grounded per `./body.md`. If two or more of these are unknown, use `spike` or `research` instead.

## Modes

- Backlog — the open, not-yet-done spec captured for later pickup; resolved in backlog mode (`./backlog.md`), recorded at any level of detail from a one-line Description to a complete spec.
- Retroactive — the change already landed; the body records facts (what changed, the cause when relevant, how it was done, the checks that ran) and publishes together with the transition to the resolved state.

## Common mistakes

- An anchorless task for work that really needs a use case or spec.
- Treating comments as the only source of acceptance criteria.
- Recording a durable cross-cutting contract only in the issue body when it belongs in a spec.
- Recording an implementation approach or step sequence in the body instead of leaving the mechanism to implementation time.
