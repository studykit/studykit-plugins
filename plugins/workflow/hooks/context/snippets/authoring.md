<bash>
workflow mustread \
  --type <type> \
  --purpose author|review \
  [--role issue|knowledge] \
  [--scope comment]
</bash>

- `--type` — required.
- `--purpose` — required. `author` returns the authoring contract
  (use when drafting or updating an artifact). `review` returns the
  review-criteria file (use when evaluating an already-written
  artifact). There is no default — calls without `--purpose` error.
- `--role` — required for dual-role types (`issue` or `knowledge`); omit
  for single-role types.
- `--scope comment` — comment-only updates. Returns the Markdown plus
  provider convention files only, not the full type body. Not
  compatible with `--purpose review`.

The resolver returns markdown listing files to read before drafting.
Treat any bullet in a notes section as a binding rule for the calling
flow. If the target is not a workflow artifact, the resolver returns
`NONE`.

Types:

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the
  `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`.
  Dual-role with the `knowledge` role: `research`, `usecase`.

Knowledge pages live under `wiki/` — edit the resolver-returned file
and commit.
