"""Tests for provider-owned issue publish CLIs."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from github_issue_drafts import main as github_issue_drafts_main  # noqa: E402
from jira_issue_drafts import main as jira_issue_drafts_main  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_github_issue_cache import GitHubIssueCache  # noqa: E402
from workflow_github import DEFAULT_ISSUE_FIELDS  # noqa: E402
from workflow_github import GitHubRepository  # noqa: E402
from workflow_jira_data_center_client import resolve_jira_data_center_site  # noqa: E402
from workflow_jira_issue_cache import JiraDataCenterIssueCache  # noqa: E402


class GitHubFakeRunner:
    def __init__(self) -> None:
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args[:3] == ("gh", "issue", "create"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout="https://github.com/studykit/studykit-plugins/issues/51\n",
            )
        if request.args == _gh_issue_view_args(51, "title,body,labels,state,stateReason"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "title": "Draft issue",
                        "body": "Draft body.\n",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                        "state": "OPEN",
                        "stateReason": None,
                    }
                ),
            )
        if request.args == _gh_issue_view_args(51, ",".join(DEFAULT_ISSUE_FIELDS)):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps(
                    {
                        "number": 51,
                        "title": "Draft issue",
                        "state": "OPEN",
                        "stateReason": None,
                        "body": "Draft body.\n",
                        "labels": [{"name": "task"}, {"name": "workflow"}],
                        "comments": [],
                        "url": "https://github.com/studykit/studykit-plugins/issues/51",
                        "createdAt": "2026-05-14T00:00:00Z",
                        "updatedAt": "2026-05-14T00:00:00Z",
                        "closedAt": None,
                    }
                ),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/51"):
            return CommandResult(
                request=request,
                returncode=0,
                stdout=json.dumps({"id": 5100, "number": 51, "updated_at": "2026-05-14T00:00:00Z"}),
            )
        if request.args == _gh_api_args("repos/studykit/studykit-plugins/issues/51/parent"):
            return CommandResult(request=request, returncode=404, stderr="not found")
        if request.args in {
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/sub_issues", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/dependencies/blocked_by", "--paginate"),
            _gh_api_args("repos/studykit/studykit-plugins/issues/51/dependencies/blocking", "--paginate"),
        }:
            return CommandResult(request=request, returncode=0, stdout="[]")
        return CommandResult(request=request, returncode=127, stderr="unexpected command")


def _write_config(project: Path) -> None:
    config_path = project / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
    path: wiki/workflow
issue_id_format: github
local_projection:
  mode: none
commit_refs:
  enabled: true
  style: provider-native
""".lstrip(),
        encoding="utf-8",
    )


def _write_jira_config(project: Path) -> None:
    config_path = project / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
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


def _repo() -> GitHubRepository:
    return GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")


def _gh_issue_view_args(issue: int | str, fields: str) -> tuple[str, ...]:
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


def _gh_api_args(*args: str) -> tuple[str, ...]:
    return ("gh", "api", *args)


def _write_body_file(project: Path, body: str, *, name: str = "draft.md") -> Path:
    path = project / name
    path.write_text(body, encoding="utf-8")
    return path


def test_github_publish_creates_issue_and_deletes_body_file(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--label",
            "workflow",
            "--body-file",
            str(body_file),
            "--confirm-provider-create",
            "--json",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["operation"] == "publish_issue"
    assert payload["issue"] == "51"
    assert payload["body_file_removed"] is True
    assert payload["cache_refreshed"] is True
    assert payload["issue_file"].endswith("/issues/51/issue.md")
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=_repo())
    assert cache.read_issue(_repo(), 51)["body"] == "Draft body.\n"
    assert not body_file.exists()
    assert runner.requests[0].args[:3] == ("gh", "issue", "create")


