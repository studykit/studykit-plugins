# Actors Authoring

An actors page is a **knowledge-backed actor registry** — the single place each person and system that participates in the project's use cases is given a canonical identity that other artifacts cite. `usecase` issues and curated pages cite actor names from here; the page should read on its own as the project's actor catalog, so a reader never has to scan use cases to learn who an actor is.

## Body shape

An `Actors` section is required — the registry of every actor participating in the project's use cases. Each entry includes:

- **Name** — canonical reference name, reused verbatim across use case issues and curated pages.
- **Type** — `person` or `system`.
- **Description** — one paragraph: who the actor is in this project, what they care about, and the scope of their involvement.
- **Privileges** — authorization scope when it shapes what the actor can do; omit when no distinction matters.

Add other sections only when useful — for example role groups clustering actors that share scope. Include a system actor only when it triggers or fulfills a user-visible flow; pure runtime components belong in `architecture`.

## Identity vs participation

Keep the two layers separate: **identity** (who the actor is in general) lives here; **participation** (what the actor does in a specific flow) lives on each use case. An actor in three use cases appears once here and three times in use case `Actors` sections, each citing the canonical name with its per-flow role.

## Name stability and specificity

Actor names are reference targets for use cases, specs, architecture, and code, so keep them stable: to rename, record the cause in `Change Log` and update affected use cases/pages or open review items. Name actors by role and scope, not generic titles — a name is too generic when two different project roles could both claim it (bad: `User`, `Operator`; good: `Study Group Owner`, `Push Notification Service`).

## Content boundaries

- `actors` — canonical identity.
- `usecase` — per-flow participation.
- `domain` — product-concept nouns, not actors.
- `context` — product framing, not the actor roster.
- `architecture` — runtime components, not system actors flows reference.
- `spec` — prescriptive contracts, not actor permissions.

## Drift and feedback

Open a `review` item targeting the actors page (describing the issue in prose) when a use case names an unregistered actor, describes an actor in a way that contradicts this page (target both), or when an entry is missing required fields, drifts in abstraction level, or duplicates another.
