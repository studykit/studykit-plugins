# Workflow Task Authoring

A workflow task records regular implementation work: new functionality,
extension, refactor, or other planned code change.

Companion contracts:

- `./issue-body.md`
- Issue rules: `./issue-authoring.md`

## Task title

Use a short human-readable title that names the intended change and the main
target area.

## Anchors and scope

A task should usually have at least one acceptance source:

- A use case or requirement the task delivers.
- A spec or knowledge page that defines the implementation contract.
- An epic or parent issue that coordinates a batch of work.

Anchorless tasks are allowed for small, obvious changes, but they should pass a smell check:

- If the task implies user-facing behavior with no use case, create or link a use case.
- If the task implies a protocol, schema, API shape, or architectural decision with no spec, create or link a spec.
- If the task is exploratory and evidence is missing, use `spike` or `research` instead.

Do not hide design decisions only in the task body when they should become curated knowledge.

## Shared narrative

When a task belongs to a larger batch of work, keep shared context in the parent
issue. The task body should record only the scope, acceptance criteria, and
implementation notes that are specific to this task.

## Granularity

Split a task when it spans:

- Unrelated code areas.
- Independent acceptance criteria.
- Independent test surfaces.
- Work that can be assigned or sequenced independently.

When a split is warranted, the decomposition pattern (sibling tasks, parent task with subtasks, or epic with members) is selected per `./decomposition-patterns.md`. Use the `blocked_by` relationship intent for hard sequencing between siblings, and a shared anchor (use case, spec, parent task, or epic) when siblings deliver toward the same goal.

## Body shape

Required sections:

- `Description` — what is changing and why. State the motivation explicitly for removals, boundary changes, agent responsibility changes, schema or contract changes, and work that prevents a known regression.
- `Unit Test Strategy` — scenarios, isolation strategy, and expected test locations.
- `Acceptance Criteria` — one or more observable completion conditions, expressed as completion-oriented checklist items.

The `Acceptance Criteria` section must exist even when the task has issue links to use cases or specs.

Use the `Approach` section to record the implementation strategy and the `Affected Paths` section for the expected file scope when present. Do not hide the motivation only in those sections. If the rationale is a long-lived design decision, create or update the relevant knowledge page instead of embedding the full decision record in the task body.

Acceptance criteria should be grounded in:

- Linked use case flow, validation, and error handling.
- Linked spec specification.
- Linked architecture/domain context.
- Explicit user request when no curated page exists yet.

Optional sections:

- `Approach` — implementation strategy: how the work will be done, including sequencing and architectural choices.
- `Affected Paths` — forward-looking scope fence naming files, packages, APIs, or migration steps expected to change.
- `Interface Contracts` — contracts this task consumes or provides.
- `Out of Scope` — work explicitly excluded from this issue. See `./issue-body.md`.
- `Alternatives Considered` — design options evaluated but not chosen. See `./issue-body.md`.
- `Risks` — technical or operational risks specific to this work. See `./issue-body.md`.
- `Resume` — current-state snapshot while mid-flight. See `./issue-body.md`.
- `Why Discarded` — reason when discarded. See `./issue-body.md`.

Unknown well-named sections are tolerated.

## Evidence-readiness

A task that is ready for implementation should be actionable as a handoff.

Before treating a task as ready, check that the issue body or linked references provide enough evidence for implementation:

- Reproduction or invocation command when relevant.
- Code coordinates or expected implementation area.
- Data flow or API contract when relevant.
- Current baseline behavior.
- Test fixture or test strategy.

If two or more evidence categories are unknown, consider `spike` or `research` instead of `task`.

## Artifacts

Issue-backed tasks usually do not need a local evidence directory.

Use linked external evidence only when they have evidentiary or comparative value, such as:

- Before/after screenshots.
- Sample inputs and outputs.
- Migration dry-run output.
- Benchmark data.

Production source paths are recorded by git history. Mention planned source changes in the `Affected Paths` section when they help scope the work.

## Completion criteria

A task is complete when:

- Required tests or verification steps have passed, or the issue explains why they are not applicable.

## Common mistakes

- Missing the `Description`, `Unit Test Strategy`, or `Acceptance Criteria` section.
- Creating an anchorless task for work that really needs a use case or spec.
- Treating comments as the only source of acceptance criteria.
- Treating a task as complete without updating affected knowledge pages.
- Embedding long design decisions in the task body instead of creating or updating a spec.
