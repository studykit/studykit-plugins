# Workflow Actors Authoring

An actors page is a **knowledge-backed actor registry**. It catalogs every person and system that participates in this project's use cases, so each actor has a single canonical identity that other artifacts can cite.

Actors is curated knowledge. It is stored in the configured knowledge backend, not the issue backend.

Companion contracts:

- `./body.md`

## Storage role

`actors` is stored in the knowledge backend.

Workflow `usecase` issues and curated `usecase` pages cite actor names from this page; the actors page itself is the only place where actor identity is defined. The page should be readable independently as the project's actor catalog — a reader should not need to scan use cases to learn who an actor is.

## Purpose

Use actors for canonical actor identity:

- Person actors (end users, operators, administrators, support roles).
- System actors (services, scheduled jobs, external integrations) when they trigger or fulfill user-visible flows.
- General role description that holds across every use case the actor participates in.
- Privileges or authorization scope when those shape what the actor can do.

Do not use actors for per-use-case behavior. Per-flow actions belong on the curated `usecase` page that names the actor.

## Body shape

Required sections:

- `Actors` — registry of every actor that participates in this project's use cases.

Each actor entry should include:

- **Name** — canonical reference name. Reused verbatim across use case issues and curated pages.
- **Type** — `person` or `system`.
- **Description** — one-paragraph definition of who the actor is in this project, what they generally care about, and the scope of their involvement.
- **Privileges** — authorization scope when it shapes what the actor can do (e.g., admin-only operations). Omit when no scope distinction matters.

Optional sections:

- `Role Groups` — clusters of actors that share scope (e.g., `Operators`, `End Users`). Useful when multiple person actors share privileges or interact with overlapping screens.
- `Related Work` — workflow issues, specs, use cases, research, or reviews that inform the actor catalog.
- `Change Log` — required for material updates. See `./body.md`.

## Actor name stability

Actor names are reference targets for use cases, specs, architecture, and code.

Do not rename an actor silently. If a rename is needed:

1. Update the actors page.
2. Add a `Change Log` entry with the causing work item.
3. Update affected use case issues and curated pages, or create review items for deferred updates.

## Identity vs participation

Keep these two layers separate:

- **Identity** lives on the actors page — who the actor is in general (description, type, privileges).
- **Participation** lives on each use case — what the actor does in *that specific flow*.

The same actor named in three use cases should appear once on the actors page, with general identity, and three times in use case `Actors` sections, each citing the canonical name with the per-flow role description.

## Specificity

Name actors by their role and scope, not by generic titles:

- Bad: `User`, `The Team`, `Operator`.
- Good: `Study Group Owner`, `Live Stream Viewer`, `Content Moderator`, `Push Notification Service`.

A name is too generic when two different roles in the project could both reasonably claim it.

## Content boundaries

Use these boundaries to place actor-related content. Do not encode these as metadata relationships.

- Use `actors` for canonical identity.
- Use `usecase` (issue and curated page) for per-flow participation.
- Use `domain` for nouns that name product concepts, not actors.
- Use `context` for product framing, not the actor roster.
- Use `architecture` for runtime components, not for system actors that user flows reference.
- Use `spec` for prescriptive contracts, not for actor permissions.

## Drift and feedback

If a use case names an actor that is missing from this page, create a `review` item targeting the actors page; describe the missing actor and the causing use case in prose.

If a use case describes an actor in a way that contradicts the identity on this page, create a `review` item targeting the actors page and the causing use case; describe the contradiction in prose so the user can decide which side to update.

If a registry entry is missing required fields, has an abstraction level that drifts from the rest of the page (e.g., one actor named by role and another by job title), or appears to duplicate another entry, create a `review` item targeting the actors page; describe the issue in prose.

## Change log

Every material actors change should include a `Change Log` entry linking to the causing work item. Do not duplicate the issue discussion in the page.

## Common mistakes

- Missing the `Actors` section.
- Defining actor identity inside individual use case bodies instead of citing the canonical name from this page.
- Generic actor names (`User`, `The System`) that conflate distinct roles.
- Mixing per-flow role description into the identity entry on this page.
- Renaming actors without updating downstream use case references or filing review items.
- Multiple registry entries that describe the same actor under different names.
- Listing system components that have no user-visible role in any use case (those belong in `architecture`).
