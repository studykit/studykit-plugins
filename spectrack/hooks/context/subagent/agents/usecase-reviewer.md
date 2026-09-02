<commands>

Per-verb flags and usage: `spectrack issue <verb> --help`. The verbs
this agent uses:

- `fetch` — fetch every `usecase` ref the caller named, plus
  every `prior-review-refs` entry, in a single `fetch` call
  (the verb accepts multiple refs). Read the cached body for use
  cases and (for prior reviews) the body only — comments are not
  needed for deduplication.
- `new` — publish the per-finding `review` issue (one finding
  per item). Used with `--type review`, `--blocking <usecase-ref>`
  (the finding blocks the use case it targets), and (when the
  provider supports labels) `--label usecase-reviewer` so `source`
  is encoded at publish time. Run `spectrack issue new --help` for
  the blocking flag the configured backend accepts.
- `link` — used only when a finding spans multiple use cases, to add
  the additional `--blocking` links that could not be set at publish
  time (verb syntax: `spectrack issue link --help`).
- `comment` — used only on prior open `review` issues that the
  agent dedups a new finding against this run. The comment carries
  the re-raised concern so the trail is visible. Never used on
  `usecase` issues themselves.

</commands>
