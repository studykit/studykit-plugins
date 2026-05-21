"""Tests for Jira Data Center workflow provider reads and cache."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_jira_issue_cache import JiraDataCenterIssueCache  # noqa: E402
from workflow_jira_data_center_client import jira_data_center_site_from_provider_config  # noqa: E402
from workflow_providers import (  # noqa: E402
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_REFRESH,
    ProviderContext,
    ProviderDispatcher,
    ProviderOperationError,
    ProviderRequest,
    default_provider_registry,
)
from workflow_config import load_workflow_config  # noqa: E402


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult | list[CommandResult]]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        if isinstance(response, list):
            if not response:
                return CommandResult(request=request, returncode=127, stderr="unexpected command")
            return response.pop(0)
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def curl_args(url: str) -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


def curl_write_args() -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--config", "-")


def write_jira_config(
    project: Path,
    *,
    deployment: str = "data-center",
    snapshot_settings: str = "",
    relationship_mappings: str = "",
) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
            f"""
version: 1
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: {deployment}
    api_version: 2
    project: TEST
    issue_type: Task
"""
            + snapshot_settings
            + relationship_mappings
            + """
  knowledge:
    kind: github
issue_id_format: jira
"""
        ).lstrip(),
        encoding="utf-8",
    )


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
            "comment": {
                "comments": [
                    {
                        "id": "20001",
                        "author": {"displayName": "Example User", "name": "example"},
                        "body": "Please keep Data Center first.",
                        "created": "2026-05-15T09:30:00.000+0900",
                        "updated": "2026-05-15T09:30:00.000+0900",
                    }
                ]
            },
            "issuelinks": [
                {
                    "id": "30001",
                    "type": {"name": "Blocks", "outward": "blocks", "inward": "is blocked by"},
                    "outwardIssue": {
                        "id": "10002",
                        "key": "TEST-1235",
                        "fields": {
                            "summary": "Follow-up",
                            "status": {"name": "Open"},
                        },
                    },
                },
                {
                    "id": "30002",
                    "type": {"name": "Blocks", "outward": "blocks", "inward": "is blocked by"},
                    "inwardIssue": {
                        "id": "10003",
                        "key": "TEST-1233",
                        "fields": {
                            "summary": "Blocking predecessor",
                            "status": {"name": "In Progress"},
                        },
                    },
                },
                {
                    "id": "30003",
                    "type": {"name": "Relates", "outward": "relates to", "inward": "relates to"},
                    "outwardIssue": {
                        "id": "10004",
                        "key": "TEST-1236",
                        "fields": {
                            "summary": "Related issue",
                            "status": {"name": "Open"},
                        },
                    },
                }
            ],
            "parent": {
                "id": "9999",
                "key": "TEST-1200",
                "fields": {
                    "summary": "Parent task",
                    "status": {"name": "Open"},
                },
            },
            "subtasks": [
                {
                    "id": "10005",
                    "key": "TEST-1237",
                    "fields": {
                        "summary": "Subtask",
                        "status": {"name": "To Do"},
                    },
                }
            ],
        },
    }


def jira_subtask_payload() -> dict[str, object]:
    payload = jira_issue_payload(body="Pending body.")
    payload["id"] = "10005"
    payload["key"] = "TEST-1237"
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["summary"] = "Pending Jira sub-task"
    fields["issuetype"] = {"name": "Sub-task"}
    fields["parent"] = {
        "id": "9999",
        "key": "TEST-1200",
        "fields": {
            "summary": "Parent task",
            "status": {"name": "Open"},
        },
    }
    fields["subtasks"] = []
    return payload


def jira_parent_payload() -> dict[str, object]:
    payload = jira_issue_payload(body="Parent body.")
    payload["id"] = "9999"
    payload["key"] = "TEST-1200"
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["summary"] = "Parent task"
    fields["issuetype"] = {"name": "Task"}
    fields.pop("parent", None)
    fields["subtasks"] = [
        {
            "id": "10005",
            "key": "TEST-1237",
            "fields": {
                "summary": "Pending Jira sub-task",
                "status": {"name": "To Do"},
            },
        }
    ]
    return payload


def remote_links_payload() -> list[dict[str, object]]:
    return [
        {
            "id": 1,
            "relationship": "mentioned in",
            "object": {
                "title": "Design note",
                "url": "https://example.com/design",
            },
        }
    ]


def issue_link_relationship_mappings() -> str:
    return """
    relationship_mappings:
      blocked_by:
        surface: issue_link
        link_type: Blocks
        direction: inward
      blocking:
        surface: issue_link
        link_type: Blocks
        direction: outward
      related:
        surface: issue_link
        link_type: Relates
        direction: outward
