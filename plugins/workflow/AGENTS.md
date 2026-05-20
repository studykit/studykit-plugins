# Workflow Plugin

The workflow plugin's Python sources live in `scripts/`; tests live in
`tests/`. There is no `pyproject.toml` — each script declares its own PEP 723
inline metadata and the bundled `scripts/workflow` launcher runs it via
`uv run --script`.

## Running tests

Run the full suite from the repository root with:

```bash
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/workflow/tests
```

`pytest`, `python-frontmatter`, and `PyYAML` are the only runtime deps required
to exercise the test modules. `uv` provisions an ephemeral environment;
nothing needs to be pre-installed.

Run a single module or test the same way — pass the path / `-k` selector
through to pytest:

```bash
# One module
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/workflow/tests/test_workflow_jira_issue_cache.py

# One test
uv run --with pytest --with python-frontmatter --with PyYAML \
  pytest plugins/workflow/tests -k test_jira_metadata_records_native_state
```

Common pytest flags work as expected (`-x`, `-q`, `-vv`, `--lf`). Tests are
fast — the full suite finishes in a few seconds — so prefer running the
whole suite once before committing.

## What to test

Before adding or changing tests, read `dev/testing-principles.md` and
`tests/AGENTS.md`. Tests protect executable behavior and stable layer
boundaries; they do not freeze prose, headings, or authoring judgment unless
that wording is intentionally a contract.
