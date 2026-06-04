# SpecTrack

The SpecTrack plugin's Python sources live in `scripts/`; tests live in
`tests/`. There is no `pyproject.toml` — each script declares its own PEP 723
inline metadata and the bundled `scripts/spectrack` launcher runs it via
`uv run --script`.

## Running tests

Run the full suite from the repository root with:

```bash
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/spectrack/tests
```

`pytest`, `python-frontmatter`, and `PyYAML` are the only runtime deps required
to exercise the test modules. `uv` provisions an ephemeral environment;
nothing needs to be pre-installed.

Run a single module or test the same way — pass the path / `-k` selector
through to pytest:

```bash
# One module
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/spectrack/tests/test_workflow_jira_issue_cache.py

# One test
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/spectrack/tests -k test_jira_metadata_records_native_state
```

Common pytest flags work as expected (`-x`, `-q`, `-vv`, `--lf`). Tests are
fast — the full suite finishes in a few seconds — so prefer running the
whole suite once before committing.

## What to test

Before adding or changing tests, read `dev/testing-principles.md` and
`tests/AGENTS.md`. Tests protect executable behavior and stable layer
boundaries; they do not freeze prose, headings, or authoring judgment unless
that wording is intentionally a contract.

## Authoring agent and skill docs — check the hook-injected context first

Before writing or editing any `agents/<name>.md` or
`skills/<name>/SKILL.md` in this plugin, **read the context that
`hooks/scripts/hook_claude.py` injects on the surface you are authoring**.
Skipping this leaves the doc duplicating runtime-injected text, restating
it stale, or — worse — assuming context that isn't actually injected on
that surface and leaving the runtime instance missing what it needs.

The fastest way to read the injected text is the `preview_context`
launcher command — it calls the same `main_context` build functions the
hooks call, so its output is byte-for-byte what the runtime receives:

```bash
# All surfaces for the project's configured provider
spectrack preview_context

# One surface, one provider/runtime
spectrack preview_context --surface session --provider jira
spectrack preview_context --surface subagent --provider github \
  --agent issue-implementer
spectrack preview_context --surface commit

# Enumerate per-agent block names
spectrack preview_context --list-agents
```

`--surface` is `session` (main), `subagent`, `commit`, or `all` (default).
Omit `--provider` to load the project's `.spectrack/config.yml`; pass it
to preview a provider without a configured project. `--agent all` dumps
every per-agent SubagentStart block.

Where the injected text comes from:

- **Skills run in the main session** — `SessionStart` injects from
  `hooks/context/main/`:
  - `session-start.md` (always)
  - `snippets/commit-prefix.md` (re-injected at `UserPromptSubmit` when
    a commit keyword fires)
- **Agents run as subagents** — `SubagentStart` injects from
  `hooks/context/subagent/`:
  - `session-start.md` (general subagent policy)
  - `agents/<agent-name>.md` (per-agent block, when present)
- **Inline snippets** — `hooks/context/snippets/authoring.md` (authoring
  resolver), `hooks/context/snippets/launcher/<runtime>.md` (launcher
  invocation), and `hooks/context/snippets/prd-path.md` (PRD-path
  resolver) are the only fragments inlined into the templates above.
  Everything else is referenced on demand.
- **On-demand reference docs** are *not* injected. The injected
  `main/session-start.md` and `subagent/session-start.md` only point at them; the
  agent reads them with `Read` when needed. They live under
  `authoring/runbook/`, organized by intent:
  - `authoring/runbook/issue-fetch/<provider>.md`
  - `authoring/runbook/issue-write/<provider>.md` — shared body-bearing
    write procedure (intent index for github/jira; full flow for
    filesystem)
  - `authoring/runbook/issue-new/<provider>.md` (github / jira)
  - `authoring/runbook/issue-comment/<provider>.md` (github / jira)
  - `authoring/runbook/issue-update/<provider>.md` (github / jira)
  - `authoring/runbook/issue-link/<provider>.md` (github / jira)
  - `authoring/runbook/issue-state/<provider>.md` (github / jira)

`hooks/hooks.json` and `hooks/scripts/hook_claude.py` are the source of truth
whenever the layout above looks stale.

Rules that follow:

- Refer to injected blocks by tag (e.g., `<launcher>`, `<authoring-resolver>`,
  `<commit-prefix>`, `<runbook>`) and point at runbook intents by tag
  (e.g., "verb syntax at `<runbook>`'s `issue-new` intent") instead of
  restating provider-specific command shapes that the runtime will inject
  anyway. Procedures that span multiple runbook intents belong in the
  agent body as a named section the body refers to internally — not in
  the SubagentStart per-agent block, which only carries injected tags.
- Do not assume cross-surface context. A skill (main session) sees
  `main/...` blocks; a subagent sees `subagent/...` blocks. Crossing the
  boundary leaves the runtime doc missing assumed context — surface the
  needed inputs through the caller's dispatch arguments instead.
- When adding a new agent that needs its own injected block, add the
  file under `hooks/context/subagent/agents/`, wire it through
  `hooks/scripts/hook_claude.py`, and only then reference it from the agent
  body.
