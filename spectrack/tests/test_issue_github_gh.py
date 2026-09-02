"""Tests for GitHub workflow wrappers."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from command import CommandRequest, CommandResult, MissingCommandError  # noqa: E402
from command import WorkflowCommandError  # noqa: E402
from issue.github.gh import DEFAULT_ISSUE_FIELDS, GitHubParseError  # noqa: E402
from issue.github.gh import GitHubVerificationError  # noqa: E402
from issue.github.gh import close_issue, comment_issue, create_issue, edit_issue, edit_issue_body  # noqa: E402
from issue.github.gh import issue_body_edit_history, issue_relationships, issue_timeline  # noqa: E402
from issue.github.gh import parse_github_remote_url, resolve_github_repository, view_issue  # noqa: E402
from issue.github.gh import reopen_issue  # noqa: E402


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult | Exception]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if isinstance(response, Exception):
            raise response
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def gh_args(project: Path, *args: str) -> tuple[str, ...]:
    _ = project
    return ("gh", *args)


def git_args(project: Path, *args: str) -> tuple[str, ...]:
    return ("git", "-C", str(project.resolve(strict=False)), *args)


def gh_issue_view_args(issue: int | str, fields: tuple[str, ...]) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        ",".join(fields),
    )


def _config_path(project: Path) -> Path:
    path = project / ".spectrack" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def test_resolves_github_repository_from_workflow_config(tmp_path: Path) -> None:
    _config_path(tmp_path).write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
""".lstrip(),
        encoding="utf-8",
    )

    repo = resolve_github_repository(tmp_path)

    assert repo.host == "github.com"
    assert repo.slug == "studykit/studykit-plugins"


@pytest.mark.parametrize(
    ("remote_url", "host", "slug"),
    [
        ("git@github.com:studykit/studykit-plugins.git", "github.com", "studykit/studykit-plugins"),
        ("https://github.example.com/studykit/studykit-plugins.git", "github.example.com", "studykit/studykit-plugins"),
        ("ssh://git@github.com/studykit/studykit-plugins.git", "github.com", "studykit/studykit-plugins"),
    ],
)
def test_parses_common_github_remote_urls(remote_url: str, host: str, slug: str) -> None:
    repo = parse_github_remote_url(remote_url)

    assert repo.host == host
    assert repo.slug == slug


def test_view_issue_uses_gh_issue_view_with_structured_fields(tmp_path: Path) -> None:
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_args(
                tmp_path,
                "issue",
                "view",
                "38",
                "--repo",
                "studykit/studykit-plugins",
                "--json",
                ",".join(DEFAULT_ISSUE_FIELDS),
            ): result(
                gh_args(
                    tmp_path,
                    "issue",
                    "view",
                    "38",
                    "--repo",
                    "studykit/studykit-plugins",
                    "--json",
                    ",".join(DEFAULT_ISSUE_FIELDS),
                ),
                stdout=json.dumps({"number": 38, "title": "Add wrappers"}),
            ),
        }
    )

    issue = view_issue("#38", project=tmp_path, runner=runner)

    assert issue["number"] == 38
    assert issue["repository"]["slug"] == "studykit/studykit-plugins"


def test_timeline_flattens_paginated_json_arrays(tmp_path: Path) -> None:
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_args(
                tmp_path,
                "api",
                "repos/studykit/studykit-plugins/issues/37/timeline",
                "--paginate",
            ): result(
                gh_args(
                    tmp_path,
                    "api",
                    "repos/studykit/studykit-plugins/issues/37/timeline",
                    "--paginate",
                ),
                stdout='[{"event":"labeled"}]\n[{"event":"sub_issue_added"}]\n',
            ),
        }
    )

    timeline = issue_timeline(37, project=tmp_path, runner=runner)

    assert [event["event"] for event in timeline["events"]] == ["labeled", "sub_issue_added"]


