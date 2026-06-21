# Domain Authoring

A domain page is a **knowledge-backed shared-vocabulary reference** — the cross-cutting product and business concepts that use cases, specs, architecture, tasks, reviews, and research reuse consistently. It is not for runtime components or framework constructs (those go in `architecture`) unless the name is itself a domain concept.

## Body shape

A `Concepts` section is required — the glossary of entities, value objects, and significant domain terms. Give each concept a name, a one-paragraph definition, examples when useful, and any invariants or constraints that matter.

Add other sections only when the vocabulary needs them — for example relationships (associations, ownership, cardinality) or named lifecycle states and their transitions. Prefer compact, scannable forms (tables, Mermaid, ASCII, short lists) over long prose when showing relationships or states.

## Concept stability

Domain terms are reference targets for use cases, specs, architecture, and code, so keep their names stable. If a concept is renamed, record the cause in `Change Log` and update the affected use cases/specs/architecture/tasks/reviews or open review items for the deferred updates. Do not rename a concept silently, and do not define the same concept under two names.

## Content boundaries

Place content on the right page rather than here:

- `architecture` — runtime components and integration boundaries.
- `context` — product/problem framing.
- `usecase` — user-visible interactions.
- `nfr` — non-functional targets.
- `spec` — prescriptive contracts.

## Drift and feedback

If a concept recurs in use cases, specs, architecture, or tasks but is missing here — or if `architecture` uses a term differently from this page — open a `review` item targeting the relevant page(s) and the causing work item, describing the gap in prose.
