<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — published mode only: fetch the audited issue. Read the
  cached body and every `comment-*.md` projection — the recorded cause or
  approach may live in a comment, not only the body.
- `comment` — published mode only: append the single verdict comment
  carrying `## Verdict` / `## Reasoning` / `## Actionable` / `## Notes`.
  This is the only tracker write this agent performs; on append failure it
  falls back to a local sidecar file. Draft mode performs no tracker write.

</commands>
