"""Tests for the agent-facing workflow pending comment append entrypoint."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from jira_issue_comments import main as jira_issue_comments_main  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_config import load_workflow_config  # noqa: E402
from workflow_jira_issue_cache import JiraDataCenterIssueCache  # noqa: E402
from workflow_jira_data_center_client import jira_data_center_site_from_provider_config  # noqa: E402


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
            "status": {"name": "In Progress", "statusCategory": {"key": "indeterminate"}},
            "comment": {"comments": []},
            "issuelinks": [],
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


def curl_write_args() -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--config", "-")


def jira_issue_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}"


def jira_remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def test_cache_comments_script_dispatches_jira_pending_comment_append(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    pending_dir = cache.comments_pending_dir(site, "TEST-1234")
    pending_dir.mkdir(parents=True)
    pending_file = pending_dir / "001.md"
    pending_file.write_text("---\nschema_version: 1\n---\n\nPending Jira comment body.\n", encoding="utf-8")
    responses: dict[tuple[str, ...], CommandResult | list[CommandResult]] = {
        curl_args(jira_issue_url()): [
            CommandResult(request=CommandRequest(args=curl_args(jira_issue_url())), returncode=0, stdout=json.dumps(jira_issue_payload())),
            CommandResult(request=CommandRequest(args=curl_args(jira_issue_url())), returncode=0, stdout=json.dumps(jira_issue_payload())),
        ],
        curl_write_args(): CommandResult(
            request=CommandRequest(args=curl_write_args()),
            returncode=0,
            stdout=json.dumps({"id": "30001", "body": "Pending Jira comment body."}),
        ),
        curl_args(jira_remote_links_url()): CommandResult(
            request=CommandRequest(args=curl_args(jira_remote_links_url())),
            returncode=0,
            stdout=json.dumps(remote_links_payload()),
        ),
    }
    runner_requests: list[CommandRequest] = []

    def runner(request: CommandRequest) -> CommandResult:
        runner_requests.append(request)
        response = responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        if isinstance(response, list):
            if not response:
                return CommandResult(request=request, returncode=127, stderr="unexpected command")
            return response.pop(0)
        return response

    stdout = io.StringIO()

    code = jira_issue_comments_main(
        ["--project", str(tmp_path), "--type", "task", "--json", "test-1234"],
        stdout=stdout,
        runner=runner,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["operation"] == "cache_append_pending_comments"
    assert payload["kind"] == "jira"
    assert "repository" not in payload
    assert payload["issues"][0]["operation"] == "append_pending_comments"
    assert payload["issues"][0]["issue"] == "TEST-1234"
    assert payload["issues"][0]["appended"] == 1
    assert not pending_file.exists()
    write_request = runner_requests[1]
    assert write_request.args == curl_write_args()
    assert 'request = "POST"' in str(write_request.input_text)
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234/comment"' in str(write_request.input_text)
    assert '\\"body\\":\\"Pending Jira comment body.\\\\n\\"' in str(write_request.input_text)
