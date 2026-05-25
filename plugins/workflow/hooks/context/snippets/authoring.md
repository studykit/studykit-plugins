<bash>
workflow mustread \
  --type <type> \
  [--side issue|knowledge] \
  [--target <type>] \
  [--scope comment]
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

The resolver returns markdown listing files to read before drafting.
Treat any bullet in a notes section as a binding rule for the calling
flow. If the target is not a workflow artifact, the resolver returns
`NONE`.

Types:

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-side with the
  `issue` side: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`.
  Dual-side with the `knowledge` side: `research`, `usecase`.

Knowledge pages live under `wiki/` — edit the resolver-returned file
and commit.
