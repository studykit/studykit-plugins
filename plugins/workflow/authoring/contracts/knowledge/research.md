# Workflow Research Authoring — Knowledge Side

This file covers the **knowledge side** of `research`: the curated report that carries final findings, evidence, options, and recommendation-neutral conclusions.

Common rules that apply across both sides (definition, dual-role overview, when research is warranted, decision neutrality) live in `../research.md`. Read that file in addition to this one.

Companion contracts:

- `./body.md`
- Research rules common to both sides: `../research.md`

## Storage role (knowledge side)

The curated report lives on the configured knowledge backend. Purpose: final findings, sources, comparisons, and reusable evidence. The curated report should link back to the workflow issue once published.

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
- `Change Log` — required for material updates. See `./body.md`.
- `Sources` — bibliography-style source list when not already covered in each option/finding.

## Publishing rule

Publish or update the curated report when:

- The research question is clear.
- Sources consulted are listed.
- Findings are grounded in sources.
- Comparative reports cover each option with similar depth or explain why not.
- Limitations or confidence boundaries are visible.
- The report can be cited by a spec, task, or review without relying on hidden discussion.

The first publication should add a `Change Log` entry linking to the workflow issue.

## Citing research

Specs and tasks should cite the curated report, not a long issue comment thread.

Use canonical references or links in the `Related Work` section using the provider's link form. The workflow issue remains useful for audit and discussion, but the curated report is the stable citation target.

## Common mistakes (knowledge side)

- Publishing raw notes as the curated report.
- Making a decision in research instead of in a spec.
- Comparing options with uneven evidence without explaining why.

## Do not (knowledge side)

- Do not create the curated report before the workflow issue unless importing existing documents.
