## authoring path resolution

Resolve authoring paths with:

```bash
"$WORKFLOW" authoring_resolver.py \
  --type <type> \
  [--role issue|knowledge] \
  [--scope comment] \
  [--provider github|jira|confluence|filesystem]
```

Flags:

- `--type` — required; see Types below.
- `--role` — required for dual-role types (`issue` or `knowledge`); omit
  for single-role types.
- `--scope comment` — for comment-only updates. Returns the Markdown plus
  provider convention files only, not the full type body.
- `--provider` — override the configured provider; omit to use
  `.workflow/config.yml`.

The resolver returns absolute paths under `required_authoring_files`. Read
those paths directly before drafting any provider-backed change. If the
target is not a workflow artifact, the resolver returns `NONE`.

When the JSON response carries a `notes` array, treat each entry as a
binding rule for the calling flow.

## Types

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the
  `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`.
  Dual-role with the `knowledge` role: `research`, `usecase`.
