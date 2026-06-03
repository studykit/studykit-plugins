# NFR Authoring

An NFR page is a **knowledge-backed non-functional requirements reference**, recording measurable cross-cutting properties such as performance, security, scalability, accessibility, reliability, privacy, compliance, and operational constraints. It is curated knowledge, stored in the configured knowledge backend, not the issue backend. Issue-backed work may cause NFR updates, but the page itself is a knowledge page.

Companion contract: `./body.md`.

## Purpose

Use NFR for measurable cross-cutting requirements: performance targets, security requirements, scalability bounds, accessibility requirements, reliability/availability targets, privacy or compliance constraints, and operational constraints. NFRs should affect use cases, architecture, specs, tests, or implementation priorities.

Do not use NFR for functional behavior; that belongs in use cases and specs.

## Body shape

Required section:

- `Requirements` — a table of NFR entries (the provider convention defines the literal table form). Recommended columns:
  - **ID** — stable short identifier for references.
  - **Description** — concise requirement statement.
  - **Affected Scope** — use cases, specs, systems, or `(all)`.
  - **Measurable Criteria** — threshold, standard, check, or measurable condition.
  - **Verification** — how the requirement is verified.

Optional sections:

- `Rationale` — why the NFR matters when not obvious.
- `Related Work` — issues, specs, reviews, research, use cases, or architecture pages related to NFR changes.
- `Change Log` — required for material updates. See `./body.md`.

## Measurability rule

Every NFR should be measurable. Avoid vague forms ("the app should be fast", "security should be strong"); prefer measurable ones:

- "p95 response latency under 200 ms for authenticated search."
- "All admin actions require audit log entries with actor, timestamp, action, and target."
- "UI meets WCAG 2.2 AA for the onboarding flow."

If a requirement cannot yet be measured, create a `review` item describing the open question or missing measurement basis rather than adding an aspirational NFR.

## Verification

Each NFR should have a verification path: automated test, CI check, monitoring query, audit process, manual review procedure, or compliance evidence. If verification is not yet known, mark it as an open question and create a review item if it blocks work.

## Content boundaries

NFR records the target.

- `architecture` — the design response.
- `ci` — how tests/checks run.
- `spec` — precise contracts when an NFR affects an API, schema, protocol, or format.

Do not put implementation strategy in the NFR page unless it is part of the requirement itself.

## Common mistakes

- Functional behavior here instead of use cases/specs.
- Implementation strategy here instead of architecture/spec.
- NFRs with no verification path or follow-up review item.
