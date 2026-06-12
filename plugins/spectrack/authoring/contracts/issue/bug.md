# Bug Authoring

A workflow bug is an **issue-backed defect fix** against expected behavior. It tracks production behavior that is wrong, missing, regressed, or inconsistent with a use case, spec, test expectation, or user-visible contract.

Bugs are stored in the configured issue backend.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`

## Evidence-readiness

A bug without a reproducible failure path is not ready for implementation.

Before treating a bug as ready for fix, capture enough evidence for a handoff:

- Reproduction steps or command.
- Observed behavior.
- Expected behavior.
- Environment, version, data shape, or relevant conditions.
- Code coordinates or suspected component when known.
- Test fixture or regression test strategy.

If reproduction is unknown and the task is mostly discovery, use `spike` or `research` instead of `bug` until the defect is pinned down.

## Body shape

Required sections:

- `Description` — what is broken, observed behavior, expected behavior, and why it matters.
- `Reproduction` — steps, command, data, or conditions that reproduce the bug.
- `Unit Test Strategy` — regression test scenario, isolation strategy, and expected test locations.
- `Acceptance Criteria` — completion-oriented checklist items such as "bug no longer reproduces" and "regression test fails before fix and passes after fix".

The `Acceptance Criteria` section must exist even when the bug is linked to a use case or spec.

Optional sections:

- `Context` — the backdrop a reader needs before the defect makes sense: the use case or contract the broken behavior violates, what the current code is expected to do, and where the gap sits. Place it first, before `Description`. Keep it to durable framing; link the curated knowledge `context` / `architecture` page rather than restating it, and fold it into `Description` when the two would say the same thing. Distinct from `Description` (what is broken) — this is the situation the defect sits in.
- `Environment` — version, browser, OS, tenant, data shape, feature flags, or deployment context.
- `Root Cause` — the diagnosed mechanism of the defect: the specific code path, state, or condition that produces the wrong behavior, with the evidence that pins it. Place it after `Description`. Distinct from `Description` (what is broken, observed vs expected) and from `Implementation Steps` (how it is fixed) — this section is *why* it breaks. A root-cause claim is a runtime-grounded claim (see `./body.md`): record the command or observation that establishes the mechanism, not an asserted hypothesis. Fold into `Description` when the mechanism is self-evident.
- `Design Decision` — key design decisions in the fix: the choice made, why, and the main alternatives rejected. A decision with lasting reference value is also linked from the Design Decision Index knowledge page (`../knowledge/decision-index.md`).
- `Implementation Steps` — the concrete, ordered fix plan: diagnosis and fix sequence, naming the files, packages, or APIs each step touches (this absorbs the older scope-fence section, so steps carry their own affected paths). The step list may open with a one-line strategy statement naming the overall approach before the ordered steps. Treat it as a falsifiable hypothesis, not a fixed spec: whoever implements it re-verifies its load-bearing premises against the current code, and re-grounds any runtime-grounded premise (see `./body.md`) by running it before building on it, revising the steps on mismatch.
- `Verification` — the ordered procedure that establishes the fix is correct: the commands, observations, or comparisons run to confirm the `Acceptance Criteria` (including that the regression test fails before and passes after), each step independently checkable. Distinct from `Acceptance Criteria` (what "done" is) — this is how it is confirmed.
- `Interface Contracts` — contracts the fix consumes or restores.
- `Out of Scope` — work explicitly excluded from this issue. See `./body.md`.
- `Alternatives Considered` — design options evaluated but not chosen. See `./body.md`.
- `Risks` — technical or operational risks specific to this work. See `./body.md`.
- `Resume` — current-state snapshot while mid-flight. See `./body.md`.
- `Why Discarded` — reason when discarded. See `./body.md`.

## Regression test rule

A bug should end with a regression test when technically feasible.

The test should:

- Fail before the fix or describe why pre-fix failure cannot be demonstrated safely.
- Pass after the fix.
- Pin the expected behavior that was violated.

If no automated regression test is feasible, document the manual verification path and reason in the `Unit Test Strategy` section.

## Artifacts

Issue-backed bugs usually do not need a local evidence directory.

Use linked external evidence only when evidence has lasting value, such as:

- Screenshots.
- Crash logs.
- Traces.
- Minimal repro repositories.
- Problematic input files.

Production source paths are recorded by git history. Name planned source changes inline in the `Implementation Steps` section when they help scope the fix.

## Completion criteria

A bug is complete when:

- Reproduction no longer fails, or the issue explains why the original reproduction is obsolete.
- Regression test or manual verification is complete.

## Common mistakes

- Treating a vague symptom as ready for fix before reproduction is clear.
- Treating comments as the only source of expected behavior.
- Marking a bug complete without a regression test or documented manual verification.

## Do not

- Do not create local bug projection files unless explicitly using a local projection workflow.
- Do not ship a fix without a regression test or a clear reason why one is not feasible.
- Do not use closing keywords or Smart Commit commands unless the workflow intentionally wants automated side effects.
