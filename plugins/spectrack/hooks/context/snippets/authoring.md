<bash>
spectrack mustread \
  --type <type> \
  [--side issue|knowledge] \
  [--target <type>] \
  [--scope comment] \
  [--mode forward|backlog|retroactive]
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
  calling, and when it is genuinely ambiguous which one applies, ask the
  user. The resolver returns a different contract set and different notes
  per mode:
  - `forward` — planning and implementing now. The body records a
    user-approved plan (via plan mode where available, or a plan already
    explicitly agreed in the conversation); the size and resolution
    audits apply.
  - `backlog` — capture the item's intent for a later planning pass. No
    planning pass now; a lighter contract relaxes the required sections
    down to `Description` and defers the rest. Use when writing a
    detailed plan now is premature.
  - `retroactive` — the work already landed; the body records facts, not a
    forward plan.

The resolver returns markdown listing files to read before drafting.
Treat any bullet in a notes section as a binding rule for the calling
flow. If the target is not a workflow artifact, the resolver returns
`NONE`.

Types:

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-side with the
  `issue` side: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `decision-index`,
  `domain`, `nfr`, `spec`. Dual-side with the `knowledge` side:
  `research`, `usecase`.

Knowledge pages live under `wiki/` — edit the resolver-returned file
and commit.
