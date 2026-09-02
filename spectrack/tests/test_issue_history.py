"""Tests for the `issue history` verb (GitHub edit-history reads)."""

from __future__ import annotations

import io
import json
import sys
from functools import partial
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from command import CommandRequest, CommandResult  # noqa: E402
from issue.dispatch import HISTORY, run_intent  # noqa: E402
from issue.github.backend import _history_payload  # noqa: E402

github_issue_history_main = partial(run_intent, HISTORY)


def write_config(project: Path) -> None:
    path = project / ".spectrack" / "config.yml"
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
    path = project / ".spectrack" / "config.yml"
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


def _body_history_graphql_stdout() -> str:
    return json.dumps(
        {
            "data": {
                "repository": {
                    "issue": {
                        "number": 17,
                        "title": "Sample issue",
                        "updatedAt": "2026-07-06T13:36:16Z",
                        "lastEditedAt": "2026-07-06T13:36:16Z",
                        "editor": {"login": "studykit"},
                        "userContentEdits": {
                            "totalCount": 2,
                            "nodes": [
                                {
                                    "editedAt": "2026-07-06T13:36:16Z",
                                    "editor": {"login": "studykit"},
                                    "deletedAt": None,
                                    "diff": "New body snapshot.",
                                },
                                {
                                    "editedAt": "2026-06-30T16:50:47Z",
                                    "editor": {"login": "studykit"},
                                    "deletedAt": None,
                                    "diff": "Original body snapshot.",
                                },
                            ],
                        },
                    }
                }
            }
        }
    )


def _comment_history_graphql_stdout() -> str:
    return json.dumps(
        {
            "data": {
                "node": {
                    "createdAt": "2026-07-05T21:05:24Z",
                    "author": {"login": "studykit"},
                    "lastEditedAt": "2026-07-06T09:00:00Z",
                    "editor": {"login": "studykit"},
                    "userContentEdits": {
                        "totalCount": 1,
                        "nodes": [
                            {
                                "editedAt": "2026-07-06T09:00:00Z",
                                "editor": {"login": "studykit"},
                                "deletedAt": None,
                                "diff": "Edited comment snapshot.",
                            }
                        ],
                    },
                }
            }
        }
    )


def test_history_emits_body_edit_snapshots(tmp_path: Path) -> None:
    write_config(tmp_path)

    def runner(request: CommandRequest) -> CommandResult:
        if request.args[:3] == ("gh", "api", "graphql") and "owner=studykit" in request.args:
            return CommandResult(request=request, returncode=0, stdout=_body_history_graphql_stdout())
        return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")

    stdout = io.StringIO()
    code = github_issue_history_main(
        ["--project", str(tmp_path), "#17"],
        stdout=stdout,
        runner=runner,
    )
    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["target"] == "body"
    assert payload["issue"] == "17"
    assert payload["title"] == "Sample issue"
    assert payload["last_editor"] == "studykit"
    assert payload["edit_count"] == 2
    assert payload["truncated"] is False
    assert [edit["body"] for edit in payload["edits"]] == [
        "New body snapshot.",
        "Original body snapshot.",
    ]


def test_history_comment_flag_resolves_node_and_emits_comment_history(tmp_path: Path) -> None:
    write_config(tmp_path)
    comment_rest_args = ("gh", "api", "repos/studykit/studykit-plugins/issues/comments/4887589235")

    def runner(request: CommandRequest) -> CommandResult:
        if request.args == comment_rest_args:
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"id": 4887589235, "node_id": "IC_node123"}),
            )
        if request.args[:3] == ("gh", "api", "graphql") and "id=IC_node123" in request.args:
            return CommandResult(request=request, returncode=0, stdout=_comment_history_graphql_stdout())
        return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")

    stdout = io.StringIO()
    code = github_issue_history_main(
        ["--project", str(tmp_path), "--comment", "4887589235", "#18"],
        stdout=stdout,
        runner=runner,
    )
    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["target"] == "comment"
    assert payload["issue"] == "18"
    assert payload["comment_id"] == "4887589235"
    assert payload["author"] == "studykit"
    assert payload["edit_count"] == 1
    assert payload["edits"][0]["body"] == "Edited comment snapshot."


def test_history_refuses_jira_provider(tmp_path: Path) -> None:
    write_jira_config(tmp_path)

    def runner(request: CommandRequest) -> CommandResult:
        raise AssertionError(f"unexpected command for unsupported provider: {request.args}")

    stderr = io.StringIO()
    code = github_issue_history_main(
        ["--project", str(tmp_path), "TEST-1234"],
        stdout=io.StringIO(),
        stderr=stderr,
        runner=runner,
    )
    assert code == 2
    assert "does not support" in stderr.getvalue()


def test_history_payload_flags_truncated_edit_history() -> None:
    provider_payload = {
        "body_edit_history": {
            "title": "Long-lived issue",
            "lastEditedAt": "2026-07-06T13:36:16Z",
            "editor": {"login": "studykit"},
            "userContentEdits": {
                "totalCount": 25,
                "nodes": [
                    {
                        "editedAt": "2026-07-06T13:36:16Z",
                        "editor": {"login": "studykit"},
                        "deletedAt": None,
                        "diff": "Snapshot.",
                    }
                ],
            },
        }
    }
    payload = _history_payload(provider_payload, issue="17")
    assert payload["edit_count"] == 25
    assert payload["truncated"] is True
    assert len(payload["edits"]) == 1
