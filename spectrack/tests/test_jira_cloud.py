"""Tests for the Jira Cloud variant of the Jira issue provider."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from command import CommandRequest, CommandResult  # noqa: E402
from config import ProviderConfig, load_workflow_config  # noqa: E402
from issue.jira import adf, client  # noqa: E402
from issue.jira.cache import JiraDataCenterIssueCache  # noqa: E402
from issue.jira.client import (  # noqa: E402
    jira_data_center_search_path,
    jira_data_center_site_from_provider_config,
)
from issue.jira.refs import JiraProviderError  # noqa: E402
from issue.providers import (  # noqa: E402
    ProviderContext,
    ProviderDispatcher,
    ProviderRequest,
    default_provider_registry,
)
from main_context import build_session_policy_context  # noqa: E402

SITE = "https://acme.atlassian.net"
GET = ("curl", "--silent", "--show-error", "--fail-with-body", "--request", "GET", "--config", "-")
WRITE = ("curl", "--silent", "--show-error", "--fail-with-body", "--config", "-")


class FakeRunner:
    """Answers GETs by URL and body-bearing writes in call order."""

    def __init__(self, gets: dict[str, object], writes: list[object]):
        self.gets = gets
        self.writes = writes
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        if request.args[: len(GET)] == GET:
            body = self.gets.get(request.args[-1])
        elif request.args == WRITE and self.writes:
            body = self.writes.pop(0)
        else:
            body = None
        if body is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        return CommandResult(request=request, returncode=0, stdout=json.dumps(body))

    def write_inputs(self) -> list[str]:
        return [request.input_text or "" for request in self.requests if request.args == WRITE]


@pytest.fixture(autouse=True)
def cloud_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JIRA_EMAIL", "user@example.test")
    monkeypatch.setenv("JIRA_API_TOKEN", "test-token")


def write_cloud_config(project: Path, *, extra: str = "") -> None:
    path = project / ".spectrack" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""
version: 1
providers:
  issues:
    kind: jira
    site: {SITE}
    project: TEST
    issue_type: Task
{extra}  knowledge:
    kind: github
issue_id_format: jira
""".lstrip(),
        encoding="utf-8",
    )


def adf_doc(text: str) -> dict[str, object]:
    return {
        "type": "doc",
        "version": 1,
        "content": [{"type": "paragraph", "content": [{"type": "text", "text": text}]}],
    }


def cloud_issue(*, comments: list[dict[str, object]] | None = None) -> dict[str, object]:
    return {
        "id": "10001",
        "key": "TEST-1",
        "fields": {
            "summary": "Cloud issue",
            "description": adf_doc("Description."),
            "status": {"name": "To Do", "statusCategory": {"key": "new"}},
            "comment": {"comments": comments or []},
        },
    }


def issue_url(key: str = "TEST-1") -> str:
    return f"{SITE}/rest/api/3/issue/{key}"


def dispatch(project: Path, runner: FakeRunner, operation: str, **payload: object):
    dispatcher = ProviderDispatcher(default_provider_registry(runner=runner))
    return dispatcher.dispatch(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation=operation,
            context=ProviderContext(project=project, artifact_type="task", cache_policy="refresh"),
            payload=payload,
        )
    )


def cloud_site():
    return jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings={"site": SITE})
    )


def test_atlassian_net_site_resolves_to_cloud_on_rest_v3() -> None:
    site = cloud_site()

    assert site.is_cloud
    assert site.api_version == "3"
    assert site.to_json()["deployment"] == "cloud"


def test_other_sites_stay_data_center_on_rest_v2() -> None:
    site = jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings={"site": "https://jira.example.test"})
    )

    assert not site.is_cloud
    assert site.api_version == "2"


def test_cloud_rejects_rest_v2() -> None:
    with pytest.raises(JiraProviderError, match="REST API version 3"):
        jira_data_center_site_from_provider_config(
            ProviderConfig(role="issue", kind="jira", settings={"site": SITE, "api_version": "2"})
        )


def test_cloud_search_uses_the_jql_endpoint() -> None:
    path = jira_data_center_search_path(cloud_site(), jql="project = TEST", max_results=5)

    assert path.startswith("/rest/api/3/search/jql?")


def test_cloud_auth_is_basic_email_and_token() -> None:
    assert client._curl_auth_lines(cloud_site()) == ['user = "user@example.test:test-token"']


def test_cloud_auth_requires_an_email(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("JIRA_EMAIL", "JIRA_USERNAME", "JIRA_USER"):
        monkeypatch.delenv(name, raising=False)

    with pytest.raises(JiraProviderError, match="JIRA_EMAIL"):
        client._curl_auth_lines(cloud_site())


def test_cloud_auth_reads_the_email_from_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("JIRA_EMAIL")
    site = jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings={"site": SITE, "email": "config@example.test"})
    )

    assert client._curl_auth_lines(site) == ['user = "config@example.test:test-token"']


