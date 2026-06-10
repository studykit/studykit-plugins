## github body-bearing writes

Every body-bearing write (publish / comment / update) shares this shape:

1. Draft the body to a temp file. A leading YAML frontmatter block is
   stripped before posting.
2. Present the draft + metadata + (for updates) the issue ref to the
   user and wait for approval.
3. Run the matching `spectrack issue <verb>` invocation.

When presenting, narrate the write — do not dump mechanics:

- Open with the verb and any state transition in one line — e.g. "The
  verb is resolve — posting the body update + resolve transition."
- Name the planned invocation as inline shorthand — `(issue update
  --issue <ref> --body-file …)`. Never show the temp-file shell script
  or the full command block; the shorthand is all the command surface
  the user needs.
- For updates, say what stays verbatim and what changes, then give the
  substance of the changed or added sections. Do not restate unchanged
  body text.
- Do not describe what the script will do internally — the freshness
  check, cache refresh, temp-file cleanup, and conflict flow run
  without narration; surface them only when one actually fails.
- Do not recount which runbook or contract files were read or restate
  their rules; apply them silently.

The script runs a per-target content fingerprint check, applies the
mutation, refreshes the cache, deletes the body file on success, and
returns the cached `issue.md` path with the issue ref. A body-only
update reuses the body you just wrote as the projection without a
re-fetch.

On `status=conflict` the targeted artifact changed on the provider
since it was last fetched. The script refreshes the cache, preserves
the body file, and returns `reread_paths` — the readable projections
(`issue.md` / `relation.md` / `comment-*.md`). Reread those paths,
reapply your change to the body file, and retry; or rerun the same verb
with `--overwrite` to replace the provider copy without rereading.

Per-intent detail:

- `../issue-new/github.md` — publish a new issue
- `../issue-comment/github.md` — append a comment
- `../issue-update/github.md` — update body, title, labels, or state
- `../issue-link/github.md` — add / remove / replace relationships
- `../issue-state/github.md` — body-less changes (state, assign,
  unassign, set-type)

Run `spectrack issue <verb> --help` for a flag not documented above.