"""


def remote_link_relationship_mappings() -> str:
    return """
    relationship_mappings:
      related:
        surface: remote_link
        relationship_label: relates to
        application_type: studykit.workflow
        application_name: Workflow
"""


def issue_link_and_field_epic_relationship_mappings(*, value_kind: str = "string") -> str:
    return f"""
    relationship_mappings:
      blocked_by:
        surface: issue_link
        link_type: Blocks
        direction: inward
      blocking:
        surface: issue_link
        link_type: Blocks
        direction: outward
      related:
        surface: issue_link
        link_type: Relates
        direction: outward
      epic:
        surface: field
        field: customfield_10350
        write_to: source
        value: {value_kind}
"""


def issue_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}"


def remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def issue_link_url() -> str:
    return "https://jira.example.test/rest/api/2/issueLink"


def dispatch_get(
    project: Path,
    runner: FakeRunner,
    *,
    cache_policy: str = "default",
    include_remote_links: bool = True,
):
    dispatcher = ProviderDispatcher(default_provider_registry(runner=runner))
    return dispatcher.dispatch(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="get",
            context=ProviderContext(project=project, artifact_type="task", cache_policy=cache_policy),
            payload={"issue": "test-1234", "include_remote_links": include_remote_links},
        )
    )


def dispatch_write(
    project: Path,
    runner: FakeRunner,
    operation: str,
    *,
    artifact_type: str = "task",
    **payload: object,
):
    dispatcher = ProviderDispatcher(default_provider_registry(runner=runner))
    return dispatcher.dispatch(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation=operation,
            context=ProviderContext(project=project, artifact_type=artifact_type),
            payload=payload,
        )
    )


def jira_site(project: Path):
    config = load_workflow_config(project)
    assert config is not None
    return jira_data_center_site_from_provider_config(config.issues)


def _split_issue_md(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        raise AssertionError("issue.md missing YAML frontmatter")
    _opening, frontmatter, body = text.split("---", 2)
    return frontmatter, body


def test_data_center_provider_fetches_issue_remote_links_and_writes_llm_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    monkeypatch.delenv("JIRA_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("JIRA_PAT", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_PASSWORD", raising=False)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert response.payload["key"] == "TEST-1234"
    assert response.payload["title"] == "Support Jira Data Center"
    assert response.payload["body"] == "Data Center description."
    assert response.payload["jira"]["deployment"] == "data_center"
    assert response.payload["relationships"]["remote_links"][0]["url"] == "https://example.com/design"
    workflow = response.payload["relationships"]["workflow"]
    assert workflow["parent"]["key"] == "TEST-1200"
    assert workflow["children"][0]["key"] == "TEST-1237"
    assert workflow["blocking"][0]["key"] == "TEST-1235"
    assert workflow["blocked_by"][0]["key"] == "TEST-1233"
    assert workflow["related"][0]["key"] == "TEST-1236"
    assert "dependencies" not in workflow
    assert "issue_links" not in workflow
    assert workflow["external_links"][0]["url"] == "https://example.com/design"
    assert [request.args for request in runner.requests] == [curl_args(issue_url()), curl_args(remote_links_url())]
    assert all(request.input_text == 'header = "Accept: application/json"\n' for request in runner.requests)

    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_dir = cache.issue_dir(site, "TEST-1234")
    assert issue_dir == tmp_path / ".workflow-cache" / "issues" / "TEST-1234"
    assert (issue_dir / "issue.json").is_file()
    assert (issue_dir / "remote-links.json").is_file()

    issue_md_text = (issue_dir / "issue.md").read_text(encoding="utf-8")
    frontmatter_text, body = _split_issue_md(issue_md_text)
    issue_md_frontmatter = yaml.safe_load(frontmatter_text)
    assert "key" not in issue_md_frontmatter
    assert issue_md_frontmatter["title"] == "Support Jira Data Center"
    assert issue_md_frontmatter["state"] == "In Progress"
    assert issue_md_frontmatter["labels"] == ["workflow", "jira"]
    assert issue_md_frontmatter["remote_links"] == [
        {"title": "Design note", "url": "https://example.com/design", "relationship": "mentioned in"}
    ]
    relationships_block = issue_md_frontmatter["relationships"]
    assert "current" not in relationships_block
    assert "dependencies" not in relationships_block
    assert "issue_links" not in relationships_block
    assert relationships_block["parent"] == "TEST-1200"
    assert relationships_block["children"] == ["TEST-1237"]
    assert relationships_block["blocked_by"] == ["TEST-1233"]
    assert relationships_block["blocking"] == ["TEST-1235"]
    assert relationships_block["related"] == ["TEST-1236"]
    assert body.strip() == "Data Center description."
    assert "Please keep Data Center first." not in issue_md_text
    assert "## Description" not in issue_md_text
    assert "## Comments" not in issue_md_text
    assert "## Remote Links" not in issue_md_text
    assert "## Workflow Relationships" not in issue_md_text
    assert "## Issue Links" not in issue_md_text
    assert not (issue_dir / "metadata.yml").exists()

    comment_files = cache.comment_files(site, "TEST-1234")
    assert [path.name for path in comment_files] == [
        "comment-2026-05-15T093000Z-20001.md",
    ]
    comment_text = comment_files[0].read_text(encoding="utf-8")
    assert "Please keep Data Center first." in comment_text
    assert "provider_comment_id: '20001'" in comment_text
    assert "author: Example User" in comment_text


def _assert_existing_workflow_buckets_unchanged(workflow: dict) -> None:
    assert workflow["parent"]["key"] == "TEST-1200"
    assert workflow["children"][0]["key"] == "TEST-1237"
    assert workflow["blocking"][0]["key"] == "TEST-1235"
    assert workflow["blocked_by"][0]["key"] == "TEST-1233"
    assert workflow["related"][0]["key"] == "TEST-1236"


def test_data_center_field_surface_string_relationship_surfaces_in_workflow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_field_epic_relationship_mappings(value_kind="string"),
    )
    monkeypatch.delenv("JIRA_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("JIRA_PAT", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_PASSWORD", raising=False)
    payload = jira_issue_payload()
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["customfield_10350"] = "TEST-EPIC-1"
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(payload)),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    workflow = response.payload["relationships"]["workflow"]
    assert workflow["epic"] == [{"provider": "jira", "key": "TEST-EPIC-1", "issue": "TEST-EPIC-1"}]
    _assert_existing_workflow_buckets_unchanged(workflow)

    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_md_text = (cache.issue_dir(site, "TEST-1234") / "issue.md").read_text(encoding="utf-8")
    frontmatter_text, _body = _split_issue_md(issue_md_text)
    frontmatter = yaml.safe_load(frontmatter_text)
    relationships_block = frontmatter["relationships"]
    assert relationships_block["epic"] == ["TEST-EPIC-1"]
    assert relationships_block["parent"] == "TEST-1200"
    assert relationships_block["children"] == ["TEST-1237"]
    assert relationships_block["blocked_by"] == ["TEST-1233"]
    assert relationships_block["blocking"] == ["TEST-1235"]
    assert relationships_block["related"] == ["TEST-1236"]


def test_data_center_field_surface_key_object_relationship_surfaces_in_workflow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_field_epic_relationship_mappings(value_kind="key_object"),
    )
    monkeypatch.delenv("JIRA_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("JIRA_PAT", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_PASSWORD", raising=False)
    payload = jira_issue_payload()
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields["customfield_10350"] = {"key": "TEST-EPIC-1"}
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(payload)),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    workflow = response.payload["relationships"]["workflow"]
    assert workflow["epic"] == [{"provider": "jira", "key": "TEST-EPIC-1", "issue": "TEST-EPIC-1"}]
    _assert_existing_workflow_buckets_unchanged(workflow)

    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_md_text = (cache.issue_dir(site, "TEST-1234") / "issue.md").read_text(encoding="utf-8")
    frontmatter_text, _body = _split_issue_md(issue_md_text)
    frontmatter = yaml.safe_load(frontmatter_text)
    assert frontmatter["relationships"]["epic"] == ["TEST-EPIC-1"]


def test_data_center_field_surface_absent_field_is_omitted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_field_epic_relationship_mappings(value_kind="string"),
    )
    monkeypatch.delenv("JIRA_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("JIRA_PAT", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_PASSWORD", raising=False)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    workflow = response.payload["relationships"]["workflow"]
    assert "epic" not in workflow
    _assert_existing_workflow_buckets_unchanged(workflow)

    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_md_text = (cache.issue_dir(site, "TEST-1234") / "issue.md").read_text(encoding="utf-8")
    frontmatter_text, _body = _split_issue_md(issue_md_text)
    frontmatter = yaml.safe_load(frontmatter_text)
    assert "epic" not in frontmatter["relationships"]


def test_data_center_snapshot_hides_comments_with_configured_markers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        snapshot_settings="""
    snapshot:
      hidden_comment_markers:
        - "!git-event"
