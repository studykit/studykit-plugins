"""Issue dispatcher integration tests.

Covers the dispatcher contract that ties the six per-intent modules
under ``issue.legacy.*`` together (now exposed through the unified
``issue.py``):

- ``--help`` reflects only the active backend's option surface for the
  configured ``providers.issues.kind`` (backend-exclusive flags from the
  other provider are hidden).
- Supplying a backend-specific option to the wrong backend produces a
  clean, descriptive error (non-zero exit, parser error on stderr).
- Shared flags carry identical semantics across backends (e.g.,
  ``--cache-policy default|refresh`` exists on both).

Per-backend payload-shape assertions stay on the existing
``test_workflow_cache_*.py`` modules; this file focuses on the routing
seam the dispatcher introduces.
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from issue.legacy.issue_attach import main as issue_attach_main  # noqa: E402
from issue.legacy.issue_comments import main as issue_comments_main  # noqa: E402
from issue.legacy.issue_new import main as issue_drafts_main  # noqa: E402
from issue.legacy.issue_fetch import main as issue_fetch_main  # noqa: E402
from issue.legacy.issue_fields import main as issue_fields_main  # noqa: E402
from issue.legacy.issue_link import main as issue_relationships_main  # noqa: E402
from issue.legacy.issue_update import main as issue_writeback_main  # noqa: E402


_GITHUB_CONFIG = """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
issue_id_format: github
"""

_JIRA_CONFIG = """
version: 1
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: data-center
    api_version: 2
    project: TEST
    issue_type: Task
  knowledge:
    kind: github
