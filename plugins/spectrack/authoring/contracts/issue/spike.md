# Spike Authoring

A workflow spike is an issue-backed, time-boxed exploration to unblock a
decision — a proof of concept, benchmark, integration probe, or focused
experiment, possibly with throwaway code.

Choose the type by output:

- `spike` — a runnable experiment or throwaway code answers a question blocked by technical uncertainty.
- `task` — the implementation approach is known and work goes into production code.
- `research` — the output is written evidence, source review, or comparison with no runnable experiment.

## Required sections

- Description — the question being explored, why a spike is needed, and what decision it informs.

## Optional sections

The body shape is yours to choose: use the sections below only when they carry
weight, and add other sections when the spike needs them. These commonly help:

- Hypothesis — what the spike tries to prove, disprove, or measure.
- Validation Method — the experiment, benchmark, integration probe, prototype, or sample-driven check.

When the question depends on the configured backend, API, or runtime behavior, ground the answer with the exact query, command, input shape, observed result, scale, limits, errors, pagination, or rate-limit cost needed to make it decisive. Link throwaway evidence rather than assuming a local evidence directory.

## Completion criteria

A spike is complete when the hypothesis is answered or invalidated, the evidence is linked or summarized, and the decision impact is clear — not when production code ships. If time expires, record what remains unanswered; expiry alone is not completion.

## Follow-up work

PoC code stays throwaway. If the outcome should become production code, create a follow-up `task` rather than turning the spike into it. Common follow-ups: `task` (implement), `spec` (record a discovered contract), `research` (deeper investigation), `review` (a surfaced gap or question). Link follow-ups visibly.

Do not let throwaway PoC code become production without a follow-up `task`.