def _derived_relationship_responses(project: Path, *, body: str, timeline: list[dict[str, Any]]) -> dict[tuple[str, ...], CommandResult]:
    base = "repos/studykit/studykit-plugins/issues/17"
    responses = {
        git_args(project, "remote", "get-url", "origin"): result(
            git_args(project, "remote", "get-url", "origin"),
            stdout="git@github.com:studykit/studykit-plugins.git\n",
        ),
        gh_args(project, "api", base): result(
            gh_args(project, "api", base),
            stdout=json.dumps({"number": 17, "body": body, "updated_at": "2026-07-06T00:00:00Z"}),
        ),
        gh_args(project, "api", f"{base}/parent"): result(
            gh_args(project, "api", f"{base}/parent"), returncode=404, stderr="not found"
        ),
        gh_args(project, "api", f"{base}/sub_issues", "--paginate"): result(
            gh_args(project, "api", f"{base}/sub_issues", "--paginate"), stdout="[]"
        ),
        gh_args(project, "api", f"{base}/dependencies/blocked_by", "--paginate"): result(
            gh_args(project, "api", f"{base}/dependencies/blocked_by", "--paginate"), stdout="[]"
        ),
        gh_args(project, "api", f"{base}/dependencies/blocking", "--paginate"): result(
            gh_args(project, "api", f"{base}/dependencies/blocking", "--paginate"),
            stdout=json.dumps([{"number": 22, "title": "Blocked twin", "state": "open"}]),
        ),
        gh_args(project, "api", f"{base}/timeline", "--paginate"): result(
            gh_args(project, "api", f"{base}/timeline", "--paginate"),
            stdout=json.dumps(timeline),
        ),
    }
    return responses


def _cross_referenced_event(number: int, *, full_name: str = "studykit/studykit-plugins", pull_request: bool = False) -> dict[str, Any]:
    source_issue: dict[str, Any] = {"number": number, "repository": {"full_name": full_name}}
    if pull_request:
        source_issue["pull_request"] = {"url": f"https://github.com/{full_name}/pull/{number}"}
    return {"event": "cross-referenced", "source": {"type": "issue", "issue": source_issue}}


def test_issue_relationships_derives_body_references_and_timeline_referenced_by(tmp_path: Path) -> None:
    body = (
        "Builds on #16 (see #16 again) and studykit/studykit-plugins#18, "
        "not other/repo#5, plus https://github.com/studykit/studykit-plugins/issues/19. "
        "Already blocking #22; self ref #17."
    )
    timeline = [
        _cross_referenced_event(22),
        _cross_referenced_event(20),
        _cross_referenced_event(30, pull_request=True),
        _cross_referenced_event(7, full_name="other/repo"),
        _cross_referenced_event(20),
        {"event": "labeled"},
    ]
    runner = FakeRunner(_derived_relationship_responses(tmp_path, body=body, timeline=timeline))

    payload = issue_relationships(17, project=tmp_path, runner=runner)

    # Outgoing: same-repo body refs minus self (#17) and native kinds (#22 blocking).
    assert payload["references"] == [16, 18, 19]
    # Incoming: timeline cross-references minus native kinds, PRs, other repos, dups.
    assert payload["referenced_by"] == [20]


def test_issue_relationships_without_derived_skips_timeline_and_reference_keys(tmp_path: Path) -> None:
    runner = FakeRunner(
        _derived_relationship_responses(tmp_path, body="Mentions #16.", timeline=[])
    )

    payload = issue_relationships(17, project=tmp_path, runner=runner, include_derived=False)

    assert "references" not in payload
    assert "referenced_by" not in payload
    assert not any("/timeline" in " ".join(request.args) for request in runner.requests)