def test_cloud_auth_env_email_overrides_config() -> None:
    site = jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings={"site": SITE, "email": "config@example.test"})
    )

    assert client._curl_auth_lines(site) == ['user = "user@example.test:test-token"']


def test_cloud_auth_falls_back_to_the_keychain(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("JIRA_API_TOKEN")
    looked_up: list[tuple[str, str]] = []

    def keychain(service: str, account: str) -> str:
        looked_up.append((service, account))
        return "keychain-token"

    monkeypatch.setattr(client, "_keychain_token", keychain)

    assert client._curl_auth_lines(cloud_site()) == ['user = "user@example.test:keychain-token"']
    assert looked_up == [("jira-api-token", "user@example.test")]


def test_cloud_auth_without_any_token_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("JIRA_API_TOKEN")
    monkeypatch.setattr(client, "_keychain_token", lambda service, account: None)

    with pytest.raises(JiraProviderError, match="JIRA_API_TOKEN"):
        client._curl_auth_lines(cloud_site())


def test_cloud_fetch_caches_adf_bodies_as_markdown(tmp_path: Path) -> None:
    write_cloud_config(tmp_path)
    comment = {
        "id": "20001",
        "author": {"displayName": "Example User", "accountId": "abc"},
        "body": adf_doc("Comment."),
        "created": "2026-05-15T09:30:00.000+0900",
        "updated": "2026-05-15T09:30:00.000+0900",
    }
    runner = FakeRunner(
        gets={issue_url(): cloud_issue(comments=[comment]), f"{issue_url()}/remotelink": []},
        writes=[{"value": "**Description.**\n"}, {"value": "_Comment._\n"}],
    )

    response = dispatch(tmp_path, runner, "get", issue="TEST-1")

    assert response.payload["body"] == "**Description.**\n"
    assert response.payload["comments"][0]["body"] == "_Comment._\n"
    convert_calls = [json.loads(_data_binary(text)) for text in runner.write_inputs()]
    assert all(call["representation"] == "atlas_doc_format" for call in convert_calls)
    assert all("contentbody/convert/markdown" in text for text in runner.write_inputs())
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    config = load_workflow_config(tmp_path)
    assert config is not None
    site = jira_data_center_site_from_provider_config(config.issues)
    assert cache.issue_file(site, "TEST-1").read_text(encoding="utf-8") == "**Description.**\n"


def test_cloud_create_sends_adf_and_account_id(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_cloud_config(tmp_path)
    converted: list[str] = []

    def to_adf(markdown: str, *, runner: object = None) -> dict[str, object]:
        converted.append(markdown)
        return adf_doc(markdown)

    monkeypatch.setattr(adf, "markdown_to_adf", to_adf)
    runner = FakeRunner(
        gets={
            f"{SITE}/rest/api/3/myself": {"accountId": "acct-1", "displayName": "Me"},
            issue_url(): cloud_issue(),
            f"{issue_url()}/remotelink": [],
        },
        writes=[{"id": "10001", "key": "TEST-1"}, {"value": "Description.\n"}],
    )

    dispatch(tmp_path, runner, "create", title="Cloud issue", body="# Heading", assignee="me")

    assert converted == ["# Heading"]
    created = json.loads(_data_binary(runner.write_inputs()[0]))
    assert created["fields"]["description"] == adf_doc("# Heading")
    assert created["fields"]["assignee"] == {"accountId": "acct-1"}


def test_cloud_comment_is_sent_as_adf(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_cloud_config(tmp_path)
    monkeypatch.setattr(adf, "markdown_to_adf", lambda markdown, runner=None: adf_doc(markdown))
    runner = FakeRunner(
        gets={issue_url(): cloud_issue(), f"{issue_url()}/remotelink": []},
        writes=[{"id": "20002"}, {"value": "Description.\n"}],
    )

    dispatch(tmp_path, runner, "add_comment", issue="TEST-1", body="Looks *good*.", freshness_check=False)

    sent = [json.loads(_data_binary(text)) for text in runner.write_inputs()]
    assert {"body": adf_doc("Looks *good*.")} in sent


def test_cloud_context_drops_wiki_markup_rules(tmp_path: Path) -> None:
    write_cloud_config(tmp_path, extra="    task_review_agent: project:task-reviewer\n")
    config = load_workflow_config(tmp_path)

    context = build_session_policy_context(config, plugin_root=_PLUGIN_ROOT, runtime="claude")

    assert "<jira-format>" not in context
    assert "jira-format-corrector" not in context
    assert "markup check" not in context
    assert "<jira-task-review>" in context


def test_markdown_to_adf_reports_a_missing_node(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    monkeypatch.setattr(adf.shutil, "which", lambda name: None)

    with pytest.raises(JiraProviderError, match="Node.js"):
        adf.markdown_to_adf("text")


def _data_binary(config_text: str) -> str:
    for line in config_text.splitlines():
        if line.startswith("data-binary = "):
            raw = line[len("data-binary = ") :]
            return json.loads(raw)
    raise AssertionError("no data-binary line in curl config")