""",
    )
    monkeypatch.delenv("JIRA_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("JIRA_PAT", raising=False)
    monkeypatch.delenv("JIRA_USERNAME", raising=False)
    monkeypatch.delenv("JIRA_PASSWORD", raising=False)
    payload = jira_issue_payload()
    comments = payload["fields"]["comment"]["comments"]  # type: ignore[index]
    comments.append(  # type: ignore[attr-defined]
        {
            "id": "20002",
            "author": {"displayName": "Automation", "name": "automation"},
            "body": "!git-event pushed commit abc123",
            "created": "2026-05-15T09:40:00.000+0900",
            "updated": "2026-05-15T09:40:00.000+0900",
        }
    )
    comments.append(  # type: ignore[attr-defined]
        {
            "id": "20003",
            "author": {"displayName": "Human User", "name": "human"},
            "body": "Human follow-up remains visible.",
            "created": "2026-05-15T09:45:00.000+0900",
            "updated": "2026-05-15T09:45:00.000+0900",
        }
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(payload)),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert any("!git-event" in comment["body"] for comment in response.payload["comments"])
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_dir = cache.issue_dir(site, "TEST-1234")
    assert "!git-event" in (issue_dir / "issue.json").read_text(encoding="utf-8")

    comment_file_names = {path.name for path in cache.comment_files(site, "TEST-1234")}
    assert comment_file_names == {
        "comment-2026-05-15T093000Z-20001.md",
        "comment-2026-05-15T094500Z-20003.md",
    }
    visible_bodies = "\n".join(
        path.read_text(encoding="utf-8") for path in cache.comment_files(site, "TEST-1234")
    )
    assert "Please keep Data Center first." in visible_bodies
    assert "Human follow-up remains visible." in visible_bodies
    assert "!git-event" not in visible_bodies
    assert "pushed commit abc123" not in visible_bodies


def test_default_cache_policy_uses_data_center_cache_hit_without_curl(tmp_path: Path) -> None:
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

    response = dispatch_get(tmp_path, runner)

    assert response.payload["body"] == "Cached Jira body."
    assert response.payload["cache"]["hit"] is True
    assert response.payload["cache"]["issue_file"].endswith("/issue.md")
    assert "issue_json" not in response.payload["cache"]
    assert "remote_links_json" not in response.payload["cache"]
    assert runner.requests == []


def test_refresh_policy_overwrites_data_center_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(site, jira_issue_payload(body="Stale body."), fetched_at="2026-05-15T01:00:00Z")
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(
                curl_args(issue_url()),
                stdout=json.dumps(jira_issue_payload(body="Fresh body.")),
            ),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner, cache_policy=CACHE_POLICY_REFRESH)

    assert response.payload["body"] == "Fresh body."
    cached = cache.read_issue(site, "TEST-1234")
    assert cached["body"] == "Fresh body."


def test_bypass_policy_reads_data_center_without_writing_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner, cache_policy=CACHE_POLICY_BYPASS)

    assert response.payload["body"] == "Data Center description."
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    assert not cache.issue_json_file(jira_site(tmp_path), "TEST-1234").exists()


def test_cloud_deployment_is_rejected_for_now(tmp_path: Path) -> None:
    write_jira_config(tmp_path, deployment="cloud")
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="Jira Cloud is out of scope"):
        dispatch_get(tmp_path, runner)


def test_data_center_create_inline_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        title="Pending Jira issue",
        body="Pending body.\n",
        labels=["workflow"],
    )

    assert response.payload["operation"] == "create_issue"
    assert response.payload["issue"] == "TEST-1234"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    assert 'request = "POST"' in str(write_request.input_text)
    assert 'url = "https://jira.example.test/rest/api/2/issue"' in str(write_request.input_text)
    assert '\\"summary\\":\\"Pending Jira issue\\"' in str(write_request.input_text)
    assert '\\"issuetype\\":{\\"name\\":\\"Task\\"}' in str(write_request.input_text)
    assert '\\"parent\\"' not in str(write_request.input_text)
    assert cache.issue_json_file(site, "TEST-1234").is_file()


def test_data_center_create_with_assignee_carries_assignee_field(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        title="Pending Jira issue",
        body="Pending body.\n",
        assignee="alice",
    )

    assert response.payload["operation"] == "create_issue"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    assert '\\"assignee\\":{\\"name\\":\\"alice\\"}' in str(write_request.input_text)


def test_data_center_create_with_assignee_me_resolves_via_myself_once(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    myself_url = "https://jira.example.test/rest/api/2/myself"
    runner = FakeRunner(
        {
            curl_args(myself_url): result(
                curl_args(myself_url),
                stdout=json.dumps({"name": "studykit-svc", "displayName": "Studykit Service"}),
            ),
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        title="Pending Jira issue",
        body="Pending body.\n",
        assignee="me",
    )

    assert response.payload["operation"] == "create_issue"
    myself_calls = [request for request in runner.requests if request.args == curl_args(myself_url)]
    assert len(myself_calls) == 1
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any(
        '\\"assignee\\":{\\"name\\":\\"studykit-svc\\"}' in str(request.input_text)
        for request in write_requests
    )


def test_data_center_subtask_create_inline_refreshes_parent_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10005", "key": "TEST-1237"})),
            curl_args(issue_url("TEST-1237")): result(
                curl_args(issue_url("TEST-1237")),
                stdout=json.dumps(jira_subtask_payload()),
            ),
            curl_args(remote_links_url("TEST-1237")): result(
                curl_args(remote_links_url("TEST-1237")),
                stdout=json.dumps([]),
            ),
            curl_args(issue_url("TEST-1200")): result(
                curl_args(issue_url("TEST-1200")),
                stdout=json.dumps(jira_parent_payload()),
            ),
            curl_args(remote_links_url("TEST-1200")): result(
                curl_args(remote_links_url("TEST-1200")),
                stdout=json.dumps([]),
            ),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        title="Pending Jira sub-task",
        body="Pending body.\n",
        jira_issue_type="Sub-task",
        subtask_parent_key="TEST-1200",
    )

    assert response.payload["operation"] == "create_issue"
    assert response.payload["issue"] == "TEST-1237"
    assert response.payload["subtask_parent"] == "TEST-1200"
    assert response.payload["parent_cache_refreshed"] is True
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    payload_text = str(write_request.input_text)
    assert '\\"issuetype\\":{\\"name\\":\\"Sub-task\\"}' in payload_text
    assert '\\"parent\\":{\\"key\\":\\"TEST-1200\\"}' in payload_text
    assert [request.args for request in runner.requests[1:]] == [
        curl_args(issue_url("TEST-1237")),
        curl_args(remote_links_url("TEST-1237")),
        curl_args(issue_url("TEST-1200")),
        curl_args(remote_links_url("TEST-1200")),
    ]
    subtask = cache.read_issue_json(site, "TEST-1237")
    subtask_fields = subtask["fields"]
    assert isinstance(subtask_fields, dict)
    assert subtask_fields["parent"]["key"] == "TEST-1200"
    parent = cache.read_issue_json(site, "TEST-1200")
    parent_fields = parent["fields"]
    assert isinstance(parent_fields, dict)
    assert parent_fields["subtasks"][0]["key"] == "TEST-1237"


def test_data_center_review_create_uses_task_type_and_review_summary_prefix(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="review",
        title="Clarify target",
        body="## Description\n\nClarify the target.",
        issue_type="Bug",
    )

    assert response.payload["operation"] == "create_issue"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    payload_text = str(write_request.input_text)
    assert '\\"summary\\":\\"[Review] Clarify target\\"' in payload_text
    assert '\\"issuetype\\":{\\"name\\":\\"Task\\"}' in payload_text


def test_data_center_spike_create_uses_task_type_and_spike_summary_prefix(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="spike",
        title="Probe Jira issue type",
        body="## Description\n\nProbe the Jira issue type.",
        issue_type="Bug",
    )

    assert response.payload["operation"] == "create_issue"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    payload_text = str(write_request.input_text)
    assert '\\"summary\\":\\"[Spike] Probe Jira issue type\\"' in payload_text
    assert '\\"issuetype\\":{\\"name\\":\\"Task\\"}' in payload_text


def test_data_center_research_create_uses_task_type_and_research_summary_prefix(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="research",
        title="Compare issue types",
        body="## Description\n\nCompare the Jira issue types.",
    )

    assert response.payload["operation"] == "create_issue"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    payload_text = str(write_request.input_text)
    assert '\\"summary\\":\\"[Research] Compare issue types\\"' in payload_text
    assert '\\"issuetype\\":{\\"name\\":\\"Task\\"}' in payload_text


def test_data_center_usecase_create_uses_story_type(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="usecase",
        title="Shape checkout flow",
        body="## Description\n\nShape the checkout flow.",
    )

    assert response.payload["operation"] == "create_issue"
    write_request = runner.requests[0]
    assert write_request.args == curl_write_args()
    payload_text = str(write_request.input_text)
    assert '\\"summary\\":\\"Shape checkout flow\\"' in payload_text
    assert '\\"issuetype\\":{\\"name\\":\\"Story\\"}' in payload_text


@pytest.mark.parametrize(
    ("artifact_type", "expected_issue_type"),
    [
        ("task", "Task"),
        ("bug", "Bug"),
        ("epic", "Epic"),
        ("research", "Task"),
        ("usecase", "Story"),
    ],
)
def test_data_center_create_uses_artifact_issue_type(
    tmp_path: Path,
    artifact_type: str,
    expected_issue_type: str,
) -> None:
    extra = (
        """
    epic_fields:
      name: customfield_12345
