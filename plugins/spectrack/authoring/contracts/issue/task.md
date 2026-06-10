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

Do not hide design decisions in the task body when they should become curated knowledge.

## Body shape

Required sections:

- `Description` — what is changing and why. State the motivation explicitly for removals, boundary changes, agent responsibility changes, schema/contract changes, and work that prevents a known regression.
- `Unit Test Strategy` — scenarios, isolation strategy, and expected test locations.
- `Acceptance Criteria` — one or more observable completion conditions as completion-oriented checklist items. Required even when the task links to use cases or specs.

Ground acceptance criteria in: linked use case flow/validation/error handling, linked spec, linked architecture/domain context, or an explicit user request when no curated page exists yet.

Optional sections:

- `Approach` — implementation strategy: how the work is done, including sequencing and architectural choices.
- `Affected Paths` — forward-looking scope fence naming files, packages, APIs, or migration steps expected to change.
- `Interface Contracts` — contracts this task consumes or provides.
- `Out of Scope`, `Alternatives Considered`, `Risks`, `Resume`, `Why Discarded` — see `./body.md`.

Do not hide the motivation only in `Approach` or `Affected Paths`. If the rationale is a long-lived design decision, create or update the relevant knowledge page instead of embedding the full record in the task body.

## Evidence-readiness

A task ready for implementation should be actionable as a handoff. Before treating it as ready, check that the body or linked references supply enough evidence:

- Reproduction or invocation command when relevant.
- Code coordinates or expected implementation area.
- Data flow or API contract when relevant.
- Current baseline behavior.
- Test fixture or test strategy.

If two or more of these are unknown, consider `spike` or `research` instead of `task`.

## Retroactive tasks

A retroactive task records work that is already done — the change exists in the working tree or history before the issue does. The body states facts, not intent: `Description` says what changed and why, `Approach` records how it was actually done, and `Acceptance Criteria` record the verification that already ran.

Because there is no upcoming implementation to plan or scope:

- Skip the planning pass that would author a forward-looking plan; the landed change is the plan of record.
- Skip the size audit (`task-size-auditor`) — sizing guards work that has not happened yet, and the actual size is already fixed.
- Publish (or apply the body update) together with the transition to the backend's resolved state, rather than opening the issue and leaving it pending.

The diagnosis audit still applies: a retroactive draft's recorded cause and fix can be validated against the landed change (`resolution-auditor`, draft mode).

## Artifacts

Issue-backed tasks usually do not need a local evidence directory. Use linked external evidence only when it has evidentiary or comparative value (before/after screenshots, sample inputs/outputs, migration dry-run output, benchmark data).

Production source paths are recorded by git history. Mention planned source changes in `Affected Paths` when they help scope the work.

## Completion criteria

A task is complete when required tests or verification steps have passed, or the issue explains why they are not applicable.

## Common mistakes

- Creating an anchorless task for work that really needs a use case or spec.
- Treating comments as the only source of acceptance criteria.
- Treating a task as complete without updating affected knowledge pages.
- Embedding long design decisions in the task body instead of creating or updating a spec.
