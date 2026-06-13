# Bug Authoring

A workflow bug is an issue-backed fix for production behavior that is wrong, missing, regressed, or inconsistent with a use case, spec, test expectation, or user-visible contract. It records the defect as a **spec**: what is broken, how to reproduce it, and what "done" means — not the fix approach, which is decided against the current code at implementation time. Read with `./body.md` (body conventions, runtime-grounded claims) and `./common.md` (issue rules, motivation, completion baseline).

A bug without a reproducible failure path is not ready for implementation. When reproduction is unknown and the work is mostly discovery, use `spike` or `research` until the defect is pinned down.

## Required sections

- Context — the backdrop a reader who was not in the room needs before the bug makes sense: where in the system it surfaces, what triggered the report, the conditions or invariants in play, and the prior decisions or anchors it relates to. This is the home for the motivation and rationale (`./common.md`).
- Description — what is broken, observed vs expected behavior, and why it matters.
- Reproduction — steps, command, data, or conditions that reproduce the bug.
- Acceptance Criteria — completion-oriented items, each stated in operational, independently checkable terms: "bug no longer reproduces" (via the Reproduction steps) and "regression test fails before the fix and passes after". Required even when the bug links to a use case or spec. When no automated test is feasible, record the manual verification path and the reason for it here, as a criterion.

Add any other sections the fix needs and fill them in; any premise they rest on must meet the runtime-grounded-claim rule in `./body.md`. One section is optional but carries a bug-specific rule:

- Root Cause — the diagnosed mechanism behind the wrong behavior: the specific code path, state, or condition responsible, pinned by evidence (a runtime-grounded claim per `./body.md`), not an asserted hypothesis. Record it only when the cause is already known — self-evident from the symptom, or surfaced before authoring; fold it into Description when self-evident. Otherwise leave it out: diagnosing a cause requires heavy code reading and is done at implementation time. Reproduction is still required; only the cause may be deferred. Do not assert an undiagnosed hypothesis as the cause.

Do not record the fix approach or a step sequence in the body — those are worked out against the current code at implementation time.

## Evidence-readiness

Before treating a bug as ready for fix, capture enough for a handoff — the body alone, with no local plan file, must let a cold implementer reproduce, diagnose, fix, and confirm: reproduction steps or command, observed behavior, expected behavior, relevant environment/version/data conditions, suspected component or code coordinates when known, and the regression behavior the fix must pin (captured as an Acceptance Criterion).

## Regression test rule

A bug should end with a regression test that fails before the fix, passes after, and pins the violated behavior. If no automated test is feasible, record the manual verification path and the reason as an Acceptance Criterion.

## Backlog mode

A backlog bug captures the defect to triage and fix later; resolved in backlog mode (`./backlog.md`), which records at least Description and adds Context, Reproduction, and Acceptance Criteria to whatever level of detail is useful now.

## Common mistakes

- Treating a vague symptom as ready for fix before reproduction is clear.
- Treating comments as the only source of expected behavior.
- Shipping a fix without a regression test or a documented reason one is not feasible.
- Asserting an undiagnosed hypothesis as the Root Cause instead of leaving the cause to implementation-time diagnosis.
