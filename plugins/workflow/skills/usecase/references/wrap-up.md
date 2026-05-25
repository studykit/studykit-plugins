# Wrap Up

The interview ends only when the user says so. Never conclude on
your own — even when all four gaps seem covered, the user may want
to go deeper.

When the user indicates they're done, mark the in-progress phase
task `completed`, then run the End-Iteration procedure below.

## End-Iteration procedure

1. **Dispatch the explorer** — `Agent(subagent_type:
   "workflow:usecase-explorer")`. Pass:
   - The list of `usecase` issue refs created or refined this session.
   - An absolute output path for the advisory exploration report
     under `$(workflow project-dir .workflow-cache/usecase-explorations/<session-slug>.md)`.

   The explorer reads each referenced `usecase` issue via `workflow
   issue fetch`, evaluates the set from fresh perspectives (usage
   environment, user proficiency, collaboration, error handling,
   security/privacy), and writes the advisory report to the named
   path. It does **not** publish any issues.

2. **Reflect accepted candidates** — read the explorer's report and
   present its candidates to the user. For each candidate the user
   accepts, re-enter the discovery loop briefly to confirm the actor,
   goal, situation, flow, and expected outcome, then publish via
   `./progressive-extraction.md`. Skip the candidates the user
   rejects.

3. **Dispatch the reviewer** — `Agent(subagent_type:
   "workflow:usecase-reviewer")`. Pass:
   - The updated list of `usecase` issue refs (including any
     candidates reflected in step 2).
   - The absolute draft directory for per-finding `review` issue
     bodies under
     `$(workflow project-dir .workflow-cache/usecase-reviewer/<session-slug>/)`.
   - Optionally, refs of prior open `review` issues whose `source`
     is `usecase-reviewer` so the reviewer can deduplicate.

   The reviewer evaluates every use case against quality criteria
   (size, actor specificity, goal concreteness, situation
   concreteness, flow completeness, abstraction discipline,
   measurable outcome, overlap, validation/error precision,
   cross-use-case consistency, and — when an actors registry exists
   — actor registry alignment and registry quality) and publishes
   one `review` issue per finding via `workflow issue new --type
   review`, linked `--related` to the target use case.

4. **Walk findings with the user** — for each `review` ref the
   reviewer published, present the finding to the user. Resolve
   in-session when possible:

   - **Resolve in place** — apply the suggested change to the
     `usecase` issue body via `workflow issue update` (verb syntax at
     `<runbook>`'s `issue-update` intent), then close the `review`
     issue via `workflow issue update --state closed` (or the
     equivalent state verb at `<runbook>`'s `issue-state` intent).
     Show the user the before/after wording before applying the
     body change.
   - **Defer** — leave the `review` issue open. The user picks it up
     in a later iteration session via `./iteration-entry.md`.

5. **Session report** — present a concise summary in dialogue:
   - `usecase` issues confirmed this session — refs and titles.
   - `usecase` issues that still carry non-empty `Open Questions`.
   - Reviewer findings published — refs, with resolved vs deferred
     counts.
   - Research issues opened — refs.
   - Mock files generated — paths.

   Mark `"Wrap Up: Session report"` completed once the summary is
   delivered.

## Execution order

Explorer first (find gaps and new use case candidates), then
reviewer (validate the full set, including any reflected candidates).
Running the reviewer before the explorer wastes a review pass on a
set that is about to grow.

## When the user re-opens discovery mid-wrap-up

If the wrap-up walk reveals a gap the user wants to explore as a new
use case rather than as a `review` item, leave the `review` issue
open, re-enter `./progressive-extraction.md`, publish the new use
case, then add the new ref to the reviewer's `--related` for the
next iteration. Do **not** silently close the `review` issue —
discovery and quality review are different surfaces.
