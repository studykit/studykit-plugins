# Spec Authoring

A workflow spec is a **knowledge-backed, prescriptive implementation contract** for a single implementation surface — an API shape, schema, protocol, renderer rule, CLI surface, file format, or other downstream contract. It is not for routine implementation choices like naming or formatting. Issue-backed work may create, review, or apply a spec, but the spec itself is a knowledge page.

## Body shape

Two sections are required:

- `Context` — why the spec exists, what surface it covers, and what is out of scope.
- `Specification` — the prescriptive contract itself, and the heart of the page: the rules, fields, grammar, API shape, protocols, constraints, and examples that downstream work must follow.

Add other sections only when the spec needs them; keep each narrow and let the contract drive the structure. Do not split one implementation surface across several specs, or pack unrelated contracts into one.

## Decision rationale

Record durable rationale in a `Decision Log` — each entry pairs a date with the chosen approach and the reason, append-only (when a decision changes, append a new entry explaining the correction). Keep spec-local rationale here rather than starting a separate decisions page. Research provides evidence; the spec makes the decision — cite the research, do not make its conclusions directly prescriptive.

## Supersession

Replacing an older spec is an explicit authoring step: list the older spec under `Supersedes`, explain the replacement in the new body, and record the cause in `Change Log` on the affected pages. The new spec carries the new contract — do not edit the old spec's body to describe it; the old spec may point forward when that is useful.

## Readiness

Do not treat a spec as an implementation contract until its `Context` is clear, its `Specification` is present and prescriptive, blocking open questions are resolved or explicitly deferred, supersession links are visible when it replaces another spec, and the related work and sources needed to understand the decision are linked.
