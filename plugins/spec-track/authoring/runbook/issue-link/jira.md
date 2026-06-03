## jira — relationships: add, remove, or replace

```bash
spec-track issue link <source-issue> \
  [--parent <KEY> | --replace-parent <KEY> | --remove-parent] \
  [--epic <KEY> | --replace-epic <KEY> | --remove-epic] \
  [--blocked-by <KEY> ...] [--remove-blocked-by <KEY> ...] \
  [--blocking <KEY> ...]  [--remove-blocking <KEY> ...] \
  [--child <KEY> ...]     [--remove-child <KEY> ...] \
  [--related <KEY-or-URL> ...] [--remove-related <KEY-or-URL> ...] \
  [--type <type>]
```

- `--parent <KEY>` adds; errors if a parent already exists.
  `--replace-parent <KEY>` overwrites. `--remove-parent` detaches
  (no-op when none).
- `--epic <KEY>` / `--replace-epic <KEY>` / `--remove-epic` mirror
  the parent group on the Epic Link customfield. Parent and Epic are
  independent — both may appear in one call against the same issue.
- `--blocked-by` / `--blocking` / `--child` / `--related`
  (repeatable) add; matching `--remove-*` flags remove by ref.
  `--related` uses the configured remote-link mapping and accepts a
  Jira key or absolute URL.
- The same ref in both add and remove for one relationship is an
  error.

The same relationship flags also work on `spec-track issue new` to
apply links in the same call as the create.

See `../../../authoring/providers/issue/jira/relationships.md` for
canonical intent usage (`parent`, `blocked_by`, `related`; invert
source/target for `child` / `blocking`).
