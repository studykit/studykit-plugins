# plugins/spectrack/hooks/

This AGENTS.md file is for SpecTrack plugin contributors. It is not runtime
guidance for LLMs using an installed SpecTrack plugin.

The hook adapter layer: host-specific entry scripts (`scripts/hook_claude.py`,
`scripts/hook_codex.py`), the manifests (`hooks.json`, `hooks.codex.json`), and the
prompt-fragment tree under `context/`. Substantive logic lives in `../scripts/hook.py`
and `../scripts/main_context.py`, which compose the `context/` fragments via `{{...}}`
substitution.

Read before working here:

- **`../dev/hooks-adapter.md`** — the adapter-layer invariants (host split, manifest
  asymmetry, `{{NAME}}` placeholder wiring, Codex env persistence, cache-projection
  write protection, the consumer-facing / do-not-leak rule for injected text) and the
  map of what each kind of change touches.
- **`../dev/authoring-injected-context.md`** — how to author agent/skill docs against
  the injected context, and how to preview it (`spectrack preview_context`).

Per-verb CLI usage is not injected and has no doc tree: the `<commands>` block points
the agent at `spectrack issue --help` and `spectrack issue <verb> --help`, the single
source of truth for issue-CLI usage.
