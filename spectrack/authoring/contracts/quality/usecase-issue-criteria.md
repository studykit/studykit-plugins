# Use Case Issue Review Criteria

Quality criteria for reviewing workflow `usecase` issues. This file defines what to flag during review.

A reviewer applies each criterion below to every targeted use case. Each non-OK verdict becomes one `review` issue that blocks the use case it targets (with exceptions noted per criterion).

## 1. Size

A use case is too large when:

- The flow has steps that serve independent goals.
- The expected outcome describes two or more unrelated results.
- The situation covers multiple distinct scenarios that don't always occur together.
- Different actors are involved in different parts of the flow.

Suggested fix proposes the split (child titles + the goal each child owns).

## 2. Actor specificity

- The actor must be a specific person or system, not a generic `user` or `the team`.
- Every actor in the `Actors` section should be reusable across use cases — same name for the same role.

Suggested fix proposes a role-scoped rename.

## 3. Goal concreteness

- One thing the actor wants to achieve.
- `and` in the goal usually signals a split candidate, not a goal refinement.

## 4. Situation concreteness

- Bad: "When managing data."
- Good: "After finishing a 30-minute meeting with three absent teammates."

## 5. Flow completeness

- Numbered user-level actions.
- No missing steps between situation and outcome.
- Logical order.
- Stays at user level (see criterion 6).

## 6. Abstraction discipline

**Critical.** Use case bodies describe what the actor sees and does, not how the system implements it. Flag implementation terms anywhere in the body — for example: database/table/column names, API endpoints, HTTP status codes, internal service names, framework-specific identifiers, queue/cache mechanics, persistence steps that aren't user-visible.

Examples of leaks and their user-level rewrites:

- "stores the entry in the database" → "saves the entry"
- "returns 404" → "shows a 'not found' message"
- "calls the X API" → "(omit; the actor doesn't see this)"
- "writes to the events table" → "(omit, or rephrase as user-visible feedback)"

When raising the finding, cite the specific leaked phrase in `Description`'s body paragraphs (and in the `Quote` section) and propose the user-level rewrite in `Suggested Fix`.

## 7. Outcome measurability

- Bad: "things work better".
- Good: "absent teammates receive a 3-line summary within two minutes".

## 8. Overlap

Flag use cases that cover the same actor / goal / situation as another use case in the set. The body should name the overlapping ref(s) and recommend whether to merge, supersede, or differentiate.

## 9. Validation / error precision

For use cases that have validation or error-handling content:

- Are constraints user-visible and specific? ("Empty messages cannot be sent; maximum 100 KB diagram source") not "validates input".
- Are error states described from the user's perspective? ("Displays error message with retry option") not "returns 500".

For use cases that have no validation / error section but clearly have meaningful failure modes: flag the missing precision.

`Suggested Fix` for this criterion includes the user-level rewrite, modeled on the same principle as criterion 6 (state what the actor sees, not what the system does internally).

## 10. Cross-use-case consistency

- A use case referenced by another use case's `Related Work` must still exist. Flag stale references.
- Same noun across multiple use cases should be named consistently (singular/plural, same role/actor name). Flag inconsistencies.

## 11. Actor registry alignment

Applies only when the project has an actors registry. Skip this criterion when no registry exists; criterion 2 still covers within-set actor specificity.

Each actor named in a use case must resolve to a canonical entry on the registry. Flag when:

- A use case names an actor that does not appear in the registry. Suggested fix proposes either adding the actor to the registry (preferred) or renaming to an existing canonical entry.
- A use case names a canonical actor with a description or scope that contradicts the registry entry. Suggested fix proposes which side to update.
- A use case uses a name that looks like a near-variant of a canonical entry (singular/plural, role vs. job title). Suggested fix proposes the canonical form.

Findings under this criterion target the actors page. The calling agent's publishing contract determines how cross-surface findings are labeled (e.g., a knowledge-side label) and whether the use case is linked.
