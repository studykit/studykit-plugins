"""Tests for the agent-facing workflow cache fetch entrypoint."""

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

from issue.dispatch import FETCH, run_intent  # noqa: E402

github_issue_fetch_main = partial(run_intent, FETCH)
jira_issue_fetch_main = partial(run_intent, FETCH)
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_config import load_workflow_config  # noqa: E402
from issue.github.cache import GitHubIssueCache  # noqa: E402
from workflow_github import DEFAULT_ISSUE_FIELDS, GitHubRepository  # noqa: E402
from issue.github.refs import issue_numbers_from_references  # noqa: E402
from issue.jira.cache import JiraDataCenterIssueCache  # noqa: E402
from workflow_jira_data_center_client import jira_data_center_site_from_provider_config  # noqa: E402
from issue.jira.refs import jira_issue_keys_from_references  # noqa: E402


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


def repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def issue_payload(number: int, *, body: str = "Issue body.") -> dict[str, object]:
    return {
        "number": number,
        "title": f"Issue {number}",
        "state": "OPEN",
        "stateReason": None,
        "body": body,
        "labels": [{"name": "task"}],
        "updatedAt": "2026-05-14T00:00:00Z",
        "comments": [],
    }


def gh_issue_view_args(issue: int | str) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        ",".join(DEFAULT_ISSUE_FIELDS),
    )


def gh_api_args(path: str, *, paginate: bool = False) -> tuple[str, ...]:
    args = ("gh", "api", path)
    if paginate:
        return (*args, "--paginate")
    return args


def relationship_responses(
    issue: int | str,
    *,
    updated_at: str = "2026-05-14T00:00:00Z",
) -> dict[tuple[str, ...], CommandResult]:
    issue_path = f"repos/studykit/studykit-plugins/issues/{issue}"
    return {
        gh_api_args(issue_path): result(
            gh_api_args(issue_path),
            stdout=json.dumps({"number": int(issue), "updated_at": updated_at}),
        ),
        gh_api_args(f"{issue_path}/parent"): result(
            gh_api_args(f"{issue_path}/parent"),
            stdout=json.dumps({"number": 40, "title": "Parent", "state": "open"}),
        ),
        gh_api_args(f"{issue_path}/sub_issues", paginate=True): result(
            gh_api_args(f"{issue_path}/sub_issues", paginate=True),
            stdout=json.dumps([{"number": 43, "title": "Child", "state": "closed"}]),
        ),
        gh_api_args(f"{issue_path}/dependencies/blocked_by", paginate=True): result(
            gh_api_args(f"{issue_path}/dependencies/blocked_by", paginate=True),
            stdout=json.dumps([{"number": 41, "title": "Blocker", "state": "closed"}]),
        ),
        gh_api_args(f"{issue_path}/dependencies/blocking", paginate=True): result(
            gh_api_args(f"{issue_path}/dependencies/blocking", paginate=True),
            stdout="[]",
        ),
    }


def write_config(project: Path) -> None:
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


def jira_site(project: Path):
    config = load_workflow_config(project)
    assert config is not None
    return jira_data_center_site_from_provider_config(config.issues)


def jira_issue_payload(*, body: str = "Data Center description.") -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "Support Jira Data Center",
            "description": body,
            "labels": ["workflow", "jira"],
            "created": "2026-05-15T09:00:00.000+0900",
            "updated": "2026-05-15T10:00:00.000+0900",
            "status": {
                "name": "In Progress",
                "statusCategory": {"key": "indeterminate"},
            },
            "comment": {"comments": []},
            "parent": {
                "id": "9999",
                "key": "TEST-1200",
                "fields": {"summary": "Parent task", "status": {"name": "Open"}},
            },
            "subtasks": [
                {
                    "id": "10005",
                    "key": "TEST-1237",
                    "fields": {"summary": "Subtask", "status": {"name": "To Do"}},
                }
            ],
            "issuelinks": [
                {
                    "id": "30001",
                    "type": {"name": "Blocks", "outward": "blocks", "inward": "is blocked by"},
                    "outwardIssue": {
                        "id": "10002",
                        "key": "TEST-1235",
                        "fields": {"summary": "Follow-up", "status": {"name": "Open"}},
                    },
                },
                {
                    "id": "30002",
                    "type": {"name": "Blocks", "outward": "blocks", "inward": "is blocked by"},
                    "inwardIssue": {
                        "id": "10003",
                        "key": "TEST-1233",
                        "fields": {"summary": "Blocking predecessor", "status": {"name": "In Progress"}},
                    },
                },
            ],
        },
    }


def remote_links_payload() -> list[dict[str, object]]:
    return [
        {
            "id": 1,
            "relationship": "mentioned in",
            "object": {"title": "Design note", "url": "https://example.com/design"},
        }
    ]


def curl_args(url: str) -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


def jira_issue_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}"


def jira_remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def test_issue_numbers_from_references_accepts_agent_shell_inputs() -> None:
    references = [
        "42",
        "#43",
        "studykit/studykit-plugins#44",
        "https://github.com/studykit/studykit-plugins/issues/45",
        "other/repo#46",
        "42",
    ]

    assert issue_numbers_from_references(references, repo=repo()) == ["42", "43", "44", "45"]


def test_issue_numbers_from_references_accepts_jira_keys() -> None:
    references = [
        "test-1234",
        "Work on TEST-1235 and test-1234.",
        "#42",
        "https://github.com/studykit/studykit-plugins/issues/43",
    ]

    assert jira_issue_keys_from_references(references) == ["TEST-1234", "TEST-1235"]