issue_id_format: jira
"""


def _write_config(project: Path, body: str) -> None:
    cfg = project / ".workflow" / "config.yml"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(body.lstrip(), encoding="utf-8")


def _capture_help(main_callable, argv: list[str]) -> tuple[int, str, str]:
    """Invoke a dispatcher with ``--help`` and capture argparse output.

    ``argparse`` writes ``--help`` to the process ``sys.stdout`` (and
    parser errors to ``sys.stderr``) regardless of what stdout/stderr
    arguments the dispatcher forwards downstream. Patch the process-level
    streams so we can assert on the printed text.
    """

    out, err = io.StringIO(), io.StringIO()
    saved_stdout, saved_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        try:
            code = main_callable(argv, stdout=out, stderr=err)
        except SystemExit as exc:
            code = int(exc.code) if isinstance(exc.code, int) else 1
    finally:
        sys.stdout, sys.stderr = saved_stdout, saved_stderr
    return code, out.getvalue(), err.getvalue()


# ---------------------------------------------------------------------------
# --help gating
# ---------------------------------------------------------------------------


def test_relationships_help_under_github_hides_jira_epic(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    code, stdout, _ = _capture_help(
        issue_relationships_main,
        ["--project", str(tmp_path), "--help"],
    )
    assert code == 0
    assert "--parent" in stdout
    assert "--blocked-by" in stdout
    assert "--child" in stdout
    assert "--related" in stdout
    assert "--epic" not in stdout
    assert "--replace-epic" not in stdout
    assert "--remove-epic" not in stdout


def test_relationships_help_under_jira_includes_epic(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_relationships_main,
        ["--project", str(tmp_path), "--help"],
    )
    assert code == 0
    assert "--parent" in stdout
    assert "--blocked-by" in stdout
    assert "--epic" in stdout
    assert "--replace-epic" in stdout
    assert "--remove-epic" in stdout


def test_drafts_help_under_github_hides_jira_only_flags(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    code, stdout, _ = _capture_help(
        issue_drafts_main,
        ["--project", str(tmp_path), "publish", "--help"],
    )
    assert code == 0
    assert "--type" in stdout
    assert "--title" in stdout
    assert "--body-file" in stdout
    assert "--state" in stdout
    # Jira-only publish flags must be hidden under github
    assert "--epic" not in stdout
    assert "--epic-name" not in stdout
    assert "--subtask-parent" not in stdout
    assert "--issue-type" not in stdout
    assert "--project-key" not in stdout


def test_drafts_help_under_jira_includes_jira_only_flags(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_drafts_main,
        ["--project", str(tmp_path), "publish", "--help"],
    )
    assert code == 0
    assert "--epic" in stdout
    assert "--epic-name" in stdout
    assert "--subtask-parent" in stdout
    assert "--issue-type" in stdout
    assert "--project-key" in stdout


def test_writeback_help_under_github_includes_state_reason(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    code, stdout, _ = _capture_help(
        issue_writeback_main,
        ["--project", str(tmp_path), "update", "--help"],
    )
    assert code == 0
    assert "--state" in stdout
    assert "--state-reason" in stdout


def test_writeback_help_under_jira_state_is_free_form(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_writeback_main,
        ["--project", str(tmp_path), "update", "--help"],
    )
    assert code == 0
    # Jira `--state` is a free-form verb keyed in
    # ``providers.issues.state_transitions`` — the GitHub enum
    # ``open|closed`` must not appear in the Jira parser help.
    assert "open|closed" not in stdout
    assert "{open,closed}" not in stdout


def test_fields_help_under_github_lists_static_verbs(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    code, stdout, _ = _capture_help(
        issue_fields_main,
        ["--project", str(tmp_path), "--help"],
    )
    assert code == 0
    for verb in ("close", "reopen", "assign", "unassign", "set-type"):
        assert verb in stdout


def test_fields_help_under_jira_omits_close_reopen(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_fields_main,
        ["--project", str(tmp_path), "--help"],
    )
    assert code == 0
    for verb in ("assign", "unassign", "set-type"):
        assert verb in stdout
    # Jira lifecycle verbs come from providers.issues.state_transitions —
    # the static GitHub `close` / `reopen` subcommands must not appear.
    assert " close " not in stdout
    assert " reopen " not in stdout


# ---------------------------------------------------------------------------
# Cross-backend flag rejection
# ---------------------------------------------------------------------------


def test_relationships_github_rejects_jira_epic_flag(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    code, _, err = _capture_help(
        issue_relationships_main,
        ["--project", str(tmp_path), "--epic", "FOO-1", "123"],
    )
    assert code != 0
    assert "--epic" in err or "unrecognized" in err


def test_drafts_github_rejects_jira_subtask_parent(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    body = tmp_path / "body.md"
    body.write_text("body\n", encoding="utf-8")
    code, _, err = _capture_help(
        issue_drafts_main,
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "T",
            "--body-file",
            str(body),
            "--subtask-parent",
            "FOO-1",
        ],
    )
    assert code != 0
    assert "--subtask-parent" in err or "unrecognized" in err


def test_drafts_github_rejects_jira_epic_name(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    body = tmp_path / "body.md"
    body.write_text("body\n", encoding="utf-8")
    code, _, err = _capture_help(
        issue_drafts_main,
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "T",
            "--body-file",
            str(body),
            "--epic-name",
            "Epic Name",
        ],
    )
    assert code != 0
    assert "--epic-name" in err or "unrecognized" in err


# ---------------------------------------------------------------------------
# Shared flags: --cache-policy semantics consistent across backends
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("config_body", [_GITHUB_CONFIG, _JIRA_CONFIG])
def test_fetch_help_lists_cache_policy_on_both_backends(
    tmp_path: Path, config_body: str
) -> None:
    _write_config(tmp_path, config_body)
    code, stdout, _ = _capture_help(
        issue_fetch_main, ["--project", str(tmp_path), "--help"]
    )
    assert code == 0
    assert "--cache-policy" in stdout
    assert "default" in stdout
    assert "refresh" in stdout


@pytest.mark.parametrize(
    "main_callable, sub_args",
    [
        (issue_comments_main, ["append", "--help"]),
        (issue_writeback_main, ["update", "--help"]),
    ],
)
@pytest.mark.parametrize("config_body", [_GITHUB_CONFIG, _JIRA_CONFIG])
def test_body_file_flag_present_on_both_backends(
    tmp_path: Path,
    main_callable,
    sub_args: list[str],
    config_body: str,
) -> None:
    _write_config(tmp_path, config_body)
    code, stdout, _ = _capture_help(
        main_callable,
        ["--project", str(tmp_path), *sub_args],
    )
    assert code == 0
    assert "--body-file" in stdout


# ---------------------------------------------------------------------------
# Missing-config error surfaces the "configure first" hint
# ---------------------------------------------------------------------------


def test_fetch_without_config_emits_setup_hint(tmp_path: Path) -> None:
    # tmp_path has no .workflow/config.yml
    code, _, err = _capture_help(
        issue_fetch_main,
        ["--project", str(tmp_path), "123"],
    )
    assert code == 2
    assert ".workflow/config.yml" in err
    assert "configure first" in err


# ---------------------------------------------------------------------------
# attach: Jira-only verb
# ---------------------------------------------------------------------------


def test_attach_under_github_is_refused(tmp_path: Path) -> None:
    _write_config(tmp_path, _GITHUB_CONFIG)
    sample = tmp_path / "report.pdf"
    sample.write_text("pdf\n", encoding="utf-8")
    code, _, err = _capture_help(
        issue_attach_main,
        ["--project", str(tmp_path), "--issue", "1", str(sample)],
    )
    assert code == 2
    assert "only supported by the Jira" in err


def test_attach_help_under_jira_lists_add_and_get_subcommands(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_attach_main,
        ["--project", str(tmp_path), "--help"],
    )
    assert code == 0
    assert "add" in stdout
    assert "get" in stdout


def test_attach_add_help_under_jira_lists_issue_and_files(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_attach_main,
        ["--project", str(tmp_path), "add", "--help"],
    )
    assert code == 0
    assert "--issue" in stdout
    assert "files" in stdout


def test_attach_get_help_under_jira_lists_selectors(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    code, stdout, _ = _capture_help(
        issue_attach_main,
        ["--project", str(tmp_path), "get", "--help"],
    )
    assert code == 0
    assert "--id" in stdout
    assert "--name" in stdout
    assert "--all" in stdout
    assert "--out" in stdout


def test_attach_add_under_jira_rejects_missing_file(tmp_path: Path) -> None:
    _write_config(tmp_path, _JIRA_CONFIG)
    missing = tmp_path / "nope.pdf"
    code, _, err = _capture_help(
        issue_attach_main,
        ["--project", str(tmp_path), "add", "--issue", "TEST-1", str(missing)],
    )
    assert code == 2
    assert "does not exist" in err
