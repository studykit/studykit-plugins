# Spike Authoring

A workflow spike is an issue-backed, time-boxed exploration to unblock a decision — a proof of concept, benchmark, integration probe, or focused experiment, possibly with throwaway code. Read with `./common.md` (issue rules, body conventions) and `./runtime-grounded-claims.md` (grounding rule for runtime claims).

Choose the type by output:

- `spike` — a runnable experiment or throwaway code answers a question blocked by technical uncertainty; the output is evidence enabling a later task or spec.
- `task` — the implementation approach is known and work goes into production code.
- `research` — the output is written evidence, source review, or comparison with no runnable experiment.

## Required sections

- Description — the question being explored, why a spike is needed, and what decision it informs.
- Hypothesis — what the spike tries to prove, disprove, or measure.
- Validation Method — the experiment, benchmark, integration probe, prototype, or sample-driven check.
- Acceptance Criteria — one or more observable outcomes that answer the question.

Add any other sections the exploration needs and fill them in; any premise they rest on must meet the runtime-grounded-claim rule in `./runtime-grounded-claims.md`. Link throwaway evidence (a scratch branch, gist, benchmark output, screenshots, or prototype under a clearly marked scratch location) rather than assuming a local evidence directory.

## Completion criteria

A spike is complete when the hypothesis is answered or invalidated, the evidence is linked or summarized, and the decision impact is clear — not when production code ships. If time expires, record what remains unanswered; expiry alone is not completion.

## Follow-up work

PoC code stays throwaway. If the outcome should become production code, create a follow-up `task` rather than turning the spike into it. Common follow-ups: `task` (implement), `spec` (record a discovered contract), `research` (deeper investigation), `review` (a surfaced gap or question). Link follow-ups visibly.

## Common mistakes

- Using `spike` for production implementation work.
- Treating the spike as complete without evidence.
- Letting throwaway PoC code become production without a follow-up task.
- Using `spike` when a written `research` item would be enough.
