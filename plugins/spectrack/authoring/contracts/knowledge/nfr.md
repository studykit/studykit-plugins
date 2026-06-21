# NFR Authoring

An NFR page is a **knowledge-backed non-functional requirements reference** — measurable cross-cutting properties such as performance, security, scalability, accessibility, reliability, privacy, compliance, and operational constraints that affect use cases, architecture, specs, tests, or priorities. Functional behavior belongs in use cases and specs, not here.

## Body shape

A `Requirements` section is required — a table of NFR entries (the provider convention defines the literal table form). Recommended columns: a stable **ID** for references, a concise **Description**, the **Affected Scope** (use cases, specs, systems, or `(all)`), the **Measurable Criteria**, and the **Verification** path.

Add other sections only when needed — for example a rationale for an NFR whose importance is not obvious.

## Measurability

Every NFR must be measurable. Avoid vague forms ("the app should be fast"); prefer thresholds and standards — "p95 latency under 200 ms for authenticated search", "all admin actions write an audit entry with actor/timestamp/action/target", "onboarding meets WCAG 2.2 AA". If a requirement cannot yet be measured, open a `review` item for the missing measurement basis rather than recording an aspirational NFR.

## Verification

Every NFR needs a verification path: automated test, CI check, monitoring query, audit process, manual review, or compliance evidence. If verification is not yet known, mark it an open question and open a review item when it blocks work.

## Content boundaries

NFR records the target; the response lives elsewhere:

- `architecture` — the design response.
- `ci` — how tests/checks run.
- `spec` — precise contracts when an NFR affects an API, schema, protocol, or format.

Keep implementation strategy out of the NFR page unless it is part of the requirement itself.
