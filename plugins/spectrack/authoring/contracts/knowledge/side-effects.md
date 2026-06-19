# Knowledge Side Effects

A "knowledge side effect" is a change implied by work on one workflow surface (a use case, a task, a research item, etc.) that requires an update on a separate knowledge page. Surface the change as a workflow `review` issue with the affected knowledge surface as the target.

This file is the shared **how**. The per-artifact authoring contracts under `./` define **when** a side effect fires for each artifact type (see each contract's `Knowledge side effects` or `Drift and feedback` section). The originating skill / agent decides the moment of detection; this procedure governs the resulting `review` filing.

Do not edit the affected knowledge page inline from the originating skill / agent. The page edit is the work the new `review` item tracks; touching the page directly defeats the trackable-resolution model.

## Side-effect categories

Trigger a `review` item when the originating work implies any of:

| Side effect | `target` (knowledge surface) | Typical situation |
|---|---|---|
| New domain concept or relationship | `domain` page | The work introduces a noun/relationship that is not yet in `domain.md`. |
| New actor (person or system) | `actors` knowledge page | Discovery or implementation surfaced an actor the project has not catalogued. |
| Scope or problem framing change | `context` page | The work widens, narrows, or contradicts the original framing in `context.md`. |
| New screen or interaction group | `context` page (Screens section) | A new UI surface is implied that the product context hasn't named. |
| New non-functional requirement | `nfr` page | A user-visible non-functional constraint surfaces (latency, freshness, throughput, accessibility). |
| New implementation contract | `spec` page | The work implies an API / schema / protocol shape that needs a `spec` to anchor downstream `task` issues. |
| Architecture decision implied | `architecture` page | The work forks based on an architectural choice that has not been made. |

Each `review` item contains one actionable finding — split unrelated side effects, but keep tightly coupled details together when they explain the same target problem.

## Publish the review item

1. Resolve the `review` authoring docs through the `<authoring-resolver>`:

   ```bash
   spectrack mustread --type review
   ```

   Follow the body shape the resolver returns. Review bodies stay deliberately compact: required `Description`, optional `Suggested Fix` and `Evidence`.

2. Draft the `review` body under a scratch path the originating skill / agent picks (e.g., `$(spectrack project-dir .spectrack-cache/<originator>-side-effects/<slug>.md)` — the helper resolves the project root and creates the parent, anchoring on the main repo so the draft survives worktree teardown). Include in `Description`:

   - What is missing or wrong on the knowledge surface.
   - Why it matters (one or two sentences, grounded in the originating work).
   - What would resolve it (which page section to add or update).

   Reference the causing workflow ref in `Description` so the reviewer can trace back without you needing a separate field.

3. Publish via `spectrack issue new --type review`. Pass:

   - `--title` — short concern phrase ("Missing domain concept: meeting summary").
   - `--body-file` — the temp file from step 2.
   - `--assignee me` — the user owns the follow-up by default.
   - `--related <originator-ref>` — link the causing artifact so the side-effect chain is reviewable from either direction.

4. If the originating skill / agent maintains a session task list, add a task `"Side effect: review <ref>"` and mark it completed once the issue is published. The `review` item is the durable record; the task list is just the session map.

## Anti-patterns

- Editing the affected knowledge page inline. The page edit is the work the new `review` item tracks; touching the page directly defeats the trackable-resolution model.
- Packing unrelated knowledge concerns into one `review` item.
- Filing a `review` item that has no concrete target ("the docs need work"). Choose the narrowest useful knowledge surface, or explain in `Description` why the concern is cross-cutting.
