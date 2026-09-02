<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch the implementation issue. Read the cached body
  and every `comment-*.md` projection.
- `comment` — append the single audit comment carrying
  `## Verdict` / `## Reasoning` / `## Actionable` / `## Notes`. This is
  the only write this agent performs; on append failure the agent
  falls back to a local sidecar file.

</commands>