"""
        if artifact_type == "epic"
        else ""
    )
    write_jira_config(tmp_path, relationship_mappings=extra)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type=artifact_type,
        title=f"Create {artifact_type}",
        body="## Description\n\nCreate the issue.",
        issue_type="Custom",
    )

    assert response.payload["operation"] == "create_issue"
    payload_text = str(runner.requests[0].input_text)
    assert f'\\"issuetype\\":{{\\"name\\":\\"{expected_issue_type}\\"}}' in payload_text


def test_data_center_create_uses_configured_epic_issue_type(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    artifact_issue_types:
      epic: Initiative
    epic_fields:
      name: customfield_12345
""",
    )
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="epic",
        title="Coordinate a larger batch",
        body="## Description\n\nCoordinate the batch.",
    )

    assert response.payload["operation"] == "create_issue"
    payload_text = str(runner.requests[0].input_text)
    assert '\\"issuetype\\":{\\"name\\":\\"Initiative\\"}' in payload_text


def test_data_center_epic_create_injects_epic_name_default_from_title(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      name: customfield_12345
""",
    )
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="epic",
        title="Coordinate a larger batch",
        body="## Description\n\nCoordinate the batch.",
    )

    assert response.payload["operation"] == "create_issue"
    payload_text = str(runner.requests[0].input_text)
    assert '\\"customfield_12345\\":\\"Coordinate a larger batch\\"' in payload_text


def test_data_center_epic_create_overrides_epic_name_when_provided(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      name: customfield_12345
""",
    )
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="epic",
        title="Coordinate a larger batch",
        body="## Description\n\nCoordinate the batch.",
        epic_name="Initiative codename",
    )

    assert response.payload["operation"] == "create_issue"
    payload_text = str(runner.requests[0].input_text)
    assert '\\"customfield_12345\\":\\"Initiative codename\\"' in payload_text