def test_github_publish_requires_provider_create_confirmation(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Draft body.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
            "--json",
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert stdout.getvalue() == ""
    assert "--confirm-provider-create" in stderr.getvalue()
    assert body_file.exists()
    assert runner.requests == []


def test_github_publish_rejects_body_file_with_frontmatter(tmp_path: Path) -> None:
    _write_config(tmp_path)
    body_file = _write_body_file(tmp_path, "---\ntitle: nope\n---\n\nBody.\n")
    runner = GitHubFakeRunner()
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(body_file),
            "--confirm-provider-create",
            "--json",
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "frontmatter" in stderr.getvalue()
    assert body_file.exists()
    assert runner.requests == []


def test_github_publish_missing_body_file_fails(tmp_path: Path) -> None:
    _write_config(tmp_path)
    runner = GitHubFakeRunner()
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = github_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Draft issue",
            "--body-file",
            str(tmp_path / "missing.md"),
            "--confirm-provider-create",
            "--json",
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert "body file does not exist" in stderr.getvalue()
    assert runner.requests == []


class JiraFakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]) -> None:
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        for key, value in self.responses.items():
            if request.args == key:
                return CommandResult(
                    request=request,
                    returncode=value.returncode,
                    stdout=value.stdout,
                    stderr=value.stderr,
                )
        return CommandResult(request=request, returncode=127, stderr=f"unexpected: {request.args}")


def _jira_curl_get_args(url: str) -> tuple[str, ...]:
    return (
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--request",
        "GET",
        "--config",
        "-",
        url,
    )


def _jira_write_args() -> tuple[str, ...]:
    return (
        "curl",
        "--silent",
        "--show-error",
        "--fail",
        "--config",
        "-",
    )


def _jira_issue_payload(key: str = "TEST-1234") -> dict[str, object]:
    return {
        "id": "10001",
        "key": key,
        "fields": {
            "summary": "Published Jira issue",
            "description": "Body.\n",
            "labels": ["workflow"],
            "status": {"name": "Open"},
            "issuetype": {"name": "Task"},
            "created": "2026-05-14T00:00:00.000+0000",
            "updated": "2026-05-14T00:00:00.000+0000",
        },
    }


def test_jira_publish_creates_issue_inline_and_deletes_body_file(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    site = resolve_jira_data_center_site(tmp_path)
    issue_url = "https://jira.example.test/rest/api/2/issue/TEST-1234"
    remote_links_url = "https://jira.example.test/rest/api/2/issue/TEST-1234/remotelink"

    runner = JiraFakeRunner(
        {
            _jira_write_args(): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps({"id": "10001", "key": "TEST-1234"}),
            ),
            _jira_curl_get_args(issue_url): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps(_jira_issue_payload()),
            ),
            _jira_curl_get_args(remote_links_url): CommandResult(
                request=CommandRequest(args=()),
                returncode=0,
                stdout=json.dumps([]),
            ),
        }
    )
    stdout = io.StringIO()

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--label",
            "workflow",
            "--body-file",
            str(body_file),
            "--confirm-provider-create",
            "--json",
        ],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["operation"] == "publish_issue"
    assert payload["issue"] == "TEST-1234"
    assert payload["body_file_removed"] is True
    assert payload["issue_file"].endswith("issues/TEST-1234/snapshot.md")
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    assert cache.issue_json_file(site, "TEST-1234").is_file()
    assert not body_file.exists()
    assert runner.requests[0].args == _jira_write_args()


def test_jira_publish_requires_provider_create_confirmation(tmp_path: Path) -> None:
    _write_jira_config(tmp_path)
    body_file = _write_body_file(tmp_path, "Body.\n")
    runner = JiraFakeRunner({})
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = jira_issue_drafts_main(
        [
            "--project",
            str(tmp_path),
            "publish",
            "--type",
            "task",
            "--title",
            "Published Jira issue",
            "--body-file",
            str(body_file),
            "--json",
        ],
        stdout=stdout,
        stderr=stderr,
        runner=runner,
    )

    assert code == 2
    assert stdout.getvalue() == ""
    assert "--confirm-provider-create" in stderr.getvalue()
    assert body_file.exists()
    assert runner.requests == []
