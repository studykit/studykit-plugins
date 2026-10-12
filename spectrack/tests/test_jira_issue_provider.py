"""Tests for Jira Cloud workflow provider reads and cache."""

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

from command import CommandRequest, CommandResult  # noqa: E402
from issue.jira.cache import JiraIssueCache  # noqa: E402
from issue.jira.provider import (  # noqa: E402
    _jira_issue_provider_settings,
    _relationship_mapping,
    _relationship_mappings,
    create_issue_link,
)
from issue.jira.relationships import normalize_jira_issue  # noqa: E402
from issue.jira.client import jira_site_from_provider_config  # noqa: E402
from issue.providers import (  # noqa: E402
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_REFRESH,
    ProviderContext,
    ProviderDispatcher,
    ProviderOperationError,
    ProviderRequest,
    default_provider_registry,
)
from config import load_workflow_config  # noqa: E402
from jira_cloud_support import adf_doc, markdown_bodies, sent_json  # noqa: E402


pytestmark = pytest.mark.usefixtures("jira_cloud")


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
    return ("curl", "--silent", "--show-error", "--fail-with-body", "--request", "GET", "--config", "-", url)


def curl_write_args() -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail-with-body", "--config", "-")


def write_jira_config(
    project: Path,
    *,
    snapshot_settings: str = "",
    relationship_mappings: str = "",
) -> None:
    path = project / ".spectrack" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
            """
version: 1
providers:
  issues:
    kind: jira
    site: https://example.atlassian.net
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


def jira_issue_payload(*, body: str = "Cloud description.") -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "Support Jira Cloud",
            "description": adf_doc(body),
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
                        "body": adf_doc("Please keep Cloud first."),
                        "created": "2026-05-15T09:30:00.000+0900",
                        "updated": "2026-05-15T09:30:00.000+0900",
                    }
                ]
            },
            # Real Jira GET shape: the populated side holds the *far* issue under
            # its own role. Per Atlassian's issue-linking model the inwardIssue
            # performs the link's outward verb, so: TEST-1234 blocks TEST-1235 ->
            # TEST-1235 sits in the outward field (current "blocks" it); TEST-1234
            # is blocked by TEST-1233 -> TEST-1233 sits in the inward field
            # (current "is blocked by" it).
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
                    # related is configured direction: outward, so from TEST-1234's
                    # perspective the far issue sits on the outward side.
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
        application_type: studykit.spectrack
        application_name: Workflow
"""


def issue_link_and_custom_field_relationship_mappings(*, value_kind: str = "string") -> str:
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
      initiative:
        surface: field
        field: customfield_10350
        write_to: source
        value: {value_kind}
