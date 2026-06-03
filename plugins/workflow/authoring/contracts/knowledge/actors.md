# Actors Authoring

An actors page is a **knowledge-backed actor registry**: it catalogs every person and system that participates in this project's use cases, giving each a single canonical identity other artifacts can cite. It is curated knowledge, stored in the configured knowledge backend, not the issue backend.

Companion contract: `./body.md`.

## Storage role

Workflow `usecase` issues and curated `usecase` pages cite actor names from this page; the actors page is the only place actor identity is defined. The page should read independently as the project's actor catalog — a reader should not have to scan use cases to learn who an actor is.

## Purpose

Use actors for canonical actor identity:

- Person actors (end users, operators, administrators, support roles).
- System actors (services, scheduled jobs, external integrations) when they trigger or fulfill user-visible flows.
- General role description that holds across every use case the actor participates in.
- Privileges or authorization scope when those shape what the actor can do.

Do not use actors for per-use-case behavior; per-flow actions belong on the curated `usecase` page that names the actor.

## Body shape

Required section:

- `Actors` — registry of every actor participating in this project's use cases. Each entry includes:
  - **Name** — canonical reference name, reused verbatim across use case issues and curated pages.
  - **Type** — `person` or `system`.
  - **Description** — one paragraph: who the actor is in this project, what they care about, and the scope of their involvement.
  - **Privileges** — authorization scope when it shapes what the actor can do (e.g., admin-only operations). Omit when no scope distinction matters.

Optional sections:

- `Role Groups` — clusters of actors sharing scope (e.g., `Operators`, `End Users`). Useful when person actors share privileges or overlapping screens.
- `Related Work` — workflow issues, specs, use cases, research, or reviews that inform the catalog.
- `Change Log` — required for material updates. See `./body.md`.

## Actor name stability

Actor names are reference targets for use cases, specs, architecture, and code. Do not rename an actor silently. To rename:

1. Update the actors page.
2. Add a `Change Log` entry with the causing work item.
3. Update affected use case issues and curated pages, or create review items for deferred updates.

## Identity vs participation

Keep the two layers separate:

- **Identity** lives on the actors page — who the actor is in general (description, type, privileges).
- **Participation** lives on each use case — what the actor does in *that specific flow*.

An actor named in three use cases appears once on the actors page (general identity) and three times in use case `Actors` sections (each citing the canonical name with its per-flow role).

## Specificity

Name actors by role and scope, not generic titles. A name is too generic when two different project roles could both reasonably claim it.

- Bad: `User`, `The Team`, `Operator`.
- Good: `Study Group Owner`, `Live Stream Viewer`, `Content Moderator`, `Push Notification Service`.

## Content boundaries

Place actor-related content by these boundaries; do not encode them as metadata relationships.

- `actors` — canonical identity.
- `usecase` (issue and curated page) — per-flow participation.
- `domain` — nouns naming product concepts, not actors.
- `context` — product framing, not the actor roster.
- `architecture` — runtime components, not system actors that user flows reference.
- `spec` — prescriptive contracts, not actor permissions.

## Drift and feedback

Create a `review` item targeting the actors page (describing the issue in prose) when:

- A use case names an actor missing from this page — include the causing use case.
- A use case describes an actor in a way that contradicts this page — target both the page and the causing use case so the user can decide which to update.
- A registry entry is missing required fields, drifts in abstraction level (e.g., one actor named by role, another by job title), or appears to duplicate another entry.

## Common mistakes

- Defining actor identity inside use case bodies instead of citing the canonical name from this page.
- Generic actor names (`User`, `The System`) that conflate distinct roles.
- Mixing per-flow role description into the identity entry here.
- Renaming actors without updating downstream use case references or filing review items.
- Multiple registry entries describing the same actor under different names.
- Listing system components with no user-visible role in any use case (those belong in `architecture`).
