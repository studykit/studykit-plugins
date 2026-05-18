# Workflow Research Authoring

A workflow research item is a **time-boxed investigation** of a question, technical topic, product question, or comparison of alternatives.

Research has two authoring surfaces:

1. An issue-backed item for scope, questions, discussion, status, and review.
2. A knowledge-backed curated report for final findings, evidence, options, and recommendation-neutral conclusions.

The issue item is always created first. The curated report is created or updated when there is stable research output worth publishing.

Companion contracts:

- `./issue-body.md`
- `./knowledge-body.md`
- Issue rules: `./issue-authoring.md`

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

## Storage role

`research` has two roles.

| Role | Backend | Purpose |
| --- | --- | --- |
| Workflow issue | Configured issue backend | Scope, questions, discussion, status, review, and follow-up tracking. |
| Curated knowledge report | Configured knowledge backend | Final findings, sources, comparisons, and reusable evidence. |

The workflow issue may exist without a curated report while the investigation is in progress. The curated report should link back to the workflow issue when published.

## Workflow issue body

The workflow issue body should define the investigation scope and current state.

Recommended sections:

- `Description` — why this research is needed and how the result will be used.
- `Research Question` — single question or comparison objective.
- `Mode` — `comparative` or `single`.
- `Options` — alternatives being compared, one per bullet (required when mode is `comparative`).

Optional sections:

- `Scope` — in-scope and out-of-scope boundaries.
- `Sources To Check` — initial source list or search plan.
- `Resume` — current-state snapshot while in progress. See `./issue-body.md`.

Use comments for ongoing notes, links discovered midstream, and review discussion. Promote stable findings into the curated report.

## Curated report body

The curated report is the citable research deliverable.

Required sections:

- `Context` — why the research was needed and what question it answers.

Required by mode:

- **Comparative mode** — an `Options` section. Each option appears as a subsection that includes `Sources Consulted` and `Key Findings` content.
- **Single mode** — a `Findings` section that includes `Sources Consulted` and `Key Findings` content.

Optional sections:

- `Summary` — concise result overview.
- `Criteria` — comparison criteria and why they matter.
- `Raw Evidence` — compact excerpts, benchmark numbers, API signatures, or tables.
- `Limitations` — known uncertainty, missing access, or confidence boundaries.
- `Related Work` — specs, tasks, use cases, or reviews that cite or depend on the research.
- `Change Log` — required for material updates. See `./knowledge-body.md`.
- `Sources` — bibliography-style source list when not already covered in each option/finding.

## Decision neutrality

Research describes evidence. Specs make decisions.

Avoid prescriptive language such as:

- "Therefore we should choose X."
- "The implementation must use Y."
- "X is the correct architecture."

Prefer evidence-oriented language:

- "X has lower operational overhead under these constraints."
- "Y lacks feature Z in the documented API."
- "The evidence supports X if revocation latency is the primary criterion."

If a decision is reached, record it in a spec's `Decision Log` section or another appropriate knowledge page, and cite the research.

## Publishing rule

Publish or update the curated report when:

- The research question is clear.
- Sources consulted are listed.
- Findings are grounded in sources.
- Comparative reports cover each option with similar depth or explain why not.
- Limitations or confidence boundaries are visible.
- The report can be cited by a spec, task, or review without relying on hidden discussion.

The first publication should add a `Change Log` entry linking to the workflow issue.

## Review before done

Before marking research `done`, perform or request a quality review for:

- Source quality.
- Claim grounding.
- Option balance in comparative mode.
- Missing criteria.
- Bias or premature decision-making.
- Clear limitations.

Review findings should become `review` items if they need workflow tracking.

## Citing research

Specs and tasks should cite the curated report, not a long issue comment thread.

Use canonical references or links in the `Related Work` section using the provider's link form. The workflow issue remains useful for audit and discussion, but the curated report is the stable citation target.

## Common mistakes

- Publishing raw notes as the curated report.
- Making a decision in research instead of in a spec.
- Comparing options with uneven evidence without explaining why.
- Marking research `done` before a citable report exists or before the issue explains why no report is needed.
- Hiding source links in comments instead of the curated report.

## Do not

- Do not store the final research deliverable only in an issue body when a knowledge backend is configured.
- Do not create the curated report before the workflow issue unless importing existing documents.
