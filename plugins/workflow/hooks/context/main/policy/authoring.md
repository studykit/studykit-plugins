## authoring path resolution

Resolve authoring paths with:

```bash
workflow authoring_resolver.py \
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

The resolver prints markdown sections headed by `## <anchor>`. The
reading-list section
(`## <type>-<role>[-comment]-reading-list`) lists one absolute path per
bullet; read each path directly before drafting any provider-backed change.
When the response includes a `## <type>-<role>[-comment]-notes` section,
treat each bullet as a binding rule for the calling flow. If the target is
not a workflow artifact, the resolver returns `NONE`.

## Types

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the
  `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`.
  Dual-role with the `knowledge` role: `research`, `usecase`.