def test_data_center_epic_create_without_epic_name_field_raises(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="epic_fields.name"):
        dispatch_write(
            tmp_path,
            runner,
            "create",
            artifact_type="epic",
            title="Coordinate",
            body="Body.",
        )


def test_data_center_epic_name_rejected_for_non_epic_artifact(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      name: customfield_12345
""",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="epic_name is only valid"):
        dispatch_write(
            tmp_path,
            runner,
            "create",
            artifact_type="task",
            title="Task title",
            body="Body.",
            epic_name="Stray epic name",
        )


def test_data_center_non_epic_create_payload_is_byte_identical_with_epic_fields(tmp_path: Path) -> None:
    """Regression: configured epic_fields must not leak into non-Epic create payload."""

    write_jira_config(tmp_path)
    runner_a = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )
    dispatch_write(
        tmp_path,
        runner_a,
        "create",
        artifact_type="task",
        title="Plain task",
        body="Plain body.\n",
        labels=["workflow"],
    )
    plain_payload = runner_a.requests[0].input_text

    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      name: customfield_12345
      link: customfield_12346
      status: customfield_12347
""",
    )
    runner_b = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )
    dispatch_write(
        tmp_path,
        runner_b,
        "create",
        artifact_type="task",
        title="Plain task",
        body="Plain body.\n",
        labels=["workflow"],
    )

    assert runner_b.requests[0].input_text == plain_payload


