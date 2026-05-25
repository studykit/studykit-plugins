# Spec Authoring

A workflow spec is a **knowledge-backed prescriptive implementation contract** for a single implementation surface: an API shape, schema, protocol, renderer rule, CLI surface, file format, integration contract, or other downstream implementation shape.

Specs are curated knowledge pages. They are stored in the configured knowledge backend, not the issue backend.

Companion contracts:

- `./body.md`

## Storage role

`spec` is stored in the knowledge backend.

Issue-backed work may create, review, or apply a spec, but the spec itself is a knowledge page.

## Supersession

Supersession is an explicit authoring decision.

When a new spec replaces an older spec:

1. Add the older spec under the `Supersedes` section.
2. Explain the replacement in the new spec body.
3. Add `Change Log` entries to affected pages as needed.

Do not edit an old spec body merely to describe the new contract. The new spec carries the new contract. The old spec may point to the replacement when that update is useful and safe.

## Body shape

Required sections:

- `Context` — why this spec exists, what implementation surface it covers, and what is out of scope.
- `Specification` — prescriptive contract.

The `Specification` section is the heart of the spec. It should contain rules, fields, grammar, examples, API shape, protocols, constraints, or other details downstream work must follow.

Optional sections:

- `Supersedes` — required when the spec replaces prior specs.
- `Related Work` — tasks, reviews, use cases, research, or epics related to this spec.
- `Open Questions` — unresolved aspects the spec deliberately defers.
- `Consequences` — downstream effects for code, tooling, operations, or users.
- `Examples` — concrete cases that pin down the rules.
- `Decision Log` — concise rationale entries for decisions embedded in the spec.
- `Rejected Alternatives` — options considered and why they lost.
- `Change Log` — semantic cause index for material edits. See `./body.md`.
- `Sources` — external sources or research reports used as evidence.

## Decision rationale

Use the `Decision Log` section for durable rationale. Each entry should pair a date with a short statement of the chosen approach and the reason. Earlier entries are append-only. If a decision changes, append a new entry explaining the correction.

Do not introduce a separate decisions page for routine spec-local rationale.

## Related work and research

Specs may be informed by research, use cases, tasks, reviews, and architecture/domain pages. Use canonical references in the `Related Work` section, one item per bullet, using the provider's link form.

Research should provide evidence. The spec makes the decision.

## Change log

Every material update should add a concise `Change Log` entry linking to the causing work item. Do not duplicate issue discussion or review threads in the spec.

## Readiness rule

A spec should not be used as an implementation contract until:

- The `Context` section is present and clear.
- The `Specification` section is present and prescriptive.
- Open questions that block implementation are resolved or explicitly deferred.
- Supersession links are visible when replacing another spec.
- Related work and sources needed to understand the decision are linked.

## Common mistakes

- Missing the `Context` or `Specification` section.
- Treating the spec as a discussion thread instead of a curated contract.
- Packing several unrelated contracts into one spec.
- Hiding implementation decisions in task issues instead of updating or creating a spec.
- Treating a spec as implementation-ready while blocking open questions remain unresolved.

## Do not

- Do not author specs for routine implementation details such as variable names or formatting choices.
- Do not make research conclusions directly prescriptive; cite research and record the spec decision separately.
