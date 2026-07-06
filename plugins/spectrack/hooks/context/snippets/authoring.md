<bash>
spectrack mustread \
  --type <type> \
  [--side issue|knowledge] \
  [--target <type>] \
  [--scope comment] \
  [--mode backlog|retroactive]
</bash>

- `--type` — required. The artifact type being authored. When `--type
  review`, the optional `--target` names the artifact type being
  reviewed; the resolver then returns the target's review criteria
  bundled with the review issue authoring contract.
- `--side` — required for dual-side types (`issue` or `knowledge`); for
  single-side types it defaults. When `--target` is set, `--side` refers
  to the target's side.
- `--target` — only valid with `--type review`. Names the artifact being
  reviewed (e.g., `--target usecase`, `--target task`). Returns review
  criteria for the target plus the review issue authoring contract.
  Cannot be `review`. Not compatible with `--scope comment`.
- `--scope comment` — comment-only updates. Returns the Markdown plus
  provider convention files only, not the full type body.
- `--mode` — required for `task`/`bug` content authoring; rejected for
  every other type, scope, or target. Names the authoring intent, which
  the resolver cannot infer — decide it from the user's request before
  calling. Check whether the change has already landed: if the code is
  already written, committed, or merged and you are documenting it after
  the fact, the mode is `retroactive` — pick it even when the user never
  says the word "retroactive". Otherwise the work is not yet done and the
  mode is `backlog`. Working out the cause, approach, and steps is not an
  authoring step — that happens against the current code when the item is
  picked up for implementation. The resolver returns a different contract
  set and different notes per mode:
  - `backlog` — the work is not yet done; the issue is the open spec.
    Record at least `Description`; add `Context`, `Acceptance Criteria`,
    and (for a bug) `Reproduction` to whatever level of detail is useful —
    a brief capture and a complete spec are both valid. No cause, approach,
    or implementation steps in the body.
  - `retroactive` — the work has already landed (already implemented,
    committed, or merged). The body records facts after the fact — what
    changed, the cause when relevant, how it was actually done, and the
    checks that ran — not a plan.

The resolver returns markdown listing files to read before drafting.
Treat any bullet in a notes section as a binding rule for the calling
flow. If `--type` is not one of SpecTrack's workflow artifact types
below, the resolver returns `NONE`: there is no authoring contract to
read, so create the artifact directly. How a non-workflow type is
recorded is provider-specific — GitHub carries it as a type label, Jira
maps it to a native issue type — so pass the requested type through. On
Jira a name with no configured mapping falls back to the site's default
`issue_type` (and errors when none is set), so set `--issue-type`
explicitly when needed (`spectrack issue <verb> --help`).

Types:

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-side with the
  `issue` side: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `decision-index`,
  `domain`, `nfr`, `spec`. Dual-side with the `knowledge` side:
  `research`, `usecase`.

Dual-side types (`research`, `usecase`) begin on the `issue` side — the
issue is the working record, the `knowledge` page consolidates it. Follow
any notes in the resolver result for the next step in the flow.

Knowledge pages live under `wiki/` — edit the resolver-returned file
and commit.
