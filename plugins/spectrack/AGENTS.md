# SpecTrack

The SpecTrack plugin's Python sources live in `scripts/`; tests live in
`tests/`. There is no `pyproject.toml` — each script declares its own PEP 723
inline metadata and the bundled `scripts/spectrack` launcher runs it via
`uv run --script`.

This file is an index: each section carries the facts you must not miss and
points at the doc with the full detail.

## Code map

All issue verbs route through `scripts/issue/dispatch.py` (verb table in its
module docstring); provider behavior lives in `scripts/issue/github/` and
`scripts/issue/jira/`. Hooks enter at `hooks/scripts/hook_claude.py` and
inject Markdown fragments from `hooks/context/`. CLI usage is self-documenting
— `spectrack issue --help` lists the backend's verbs and `spectrack issue
<verb> --help` shows each verb's flags — so a feature change spans the dispatch
surface, the provider drivers (including their argparse `--help` wording),
tests, and a dual Claude+Codex version bump — module responsibilities and the
full checklist are in `dev/code-map.md`.

## Tests

Run the full suite from the repository root with:

```bash
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/spectrack/tests
```

Nothing needs pre-installing; pass paths or `-k` selectors through to pytest
as usual. The suite finishes in seconds — run it fully before committing.
Before adding or changing tests, read `dev/testing-principles.md` and
`tests/AGENTS.md`: tests protect executable behavior and stable layer
boundaries, not prose or authoring judgment.

## Fetched issues are cached locally

`spectrack issue fetch` is cache-backed, not a pass-through remote read. A
fetch writes read-only per-issue projections under the project's
`.spectrack-cache/`, and the default cache policy reuses that local copy
while fresh — so a fetch may return without contacting the provider.
`--cache-policy refresh` forces a remote re-read. The same freshness
metadata gates write-backs: body-bearing writes compare cached fingerprints
and refuse when the remote moved since the last fetch. Never edit cache
files in place.

Projection shape (file names, sidecars, frontmatter) is implementation-owned;
`dev/cache-projection-boundary.md` forbids enumerating it in prose docs. Use
`scripts/issue/cache.py`, the provider carriers
(`scripts/issue/github/cache.py`, `scripts/issue/jira/cache.py`), and their
tests as the source of truth.

## Authoring agent and skill docs

Before writing or editing any `agents/<name>.md` or `skills/<name>/SKILL.md`,
read the context the hooks inject on the surface you are authoring. Render it
with `preview_context` — its output is byte-for-byte what the runtime receives.
Never raw-`cat` the `hooks/context/` templates: their `{{...}}` snippet
placeholders only expand at build time, so the raw files are not what the
runtime sees.

```bash
spectrack preview_context --surface session|subagent|commit|all \
  [--provider github|jira|filesystem] [--agent <name>|all]
```

Two rules you must not miss: refer to injected blocks by tag and point at
`spectrack issue <verb> --help` for CLI usage instead of restating provider
command shapes, and never assume cross-surface context (skills see `main/...`
blocks, subagents see `subagent/...` blocks). The injection layout, full
`preview_context` flag semantics, and the rest of the rules are in
`dev/authoring-injected-context.md`.