def test_data_center_update_writes_body_and_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(body="Cached body."),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload(body="Cached body."))),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload(body="Updated body."))),
            ],
            curl_write_args(): result(curl_write_args(), stdout=""),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "update",
        issue="TEST-1234",
        body="Updated body.",
        freshness_check=True,
    )

    assert response.payload["operation"] == "update_issue"
    assert response.payload["state_changed"] is False
    write_request = runner.requests[1]
    assert write_request.args == curl_write_args()
    assert 'request = "PUT"' in str(write_request.input_text)
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234"' in str(write_request.input_text)
    assert '\\"description\\":\\"Updated body.\\"' in str(write_request.input_text)


def test_data_center_update_rejects_empty_payload(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="at least one of body, title, labels"):
        dispatch_write(tmp_path, runner, "update", issue="TEST-1234")

    assert runner.requests == []


def test_data_center_update_applies_state_transition(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    state_transitions:
      close: Done
      reopen: Reopen
""",
    )
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(body="Cached body."),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    transitions_url = f"https://jira.example.test/rest/api/2/issue/TEST-1234/transitions"
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload(body="Cached body."))),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload(body="Closing body."))),
            ],
            curl_args(transitions_url): result(
                curl_args(transitions_url),
                stdout=json.dumps({"transitions": [{"id": "31", "name": "Done"}]}),
            ),
            curl_write_args(): [
                result(curl_write_args(), stdout=""),
                result(curl_write_args(), stdout=""),
            ],
            curl_args(remote_links_url()): result(
                curl_args(remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "update",
        issue="TEST-1234",
        body="Closing body.",
        state="close",
        state_reason="completed",
        freshness_check=True,
    )

    assert response.payload["state_changed"] is True
    assert response.payload["state"]["transition_name"] == "Done"
    assert response.payload["state"]["transition_id"] == "31"
    assert response.payload["state"]["verb"] == "close"
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert any('\\"transition\\":{\\"id\\":\\"31\\"}' in str(request.input_text) for request in write_requests)


def test_data_center_update_state_without_configured_transition_errors(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(curl_write_args(), stdout=""),
        }
    )

    with pytest.raises(ProviderOperationError) as excinfo:
        dispatch_write(
            tmp_path,
            runner,
            "update",
            issue="TEST-1234",
            body="Body.",
            state="close",
            freshness_check=True,
        )

    message = str(excinfo.value)
    # No baked verb mapping; setup-skill discovery is required.
    assert "verb 'close'" in message
    assert "state_transitions.close" in message
    assert "jira-state-transition-inspect" in message
    assert "setup skill" in message


def test_data_center_add_comment_posts_body_and_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(
                curl_write_args(),
                stdout=json.dumps({"id": "30001", "body": "Inline comment body.\n"}),
            ),
            curl_args(remote_links_url()): result(
                curl_args(remote_links_url()),
                stdout=json.dumps(remote_links_payload()),
            ),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "add_comment",
        issue="TEST-1234",
        body="Inline comment body.\n",
        freshness_check=True,
    )

    assert response.payload["operation"] == "add_comment"
    assert response.payload["state_changed"] is False
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    assert 'request = "POST"' in str(write_request.input_text)
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234/comment"' in str(write_request.input_text)
    assert '\\"body\\":\\"Inline comment body.\\\\n\\"' in str(write_request.input_text)


def test_data_center_issue_link_relationships_are_applied_from_inline_intent(tmp_path: Path) -> None:
    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): [
                result(curl_write_args(), stdout=""),
                result(curl_write_args(), stdout=""),
                result(curl_write_args(), stdout=""),
            ],
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={
            "blocked_by_add": ["TEST-1233"],
            "blocking_add": ["TEST-1235"],
            "related_add": ["TEST-1236"],
        },
    )

    assert response.payload["operation"] == "apply_relationships"
    assert response.payload["applied"] == 3
    assert response.payload["cache_refreshed"] is True
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert len(write_requests) == 3
    blocked_by_request = str(write_requests[0].input_text)
    assert 'request = "POST"' in blocked_by_request
    assert f'url = "{issue_link_url()}"' in blocked_by_request
    assert '\\"type\\":{\\"name\\":\\"Blocks\\"}' in blocked_by_request
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1234\\"}' in blocked_by_request
    assert '\\"outwardIssue\\":{\\"key\\":\\"TEST-1233\\"}' in blocked_by_request
    blocking_request = str(write_requests[1].input_text)
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1235\\"}' in blocking_request
    assert '\\"outwardIssue\\":{\\"key\\":\\"TEST-1234\\"}' in blocking_request
    related_request = str(write_requests[2].input_text)
    assert '\\"type\\":{\\"name\\":\\"Relates\\"}' in related_request
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1236\\"}' in related_request


def test_data_center_epic_link_relationship_writes_bare_key_string(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      name: customfield_12345
      link: customfield_12346
    relationship_mappings:
      epic:
        surface: field
        field: customfield_12346
        write_to: source
        value: string
""",
    )
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(curl_write_args(), stdout=""),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={"epic_add": "TEST-10"},
    )

    assert response.payload["applied"] == 1
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    body = str(write_request.input_text)
    assert 'request = "PUT"' in body
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234"' in body
    assert '\\"customfield_12346\\":\\"TEST-10\\"' in body
    assert '\\"key\\":\\"TEST-10\\"' not in body


