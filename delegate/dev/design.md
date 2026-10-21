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
- Claude's skill lives under `claude/skills/`, which `.claude-plugin/plugin.json` names in
  `skills`; that field adds to Claude's default `skills/` scan rather than replacing it, and
  Codex reads only the path its own manifest names. Each host's skills thus sit under a
  directory named for it. Claude's agents are `agents/delegate-sizer.md` and
  `agents/delegate-verifier.md`; Claude reads only `.md` agents, so the Codex
  `agents/*.toml` definitions beside them are invisible to it.

A test pins this: no `skills/`, no `hooks/hooks.json`, and every manifest path resolves.

## Claude Code edition

Claude loads plugin agents natively, so there is no setup skill and no hook. The skill's
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

The worker ladder stops at `opus` / `high`, on the user's call: `fable` and `opus` / `xhigh`
cost more tokens than the work they would rescue was judged worth. The ledger adapter still
accepts `fable` so older records keep their tier order. A piece that fails on capability at
the ceiling is given up rather than retried.

`delegate-verifier` checks each worker's result and proposes its verdict and cause. It
replaced verification by the main session for two reasons: diffs and test output stayed in the
main session's context, and the main session was grading its own prompt — every miss it put
on `capability` instead of `instruction` pushed later runs up the ladder. The verifier sees the
worker's prompt verbatim, which is what judging `instruction` needs. It runs on `opus` /
`high` whatever the worker's tier, on the user's call. A verifier that followed the worker's
tier would judge cheap tiers more leniently, so their pass rates would look better than the
expensive tiers' and probes would walk down on that bias; one fixed judge keeps the record
comparable across tiers. Nothing checks the verifier's judgment, and the `capability` /
`instruction` call is the same kind of depth the sizer runs on `opus` for. The cost stays
modest because short pieces verify quickly. If it grows, lower the effort before the model.
A lenient verifier inflates passes and lets
probes walk tiers down, so the main session rejects a criterion marked met without evidence,
may overturn a verdict with a reason, and records the overturn as an `amend --by dispatcher`
so both judgments stay in the history.

Each piece gets two attempts. The sizer gives a wall-clock budget per piece; the skill times
it with a background `sleep` and stops an overrunning worker with `TaskStop`, which the
subagent documentation names for stopping a background subagent. The Agent tool has no
timeout of its own. `recall` prints average durations so budgets can follow the record.

The sizer gives each piece a scope and the pieces it comes after, so the main session can send
every ready piece at once and keep writers off each other's files without re-deriving either.

The entry point never uses `fork`: a fork runs on the caller's model and effort and ignores the
Agent tool's per-call `model` and `effort`, so the record would credit a tier that never ran.

This edition replaced an earlier user-level skill and agent under the repository's `global/`.
Its ledger lived at `~/.claude/delegate/ledger.jsonl` with the same schema; point
`DELEGATE_LEDGER` at it to keep that history.

## Shared policy

Capability failures and budget stops require a strictly higher tier; prompt and environment
failures alone do not. A piece gets at most two attempts. Without a cause, a vague prompt
reads as a weak model and every later run of that category climbs to a tier it does not need.
The verifier proposes the verdict; the main session records it and can amend it with a reason.
The user may also amend it; `amend` appends rather than rewrites, so the
original judgment stays visible. The tier ladders are judgments, not measurements; the ledger
is what should correct them.

## Ownership

The custom `delegate-sizer` agent owns decomposition, categories, the provisional worker
ladder, ambiguity/depth/breadth/undetected-cost questions, recall adjustments, and capability
and budget retry sizing. Its fixed configuration is `gpt-6.1-sol` / `high`, selected directly by the user.
The main skill passes through the original instruction, known paths, an absolute ledger
command, and available worker pairs. It follows the answer, writes worker prompts, dispatches
verification, and records verdicts. A missing named role or unavailable pair stops the workflow.

The Codex worker ladder ends at `gpt-6-astra/high`, selected by the user. Historical ledger
records above that ceiling remain readable; the ceiling governs new dispatches. Each piece
has a stable ID, non-overlapping writer scope, dependency IDs, and a positive minute budget.
Only verified usable prerequisites release dependent pieces. Attempt labels may contain a
hyphen, but native `task_name` values use underscores (`p1_1`), as required by the tested
Codex schema. A retry preserves identity and
scope; it cannot create fresh pieces to reset the two-attempt limit. An abandoned piece is
never taken over by the dispatcher, and its transitive dependents do not run.

`delegate-verifier` fixes `gpt-6.1-sol/high`, on the user's call, and the skill supplies that
same pair explicitly. A fixed judge keeps ledger verdicts comparable across worker tiers
and avoids making cheaper workers look better because a weaker judge missed their errors.
The verifier gets the prompt verbatim,
acceptance criteria, scope baseline, and worker report or stop evidence. Local tests and build
scratch output are permitted, but source edits and ledger writes are not. This is an
instruction boundary, not a separate read-only sandbox; native agents inherit parent
permissions. A dispatcher correction is an append-only `amend --by dispatcher`, preserving
the verifier's original verdict.

