# Knowledge Side Effects

This skill produces workflow `usecase` issues only. Whenever a
confirmed use case implies a change on the knowledge side, surface
the change as a workflow `review` issue with the affected knowledge
surface as the target — per the **Knowledge side effects** rule in
`${CLAUDE_PLUGIN_ROOT}/authoring/common/usecase-issue-authoring.md`.

Do not edit knowledge pages inline from this skill, and do not draft
or publish curated `usecase` knowledge pages. The curated-page
publishing rule (in `usecase-knowledge-authoring.md`) requires the
flow to be stable; that happens in a follow-on session, not here.

## Side-effect categories

Trigger a `review` item when the use case implies any of:

| Side effect | `target` (knowledge surface) | Typical situation |
|---|---|---|
| New domain concept or relationship | `domain` page | The actor or flow introduces a noun/relationship that is not yet in `domain.md`. |
| New actor (person or system) | `actors` knowledge page (or `context` if the project has no `actors` page) | Discovery surfaced an actor the project has not catalogued. |
| Scope or problem framing change | `context` page | The use case widens, narrows, or contradicts the original framing in `context.md`. |
| New screen or interaction group | `context` page (Screens section) | A new UI surface is implied that the product context hasn't named. |
| New non-functional requirement | `nfr` page | A user-visible non-functional constraint surfaces (latency, freshness, throughput, accessibility). |
| New implementation contract | `spec` page | The use case implies an API / schema / protocol shape that needs a `spec` to anchor downstream `task` issues. |
| Architecture decision implied | `architecture` page | The use case forks based on an architectural choice that has not been made. |

Each `review` item contains **one concern** — do not pack several
side effects into one item.

## Publish the review item

1. Resolve the `review` authoring docs through the
   `<authoring-resolver>`:

   ```bash
   workflow authoring_resolver.py --type review
   ```

   Follow the body shape the resolver returns. `review-authoring.md`
   keeps the body deliberately compact: required `Description`,
   optional `Suggested Fix`, `Evidence`, `Resume`.

2. Draft the `review` body under
   `/tmp/workflow-usecase-side-effects/<slug>.md`. Include in
   `Description`:

   - What is missing or wrong on the knowledge surface.
   - Why it matters (one or two sentences, grounded in the use case
     just confirmed).
   - What would resolve it (which page section to add or update).

   Reference the causing `usecase` issue ref in `Description` so the
   reviewer can trace back without you needing a separate field.

3. Publish via `workflow issue new --type review` (verb syntax at
   `<runbook>`'s `issue-new` intent). Pass:

   - `--title` — short concern phrase ("Missing domain concept:
     meeting summary").
   - `--body-file` — the temp file from step 2.
   - `--assignee me` — the user owns the follow-up by default.
   - `--related <usecase-ref>` — link the causing use case so the
     side-effect chain is reviewable from either direction.

4. Add a task `"Side effect: review <ref>"` and mark it completed
   once the issue is published. The `review` item is the durable
   record; the task list is just the session map.

## When the side effect is local to one use case

If the concern is genuinely local — a vague situation in the use case
itself, an outcome that is not measurable — do **not** open a
separate `review` item. Append a comment to the `usecase` issue via
`workflow issue comment` (verb syntax at `<runbook>`'s `issue-comment`
intent) and name the concern in the issue's `Open Questions` section
on next body update. The wrap-up reviewer covers quality concerns of
this kind; do not pre-empt it with a `review` item here.

## Anti-patterns

- Editing `domain.md`, `actors.md`, `nfr.md`, or `context.md` inline.
  This skill is issue-only.
- Drafting a curated `usecase` knowledge page now. Defer per the
  publishing rule in `usecase-knowledge-authoring.md`.
- Packing multiple knowledge concerns into one `review` item. One
  item, one concern.
- Filing a `review` item that has no concrete target ("the docs need
  work"). Choose the narrowest useful knowledge surface, or explain
  in `Description` why the concern is cross-cutting.
