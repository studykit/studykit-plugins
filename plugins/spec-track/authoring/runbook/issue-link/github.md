## github — relationships: add, remove, or replace

```bash
spec-track issue link <source-issue> \
  [--parent <ref> | --replace-parent <ref> | --remove-parent] \
  [--blocked-by <ref> ...] [--remove-blocked-by <ref> ...] \
  [--blocking <ref> ...]  [--remove-blocking <ref> ...] \
  [--child <ref> ...]     [--remove-child <ref> ...] \
  [--type <type>]
```

- `--parent <ref>` adds; errors if a parent already exists.
  `--replace-parent <ref>` overwrites. `--remove-parent` detaches
  (no-op when none).
- `--blocked-by` / `--blocking` / `--child` (repeatable) add; matching
  `--remove-*` flags remove by ref.
- The same ref in both add and remove for one relationship is an
  error.

The same relationship flags also work on `spec-track issue new` and
`spec-track issue update` to apply links in the same call.

See `../../../authoring/providers/issue/github/relationships.md` for
canonical intent usage (`parent`, `blocked_by`; invert source/target
for `child` / `blocking`).
