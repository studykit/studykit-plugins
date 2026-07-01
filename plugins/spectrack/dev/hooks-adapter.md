# Hook adapter layer

Deep reference for maintaining SpecTrack's hook adapter layer — the host-specific
entry scripts, manifests, and prompt-fragment tree under `hooks/`. Not auto-loaded;
open it when editing hooks. The substantive dispatch logic lives in
`../scripts/hook.py` and `../scripts/main_context.py`; the injected-text layout and the
rules for *authoring* agent/skill docs against it are in
`authoring-injected-context.md`. The source and manifests are the truth — this file
records the invariants that must not regress.

## Invariants

- **Adapters are host-specific; shared logic is host-neutral.** `hook_claude.py` /
  `hook_codex.py` parse the host payload and dispatch to shared functions in
  `../scripts/hook.py`. Do not add Claude/Codex branches inside `hook.py` — push the
  host detail into the adapter.
- **Manifest asymmetry is deliberate.** Codex (`hooks.codex.json`) registers
  `SessionStart`, `SubagentStart`, `UserPromptSubmit`, and `Stop`. Claude
  (`hooks.json`) additionally registers `PreToolUse` (cache-projection write
  protection); Claude `Stop` stays unregistered. New behavior must fit one of those
  events on the target runtime or be runtime-only.
- **Stdout is JSON or empty.** Empty stdout = no-op. Never emit plain text.
- **Subagents inherit env, not policy.** SubagentStart injection stays narrow
  (launcher + authoring resolver + PRD-path resolver + the same `<commands>` `--help`
  pointer as the main session, plus per-agent flow blocks). Per-verb CLI usage lives in
  `spectrack issue <verb> --help` for both main session and subagents.
- **Codex cannot persist env directly from hooks.** `hook_codex.py` records main and
  subagent session state under `.spectrack-cache/hook-state/`; the
  `../scripts/spectrack` wrapper sources the exports later via `CODEX_THREAD_ID`. Do not
  rely on `os.environ` for the `SPECTRACK_*` contract on Codex.
- **Placeholders use `{{NAME}}`, not `$NAME`,** substituted in
  `../scripts/main_context.py`. Adding a placeholder means wiring it there in the same
  change as the template wording.
- **Provider cache projections are read-only; dotfile sources are internal.** Claude's
  `PreToolUse` write protection blocks edits to the readable projections (`issue.md` /
  `state.md` / `relation.md` / `comment-*.md`) — refresh those through the matching
  fetch script. The internal dotfiles (`.meta.json` freshness fingerprints for both
  providers, GitHub's `.relation.json`, Jira's `.issue.json` / `.remote-links.json`) are
  blocked for both read and write; they are projection bookkeeping, not issue content.
- **Injected text is consumer-facing.** The agent calls scripts; it does not implement
  them. In `context/main/`, `context/subagent/`, and `context/snippets/`, describe verb
  syntax, flag meaning, output kind, and consumer-side constraints — nothing more.
  **Do not leak** JSON field schemas, env-var contracts the agent doesn't set,
  dispatcher routing prose, script filenames (`*.py`, `_dispatch.py`), output
  section-anchor regexes, or any "how the script does it" detail. Those belong in source
  or the verb's `--help`.

## Where to make changes

| Change | Touch |
|---|---|
| New hook event on a runtime | adapter (`hook_claude.py` / `hook_codex.py`) + shared fn in `../scripts/hook.py` + matching manifest |
| New SessionStart wording | `context/main/session-start.md`, with a `{{...}}` placeholder if provider/runtime-specific |
| New SubagentStart wording | `context/subagent/session-start.md` or `context/subagent/agents/<agent-name>.md` |
| New provider/runtime snippet variant | `context/snippets/<group>/<key>.md`; wire the placeholder in `../scripts/main_context.py` |
| New/changed verb CLI usage | the verb's argparse `--help` wording in `../scripts/issue/dispatch.py` + `../scripts/issue/<provider>/backend.py` (not injected text) |
