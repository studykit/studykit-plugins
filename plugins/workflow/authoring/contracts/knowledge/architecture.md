# Architecture Authoring

An architecture page is a **knowledge-backed design-intent reference** for the current system shape: components, responsibilities, integration boundaries, technology stack, and test strategy.

Architecture is curated knowledge, stored in the configured knowledge backend, not the issue backend. Issue-backed work may cause architecture updates, but the page itself is a knowledge page.

Companion contracts:

- `./body.md`

## Purpose

Architecture records the current design shape that implementation work should align with.

Use it for:

- System overview.
- Component responsibilities.
- Interfaces exposed or consumed by components.
- Cross-component dependencies.
- Technology stack.
- Testing strategy at the system level.

Do not use it for:

- Long decision rationale.
- Raw discussion.
- Roadmaps.
- Task-level implementation plans.
- Detailed API/schema contracts that belong in specs.

## Body shape

Required sections:

- `Overview` — high-level architectural narrative.
- `Components` — component definitions, responsibilities, interfaces, and dependencies.
- `Technology Stack` — chosen runtime, framework, libraries, persistence, and build tooling.
- `Test Strategy` — unit/integration/e2e split, isolation strategy, fixtures, and test boundaries.

Optional sections:

- `Component Diagram` — diagram or link to external diagram artifact.
- `External Dependencies` — third-party services, vendor APIs, upstream systems.
- `Related Work` — issues, specs, reviews, use cases, or research that inform the architecture.
- `Change Log` — required for material updates. See `./body.md`.

## Component anchors

Component headings are reference targets for tasks, bugs, specs, and reviews.

Keep component names stable. If a component is renamed:

1. Update the architecture page.
2. Add a `Change Log` entry with the causing work item.
3. Update affected specs/tasks/reviews or create review items for deferred updates.

Do not silently rename component headings.

## Decision rationale

Architecture records the current shape. Durable rationale belongs in specs, especially the spec's `Decision Log` or `Rejected Alternatives` sections.

A short rationale sentence is acceptable when it helps readers understand the current shape. Long comparisons and rejected options belong in a spec or research report.

## Content boundaries

Use these boundaries to place architecture content. Do not encode these as metadata relationships.

- Use `domain` for vocabulary, concepts, relationships, and state transitions.
- Use `context` for problem framing, product scope, and original idea.
- Use `nfr` for non-functional requirements.
- Use `ci` for exact test commands and CI execution contract.
- Use `spec` for prescriptive API/schema/protocol contracts.

## Common mistakes

- Writing executable test commands here instead of `ci`.
- Using architecture as a roadmap or milestone plan.
- Listing considered options in `Technology Stack` instead of recording chosen stack only.
- Packing long decision rationale into `Overview` instead of a spec.
- Renaming component headings without updating references or creating review items.
