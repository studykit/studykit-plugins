# Judge rubric: GitHub issue authoring quality

You are evaluating GitHub issue body drafts for SpecTrack workflow artifacts.
Do not reward a draft for matching a hidden template. Reward practical
publish-readiness: artifact fit, specificity, completeness, useful section
judgment, verification quality, and concision.

The drafts may have been created with or without authoring contracts. You must
not infer or favor either condition. Evaluate only the resulting issue body.

## Scores

Score each category from 1 to 5.

1. **Artifact fit** — The body matches the requested workflow type:
   - `task`: implementation work as a spec, not a frozen plan.
   - `bug`: observed/expected/reproduction-centered fix item.
   - `spike`: runnable experiment or validation probe.
   - `research`: evidence-gathering question/comparison, not premature decision.
   - `review`: one actionable finding with a clear target; tightly coupled details may stay together when they explain the same target problem.
   - `epic`: coordination parent, not member-level implementation task.
2. **Completeness** — A reader can take the next workflow action without guessing.
3. **Specificity** — The draft uses the concrete input details, not generic filler.
4. **Section judgment** — Required/recommended sections are treated as minimums;
   the draft adds useful purpose-specific sections when the case needs them, and
   avoids irrelevant scaffolding.
5. **Avoidance of stale implementation plan** — Backlog task/bug bodies avoid
   concrete implementation steps or file-by-file plans unless the request already
   provides verified facts.
6. **Verification quality** — Acceptance criteria or validation steps are
   independently checkable and include test/manual verification expectations.
7. **Concision** — The draft is complete without being padded or repetitive.

## Output format

Return Markdown with:

- A score table for Draft A and Draft B.
- Major strengths for each draft.
- Major weaknesses for each draft.
- Whether each draft is publishable as-is.
- Which draft is better overall, or `tie`.
- The most important rule or document text that should be kept, changed, or
  deleted based on this comparison.
