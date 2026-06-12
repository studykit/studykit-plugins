# Task Authoring

A workflow task records regular implementation work: new functionality, extension, refactor, or other planned code change.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`
- Decomposition choice: `./decomposition-patterns.md`

## Task title

Short and human-readable, naming the intended change and the main target area.

## Anchors and scope

A task should usually have at least one acceptance source: a use case or requirement it delivers, a spec or knowledge page defining the implementation contract, or an epic/parent issue coordinating a batch.

Anchorless tasks are allowed for small, obvious changes, but should pass a smell check:

- User-facing behavior with no use case → create or link a use case.
- A protocol, schema, API shape, or architectural decision with no spec → create or link a spec.
- Exploratory work with missing evidence → use `spike` or `research` instead.

## Body shape

Required sections:

- `Description` — what is changing and why. State the motivation explicitly for removals, boundary changes, agent responsibility changes, schema/contract changes, and work that prevents a known regression.
- `Unit Test Strategy` — scenarios, isolation strategy, and expected test locations.
- `Acceptance Criteria` — one or more observable completion conditions as completion-oriented checklist items. Required even when the task links to use cases or specs.

Ground acceptance criteria in: linked use case flow/validation/error handling, linked spec, linked architecture/domain context, or an explicit user request when no curated page exists yet.

Optional sections:

- `Context` — the backdrop a reader needs before the change makes sense: the anchoring use case or constraint, what the current code already provides, and the gap this task closes. Place it first, before `Description`. Keep it to durable framing; link the curated knowledge `context` / `architecture` page rather than restating it, and fold it into `Description` instead when the two would say the same thing. Distinct from `Description` (what is changing) — this is the situation the change sits in.
- `Root Cause` — for a fix or diagnostic task, the diagnosed mechanism behind the behavior being changed: the specific code path, state, or condition responsible, with the evidence that pins it. Place it after `Description`. Distinct from `Description` (what is changing) and `Implementation Steps` (how) — this section is *why* the current behavior occurs. A root-cause claim is a runtime-grounded claim (see `./body.md`): record the command or observation that establishes it. Skip for greenfield or extension work with no existing behavior to diagnose.
- `Design Decision` — key design decisions this task commits to: the choice made, why, and the main alternatives rejected. Scope each to this change; a durable cross-cutting decision still earns a spec (see the Anchors and scope smell check), and a decision with lasting reference value is also linked from the Design Decision Index knowledge page (`../knowledge/decision-index.md`).
- `Implementation Steps` — the concrete, ordered plan: what is done in what sequence, naming the files, packages, or APIs each step touches (this absorbs the older scope-fence section, so steps carry their own affected paths). The step list may open with a one-line strategy statement naming the overall approach before the ordered steps. Treat the plan as a falsifiable hypothesis, not a fixed spec: whoever implements it — even the authoring session — re-verifies its load-bearing premises against the current code, and re-grounds any runtime-grounded premise (see `./body.md`) by running it before building on it, revising the steps on mismatch.
- `Verification` — the ordered procedure that establishes completion: the commands, observations, or comparisons run to confirm the `Acceptance Criteria`, each step independently checkable. Distinct from `Acceptance Criteria` (what "done" is) — this is how it is confirmed. Any runtime-grounded check must be runtime-grounded per `./body.md`.
- `Interface Contracts` — contracts this task consumes or provides.
- `Out of Scope`, `Alternatives Considered`, `Risks`, `Resume`, `Why Discarded` — see `./body.md`.

Do not bury the motivation only in `Implementation Steps`; state it in `Description` (and, for a design choice, `Design Decision`).

## Evidence-readiness

A task ready for implementation should be actionable as a handoff. Before treating it as ready, check that the body or linked references supply enough evidence:

- Reproduction or invocation command when relevant.
- Code coordinates or expected implementation area.
- Data flow or API contract when relevant.
- Current baseline behavior.
- Test fixture or test strategy.

Any load-bearing claim about runtime behavior must be runtime-grounded per `./body.md` — recorded with the command that produced it and its captured result, and re-confirmed by running it (or by adding temporary logging at the decisive point and observing) before implementation. A premise asserted from reasoning but never executed counts as unknown evidence here, even when the author feels certain of it.

If two or more of these are unknown, consider `spike` or `research` instead of `task`.

## Retroactive tasks

A retroactive task records work that is already done — the change exists in the working tree or history before the issue does. The body states facts, not intent: `Description` says what changed and why, `Implementation Steps` records how it was actually done, and `Acceptance Criteria` plus `Verification` record the checks that already ran.

Because there is no upcoming implementation to plan or scope:

- Skip the planning pass that would author a forward-looking plan; the landed change is the plan of record.
- Skip the size audit (`task-size-auditor`) — sizing guards work that has not happened yet, and the actual size is already fixed.
- Publish (or apply the body update) together with the transition to the backend's resolved state, rather than opening the issue and leaving it pending.

The diagnosis audit still applies: a retroactive draft's recorded cause and fix can be validated against the landed change (`resolution-auditor`, draft mode).

## Artifacts

Issue-backed tasks usually do not need a local evidence directory. Use linked external evidence only when it has evidentiary or comparative value (before/after screenshots, sample inputs/outputs, migration dry-run output, benchmark data).

Production source paths are recorded by git history. Name planned source changes inline in `Implementation Steps` when they help scope the work.

## Completion criteria

A task is complete when required tests or verification steps have passed, or the issue explains why they are not applicable.

## Common mistakes

- Creating an anchorless task for work that really needs a use case or spec.
- Treating comments as the only source of acceptance criteria.
- Treating a task as complete without updating affected knowledge pages.
- Recording a durable cross-cutting contract only in `Design Decision` when it belongs in a spec.