Budget enforcement uses measured dispatch/deadline clocks and bounded native agent waits.
A wait timeout does not stop a worker. At a deadline the dispatcher checks status and calls
the actual host's native interrupt/stop tool, then confirms the worker and any running shell
command cannot still write before checking or retrying the scope. The public subagent docs
confirm stop/close orchestration but do not specify these tools' exact argument schemas;
the skill follows the tools exposed in the current session (`interrupt_agent`, or
`close_agent` when it supports stopping). Missing stop capability blocks dispatch rather than
pretending a deadline can be enforced. Budget stops require the sizer to choose both a
higher tier and a longer budget; the verifier still distinguishes capability from a tool or
permission blocker. At the ceiling or after the second miss, abandon the piece.

The agent's short description reserves it for the skill. This is instructional routing;
Codex documents no custom-agent equivalent of the skill's explicit-only policy. Native
memories are disabled because Codex does not document Claude's per-agent `memory: user`
store or its narrow saving policy. Instead, the sizer receives an explicit plugin-owned
lessons path and maintains qualitative lessons with ledger record IDs. No run/count/verdict
copies or unrelated project content belong there; contrary ledger evidence removes a lesson.

## Packaging and setup

Both runtime manifests carry the same plugin version.
The Codex marketplace registers the plugin. No unsupported `agents` manifest field is used. The tested CLI 0.163.0 ignored plugin hooks
when a portable root manifest was also present; with the Codex manifest alone, `hooks/list`
discovered the plugin SessionStart hook. Keep this package in the verified compatibility
format until that host limitation is resolved.
The package contains both Codex skills, its agent definitions, a storage hook, all scripts, and a host-neutral
ledger core; no file depends on `global/` or another installed package.

`delegate-setup` installs regular snapshots for both agents under native plugin data and
registers them through separate marked `[agents.delegate-sizer]` and
`[agents.delegate-verifier]` blocks. It never registers a versioned plugin
cache path. An agent-file symlink in the discovery directory was unavailable in the tested
CLI; a regular file referenced by explicit configuration worked. The snapshot is therefore
kept in a dedicated data directory outside standalone-agent discovery, preventing duplicate
role names. Setup after an update refreshes it only when its prior content hash still matches
managed state. It preserves user edits instead of overwriting them. Both roles are preflighted
before any write, so a verifier conflict cannot partially update or remove the sizer. The
original single-sizer `agent_sha256` state upgrades to a per-role hash map without taking
ownership of a user verifier. Status validates complete managed blocks and all agent hashes.

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

Codex subagent and configuration behavior rechecked on 2026-10-21 (other references below
were checked on 2026-10-20):

- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/config-file/config-reference
- https://learn.chatgpt.com/docs/config-file/config-sample
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
confirm the named verifier supplies evidence and the main session alone records its verdict.
Also inspect deadline interruption and dependent scheduling; a successful setup or ordinary
lookup does not establish those branches.

On 2026-10-21, Codex CLI 0.163.0 passed the isolated-profile setup and delegation probes
against version 0.3.0 installed from the working-tree marketplace, including the per-host
skill and hook layout. The launching environments had neither `PLUGIN_ROOT` nor `PLUGIN_DATA`;
the reviewed SessionStart hook supplied native storage context using the one-invocation
hook-trust flag. Setup installed and reported both named agents as configured and current.

The parallel lookup probe used `gpt-6-luna/low` for the root; persisted child turn contexts
confirmed the sizer on `gpt-6.1-sol/high` and two independent lookup workers on
`gpt-6-luna/low`. The fixture was a separate project with a clean baseline commit. Both
workers were launched before either was awaited; named verifiers read the fixture and
compared it with its starting state. Both results were recorded as passes, with no project
files changed.

After pinning the verifier, a fresh installed profile repeated setup and a verification
handoff. Setup reported both roles on `gpt-6.1-sol/high`, and the verifier's persisted turn
context confirmed that exact pair despite the root using `gpt-6-luna/low`.

An earlier probe exposed an invalid hyphenated task name. The verifier classified the rejected
spawn as an environment failure; the dispatcher recorded it and linked the successful retry.
The skill now specifies valid underscore names. A separate native control probe recorded
`running` before interruption, `previous_status: running` from `interrupt_agent`, and
`interrupted` from the following `list_agents`. That probe used no shell subprocess; it does
not establish cancellation of an in-flight shell command. Full budget-overrun escalation,
capability retry at the ceiling, dependent abandonment, and dispatcher corrections have not
been exercised end to end.

All 21 behavioral tests pass, including sizer-only upgrades, verifier conflicts, user-edited
files and blocks, incomplete managed blocks, relocated package upgrades, byte-preserving
config updates, and history retention. Both Codex skill frontmatters pass the skill validator;
JSON, YAML, and agent TOML parse. `claude plugin validate ./delegate` passes with a directory
listing warning about the missing icon and advice about the install line. These notices do
not affect manifest validation.

The earlier app-server probe accepted the root hook-trust flag but did not execute the
untrusted plugin hook; hook discovery alone did not prove execution. The current `codex exec`
probes establish actual hook delivery. Do not count unit-test environment injection as
proof that a host executed a hook.