def test_body_edit_history_uses_graphql_user_content_edits(tmp_path: Path) -> None:
    graphql_response = {
        "data": {
            "repository": {
                "issue": {
                    "number": 37,
                    "userContentEdits": {
                        "nodes": [{"editedAt": "2026-05-13T00:00:00Z", "diff": "@@"}]
                    },
                }
            }
        }
    }
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
        }
    )

    def graphql_runner(request: CommandRequest) -> CommandResult:
        if request.args[:3] == ("git", "-C", str(tmp_path.resolve(strict=False))):
            return runner(request)
        if request.args[:3] == ("gh", "api", "graphql"):
            return CommandResult(request=request, returncode=0, stdout=json.dumps(graphql_response))
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    history = issue_body_edit_history(37, project=tmp_path, runner=graphql_runner)

    assert history["body_edit_history"]["number"] == 37
    assert history["body_edit_history"]["userContentEdits"]["nodes"][0]["diff"] == "@@"


def test_comment_issue_uses_body_file(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "comment"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            assert body_file.read_text(encoding="utf-8") == "Implemented wrapper."
            return CommandResult(request=request, returncode=0)
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = comment_issue(
        38,
        body="Implemented wrapper.",
        project=tmp_path,
        runner=runner,
    )

    assert result_payload["operation"] == "comment_issue"


def test_create_issue_verifies_after_write(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "create"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            assert body_file.read_text(encoding="utf-8") == "Draft body."
            assert "--title" in request.args
            assert request.args[request.args.index("--title") + 1] == "Draft issue"
            assert request.args.count("--label") == 2
            return CommandResult(
                request=request,
                returncode=0,
                stdout="https://github.com/studykit/studykit-plugins/issues/51\n",
            )
        if request.args == gh_issue_view_args(51, ("title", "body", "labels", "state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": "Draft issue",
                        "body": "Draft body.",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                        "state": "OPEN",
                        "stateReason": None,
                    }
                ),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = create_issue(
        title="Draft issue",
        body="Draft body.",
        labels=("task", "workflow"),
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "create_issue", "issue": "51", "verified": True}


def test_create_issue_passes_assignee_to_gh(tmp_path: Path) -> None:
    recorded: dict[str, tuple[str, ...]] = {}

    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "create"):
            recorded["create"] = request.args
            return CommandResult(
                request=request,
                returncode=0,
                stdout="https://github.com/studykit/studykit-plugins/issues/61\n",
            )
        if request.args == gh_issue_view_args(61, ("title", "body", "labels", "state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": "Draft issue",
                        "body": "Draft body.",
                        "labels": [{"name": "task"}],
                        "state": "OPEN",
                        "stateReason": None,
                    }
                ),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = create_issue(
        title="Draft issue",
        body="Draft body.",
        labels=("task",),
        assignee="alice",
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "create_issue", "issue": "61", "verified": True}
    create_args = recorded["create"]
    assert "--assignee" in create_args
    assert create_args[create_args.index("--assignee") + 1] == "alice"


def test_edit_issue_body_verifies_after_write(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "edit"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            assert body_file.read_text(encoding="utf-8") == "Updated body."
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("body",)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"body": "Updated body."}),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = edit_issue_body(
        38,
        body="Updated body.",
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "edit_issue_body", "issue": "38", "verified": True}


def test_edit_issue_reconciles_title_body_and_labels(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "edit"):
            body_file = Path(request.args[request.args.index("--body-file") + 1])
            assert body_file.read_text(encoding="utf-8") == "Updated body."
            assert request.args[request.args.index("--title") + 1] == "Updated title"
            assert ("--add-label", "workflow") in zip(request.args, request.args[1:])
            assert ("--remove-label", "old") in zip(request.args, request.args[1:])
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("title", "body", "labels")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": "Updated title",
                        "body": "Updated body.",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                    }
                ),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = edit_issue(
        38,
        title="Updated title",
        body="Updated body.",
        labels=("task", "workflow"),
        current_labels=("task", "old"),
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "edit_issue", "issue": "38", "verified": True}


