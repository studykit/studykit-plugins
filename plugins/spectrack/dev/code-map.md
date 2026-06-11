# Code Map

How the SpecTrack plugin's runtime code is organized, and what a typical
feature change touches.

## Launcher

The `scripts/spectrack` launcher resolves `<command>` to
`scripts/<command>.py` or a package's `scripts/<command>/__main__.py` and
runs it with `uv run --script`. There is no entry-point registration —
adding a top-level command means adding a script or package there.

## Issue dispatch

All issue operations route through `scripts/issue/dispatch.py`: the verb
table in its module docstring maps `spectrack issue <verb>` to intents, and
`run_intent` owns the provider-agnostic boilerplate (load
`.spectrack/config.yml`, resolve the driver via `get_backend` in
`scripts/issue/backend.py`, assemble argparse, execute). Provider-specific
behavior lives in `scripts/issue/github/` and `scripts/issue/jira/` (driver,
provider wrapper, cache carrier, reference parsing);
`scripts/issue/providers.py` is the transport scaffold — native CLI/API
wrappers first, MCP as fallback.

## Hooks and supporting scripts

Hooks enter at `hooks/scripts/hook_claude.py` (wired by `hooks/hooks.json`)
and build injected text via `scripts/main_context.py` from the Markdown
fragments under `hooks/context/`. `scripts/setup.py` writes
`.spectrack/config.yml`; `scripts/mustread.py` resolves authoring contracts
under `authoring/`.

## Changing an issue feature end-to-end

A new or changed issue verb/intent usually touches, in one change:

1. the verb/intent surface in `scripts/issue/dispatch.py` and the provider
   drivers in `scripts/issue/<provider>/backend.py`;
2. the on-demand runbook doc(s) under
   `authoring/runbook/<intent>/<provider>.md` that tell the runtime agent
   how to invoke it;
3. injected context under `hooks/context/` — only when a pointer or policy
   line there changes;
4. tests under `tests/`;
5. the Claude and Codex plugin version bump per the repository-root
   `AGENTS.md`.

The user-facing surfaces are the skills (`skills/*/SKILL.md`, main-session
orchestrators) and the agents they dispatch (`agents/*.md`); each skill's
frontmatter description records which agents it dispatches. Authoring rules
for those docs are in `dev/authoring-injected-context.md`.
