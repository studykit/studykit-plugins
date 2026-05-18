## workflow operator bootstrap

Workflow shell env exports are not persisted into the operator's bash shell
in Codex. Use the literal launcher and resolver paths instead:

- `plugins/workflow/scripts/workflow` — workflow script launcher; replaces
  every `$WORKFLOW` reference in operator-context fragments.
- `plugins/workflow/scripts/authoring_resolver.py` — authoring resolver;
  replaces every `$AUTHORING_RESOLVER` reference.

Both paths are relative to the project root. The launcher self-sources its
own env file when invoked, so no shell-level export is required.

Do not derive either path from project layout in any other way or inspect
runtime-specific session files directly.
