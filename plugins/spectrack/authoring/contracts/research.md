# Research Authoring

A research item is a **time-boxed, evidence-gathering investigation** — of a question, a technical topic, a product question, or a comparison of alternatives. Use it when the next step is gathering evidence, not building. Use `spike` instead when the output is exploratory code or a runnable proof of concept, and `spec` when the decision is already made and the task is to write the prescriptive contract.

## Clarify the brief first

Research is only useful if it answers the right question, so settle the brief with the requester before investigating. Confirm:

- The question or decision the research must inform, in one sentence.
- The alternatives or scope to cover, and what is explicitly out of scope.
- The criteria that make an answer good enough — what actually matters for the decision.
- How the result will be used — which spec, task, or decision depends on it.

If any of these is unclear, ask rather than assume.

## Minimum content

Keep the write-up minimal and shaped to the subject. Only two things are required:

- A `Context` section — why the research was needed and the question it answers.
- A body of findings grounded in sources, organized in whatever shape fits the subject: one subsection per alternative for a comparison, a single findings section for one question, or subject-specific sections that mirror what was investigated.

There is no prescribed section list beyond these. Add a section only when the subject needs it and it carries one clear thing; otherwise fold the content into an existing section. Write it as curated reference material — current findings, not raw notes or work logs. Use clear, canonical section names.

## Evidence discipline

Findings are only as trustworthy as their grounding:

- Attribute every load-bearing claim to a source that was actually consulted.
- Prefer primary or authoritative sources over secondary summaries. When a figure comes from an interested or unverifiable source, label it as directional rather than stating it as fact.
- When sources disagree, reconcile them rather than silently choosing one.
- Cover each compared alternative with similar depth, or say why not.
- Do not defer anything answerable with the sources at hand — investigate it. Reserve open items for genuine boundaries (missing access, a time box, scope set aside), each stated with its reason.

## Decision neutrality

Research describes evidence; specs make decisions. Avoid prescriptive language ("we should choose X", "the implementation must use Y") and do not add a recommendation or decision section. Prefer evidence-oriented statements: "X has lower operational overhead under these constraints"; "the evidence supports X if revocation latency is the primary criterion". If a decision is reached, record it in a spec and cite the research.
