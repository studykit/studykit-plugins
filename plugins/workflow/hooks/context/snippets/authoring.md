```bash
workflow authoring_resolver.py \
  --type <type> \
  [--role issue|knowledge] \
  [--scope comment]
```

- `--type` — required.
- `--role` — required for dual-role types (`issue` or `knowledge`); omit
  for single-role types.
- `--scope comment` — comment-only updates. Returns the Markdown plus
  provider convention files only, not the full type body.

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
