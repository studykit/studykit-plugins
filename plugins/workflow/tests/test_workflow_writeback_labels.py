"""Tests for writeback label flags on both providers."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_github import DEFAULT_ISSUE_FIELDS, GitHubRepository  # noqa: E402
from issue.github.cache import GitHubIssueCache  # noqa: E402
from issue.github.backend import (  # noqa: E402
    GitHubIssueWritebackError,
    update_issue as github_writeback_update,
)
from issue.jira.backend import (  # noqa: E402
    JiraIssueWritebackError,
    update_issue as jira_writeback_update,
)


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def gh_issue_view_args(issue: int, fields: str) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        fields,
    )


def gh_api_args(*args: str) -> tuple[str, ...]:
    return ("gh", "api", *args)


def write_github_config(project: Path) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
issue_id_format: github
""".lstrip(),
        encoding="utf-8",
    )


def write_jira_config(project: Path) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        """
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
""".lstrip(),
        encoding="utf-8",
    )


def github_issue_payload(*, labels: list[str] | None = None) -> dict[str, object]:
    return {
        "number": 39,
        "title": "Cached title",
        "state": "OPEN",
        "stateReason": None,
        "body": "Cached body.",
        "labels": [{"name": label} for label in (labels or ["task", "workflow"])],
        "comments": [],
        "updatedAt": "2026-05-13T12:00:00Z",
    }


def _write_body_file(project: Path, body: str = "Updated body.\n") -> Path:
    path = project / "body.md"
    path.write_text(body, encoding="utf-8")
    return path


def _seed_github_cache(project: Path, *, labels: list[str] | None = None) -> GitHubIssueCache:
    cache = GitHubIssueCache.for_project(project, configured_repo=repo())
    cache.write_issue_bundle(repo(), github_issue_payload(labels=labels), fetched_at="2026-05-13T12:34:56Z")
    return cache


class WritebackLabelRunner:
    """Prefix-matching runner for github writeback label tests."""

    def __init__(self, *, current_labels: list[str], labels_after: list[str]) -> None:
        self.requests: list[CommandRequest] = []
        self.current_labels = current_labels
        self.labels_after = labels_after
        self.edit_label_args: list[tuple[str, ...]] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args == gh_issue_view_args(39, "number,updatedAt"):
            return result(request.args, stdout=json.dumps({"number": 39, "updatedAt": "2026-05-13T12:00:00Z"}))
        if request.args == gh_issue_view_args(39, "number,labels"):
            return result(
                request.args,
                stdout=json.dumps({"number": 39, "labels": [{"name": name} for name in self.current_labels]}),
            )
        if request.args[:3] == ("gh", "issue", "edit"):
            label_args = tuple(
                arg for arg in request.args
                if arg in {"--add-label", "--remove-label"} or self._is_label_value(request.args, arg)
            )
            self.edit_label_args.append(label_args)
            return result(request.args)
        # Post-edit verification calls
        if request.args == gh_issue_view_args(39, "body"):
            return result(request.args, stdout=json.dumps({"body": "Updated body.\n"}))
        if request.args == gh_issue_view_args(39, "body,labels"):
            return result(
                request.args,
                stdout=json.dumps({"body": "Updated body.\n", "labels": [{"name": name} for name in self.labels_after]}),
            )
        # Cache refresh
        if request.args == gh_issue_view_args(39, ",".join(DEFAULT_ISSUE_FIELDS)):
            return result(request.args, stdout=json.dumps(github_issue_payload(labels=self.labels_after)))
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/39"):
            return result(
                request.args,
                stdout=json.dumps({"id": 3900, "number": 39, "updated_at": "2026-05-13T12:00:00Z"}),
            )
        if request.args == gh_api_args("repos/studykit/studykit-plugins/issues/39/parent"):
            return result(request.args, stderr="not found", returncode=404)
        if request.args in {
            gh_api_args("repos/studykit/studykit-plugins/issues/39/sub_issues", "--paginate"),
            gh_api_args("repos/studykit/studykit-plugins/issues/39/dependencies/blocked_by", "--paginate"),
            gh_api_args("repos/studykit/studykit-plugins/issues/39/dependencies/blocking", "--paginate"),
        }:
            return result(request.args, stdout="[]")
        return result(request.args, returncode=127, stderr=f"unexpected command: {request.args}")

    @staticmethod
    def _is_label_value(args: tuple[str, ...], arg: str) -> bool:
        # Include the value that follows --add-label or --remove-label.
        for idx, token in enumerate(args):
            if idx > 0 and token == arg and args[idx - 1] in {"--add-label", "--remove-label"}:
                return True
        return False


def test_github_writeback_add_label_repeatable(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_github_cache(tmp_path)
    body_file = _write_body_file(tmp_path)
    runner = WritebackLabelRunner(current_labels=["task", "workflow"], labels_after=["task", "workflow", "foo", "bar"])

    github_writeback_update(
        project=tmp_path,
        artifact_type="task",
        issue="#39",
        body_file=body_file,
        add_labels=("foo", "bar"),
        runner=runner,
    )

    assert runner.edit_label_args == [("--add-label", "bar", "--add-label", "foo")]


def test_github_writeback_remove_label(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_github_cache(tmp_path)
    body_file = _write_body_file(tmp_path)
    runner = WritebackLabelRunner(current_labels=["task", "workflow"], labels_after=["task"])

    github_writeback_update(
        project=tmp_path,
        artifact_type="task",
        issue="#39",
        body_file=body_file,
        remove_labels=("workflow",),
        runner=runner,
    )

    assert runner.edit_label_args == [("--remove-label", "workflow")]


def test_github_writeback_set_labels_replaces(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_github_cache(tmp_path, labels=["task", "workflow"])
    body_file = _write_body_file(tmp_path)
    runner = WritebackLabelRunner(current_labels=["task", "workflow"], labels_after=["a", "b", "c"])

    github_writeback_update(
        project=tmp_path,
        artifact_type="task",
        issue="#39",
        body_file=body_file,
        set_labels=("a", "b", "c"),
        runner=runner,
    )

    assert runner.edit_label_args == [
        ("--add-label", "a", "--add-label", "b", "--add-label", "c",
         "--remove-label", "task", "--remove-label", "workflow")
    ]


def test_github_writeback_set_labels_conflict_with_add(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    body_file = _write_body_file(tmp_path)
    with pytest.raises(GitHubIssueWritebackError, match="cannot be combined"):
        github_writeback_update(
            project=tmp_path,
            artifact_type="task",
            issue="#39",
            body_file=body_file,
            add_labels=("foo",),
            set_labels=("a", "b"),
        )


def test_jira_writeback_set_labels_conflict_with_remove(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path)
    with pytest.raises(JiraIssueWritebackError, match="cannot be combined"):
        jira_writeback_update(
            project=tmp_path,
            artifact_type="task",
            issue="TEST-1234",
            body_file=body_file,
            remove_labels=("foo",),
            set_labels=("a", "b"),
        )
