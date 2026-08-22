---
name: guard-hook-py-dead-constant
description: RESOLVED as of 2026-08-22 audit — _CLI_MUTATING_VERBS no longer exists in guard_hook.py; the constant and its stale comment were removed between audits.
metadata:
  type: project
---

Historical note only: an earlier audit (before 2026-08-22) found `_CLI_MUTATING_VERBS =
{"set", "add", "remove", "rm", "clear"}` as a dead constant with a comment describing a
list-CLI shape (`add`/`remove`/`rm`/`clear`) that `cmd_settings` never implemented (only
`set`/`unset`/`show`). Verified by grep on 2026-08-22: the constant is gone entirely from
`plugins/guard/scripts/guard_hook.py`. Whoever fixed it did so as a code change (removing
the dead constant), which was correctly out of scope for a comment-only audit and must
have been done by the user or a code-editing pass, not by comment-corrector.

**How to apply:** do not keep reporting this as an open defect — check with `grep -n
_CLI_MUTATING_VERBS` first; if it's absent (as of 2026-08-22) the item is closed. Keep this
entry only as an example of the "dead code with a stale comment" pattern for future
reference, in case something similar recurs (e.g. a new orphaned constant).
