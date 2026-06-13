<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch every `usecase` ref the caller named, plus
  every `prior-review-refs` entry, in a single `fetch` call
  (the verb accepts multiple refs). Read the cached body for use
  cases and (for prior reviews) the body only — comments are not
  needed for deduplication.
- `new` — publish the per-finding `review` issue (one finding
  per item). Used with `--type review`, `--related <usecase-ref>`,
  and (when the provider supports labels) `--label usecase-reviewer`
  so `source` is encoded at publish time.
- `link` — used only when a finding spans multiple use cases
  and the additional `--related` links could not be set at publish
  time.
- `comment` — used only on prior open `review` issues that the
  agent dedups a new finding against this run. The comment carries
  the re-raised concern so the trail is visible. Never used on
  `usecase` issues themselves.

</commands>
