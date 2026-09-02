"""Tests for the agent-facing ``issue search`` entrypoint.

Search is a read-only, no-cache operation: it runs the configured
backend's native query (GitHub search syntax / Jira JQL) and prints a
lightweight ref list the caller feeds back to ``issue fetch``. These
tests pin the routing seam, the per-backend native command shape, and the
shared output envelope.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from functools import partial  # noqa: E402

from command import CommandRequest, CommandResult  # noqa: E402
from config import load_workflow_config  # noqa: E402
from issue.dispatch import SEARCH, run_intent  # noqa: E402
from issue.github.gh import SEARCH_ISSUE_FIELDS  # noqa: E402
from issue.jira.client import (  # noqa: E402
    jira_data_center_search_path,
    jira_data_center_site_from_provider_config,
)
from issue.jira.provider import JIRA_SEARCH_FIELDS  # noqa: E402

issue_search_main = partial(run_intent, SEARCH)


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


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


def gh_search_args(query: str, *, limit: int = 30) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "list",
        "--repo",
        "studykit/studykit-plugins",
        "--search",
        query,
        "--state",
        "all",
        "--json",
        ",".join(SEARCH_ISSUE_FIELDS),
        "--limit",
        str(limit),
    )


def jira_search_args(project: Path, jql: str, *, max_results: int = 30) -> tuple[str, ...]:
    config = load_workflow_config(project)
    assert config is not None
    site = jira_data_center_site_from_provider_config(config.issues)
    path = jira_data_center_search_path(
        site, jql=jql, max_results=max_results, fields=JIRA_SEARCH_FIELDS
    )
    url = f"{site.base_url}{path}"
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


# ---------------------------------------------------------------------------
# GitHub
# ---------------------------------------------------------------------------


def test_github_search_returns_lightweight_ref_list(tmp_path: Path) -> None:
    write_config(tmp_path)
    query = "is:open label:bug"
    remote = json.dumps(
        [
            {
                "number": 12,
                "title": "Fix the crash",
                "state": "OPEN",
                "assignees": [{"login": "alice"}],
                "url": "https://github.com/studykit/studykit-plugins/issues/12",
            },
            {
                "number": 7,
                "title": "Old bug",
                "state": "CLOSED",
                "assignees": [],
                "url": "https://github.com/studykit/studykit-plugins/issues/7",
            },
        ]
    )
    runner = FakeRunner({gh_search_args(query): result(gh_search_args(query), stdout=remote)})
    stdout = io.StringIO()

    code = issue_search_main(
        ["--project", str(tmp_path), query],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["kind"] == "github"
    assert payload["query"] == query
    assert payload["count"] == 2
    assert payload["issues"][0] == {
        "issue": "12",
        "title": "Fix the crash",
        "state": "OPEN",
        "assignees": ["alice"],
        "url": "https://github.com/studykit/studykit-plugins/issues/12",
    }
    assert payload["issues"][1]["issue"] == "7"
    assert payload["issues"][1]["assignees"] == []
    assert [request.args for request in runner.requests] == [gh_search_args(query)]


def test_github_search_passes_limit_through(tmp_path: Path) -> None:
    write_config(tmp_path)
    query = "sort:updated-desc"
    runner = FakeRunner({gh_search_args(query, limit=5): result(gh_search_args(query, limit=5), stdout="[]")})
    stdout = io.StringIO()

    code = issue_search_main(
        ["--project", str(tmp_path), "--limit", "5", query],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["count"] == 0
    assert payload["issues"] == []
    assert [request.args for request in runner.requests] == [gh_search_args(query, limit=5)]


def test_search_rejects_non_positive_limit(tmp_path: Path) -> None:
    write_config(tmp_path)
    runner = FakeRunner({})
    stderr = io.StringIO()

    code = issue_search_main(
        ["--project", str(tmp_path), "--limit", "0", "anything"],
        stdout=io.StringIO(),
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "limit must be positive" in stderr.getvalue()
    # The bad limit is rejected before any provider command runs.
    assert runner.requests == []


# ---------------------------------------------------------------------------
# Jira
# ---------------------------------------------------------------------------


def test_jira_search_returns_lightweight_ref_list(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    jql = "project = TEST AND status = \"In Progress\""
    remote = json.dumps(
        {
            "issues": [
                {
                    "key": "TEST-1",
                    "fields": {
                        "summary": "Do the thing",
                        "status": {"name": "In Progress"},
                        "assignee": {"name": "bob", "displayName": "Bob B"},
                    },
                }
            ]
        }
    )
    args = jira_search_args(tmp_path, jql)
    runner = FakeRunner({args: result(args, stdout=remote)})
    stdout = io.StringIO()

    code = issue_search_main(
        ["--project", str(tmp_path), jql],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["kind"] == "jira"
    assert payload["query"] == jql
    assert payload["count"] == 1
    assert payload["issues"][0] == {
        "issue": "TEST-1",
        "title": "Do the thing",
        "state": "IN PROGRESS",
        "assignees": ["bob"],
        "url": "https://jira.example.test/browse/TEST-1",
    }
    assert [request.args for request in runner.requests] == [args]


def test_jira_search_handles_empty_results(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    jql = "project = TEST"
    args = jira_search_args(tmp_path, jql)
    runner = FakeRunner({args: result(args, stdout=json.dumps({"issues": []}))})
    stdout = io.StringIO()

    code = issue_search_main(
        ["--project", str(tmp_path), jql],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["count"] == 0
    assert payload["issues"] == []