def test_data_center_combined_parent_and_epic_relationships_write_independently(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    epic_fields:
      link: customfield_12346
    relationship_mappings:
      child:
        surface: field
        field: parent
        write_to: target
        value: key
      epic:
        surface: field
        field: customfield_12346
        write_to: source
        value: string
""",
    )
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_subtask_payload(),
        remote_links=[],
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url("TEST-1237")): [
                result(curl_args(issue_url("TEST-1237")), stdout=json.dumps(jira_subtask_payload())),
                result(curl_args(issue_url("TEST-1237")), stdout=json.dumps(jira_subtask_payload())),
            ],
            curl_args(issue_url("TEST-50")): result(
                curl_args(issue_url("TEST-50")),
                stdout=json.dumps({"key": "TEST-50", "fields": {"summary": "Story", "issuetype": {"name": "Story"}}}),
            ),
            curl_write_args(): [
                result(curl_write_args(), stdout=""),
                result(curl_write_args(), stdout=""),
            ],
            curl_args(remote_links_url("TEST-1237")): result(curl_args(remote_links_url("TEST-1237")), stdout=json.dumps([])),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1237",
        relationship_intent={
            "child_add": ["TEST-50"],
            "epic_add": "TEST-10",
        },
    )

    assert response.payload["applied"] == 2
    write_requests = [request for request in runner.requests if request.args == curl_write_args()]
    assert len(write_requests) == 2
    bodies = [str(req.input_text) for req in write_requests]
    epic_body = next(body for body in bodies if "customfield_12346" in body)
    child_body = next(body for body in bodies if 'url = "https://jira.example.test/rest/api/2/issue/TEST-50"' in body)
    assert '\\"customfield_12346\\":\\"TEST-10\\"' in epic_body
    assert '\\"parent\\":{\\"key\\":\\"TEST-1237\\"}' in child_body


def test_data_center_remote_link_relationships_are_applied_with_stable_global_id(tmp_path: Path) -> None:
    write_jira_config(tmp_path, relationship_mappings=remote_link_relationship_mappings())
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": 100})),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={
            "related_add": ["https://github.com/studykit/studykit-plugins/issues/57"],
        },
    )

    assert response.payload["applied"] == 1
    write_request = next(request for request in runner.requests if request.args == curl_write_args())
    body = str(write_request.input_text)
    assert 'request = "POST"' in body
    assert 'url = "https://jira.example.test/rest/api/2/issue/TEST-1234/remotelink"' in body
    assert '\\"globalId\\":\\"system=studykit-workflow&id=' in body
    assert '\\"relationship\\":\\"relates to\\"' in body
    assert '\\"url\\":\\"https://github.com/studykit/studykit-plugins/issues/57\\"' in body
    assert '\\"title\\":\\"57\\"' in body


def test_data_center_missing_relationship_mapping_fails_before_mutation(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="Jira relationship 'blocking' is not configured"):
        dispatch_write(
            tmp_path,
            runner,
            "apply_relationships",
            issue="TEST-1234",
            relationship_intent={"blocking_add": ["TEST-1235"]},
        )

    assert runner.requests == []


def test_data_center_bad_relationship_direction_fails_before_mutation(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    relationship_mappings:
      blocking:
        surface: issue_link
        link_type: Blocks
        direction: sideways
""",
    )
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="requires direction"):
        dispatch_write(
            tmp_path,
            runner,
            "apply_relationships",
            issue="TEST-1234",
            relationship_intent={"blocking_add": ["TEST-1235"]},
        )

    assert runner.requests == []


