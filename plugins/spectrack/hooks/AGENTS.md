# plugins/spectrack/hooks/

Hook adapter layer. Substantive logic lives in
`../scripts/hook.py` and `../scripts/main_context.py`;
this directory holds the host-specific entry scripts, manifests, and
prompt-fragment tree. For per-event behavior read the dispatcher and the
shared functions — do not duplicate them here.

## Layout

- `hooks.json` — Claude hook manifest.
- `hooks.codex.json` — Codex hook manifest, referenced from
  `../.codex-plugin/plugin.json`.
- `scripts/hook_claude.py`, `scripts/hook_codex.py` — runtime adapters.
  Parse the host payload, extract env, dispatch to shared functions in
  `../scripts/hook.py`.
- `context/main/` — main-session SessionStart entry point
  (`session-start.md`).
- `context/subagent/` — SubagentStart fragments. `session-start.md` plus
  optional `agents/<agent-name>.md` per-agent blocks.
- `context/snippets/authoring.md` — single-file snippet inlined into both
  `SessionStart` and `SubagentStart` (the authoring-resolver invocation).
- `context/snippets/commit-prefix.md` — commit-prefix guidance returned
  by `build_commit_prefix_context()` and injected at `UserPromptSubmit`
  when a commit keyword fires.
- `context/snippets/launcher/<runtime>.md` — runtime-keyed launcher
  snippet inlined into both `SessionStart` and `SubagentStart`.
- `context/snippets/prd-path.md` — single-file snippet inlined into both
  `SessionStart` and `SubagentStart` (the PRD-path resolver invocation).

All of the above are composed into the templates above via `{{...}}`
substitution in `../scripts/main_context.py`.

On-demand reference docs the injected text *points at* — intent-keyed
runbook pages (`issue-fetch/<provider>.md`, `issue-write/<provider>.md`,
`issue-new/<provider>.md`, `issue-comment/<provider>.md`,
`issue-update/<provider>.md`, `issue-link/<provider>.md`,
`issue-state/<provider>.md`) — live under `../authoring/runbook/`, not
in this tree. `hooks/context/` holds only what hooks read for injection.
Both main session and subagents resolve verb syntax and flag sets by
reading those runbook files on demand; the inlined snippets are
deliberately limited to the launcher invocation, the authoring resolver
block, and the PRD-path resolver block.

## Invariants

- **Adapters are host-specific; shared logic is host-neutral.** Do not add
  Claude/Codex branches inside `../scripts/hook.py` — push the
  host detail into the adapter.
- **Manifest asymmetry is deliberate.** Codex registers only `SessionStart`
  + `UserPromptSubmit`. Claude additionally registers `PreToolUse` (cache
  projection protection + authoring-read notice), `PostToolUse`
  (authoring-read tracking), and `SubagentStart`. New behavior must fit
  one of those events on the target runtime or be runtime-only.
- **Stdout is JSON or empty.** Empty stdout = no-op. Never emit plain text.
- **Subagents inherit env, not policy.** SubagentStart injection stays
  narrow (launcher + authoring resolver + PRD-path resolver + the same
  runbook reference list as the main session, plus per-agent flow blocks
  for `issue-implementer`). Verb syntax lives in the runbook for both
  main session and subagents.
- **Codex cannot persist env from SessionStart.** `hook_codex.py` records
  session state under `.spectrack-cache/hook-state/`; the
  `../scripts/spectrack` wrapper sources the exports later via
  `CODEX_THREAD_ID`. Do not rely on `os.environ` for the `SPECTRACK_*`
  contract on Codex.
- **Placeholders use `{{NAME}}`, not `$NAME`.** Substituted in
  `../scripts/main_context.py`. Adding a new placeholder
  requires wiring it there in the same change as the template wording.
  Snippet placeholders: `{{SNIPPET_AUTHORING}}` ↔
  `snippets/authoring.md`, `{{SNIPPET_LAUNCHER}}` ↔
  `snippets/launcher/<runtime>.md`, `{{SNIPPET_PRD_PATH}}` ↔
  `snippets/prd-path.md`, and (main session only)
  `{{SNIPPET_PROVIDER_RUNBOOK}}` ↔ `snippets/runbook/<provider>.md` for
  provider-only runbook intents (e.g. Jira `issue-attach`; missing
  fragment → nothing injected). Other usage (fetch / write / link /
  etc.) is referenced via `{{SPECTRACK_RUNBOOK_DIR}}` +
  `{{SPECTRACK_ISSUE_PROVIDER}}` pointing at
  `authoring/runbook/<intent>/<provider>.md`.
- **Provider cache projections are read-only; dotfile sources are internal.**
  `PreToolUse` write protection blocks edits to the readable projections
  (`issue.md` / `relation.md` / `comment-*.md`); refresh those
  through the matching fetch script rather than editing in place. The
  internal dotfiles — `.meta.json` (per-target freshness fingerprints) and,
  for GitHub, `.relation.json` (the machine relationship source the
  readable `relation.md` is rendered from) — are blocked for both read
  and write; they are projection bookkeeping, not issue content.
- **Authoring read-tracking scope is `../authoring/` only.**
  `mustread.authoring_relative_path` defines the surface. A new
  reference doc that needs re-read tracking belongs under
  `../authoring/`, not under `./context/`.
- **Injected text is consumer-facing.** The main agent calls scripts; it
  does not implement them. In `context/main/`, `context/subagent/`, and
  `context/snippets/`, describe verb syntax, flag meaning, output kind,
  and consumer-side constraints — nothing more. **Do not leak**: JSON
  field schemas, env-var contracts the agent doesn't set, dispatcher
  routing prose, script filenames (`*.py`, `_dispatch.py`), output
  section-anchor regexes, or any "how the script does it" detail. Those
  belong in source code or the runbook, not in injected text.

## Where to make changes

| Change | Touch |
|---|---|
| New hook event on a runtime | adapter (`hook_claude.py` / `hook_codex.py`) + shared fn in `../scripts/hook.py` + matching manifest |
| New SessionStart wording | `context/main/session-start.md`, with a `{{...}}` placeholder if provider/runtime-specific |
| New SubagentStart wording | `context/subagent/session-start.md` or `context/subagent/agents/<agent-name>.md` |
| New provider/runtime snippet variant | `context/snippets/<group>/<key>.md`; wire the placeholder in `../scripts/main_context.py` |
| New on-demand reference doc | `../authoring/runbook/...`; point at it from injected text via `{{SPECTRACK_RUNBOOK_DIR}}/...` |
