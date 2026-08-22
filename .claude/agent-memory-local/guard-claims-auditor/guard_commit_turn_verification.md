---
name: guard_commit_turn_verification
description: How to verify a guard-plugin "commit completed" turn (hash, stats, file contents, issue-ref decision)
metadata:
  type: project
---

This repo's assistant turns often end with a Korean "commit done" report (e.g.
`guard: vX.Y.Z — ...`) summarizing a git commit just made. To verify such a turn:

- `git show --stat <hash>` confirms file count and +/- insertion/deletion counts, and the
  subject line, directly.
- Per-file content claims (e.g. "agent X has no WebFetch tool", "router model changed
  sonnet->opus") are checked by reading the file at HEAD (post-commit) and/or
  `git show <hash>~1:<path>` for the pre-commit version.
- The "no issue ref, user chose 'no issue'" pattern recurs across guard commits (checked
  bc2876a2, 8e79c56c, 5598f3ec, c806f4db, 11df75bb, 999cb2f5, 7051d793 — none carry issue
  refs). When the response also claims "the user selected X", check the transcript via
  `guard_hook.py transcript find --pattern "AskUserQuestion|이슈"` — this project's turns
  often route decisions through an `AskUserQuestion` tool call, which is authoritative
  (records the option text and the user's selection), not testimony from the assistant.
- Push status: `git status -sb` shows `ahead N` vs `origin/main` — use it to confirm "did
  not push" claims directly rather than trusting the response.

**Verdict so far**: turn `5b228714-162a-4f72-a1f1-b2edc70bdc40` (commit `7051d793`) passed
full audit — every claim checked out against `git show`, file diffs, and the
`AskUserQuestion` transcript record. No false positives to record yet.
