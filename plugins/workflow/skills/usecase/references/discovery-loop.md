# Discovery Loop

Uncover enough context to write a concrete use case by targeting four
gaps. Pick the gap that is currently least clear and ask one focused
question; do not ask more than one question per turn.

- **What's happening now?** Current situation, trigger, surrounding work.
- **Who's involved?** People and systems participating → actors.
- **What should change?** The desired actor action or system response → flow.
- **What does success look like?** The observable outcome the actor expects.

Follow the conversation naturally. Stop probing a gap once it is
concrete enough to draft a use case at the right level of abstraction
(see the abstraction discipline in
`${CLAUDE_PLUGIN_ROOT}/authoring/common/usecase-authoring.md`).

## Actor capture

When the conversation reveals a new actor (person or system the use
case will name in the `Actors` section):

1. Confirm with the user — name, type (`person` / `system`), short
   description, and the privilege level the actor needs for this use
   case if relevant.
2. Record the actor in your working notes for the session. Reuse the
   same actor name across use cases when referring to the same role,
   so the actors story stays consistent on every issue body.
3. If the project's knowledge backend has an `actors` page, treat the
   new actor as a knowledge side effect — see
   `./knowledge-side-effects.md` for the `review`-item path. **Do not
   edit the `actors` page from this skill**; the skill's surface is
   issue-only.

## Anti-patterns

- Asking two or three questions at once because they feel related.
  Pick the most load-bearing one.
- Drilling into implementation ("which database?", "REST or
  WebSocket?"). Those belong in `spec`, `architecture`, or
  implementation tasks, not in use case discovery.
- Naming actors by their job title alone ("the user") when the
  privilege level or the specific role matters for what they can do
  in the flow.
