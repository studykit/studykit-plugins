# Task Authoring

A workflow task records planned implementation work — new functionality, extension, refactor, or other intended code change. Read with `./body.md` (body conventions, runtime-grounded claims, reusable sections) and `./common.md` (issue rules, motivation, completion baseline); choose decomposition via `./decomposition-patterns.md`.

Use `spike` or `research` instead when the path is still uncertain (see Evidence-readiness).

## Required sections

- Description
- Unit Test Strategy
- Acceptance Criteria — required even when the task links to a use case or spec; ground each criterion in the linked use case flow/validation, linked spec, linked architecture/domain context, or an explicit user request when no curated page exists.
- Verification — the ordered procedure that confirms the Acceptance Criteria: the commands, observations, or comparisons run, each independently checkable. Distinct from Acceptance Criteria (what "done" is) — this is how it is confirmed; any runtime check must be runtime-grounded per `./body.md`.

Add any other sections the work needs and fill them in; any premise they rest on must meet the runtime-grounded-claim rule in `./body.md`.

## Anchors and scope

A task should usually have an acceptance source — a use case or requirement it delivers, a spec or knowledge page defining the contract, or an epic/parent coordinating a batch. Anchorless tasks are fine for small, obvious changes, but route instead when:

- User-facing behavior with no use case → create or link a use case.
- A protocol, schema, API shape, or architectural decision with no spec → create or link a spec.
- Exploratory work with missing evidence → use `spike` or `research`.

A durable, cross-cutting design decision likewise earns a spec rather than living only in the issue body, and is linked from the Design Decision Index (`../knowledge/decision-index.md`) when it has lasting reference value.

## Evidence-readiness

A task ready for implementation is actionable as a handoff. Check the body or linked references supply: reproduction or invocation command when relevant, code coordinates or expected area, data flow or API contract when relevant, baseline behavior, and test strategy. Any load-bearing runtime claim must be runtime-grounded per `./body.md`. If two or more of these are unknown, use `spike` or `research` instead.

## Modes

- Backlog — capture intent for a later planning pass without a forward plan; resolved in backlog mode (`./backlog.md`), which relaxes required sections to Description. Do not hand-author a plan-light task under this forward contract.
- Retroactive — the change already landed; the body records facts (what changed, how it was done, the checks that ran), skips the forward planning pass and the size audit, and publishes together with the transition to the resolved state. The diagnosis audit still applies.

## Common mistakes

- An anchorless task for work that really needs a use case or spec.
- Treating comments as the only source of acceptance criteria.
- Recording a durable cross-cutting contract only in the issue body when it belongs in a spec.
</content>
</invoke>