def test_data_center_stale_cache_blocks_write_before_put(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(body="Cached body."),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    newer = jira_issue_payload(body="Newer provider body.")
    newer["fields"]["updated"] = "2026-05-15T11:00:00.000+0900"  # type: ignore[index]
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(newer)),
                result(curl_args(issue_url()), stdout=json.dumps(newer)),
            ],
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "update",
        issue="TEST-1234",
        body="Updated body.",
        freshness_check=True,
    )

    assert response.payload["operation"] == "update_issue"
    assert response.payload["status"] == "blocked"
    assert response.payload["reason"] == "stale_cache"
    assert response.payload["reread_required"] is True
    assert response.payload["cache_refreshed"] is True
    assert response.payload["freshness"]["status"] == "stale"
    assert "issue.md" in "\n".join(response.payload["reread_paths"])
    assert all(request.args != curl_write_args() for request in runner.requests)


def test_data_center_comment_stale_cache_blocks_and_refreshes_before_post(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        jira_issue_payload(),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    newer = jira_issue_payload(body="Newer provider body.")
    newer["fields"]["updated"] = "2026-05-15T11:00:00.000+0900"  # type: ignore[index]
    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(newer)),
                result(curl_args(issue_url()), stdout=json.dumps(newer)),
            ],
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "add_comment",
        issue="TEST-1234",
        body="New comment.",
        freshness_check=True,
    )

    assert response.payload["operation"] == "add_comment"
    assert response.payload["status"] == "blocked"
    assert response.payload["reread_required"] is True
    assert all(request.args != curl_write_args() for request in runner.requests)
