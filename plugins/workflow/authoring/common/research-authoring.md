# Workflow Research Authoring — Common

A workflow research item is a **time-boxed investigation** of a question, technical topic, product question, or comparison of alternatives.

Research is a dual-role type: it has an **issue side** (scope, questions, status, review discussion) and a **knowledge side** (curated report that carries final findings, evidence, options, and recommendation-neutral conclusions). The workflow issue is always created first; the curated report is created or updated later when there is stable research output worth publishing.

This file carries the rules that apply across both sides. Role-specific rules live in the companion contracts.

## When research is warranted

Use research when the next step is evidence-gathering, not implementation.

Good research inputs:

- Compare alternatives.
- Understand an external API, SDK, service, or integration.
- Gather evidence before committing to a spec.
- Investigate feasibility, cost, risk, or constraints.
- Produce citable findings for later specs, tasks, or decisions.

Use `spike` instead when the output is exploratory code or a runnable proof of concept.

Use `spec` instead when the decision is already known and the task is to write the prescriptive contract.

## Decision neutrality

Research describes evidence. Specs make decisions. This rule applies on both surfaces — the workflow issue body and the curated report.

Avoid prescriptive language such as:

- "Therefore we should choose X."
- "The implementation must use Y."
- "X is the correct architecture."

Prefer evidence-oriented language:

- "X has lower operational overhead under these constraints."
- "Y lacks feature Z in the documented API."
- "The evidence supports X if revocation latency is the primary criterion."

If a decision is reached, record it in a spec's `Decision Log` section or another appropriate knowledge page, and cite the research.