def test_close_issue_verifies_after_write(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args == (
            "gh",
            "issue",
            "close",
            "38",
            "--repo",
            "studykit/studykit-plugins",
            "--reason",
            "completed",
        ):
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": "CLOSED", "stateReason": "COMPLETED"}),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = close_issue(
        38,
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "close_issue", "issue": "38", "verified": True}


def test_close_issue_normalizes_not_planned_reason(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args == (
            "gh",
            "issue",
            "close",
            "38",
            "--repo",
            "studykit/studykit-plugins",
            "--reason",
            "not planned",
        ):
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": "CLOSED", "stateReason": "NOT_PLANNED"}),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = close_issue(
        38,
        project=tmp_path,
        reason="not_planned",
        runner=runner,
    )

    assert result_payload == {"operation": "close_issue", "issue": "38", "verified": True}


def test_reopen_issue_verifies_after_write(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args == (
            "gh",
            "issue",
            "reopen",
            "38",
            "--repo",
            "studykit/studykit-plugins",
        ):
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": "OPEN", "stateReason": None}),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    result_payload = reopen_issue(
        38,
        project=tmp_path,
        runner=runner,
    )

    assert result_payload == {"operation": "reopen_issue", "issue": "38", "verified": True}


def test_close_issue_raises_when_verification_fails(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        if request.args == git_args(tmp_path, "remote", "get-url", "origin"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            )
        if request.args[:3] == ("gh", "issue", "close"):
            return CommandResult(request=request, returncode=0)
        if request.args == gh_issue_view_args(38, ("state", "stateReason")):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"state": "OPEN", "stateReason": None}),
            )
        return CommandResult(request=request, returncode=127, stderr="unexpected command")

    with pytest.raises(GitHubVerificationError, match="state verification failed"):
        close_issue(
            38,
            project=tmp_path,
                runner=runner,
        )


def test_missing_gh_tool_is_reported(tmp_path: Path) -> None:
    request = CommandRequest(
        args=gh_args(
            tmp_path,
            "issue",
            "view",
            "38",
            "--repo",
            "studykit/studykit-plugins",
            "--json",
            ",".join(DEFAULT_ISSUE_FIELDS),
        )
    )
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            request.args: MissingCommandError("command not found: gh", request=request),
        }
    )

    with pytest.raises(MissingCommandError):
        view_issue(38, project=tmp_path, runner=runner)


def test_failed_gh_command_is_reported(tmp_path: Path) -> None:
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_args(
                tmp_path,
                "issue",
                "view",
                "38",
                "--repo",
                "studykit/studykit-plugins",
                "--json",
                ",".join(DEFAULT_ISSUE_FIELDS),
            ): result(
                gh_args(
                    tmp_path,
                    "issue",
                    "view",
                    "38",
                    "--repo",
                    "studykit/studykit-plugins",
                    "--json",
                    ",".join(DEFAULT_ISSUE_FIELDS),
                ),
                stderr="not found",
                returncode=1,
            ),
        }
    )

    with pytest.raises(WorkflowCommandError):
        view_issue(38, project=tmp_path, runner=runner)


def test_invalid_json_is_parse_error(tmp_path: Path) -> None:
    runner = FakeRunner(
        {
            git_args(tmp_path, "remote", "get-url", "origin"): result(
                git_args(tmp_path, "remote", "get-url", "origin"),
                stdout="git@github.com:studykit/studykit-plugins.git\n",
            ),
            gh_args(
                tmp_path,
                "issue",
                "view",
                "38",
                "--repo",
                "studykit/studykit-plugins",
                "--json",
                ",".join(DEFAULT_ISSUE_FIELDS),
            ): result(
                gh_args(
                    tmp_path,
                    "issue",
                    "view",
                    "38",
                    "--repo",
                    "studykit/studykit-plugins",
                    "--json",
                    ",".join(DEFAULT_ISSUE_FIELDS),
                ),
                stdout="not json",
            ),
        }
    )

    with pytest.raises(GitHubParseError):
        view_issue(38, project=tmp_path, runner=runner)