def test_cache_fetch_uses_cache_hit_without_remote_issue_view(tmp_path: Path) -> None:
    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload(42, body="Cached body."))
    runner = FakeRunner({})
    stdout = io.StringIO()

    code = github_issue_fetch_main(
        ["--project", str(tmp_path), "42"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert set(payload) == {"basedir", "issues"}
    assert payload["basedir"] == ".workflow-cache/issues/"
    # The payload has no relationships, so relation.md is never written and the
    # fetch entry omits the relationships key entirely.
    assert set(payload["issues"][0]) == {
        "issue",
        "title",
        "state",
        "cache_refreshed",
    }
    assert payload["issues"][0]["issue"] == "42/issue.md"
    assert "relationships" not in payload["issues"][0]
    assert payload["issues"][0]["cache_refreshed"] is False
    assert runner.requests == []


def issue_payload_with_comment(
    number: int,
    *,
    comment_id: str = "4440388606",
    comment_created_at: str = "2026-05-13T11:20:53Z",
) -> dict[str, object]:
    payload = issue_payload(number, body="Cached body.")
    payload["comments"] = [
        {
            "id": "IC_node",
            "url": f"https://github.com/studykit/studykit-plugins/issues/{number}#issuecomment-{comment_id}",
            "author": {"login": "studykit"},
            "body": "Comment body.",
            "createdAt": comment_created_at,
            "updatedAt": comment_created_at,
        }
    ]
    return payload


def test_cache_fetch_lists_comment_paths_in_json(tmp_path: Path) -> None:
    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload_with_comment(42))
    stdout = io.StringIO()

    code = github_issue_fetch_main(
        ["--project", str(tmp_path), "42"],
        stdout=stdout,
        runner=FakeRunner({}),
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["issues"][0]["comments"] == [
        "42/comment-2026-05-13T112053Z-4440388606.md",
    ]


def test_cache_fetch_omits_comments_key_when_no_cached_comments(tmp_path: Path) -> None:
    write_config(tmp_path)
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo())
    cache.write_issue_bundle(repo(), issue_payload(42, body="Cached body."))
    stdout = io.StringIO()

    code = github_issue_fetch_main(
        ["--project", str(tmp_path), "42"],
        stdout=stdout,
        runner=FakeRunner({}),
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert "comments" not in payload["issues"][0]


def test_cache_fetch_refresh_reads_remote_and_updates_cache(tmp_path: Path) -> None:
    write_config(tmp_path)
    remote = issue_payload(42, body="Fresh body.")
    runner = FakeRunner(
        {
            gh_issue_view_args(42): result(gh_issue_view_args(42), stdout=json.dumps(remote)),
            **relationship_responses(42),
        }
    )
    stdout = io.StringIO()

    code = github_issue_fetch_main(
        ["--project", str(tmp_path), "--cache-policy", "refresh", "42"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["basedir"] == ".workflow-cache/issues/"
    assert payload["issues"][0]["cache_refreshed"] is True
    assert [request.args for request in runner.requests] == [
        gh_issue_view_args(42),
        gh_api_args("repos/studykit/studykit-plugins/issues/42"),
        gh_api_args("repos/studykit/studykit-plugins/issues/42/parent"),
        gh_api_args("repos/studykit/studykit-plugins/issues/42/sub_issues", paginate=True),
        gh_api_args("repos/studykit/studykit-plugins/issues/42/dependencies/blocked_by", paginate=True),
        gh_api_args("repos/studykit/studykit-plugins/issues/42/dependencies/blocking", paginate=True),
    ]
    cached = GitHubIssueCache.for_project(tmp_path, configured_repo=repo()).read_issue(repo(), 42)
    assert cached["body"] == "Fresh body."
    relationships = GitHubIssueCache.for_project(tmp_path, configured_repo=repo()).read_relationships(repo(), 42)
    assert relationships["parent"]["number"] == 40
    assert relationships["children"][0]["number"] == 43
    assert relationships["blocked_by"][0]["number"] == 41
    assert payload["issues"][0]["relationships"] == "42/relation.md"


def test_cache_fetch_uses_jira_cache_hit_without_remote_read(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(body="Cached Jira body."),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T01:00:00Z",
    )
    runner = FakeRunner({})
    stdout = io.StringIO()

    code = jira_issue_fetch_main(
        ["--project", str(tmp_path), "test-1234"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert set(payload) == {"basedir", "issues"}
    assert payload["basedir"] == ".workflow-cache/issues/"
    assert payload["issues"][0]["issue"] == "TEST-1234/issue.md"
    assert payload["issues"][0]["cache_refreshed"] is False
    assert payload["issues"][0]["relationships"] == "TEST-1234/relation.md"
    assert runner.requests == []


def test_cache_fetch_refresh_reads_remote_jira_and_updates_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()),
                stdout=json.dumps(jira_issue_payload(body="Fresh Jira body.")),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_fetch_main(
        ["--project", str(tmp_path), "--cache-policy", "refresh", "TEST-1234"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["basedir"] == ".workflow-cache/issues/"
    assert payload["issues"][0]["issue"] == "TEST-1234/issue.md"
    assert payload["issues"][0]["cache_refreshed"] is True
    assert [request.args for request in runner.requests] == [
        curl_args(jira_issue_url()),
        curl_args(jira_remote_links_url()),
    ]
    cached = JiraDataCenterIssueCache.for_project(tmp_path).read_issue(jira_site(tmp_path), "TEST-1234")
    assert cached["body"] == "Fresh Jira body."
