"""Tests for the GitHub issue body-less field mutation CLI."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from issue.github.gh import DEFAULT_ISSUE_FIELDS, GitHubRepository  # noqa: E402
from issue.github.cache import GitHubIssueCache  # noqa: E402
from issue.github.backend import (  # noqa: E402
    GitHubIssueFieldsError,
    fields_payload,
)
from functools import partial  # noqa: E402

from issue.dispatch import FIELDS, run_intent  # noqa: E402

github_issue_fields_main = partial(run_intent, FIELDS)


_DROPPED_FIELD_KEYS = ("provider", "cache", "repository", "operation", "role", "kind", "verified")


def _assert_flat_field_envelope(payload: dict, *, issue_basename: str = "39/issue.md") -> None:
    """Assert the flattened envelope contract for GitHub field write payloads."""
    for dropped in _DROPPED_FIELD_KEYS:
        assert dropped not in payload, f"{dropped!r} should not be in payload"
    assert payload["issue"].endswith(issue_basename), payload["issue"]
    assert payload["cache_refreshed"] is True


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def gh_issue_view_args(issue: int | str, fields: str) -> tuple[str, ...]:
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


def git_args(project: Path, *args: str) -> tuple[str, ...]:
    return ("git", "-C", str(project), *args)


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


def issue_payload(*, title: str = "Cached title", labels: list[str] | None = None, assignees: list[str] | None = None) -> dict[str, object]:
    payload: dict[str, object] = {
        "number": 39,
        "title": title,
        "state": "OPEN",
        "stateReason": None,
        "body": "Cached body.",
        "labels": [{"name": label} for label in (labels or ["task", "workflow"])],
        "comments": [],
        "updatedAt": "2026-05-13T12:00:00Z",
    }
    if assignees is not None:
        payload["assignees"] = [{"login": login} for login in assignees]
    return payload


def _seed_cache(project: Path, *, labels: list[str] | None = None) -> GitHubIssueCache:
    cache = GitHubIssueCache.for_project(project, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload(labels=labels), fetched_at="2026-05-13T12:34:56Z")
    return cache


def _freshness_args() -> tuple[str, ...]:
    return gh_issue_view_args(39, "number,title,body")


# Provider content matching the seeded cache — keeps the content fingerprint fresh.
_FRESH_CONTENT = {"number": 39, "title": "Cached title", "body": "Cached body."}
# Diverged content drives the freshness conflict path.
_CONFLICT_CONTENT = {"number": 39, "title": "Cached title", "body": "Provider changed body."}


def _refresh_args() -> tuple[str, ...]:
    return gh_issue_view_args(39, ",".join(DEFAULT_ISSUE_FIELDS))


def _refresh_relationship_args() -> dict[tuple[str, ...], CommandResult]:
    rest_issue_args = gh_api_args("repos/studykit/studykit-plugins/issues/39")
    parent_args = gh_api_args("repos/studykit/studykit-plugins/issues/39/parent")
    children_args = gh_api_args("repos/studykit/studykit-plugins/issues/39/sub_issues", "--paginate")
    blocked_by_args = gh_api_args("repos/studykit/studykit-plugins/issues/39/dependencies/blocked_by", "--paginate")
    blocking_args = gh_api_args("repos/studykit/studykit-plugins/issues/39/dependencies/blocking", "--paginate")
    return {
        rest_issue_args: result(
            rest_issue_args,
            stdout=json.dumps({"id": 3900, "number": 39, "updated_at": "2026-05-13T12:00:00Z"}),
        ),
        parent_args: result(parent_args, stderr="not found", returncode=404),
        children_args: result(children_args, stdout="[]"),
        blocked_by_args: result(blocked_by_args, stdout="[]"),
        blocking_args: result(blocking_args, stdout="[]"),
    }


def test_set_type_preserves_non_type_labels_and_swaps_type_label(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    cache = _seed_cache(tmp_path, labels=["task", "workflow"])
    edit_args = (
        "gh",
        "issue",
        "edit",
        "39",
        "--repo",
        "studykit/studykit-plugins",
        "--add-label",
        "bug",
        "--remove-label",
        "task",
    )
    refreshed = issue_payload(labels=["bug", "workflow"])
    responses = {
        _freshness_args(): result(_freshness_args(), stdout=json.dumps(_FRESH_CONTENT)),
        gh_issue_view_args(39, "number,labels"): result(
            gh_issue_view_args(39, "number,labels"),
            stdout=json.dumps({"number": 39, "labels": [{"name": "task"}, {"name": "workflow"}]}),
        ),
        edit_args: result(edit_args),
        gh_issue_view_args(39, "labels"): result(
            gh_issue_view_args(39, "labels"),
            stdout=json.dumps({"labels": [{"name": "bug"}, {"name": "workflow"}]}),
        ),
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(refreshed)),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="set-type",
        issue="#39",
        new_type="bug",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    cached = cache.read_issue(repo(), 39, include_body=False, include_comments=False, include_relationships=False)
    assert sorted(cached["labels"]) == ["bug", "workflow"]
    assert edit_args in {request.args for request in runner.requests}


def test_assign_me_resolves_via_gh_api_user(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_cache(tmp_path)
    me_args = gh_api_args("user", "--jq", ".login")
    edit_args = (
        "gh",
        "issue",
        "edit",
        "39",
        "--repo",
        "studykit/studykit-plugins",
        "--add-assignee",
        "studykit-bot",
    )
    responses = {
        me_args: result(me_args, stdout="studykit-bot\n"),
        _freshness_args(): result(_freshness_args(), stdout=json.dumps(_FRESH_CONTENT)),
        edit_args: result(edit_args),
        gh_issue_view_args(39, "title,labels"): result(
            gh_issue_view_args(39, "title,labels"),
            stdout=json.dumps({"title": "Cached title", "labels": [{"name": "task"}, {"name": "workflow"}]}),
        ),
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(issue_payload(assignees=["studykit-bot"]))),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="assign",
        issue="#39",
        user="me",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    assert edit_args in {request.args for request in runner.requests}
    me_calls = [request for request in runner.requests if request.args == me_args]
    assert len(me_calls) == 1


def test_unassign_clears_all_current_assignees(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_cache(tmp_path)
    assignees_args = gh_issue_view_args(39, "assignees")
    edit_args = (
        "gh",
        "issue",
        "edit",
        "39",
        "--repo",
        "studykit/studykit-plugins",
        "--remove-assignee",
        "alice",
        "--remove-assignee",
        "bob",
    )
    responses = {
        _freshness_args(): result(_freshness_args(), stdout=json.dumps(_FRESH_CONTENT)),
        assignees_args: result(
            assignees_args,
            stdout=json.dumps({"assignees": [{"login": "alice"}, {"login": "bob"}]}),
        ),
        edit_args: result(edit_args),
        gh_issue_view_args(39, "title,labels"): result(
            gh_issue_view_args(39, "title,labels"),
            stdout=json.dumps({"title": "Cached title", "labels": [{"name": "task"}, {"name": "workflow"}]}),
        ),
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(issue_payload(assignees=[]))),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="unassign",
        issue="#39",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    assert edit_args in {request.args for request in runner.requests}


def test_set_type_rejects_empty_type(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    with pytest.raises(GitHubIssueFieldsError, match="non-empty type"):
        fields_payload(
            project=tmp_path,
            artifact_type="task",
            verb="set-type",
            issue="#39",
            new_type="   ",
        )


def _close_args(reason: str = "completed") -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "close",
        "39",
        "--repo",
        "studykit/studykit-plugins",
        "--reason",
        reason,
    )


def _reopen_args() -> tuple[str, ...]:
    return ("gh", "issue", "reopen", "39", "--repo", "studykit/studykit-plugins")


def _verify_state_args() -> tuple[str, ...]:
    return gh_issue_view_args(39, "state,stateReason")


def test_close_returns_flat_envelope(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_cache(tmp_path)
    refreshed = issue_payload()
    refreshed["state"] = "CLOSED"
    refreshed["stateReason"] = "COMPLETED"
    responses = {
        _freshness_args(): result(_freshness_args(), stdout=json.dumps(_FRESH_CONTENT)),
        _close_args(): result(_close_args()),
        _verify_state_args(): result(
            _verify_state_args(),
            stdout=json.dumps({"state": "CLOSED", "stateReason": "COMPLETED"}),
        ),
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(refreshed)),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="close",
        issue="#39",
        reason="completed",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    assert _close_args() in {request.args for request in runner.requests}


def test_reopen_returns_flat_envelope(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    cache = _seed_cache(tmp_path)
    # Seed cache as closed so reopen lands at OPEN.
    closed = issue_payload()
    closed["state"] = "CLOSED"
    closed["stateReason"] = "COMPLETED"
    cache.write_issue_bundle(repo(), closed, fetched_at="2026-05-13T12:34:56Z")
    refreshed = issue_payload()
    responses = {
        _freshness_args(): result(_freshness_args(), stdout=json.dumps(_FRESH_CONTENT)),
        _reopen_args(): result(_reopen_args()),
        _verify_state_args(): result(
            _verify_state_args(),
            stdout=json.dumps({"state": "OPEN", "stateReason": None}),
        ),
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(refreshed)),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)

    payload = fields_payload(
        project=tmp_path,
        artifact_type="task",
        verb="reopen",
        issue="#39",
        runner=runner,
    )

    _assert_flat_field_envelope(payload)
    assert _reopen_args() in {request.args for request in runner.requests}


def test_close_on_provider_conflict_returns_conflict_envelope_and_exit_3(tmp_path: Path) -> None:
    write_github_config(tmp_path)
    _seed_cache(tmp_path)
    # Provider content diverges from the cached projection's content fingerprint.
    drifted_freshness = result(_freshness_args(), stdout=json.dumps(_CONFLICT_CONTENT))
    refreshed = issue_payload()
    responses = {
        _freshness_args(): drifted_freshness,
        _refresh_args(): result(_refresh_args(), stdout=json.dumps(refreshed)),
        **_refresh_relationship_args(),
    }
    runner = FakeRunner(responses)
    stdout = io.StringIO()
    stderr = io.StringIO()

    exit_code = github_issue_fields_main(
        ["--project", str(tmp_path), "close", "#39"],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert exit_code == 3, stderr.getvalue()
    payload = json.loads(stdout.getvalue())
    assert payload["status"] == "conflict"
    assert payload["reason"] == "provider_changed"
    assert payload["reread_required"] is True
    assert payload["reread_paths"]
    assert all(not path.endswith("/.meta.json") for path in payload["reread_paths"])
    # Provider close was not issued because the freshness gate blocked first.
    assert _close_args() not in {request.args for request in runner.requests}