"""


def issue_url(issue: str = "TEST-1234") -> str:
    return f"https://example.atlassian.net/rest/api/3/issue/{issue}"


def remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://example.atlassian.net/rest/api/3/issue/{issue}/remotelink"


def issue_link_url() -> str:
    return "https://example.atlassian.net/rest/api/3/issueLink"


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
    return jira_site_from_provider_config(config.issues)


def _split_issue_md(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        raise AssertionError("issue.md missing YAML frontmatter")
    _opening, frontmatter, body = text.split("---", 2)
    return frontmatter, body


def test_jira_provider_fetches_issue_remote_links_and_writes_llm_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    assert response.payload["key"] == "TEST-1234"
    assert response.payload["title"] == "Support Jira Cloud"
    assert response.payload["body"] == "Cloud description."
    assert response.payload["jira"] == {
        "base_url": "https://example.atlassian.net",
        "authority": "example.atlassian.net",
        "project": "TEST",
        "issue_type": "Task",
        "key": "TEST-1234",
    }
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
    assert all(
        request.input_text == 'header = "Accept: application/json"\nuser = "user@example.test:test-token"\n'
        for request in runner.requests
    )

    cache = JiraIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_dir = cache.issue_dir(site, "TEST-1234")
    assert issue_dir == tmp_path / ".spectrack-cache" / "issues" / "TEST-1234"
    assert (issue_dir / ".issue.json").is_file()
    assert (issue_dir / ".remote-links.json").is_file()

    issue_md_text = (issue_dir / "issue.md").read_text(encoding="utf-8")
    # issue.md is the pure authored body; title / state / labels / relationships
    # are served from the native .issue.json + .remote-links.json projections and
    # are already asserted via the GET response above.
    assert issue_md_text == "Cloud description."
    assert "Please keep Cloud first." not in issue_md_text
    assert not (issue_dir / "metadata.yml").exists()

    comment_files = cache.comment_files(site, "TEST-1234")
    assert [path.name for path in comment_files] == [
        "comment-2026-05-15T093000Z-20001.md",
    ]
    comment_text = comment_files[0].read_text(encoding="utf-8")
    assert "Please keep Cloud first." in comment_text
    assert "provider_comment_id: '20001'" in comment_text
    assert "author: Example User" in comment_text


def _assert_existing_workflow_buckets_unchanged(workflow: dict) -> None:
    assert workflow["parent"]["key"] == "TEST-1200"
    assert workflow["children"][0]["key"] == "TEST-1237"
    assert workflow["blocking"][0]["key"] == "TEST-1235"
    assert workflow["blocked_by"][0]["key"] == "TEST-1233"
    assert workflow["related"][0]["key"] == "TEST-1236"


@pytest.mark.parametrize("relationship", ["blocked_by", "blocking", "related"])
def test_jira_issue_link_write_read_round_trips(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    relationship: str,
) -> None:
    """A relationship written via create_issue_link must read back into the
    same workflow bucket. This couples the write direction (create_issue_link)
    to the read direction (normalize) so neither can silently invert blocking /
    blocked_by again — see issue #131 and the read fixtures above, which are
    hand-authored and could otherwise drift from real Jira output.
    """

    source = "TEST-1234"
    target = "TEST-2001"
    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    site = jira_site(tmp_path)
    settings = _jira_issue_provider_settings(tmp_path)
    mappings = _relationship_mappings(settings)
    mapping = _relationship_mapping(settings, relationship)

    # Capture the body create_issue_link would POST without serializing to curl.
    captured: dict[str, object] = {}

    def fake_send(_site, _method, _path, payload, *, runner=None):
        captured["payload"] = payload
        return {}

    monkeypatch.setattr("issue.jira.provider.jira_send_json", fake_send)
    create_issue_link(
        site,
        source_issue=source,
        target_issue=target,
        link_type=mapping.link_type or "",
        direction=mapping.direction or "",
    )
    payload = captured["payload"]
    assert isinstance(payload, dict)
    inward_key = payload["inwardIssue"]["key"]
    outward_key = payload["outwardIssue"]["key"]

    # Jira's GET projection drops the current issue's own side and keeps the
    # far issue under its real role field. Build that shape from the POST body.
    if inward_key == source:
        far_side, far_key = "outwardIssue", outward_key
    else:
        far_side, far_key = "inwardIssue", inward_key
    assert far_key == target

    link_entry = {
        "id": "70001",
        "type": {
            "name": mapping.link_type,
            "inward": "is blocked by",
            "outward": "blocks",
        },
        far_side: {
            "key": target,
            "fields": {"summary": "Far issue", "status": {"name": "Open"}},
        },
    }
    issue = {
        "id": "10001",
        "key": source,
        "fields": {
            "summary": "Round trip",
            "description": "body",
            "status": {"name": "Open", "statusCategory": {"key": "new"}},
            "issuelinks": [link_entry],
        },
    }

    normalized = normalize_jira_issue(
        issue,
        site=site,
        relationship_mappings=mappings,
    )
    workflow = normalized["relationships"]["workflow"]
    assert workflow.get(relationship, []) and workflow[relationship][0]["key"] == target
    # The relationship must not leak into the opposite bucket or stay unmapped.
    opposite = {"blocked_by": "blocking", "blocking": "blocked_by"}.get(relationship)
    if opposite:
        assert opposite not in workflow
    assert "issue_links" not in workflow


def test_jira_field_surface_string_relationship_surfaces_in_workflow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_custom_field_relationship_mappings(value_kind="string"),
    )
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
    assert workflow["initiative"] == [{"provider": "jira", "key": "TEST-EPIC-1", "issue": "TEST-EPIC-1"}]
    _assert_existing_workflow_buckets_unchanged(workflow)


def test_jira_field_surface_key_object_relationship_surfaces_in_workflow(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_custom_field_relationship_mappings(value_kind="key_object"),
    )
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
    assert workflow["initiative"] == [{"provider": "jira", "key": "TEST-EPIC-1", "issue": "TEST-EPIC-1"}]
    _assert_existing_workflow_buckets_unchanged(workflow)


def test_jira_field_surface_absent_field_is_omitted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=issue_link_and_custom_field_relationship_mappings(value_kind="string"),
    )
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner)

    workflow = response.payload["relationships"]["workflow"]
    assert "initiative" not in workflow
    _assert_existing_workflow_buckets_unchanged(workflow)


def test_jira_snapshot_hides_comments_with_configured_markers(
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
    cache = JiraIssueCache.for_project(tmp_path)
    site = jira_site(tmp_path)
    issue_dir = cache.issue_dir(site, "TEST-1234")
    assert "!git-event" in (issue_dir / ".issue.json").read_text(encoding="utf-8")

    comment_file_names = {path.name for path in cache.comment_files(site, "TEST-1234")}
    assert comment_file_names == {
        "comment-2026-05-15T093000Z-20001.md",
        "comment-2026-05-15T094500Z-20003.md",
    }
    visible_bodies = "\n".join(
        path.read_text(encoding="utf-8") for path in cache.comment_files(site, "TEST-1234")
    )
    assert "Please keep Cloud first." in visible_bodies
    assert "Human follow-up remains visible." in visible_bodies
    assert "!git-event" not in visible_bodies
    assert "pushed commit abc123" not in visible_bodies


def test_default_cache_policy_uses_cache_hit_without_curl(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload(body="Cached Jira body.")),
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


def test_refresh_policy_overwrites_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(site, markdown_bodies(jira_issue_payload(body="Stale body.")), fetched_at="2026-05-15T01:00:00Z")
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


def test_bypass_policy_reads_without_writing_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_get(tmp_path, runner, cache_policy=CACHE_POLICY_BYPASS)

    assert response.payload["body"] == "Cloud description."
    cache = JiraIssueCache.for_project(tmp_path)
    assert not cache.issue_json_file(jira_site(tmp_path), "TEST-1234").exists()


def test_jira_create_inline_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
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
    assert 'url = "https://example.atlassian.net/rest/api/3/issue"' in str(write_request.input_text)
    assert '\\"summary\\":\\"Pending Jira issue\\"' in str(write_request.input_text)
    assert '\\"issuetype\\":{\\"name\\":\\"Task\\"}' in str(write_request.input_text)
    assert '\\"parent\\"' not in str(write_request.input_text)
    assert cache.issue_json_file(site, "TEST-1234").is_file()


def test_jira_create_with_assignee_carries_assignee_field(tmp_path: Path) -> None:
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
    assert '\\"assignee\\":{\\"accountId\\":\\"alice\\"}' in str(write_request.input_text)


def test_jira_create_with_assignee_me_resolves_via_myself_once(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    myself_url = "https://example.atlassian.net/rest/api/3/myself"
    runner = FakeRunner(
        {
            curl_args(myself_url): result(
                curl_args(myself_url),
                stdout=json.dumps({"accountId": "studykit-svc", "displayName": "Studykit Service"}),
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
        '\\"assignee\\":{\\"accountId\\":\\"studykit-svc\\"}' in str(request.input_text)
        for request in write_requests
    )


def test_jira_subtask_create_inline_refreshes_parent_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
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


def test_jira_review_create_uses_task_type_and_review_summary_prefix(tmp_path: Path) -> None:
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


def test_jira_spike_create_uses_task_type_and_spike_summary_prefix(tmp_path: Path) -> None:
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


def test_jira_research_create_uses_task_type_and_research_summary_prefix(tmp_path: Path) -> None:
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


def test_jira_usecase_create_uses_story_type(tmp_path: Path) -> None:
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
def test_jira_create_uses_artifact_issue_type(
    tmp_path: Path,
    artifact_type: str,
    expected_issue_type: str,
) -> None:
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
        artifact_type=artifact_type,
        title=f"Create {artifact_type}",
        body="## Description\n\nCreate the issue.",
        issue_type="Custom",
    )

    assert response.payload["operation"] == "create_issue"
    payload_text = str(runner.requests[0].input_text)
    assert f'\\"issuetype\\":{{\\"name\\":\\"{expected_issue_type}\\"}}' in payload_text


def test_jira_create_uses_configured_epic_issue_type(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    artifact_issue_types:
      epic: Initiative
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


def test_jira_update_writes_body_and_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload(body="Cached body.")),
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
    assert 'url = "https://example.atlassian.net/rest/api/3/issue/TEST-1234"' in str(write_request.input_text)
    assert sent_json(str(write_request.input_text))["fields"]["description"] == adf_doc("Updated body.")


def attachments_url(issue: str = "TEST-1234") -> str:
    return f"https://example.atlassian.net/rest/api/3/issue/{issue}/attachments"


def attachments_payload() -> list[dict[str, object]]:
    return [
        {
            "id": "40001",
            "filename": "report.pdf",
            "size": 2048,
            "mimeType": "application/pdf",
            "content": "https://example.atlassian.net/secure/attachment/40001/report.pdf",
            "created": "2026-06-02T10:00:00.000+0900",
        }
    ]


def test_curl_multipart_config_sets_token_and_repeated_form_lines() -> None:
    from issue.jira.client import JiraSite, _curl_multipart_config

    config = _curl_multipart_config(
        JiraSite(base_url="https://example.atlassian.net", authority="example.atlassian.net"),
        url="https://example.atlassian.net/rest/api/3/issue/TEST-1234/attachments",
        file_paths=["/tmp/a.png", "/tmp/b.pdf"],
    )
    assert 'header = "X-Atlassian-Token: no-check"' in config
    assert 'request = "POST"' in config
    assert 'form = "file=@/tmp/a.png"' in config
    assert 'form = "file=@/tmp/b.pdf"' in config
    # multipart sets its own Content-Type/boundary — never override it
    assert "Content-Type" not in config


def test_jira_add_attachment_uploads_and_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    runner = FakeRunner(
        {
                ("curl", "--silent", "--show-error", "--fail", "--config", "-"): result(curl_write_args(), stdout=json.dumps(attachments_payload())),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "add_attachment",
        issue="TEST-1234",
        files=["/tmp/report.pdf"],
    )

    assert response.payload["operation"] == "add_attachment"
    assert response.payload["issue"] == "TEST-1234"
    assert response.payload["cache_refreshed"] is True
    assert response.payload["attachments"][0]["filename"] == "report.pdf"
    assert response.payload["attachments"][0]["id"] == "40001"

    upload_request = runner.requests[0]
    assert upload_request.args == ("curl", "--silent", "--show-error", "--fail", "--config", "-")
    text = str(upload_request.input_text)
    assert 'header = "X-Atlassian-Token: no-check"' in text
    assert 'request = "POST"' in text
    assert f'url = "{attachments_url()}"' in text
    assert 'form = "file=@/tmp/report.pdf"' in text
    assert cache.issue_json_file(site, "TEST-1234").is_file()


def test_jira_add_attachment_requires_files(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="non-empty 'files'"):
        dispatch_write(tmp_path, runner, "add_attachment", issue="TEST-1234", files=[])

    assert runner.requests == []


def _issue_payload_with_attachments() -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": "x",
            "description": "y",
            "status": {"name": "Open", "statusCategory": {"key": "new"}},
            "attachment": [
                {
                    "id": "40001",
                    "filename": "report.pdf",
                    "size": 2048,
                    "content": "https://example.atlassian.net/secure/attachment/40001/report.pdf",
                },
                {
                    "id": "40002",
                    "filename": "notes.txt",
                    "size": 12,
                    "content": "https://example.atlassian.net/secure/attachment/40002/notes.txt",
                },
            ],
        },
    }


_DOWNLOAD_ARGS = ("curl", "--silent", "--show-error", "--fail", "--location", "--config", "-")


def test_jira_get_attachment_resolves_id_and_downloads(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(_issue_payload_with_attachments())),
            _DOWNLOAD_ARGS: result(_DOWNLOAD_ARGS, stdout=""),
        }
    )
    out_dir = tmp_path / "dl"

    response = dispatch_write(
        tmp_path,
        runner,
        "get_attachment",
        issue="TEST-1234",
        ids=["40001"],
        names=[],
        all=False,
        out=str(out_dir),
    )

    downloaded = response.payload["downloaded"]
    assert response.payload["operation"] == "get_attachment"
    assert [item["id"] for item in downloaded] == ["40001"]
    assert downloaded[0]["filename"] == "report.pdf"
    assert downloaded[0]["path"].endswith("/report.pdf")

    download_request = next(req for req in runner.requests if req.args == _DOWNLOAD_ARGS)
    text = str(download_request.input_text)
    assert "secure/attachment/40001/report.pdf" in text
    assert "40002" not in text


def test_jira_get_attachment_all_downloads_every_file(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(_issue_payload_with_attachments())),
            _DOWNLOAD_ARGS: result(_DOWNLOAD_ARGS, stdout=""),
        }
    )

    response = dispatch_write(
        tmp_path,
        runner,
        "get_attachment",
        issue="TEST-1234",
        ids=[],
        names=[],
        all=True,
        out=str(tmp_path / "dl"),
    )

    assert {item["id"] for item in response.payload["downloaded"]} == {"40001", "40002"}
    assert sum(1 for req in runner.requests if req.args == _DOWNLOAD_ARGS) == 2


def test_jira_get_attachment_no_match_raises(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(_issue_payload_with_attachments())),
        }
    )

    with pytest.raises(ProviderOperationError, match="no matching attachment"):
        dispatch_write(
            tmp_path,
            runner,
            "get_attachment",
            issue="TEST-1234",
            ids=["99999"],
            names=[],
            all=False,
            out=str(tmp_path / "dl"),
        )


def test_jira_update_rejects_empty_payload(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="at least one of body, title, labels"):
        dispatch_write(tmp_path, runner, "update", issue="TEST-1234")

    assert runner.requests == []


def test_jira_update_applies_state_transition(tmp_path: Path) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings="""
    state_transitions:
      close: Done
      reopen: Reopen
