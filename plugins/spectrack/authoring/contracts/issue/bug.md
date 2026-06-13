# Bug Authoring

A workflow bug is an issue-backed fix for production behavior that is wrong, missing, regressed, or inconsistent with a use case, spec, test expectation, or user-visible contract. Read with `./body.md` (body conventions, runtime-grounded claims) and `./common.md` (issue rules, motivation, completion baseline).

A bug without a reproducible failure path is not ready for implementation. When reproduction is unknown and the work is mostly discovery, use `spike` or `research` until the defect is pinned down.

## Required sections

- Description — what is broken, observed vs expected behavior, and why it matters.
- Reproduction — steps, command, data, or conditions that reproduce the bug.
- Unit Test Strategy — regression scenario, isolation strategy, and expected test locations.
- Acceptance Criteria — completion-oriented items such as "bug no longer reproduces" and "regression test fails before the fix and passes after"; required even when the bug links to a use case or spec.

Add any other sections the fix needs and fill them in; any premise they rest on must meet the runtime-grounded-claim rule in `./body.md`. One section carries a bug-specific rule:

- Root Cause — the diagnosed mechanism behind the wrong behavior: the specific code path, state, or condition responsible, pinned by evidence (a runtime-grounded claim per `./body.md`), not an asserted hypothesis. Fold into Description when the mechanism is self-evident; skip when not yet diagnosed.

## Evidence-readiness

Before treating a bug as ready for fix, capture enough for a handoff: reproduction steps or command, observed behavior, expected behavior, relevant environment/version/data conditions, suspected component or code coordinates when known, and a regression test strategy.

## Regression test rule

A bug should end with a regression test that fails before the fix, passes after, and pins the violated behavior. If no automated test is feasible, document the manual verification path and the reason in Unit Test Strategy.

## Backlog mode

A backlog bug captures the defect to triage later without a forward plan; resolved in backlog mode (`./backlog.md`), which relaxes required sections to Description. Do not hand-author a plan-light bug under this forward contract.

## Common mistakes

- Treating a vague symptom as ready for fix before reproduction is clear.
- Treating comments as the only source of expected behavior.
- Shipping a fix without a regression test or a documented reason one is not feasible.
