# Delegate plugin design

The plugin runs in Codex and Claude Code. Both editions share `scripts/ledger_core.py`
through a per-host adapter (`scripts/ledger.py` for Codex, `scripts/ledger_claude.py` for
Claude) and keep the same ownership split; each host has its own entry point and sizer
definition because the dispatch tools, model names and storage mechanics differ.

## Layout

Claude Code always scans `skills/` and always loads `hooks/hooks.json`; a manifest path only
adds to them. Both would pick up the Codex skills and the Codex storage hook, so neither
exists here:

- Codex skills live under `codex/skills/`, and `.codex-plugin/plugin.json` points `skills` and
  `onboardingSkill` there. This departs from the repository's usual `./skills/` because
  nothing in `skills/` can be kept out of Claude.
- The Codex hook manifest is `hooks/hooks.codex.json`, the repository convention.
- Claude's entry point is `commands/delegate.md`, a directory Codex does not read. Claude's
  sizer is `agents/delegate-sizer.md`; Claude reads only `.md` agents, so the Codex
  `agents/delegate-sizer.toml` beside it is invisible to it.

A test pins this: no `skills/`, no `hooks/hooks.json`, and every manifest path resolves.

## Claude Code edition

Claude loads plugin agents natively, so there is no setup skill and no hook. The command's
content gets `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` substituted, and it passes the
data path to the ledger adapter as `--data-dir` and to the sizer as the lessons path: the
Bash tool's environment does not carry `CLAUDE_PLUGIN_DATA`, and whether an agent body is
substituted is documented inconsistently, so the sizer receives concrete paths instead.

The sizer is `delegate:delegate-sizer`, `model: opus`, `effort: high`, on the maintainer's call
and unmeasured. A missized run costs a failed worker plus a retry, or a worker on a tier it did
not need, and either costs more than one sizing; the sizer's output is a few lines; and a
weaker sizer errs in one direction — it cannot see depth it does not itself have, so it sizes
hard work low. If sizing cost starts to rival the work it sizes, this field is the first place
to look.

It has no `memory:` field. The lessons file in plugin data replaces it, matching the Codex
edition, and keeps lessons beside the ledger they cite rather than in a store the ledger cannot
see. `Write` and `Edit` are granted for that file alone; the body is what holds the boundary.
Plugin data is deleted on uninstall unless the user passes `--keep-data`.

The entry point never uses `fork`: a fork runs on the caller's model and effort and ignores the
Agent tool's per-call `model` and `effort`, so the record would credit a tier that never ran.

This edition replaced an earlier user-level skill and agent under the repository's `global/`.
Its ledger lived at `~/.claude/delegate/ledger.jsonl` with the same schema; point
`DELEGATE_LEDGER` at it to keep that history.

## Shared policy

Only `capability` failures move the tier. Without a cause, a vague prompt reads as a weak
model and every later run of that category climbs to a tier it does not need. The verdict is
the main session's, amendable by the user; `amend` appends rather than rewrites, so the
original judgment stays visible. The tier ladders are judgments, not measurements; the ledger
is what should correct them.

## Ownership

The custom `delegate-sizer` agent owns decomposition, categories, the provisional worker
ladder, ambiguity/depth/breadth/undetected-cost questions, recall adjustments, and capability
retry sizing. Its fixed configuration is `gpt-6.1-sol` / `high`, selected directly by the user.
The main skill passes through the original instruction, known paths, an absolute ledger
command, and available worker pairs. It follows the answer, writes worker prompts, verifies
results, and records verdicts. A missing sizer or unavailable pair stops the workflow.

The agent's short description reserves it for the skill. This is instructional routing;
Codex documents no custom-agent equivalent of the skill's explicit-only policy. Native
memories are disabled because Codex does not document Claude's per-agent `memory: user`
store or its narrow saving policy. Instead, the sizer receives an explicit plugin-owned
lessons path and maintains qualitative lessons with ledger record IDs. No run/count/verdict
copies or unrelated project content belong there; contrary ledger evidence removes a lesson.

## Packaging and setup