""",
    )
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload(body="Cached body.")),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )
    transitions_url = f"https://example.atlassian.net/rest/api/3/issue/TEST-1234/transitions"
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


def test_jira_update_state_without_configured_transition_errors(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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


def test_jira_add_comment_posts_body_and_refreshes_cache(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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
    assert 'url = "https://example.atlassian.net/rest/api/3/issue/TEST-1234/comment"' in str(write_request.input_text)
    assert sent_json(str(write_request.input_text)) == {"body": adf_doc("Inline comment body.\n")}


def test_jira_issue_link_relationships_are_applied_from_inline_intent(tmp_path: Path) -> None:
    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    # Seed with the configured relationship mappings so the cached relationships
    # fingerprint matches the provider's freshness re-compute (which uses them).
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
        relationship_mappings=_relationship_mappings(_jira_issue_provider_settings(tmp_path)),
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
    # Atlassian semantics: the POST inwardIssue performs the outward verb. So a
    # `blocked_by` (source is blocked) puts the source in outwardIssue and the
    # blocker (target) in inwardIssue; `blocking` is the mirror.
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1233\\"}' in blocked_by_request
    assert '\\"outwardIssue\\":{\\"key\\":\\"TEST-1234\\"}' in blocked_by_request
    blocking_request = str(write_requests[1].input_text)
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1234\\"}' in blocking_request
    assert '\\"outwardIssue\\":{\\"key\\":\\"TEST-1235\\"}' in blocking_request
    related_request = str(write_requests[2].input_text)
    assert '\\"type\\":{\\"name\\":\\"Relates\\"}' in related_request
    assert '\\"inwardIssue\\":{\\"key\\":\\"TEST-1234\\"}' in related_request


def _jira_target_payload(key: str, *, blocks_key: str) -> dict[str, object]:
    """A minimal target issue carrying a Blocks link to ``blocks_key``.

    With the ``blocking`` mapping (Blocks/outward) this renders ``blocks_key``
    into the target's ``relation.md``, so a refreshed projection is observable.
    """

    return {
        "id": "10002",
        "key": key,
        "fields": {
            "summary": f"Blocker {key}",
            "description": "",
            "status": {"name": "Open", "statusCategory": {"key": "new"}},
            "issuelinks": [
                {
                    "id": "30001",
                    "type": {"name": "Blocks", "inward": "is blocked by", "outward": "blocks"},
                    "outwardIssue": {"key": blocks_key, "fields": {"summary": "blocked issue"}},
                }
            ],
        },
    }


def test_jira_relationship_apply_refreshes_cached_target_relation_md(tmp_path: Path) -> None:
    """Linking refreshes relation.md for every *already-cached* far endpoint.

    A Jira issue link is one object surfaced from both issues, so the target's
    cached relation.md goes stale unless re-projected. An uncached target is not
    materialized.
    """

    write_jira_config(tmp_path, relationship_mappings=issue_link_relationship_mappings())
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    mappings = _relationship_mappings(_jira_issue_provider_settings(tmp_path))
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
        relationship_mappings=mappings,
    )
    # TEST-1233 (the blocker) is already tracked locally; TEST-1235 is not.
    cache.write_issue_bundle(
        site,
        markdown_bodies(_jira_target_payload("TEST-1233", blocks_key="TEST-1234")),
        remote_links=[],
        fetched_at="2026-05-15T10:00:00.000+0900",
        relationship_mappings=mappings,
    )
    assert cache.has_issue_projection(site, "TEST-1233")
    assert not cache.has_issue_projection(site, "TEST-1235")

    runner = FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
                result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            ],
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
            curl_args(issue_url("TEST-1233")): result(
                curl_args(issue_url("TEST-1233")),
                stdout=json.dumps(_jira_target_payload("TEST-1233", blocks_key="TEST-1234")),
            ),
            curl_args(remote_links_url("TEST-1233")): result(curl_args(remote_links_url("TEST-1233")), stdout="[]"),
            curl_write_args(): [
                result(curl_write_args(), stdout=""),
                result(curl_write_args(), stdout=""),
            ],
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
        },
    )

    assert response.payload["target_cache_refreshed"] == ["TEST-1233"]
    # The uncached target is never fetched or materialized.
    assert "target_cache_errors" not in response.payload
    assert not cache.has_issue_projection(site, "TEST-1235")
    assert not any(req.args == curl_args(issue_url("TEST-1235")) for req in runner.requests)
    # The cached target's relation.md was re-projected and points back at the source.
    target_relation = cache.relationships_file(site, "TEST-1233")
    assert target_relation.is_file()
    assert "TEST-1234" in target_relation.read_text(encoding="utf-8")


def test_jira_remote_link_relationships_are_applied_with_stable_global_id(tmp_path: Path) -> None:
    write_jira_config(tmp_path, relationship_mappings=remote_link_relationship_mappings())
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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
    assert 'url = "https://example.atlassian.net/rest/api/3/issue/TEST-1234/remotelink"' in body
    assert '\\"globalId\\":\\"system=studykit-workflow&id=' in body
    assert '\\"relationship\\":\\"relates to\\"' in body
    assert '\\"url\\":\\"https://github.com/studykit/studykit-plugins/issues/57\\"' in body
    assert '\\"title\\":\\"57\\"' in body


def test_jira_missing_relationship_mapping_fails_before_mutation(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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


def test_jira_bad_relationship_direction_fails_before_mutation(tmp_path: Path) -> None:
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
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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


def test_jira_stale_cache_blocks_write_before_put(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload(body="Cached body.")),
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
    assert response.payload["status"] == "conflict"
    assert response.payload["reason"] == "provider_changed"
    assert response.payload["reread_required"] is True
    assert response.payload["cache_refreshed"] is True
    assert response.payload["conflict"]["status"] == "conflict"
    assert "issue.md" in "\n".join(response.payload["reread_paths"])
    assert all(not path.endswith("/.meta.json") for path in response.payload["reread_paths"])
    assert all(request.args != curl_write_args() for request in runner.requests)


def test_jira_comment_stale_cache_blocks_and_refreshes_before_post(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    site = jira_site(tmp_path)
    cache = JiraIssueCache.for_project(tmp_path)
    cache.write_issue_bundle(
        site,
        markdown_bodies(jira_issue_payload()),
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
    assert response.payload["status"] == "conflict"
    assert response.payload["reason"] == "provider_changed"
    assert response.payload["reread_required"] is True
    assert all(request.args != curl_write_args() for request in runner.requests)


# ---------------------------------------------------------------------------
# Built-in hierarchy relationships: parent / epic / child use the native
# ``parent`` field and need no relationship_mappings entry.
# ---------------------------------------------------------------------------


def _issue_without_parent() -> dict[str, object]:
    payload = jira_issue_payload()
    fields = payload["fields"]
    assert isinstance(fields, dict)
    fields.pop("parent")
    return payload


def _seed_hierarchy_cache(project: Path, payload: dict[str, object]) -> None:
    JiraIssueCache.for_project(project).write_issue_bundle(
        jira_site(project),
        markdown_bodies(payload),
        remote_links=remote_links_payload(),
        fetched_at="2026-05-15T10:00:00.000+0900",
    )


def _hierarchy_runner(current: dict[str, object]) -> FakeRunner:
    return FakeRunner(
        {
            curl_args(issue_url()): [
                result(curl_args(issue_url()), stdout=json.dumps(current)),
                result(curl_args(issue_url()), stdout=json.dumps(current)),
            ],
            curl_write_args(): result(curl_write_args(), stdout=""),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )


def _field_writes(runner: FakeRunner) -> list[tuple[str, object]]:
    writes = []
    for request in runner.requests:
        if request.args != curl_write_args():
            continue
        text = str(request.input_text)
        url = next(line for line in text.splitlines() if line.startswith("url = "))
        writes.append((url, sent_json(text)))
    return writes


@pytest.mark.parametrize("intent_key", ["parent_add", "epic_add"])
def test_parent_and_epic_add_write_the_native_parent_field(tmp_path: Path, intent_key: str) -> None:
    write_jira_config(tmp_path)
    _seed_hierarchy_cache(tmp_path, _issue_without_parent())
    runner = _hierarchy_runner(_issue_without_parent())

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={intent_key: "TEST-10"},
    )

    assert response.payload["applied"] == 1
    assert _field_writes(runner) == [
        (f'url = "{issue_url()}"', {"fields": {"parent": {"key": "TEST-10"}}}),
    ]


def test_child_add_writes_the_target_parent_field(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_hierarchy_cache(tmp_path, jira_issue_payload())
    runner = _hierarchy_runner(jira_issue_payload())

    dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={"child_add": ["TEST-2001"]},
    )

    assert _field_writes(runner) == [
        (f'url = "{issue_url("TEST-2001")}"', {"fields": {"parent": {"key": "TEST-1234"}}}),
    ]


@pytest.mark.parametrize("intent_key", ["parent_remove", "epic_remove"])
def test_parent_and_epic_remove_clear_the_native_parent(tmp_path: Path, intent_key: str) -> None:
    write_jira_config(tmp_path)
    _seed_hierarchy_cache(tmp_path, jira_issue_payload())
    runner = _hierarchy_runner(jira_issue_payload())

    response = dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={intent_key: True},
    )

    assert response.payload["operations"][0]["target_ref"] == "TEST-1200"
    assert _field_writes(runner) == [
        (f'url = "{issue_url()}"', {"fields": {"parent": None}}),
    ]


def test_parent_add_on_an_issue_with_a_parent_fails_before_any_request(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_hierarchy_cache(tmp_path, jira_issue_payload())
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="parent already exists.*--replace-parent"):
        dispatch_write(
            tmp_path,
            runner,
            "apply_relationships",
            issue="TEST-1234",
            relationship_intent={"parent_add": "TEST-1300"},
        )

    assert runner.requests == []


def test_replace_parent_overwrites_an_existing_parent(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    _seed_hierarchy_cache(tmp_path, jira_issue_payload())
    runner = _hierarchy_runner(jira_issue_payload())

    dispatch_write(
        tmp_path,
        runner,
        "apply_relationships",
        issue="TEST-1234",
        relationship_intent={"parent_replace": "TEST-1300"},
    )

    assert _field_writes(runner) == [
        (f'url = "{issue_url()}"', {"fields": {"parent": {"key": "TEST-1300"}}}),
    ]


@pytest.mark.parametrize("relationship", ["parent", "epic", "child"])
def test_hierarchy_relationship_mapping_raises_cloud_only_error(tmp_path: Path, relationship: str) -> None:
    write_jira_config(
        tmp_path,
        relationship_mappings=f"""
    relationship_mappings:
      {relationship}:
        surface: field
        field: parent
        write_to: source
        value: key
""",
    )
    runner = FakeRunner({})

    with pytest.raises(ProviderOperationError, match="spectrack supports Jira Cloud only"):
        dispatch_write(
            tmp_path,
            runner,
            "apply_relationships",
            issue="TEST-1234",
            relationship_intent={"blocked_by_add": ["TEST-1233"]},
        )

    assert runner.requests == []


def test_epic_create_sends_no_epic_name(tmp_path: Path) -> None:
    write_jira_config(tmp_path)
    runner = FakeRunner(
        {
            curl_write_args(): result(curl_write_args(), stdout=json.dumps({"id": "10001", "key": "TEST-1234"})),
            curl_args(issue_url()): result(curl_args(issue_url()), stdout=json.dumps(jira_issue_payload())),
            curl_args(remote_links_url()): result(curl_args(remote_links_url()), stdout=json.dumps(remote_links_payload())),
        }
    )

    dispatch_write(
        tmp_path,
        runner,
        "create",
        artifact_type="epic",
        title="Coordinate a larger batch",
        body="Coordinate the batch.",
    )

    fields = sent_json(str(runner.requests[0].input_text))["fields"]
    assert set(fields) == {"project", "summary", "description", "issuetype"}
    assert fields["issuetype"] == {"name": "Epic"}
