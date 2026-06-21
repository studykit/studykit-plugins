# Architecture Authoring

An architecture page is a **knowledge-backed reference for the current system shape** — components, responsibilities, integration boundaries, and the chosen technology stack. It records the design that implementation work should align with, not decision rationale (that belongs in a `spec`) or a roadmap.

## Body shape

There is no fixed section list. Describe the system's shape in whatever sections fit it, keeping each one narrow and letting the structure follow the architecture. A typical page covers a high-level overview, the components and their responsibilities/interfaces/dependencies, the chosen technology stack, and the system-level test strategy — but include only what the system actually needs.

Record the **chosen** shape and stack, not the options considered; comparisons and rejected alternatives belong in a `spec` or a research report. A short rationale sentence is fine when it helps a reader understand the current shape.

## Component anchors

Component headings are reference targets for tasks, bugs, specs, and reviews, so keep their names stable. If a component is renamed, record the cause in `Change Log` and update the affected specs/tasks/reviews or open review items for the deferred updates. Do not silently rename a component heading.

## Content boundaries

Place content on the right page rather than packing it here:

- `domain` — vocabulary, concepts, relationships, state transitions.
- `context` — problem framing, product scope, original idea.
- `nfr` — non-functional requirements.
- `ci` — exact test commands and the CI execution contract.
- `spec` — prescriptive API/schema/protocol contracts and decision rationale.