The supported Codex compatibility manifest describes version 0.1.0.
The Codex marketplace registers the plugin. No unsupported `agents` manifest field is used. The tested CLI 0.163.0 ignored plugin hooks
when a portable root manifest was also present; with the Codex manifest alone, `hooks/list`
discovered the plugin SessionStart hook. Keep this package in the verified compatibility
format until that host limitation is resolved.
The package contains both Codex skills, its agent definition, a storage hook, all scripts, and a host-neutral
ledger core; no file depends on `global/` or another installed package.

`delegate-setup` installs a regular agent snapshot under native plugin data and registers
it through a marked `[agents.delegate-sizer]` block. It never registers a versioned plugin
cache path. An agent-file symlink in the discovery directory was unavailable in the tested
CLI; a regular file referenced by explicit configuration worked. The snapshot is therefore
kept in a dedicated data directory outside standalone-agent discovery, preventing duplicate
role names. Setup after an update refreshes it only when its prior content hash still matches
managed state. It preserves user edits instead of overwriting them.

Role updates retain unrelated TOML bytes and config-file symlinks. Writes use atomic
replacement. Cleanup removes only managed, unchanged artifacts and always preserves history.
Plugin removal does not imply teardown hooks; users run the setup skill's `remove` operation
before uninstalling. A new session is needed to load an added or updated custom agent.

Codex supplies `PLUGIN_DATA` to plugin hooks, not ordinary skill shells. A minimal SessionStart
adapter emits the resolved native path as additional context, without writing files. Skills
pass that path explicitly through `--data-dir` to setup and ledger commands and pass the
lessons-file path to the sizer. Missing context stops the workflow rather than inventing a
home-directory substitute. Hook definitions must be reviewed/trusted; automatic installation
does not grant that trust. One-off isolated tests may use the documented bypass flag after
vetting this hook; that does not persist trust in the user's environment.

Ledger records, qualitative lessons, installed agent snapshots, and setup ownership state all
live in native plugin data. Agent cleanup preserves the ledger and lessons. The ledger adapter
normalizes the path and model ordering before calling the bundled host-neutral core. Its
JSONL schema remains compatible with the previous global implementation; users retaining an
older history can point `DELEGATE_LEDGER` at that file. No unrequested history migration runs.

## Official references

Checked on 2026-10-20:

- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/config-file/config-reference
- https://learn.chatgpt.com/docs/customization/memories
- https://learn.chatgpt.com/docs/hooks

## Validation

Run `python3 -m unittest discover -s delegate/tests -v`. Tests exercise both ledger adapters, the
per-host layout, ledger amendments,
path overrides, invalid verdicts, setup ownership and conflicts, config preservation,
relocated packages, and managed-agent upgrades. Validate both skill frontmatters and parse
the JSON/YAML/TOML metadata. Install the working-tree marketplace into an isolated Codex
profile, confirm plugin-owned skills are discovered, run setup, then start a fresh session
in a throwaway project. Inspect raw subagent events for the sizer and selected worker and
confirm the main session alone writes a verified verdict.

On 2026-10-20, Codex CLI 0.163.0 passed all 12 behavioral tests and both skill validators.
That run predates the move of the Codex skills to `codex/skills/` and of the hook manifest to
`hooks/hooks.codex.json`; the installed-plugin checks below have not been repeated since.
An isolated profile installed the plugin from this working-tree marketplace. With native
plugin variables absent in the launching shell, the trusted-for-one-invocation SessionStart
hook supplied the host's data directory. The setup skill installed the named agent there;
a fresh session dispatched the sizer on `gpt-6.1-sol` / `high` and its selected lookup worker
on `gpt-6-luna` / `low`. Persisted child turn contexts confirmed those effective settings.
The parent verified the fixture and wrote one pass record in native plugin data. No empty
lessons file was created. These checks exercised the installed cache, not direct working-tree
scripts with manually supplied native variables.

The app-server accepted the root hook-trust bypass flag but did not execute the untrusted
plugin hook in this probe; the supported `codex exec` invocation did. The skill correctly
stopped when native storage context was absent. Do not count app-server hook discovery or
unit-test environment injection as evidence that the host executed a hook.
