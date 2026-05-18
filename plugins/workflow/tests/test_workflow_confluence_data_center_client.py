"""Tests for the Confluence Data Center client helpers."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_confluence_data_center_client import (  # noqa: E402
    ConfluenceDataCenterSite,
    ConfluenceProviderError,
    confluence_content_path,
    confluence_content_search_path,
    confluence_create_content_path,
    confluence_data_center_site_from_provider_config,
    confluence_get_json,
    confluence_page_url,
    normalize_confluence_page,
    resolve_confluence_data_center_site,
    _curl_base_config_lines,
)
from workflow_config import load_workflow_config  # noqa: E402


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


def write_confluence_config(
    project: Path,
    *,
    deployment: str = "data-center",
    extra: str = "",
    site_key: str = "site",
    site_value: str = "https://wiki.example.internal",
    space_value: str | None = "ENG",
    space_key: str = "space",
) -> None:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    space_line = f"    {space_key}: {space_value}\n" if space_value is not None else ""
    path.write_text(
        f"""version: 1
providers:
  issues:
    kind: github
  knowledge:
    kind: confluence
    {site_key}: {site_value}
    deployment: {deployment}
{space_line}{extra}""",
        encoding="utf-8",
    )


def site(project: Path) -> ConfluenceDataCenterSite:
    return resolve_confluence_data_center_site(project)


def test_resolve_data_center_site_reads_workflow_config(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, extra="    space_id: \"123456\"\n    parent_page_id: \"987654\"\n")

    resolved = site(tmp_path)

    assert resolved.base_url == "https://wiki.example.internal"
    assert resolved.authority == "wiki.example.internal"
    assert resolved.deployment == "data_center"
    assert resolved.space == "ENG"
    assert resolved.space_id == "123456"
    assert resolved.parent_page_id == "987654"


@pytest.mark.parametrize("site_key", ["site", "base_url", "url", "host", "hostname"])
def test_site_aliases_normalize_to_same_base_url(tmp_path: Path, site_key: str) -> None:
    write_confluence_config(tmp_path, site_key=site_key)
    resolved = site(tmp_path)
    assert resolved.base_url == "https://wiki.example.internal"
    assert resolved.authority == "wiki.example.internal"


@pytest.mark.parametrize("deployment", ["data-center", "data_center", "server", "dc"])
def test_deployment_aliases_normalize_to_data_center(tmp_path: Path, deployment: str) -> None:
    write_confluence_config(tmp_path, deployment=deployment)
    assert site(tmp_path).deployment == "data_center"


def test_cloud_deployment_is_rejected(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, deployment="cloud")
    with pytest.raises(ConfluenceProviderError, match="confluence cloud is not supported"):
        site(tmp_path)


def test_space_key_alias_normalizes_to_space(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, space_key="space_key")
    assert site(tmp_path).space == "ENG"


def test_api_version_setting_is_ignored_and_paths_have_no_version_segment(tmp_path: Path) -> None:
    write_confluence_config(tmp_path, extra="    api_version: 1\n")
    resolved = site(tmp_path)

    assert "api_version" not in resolved.to_json()
    assert confluence_content_path(resolved, "42") == "/rest/api/content/42"
    search_path = confluence_content_search_path(resolved, 'type = page AND space = "ENG"')
    assert search_path.startswith("/rest/api/content/search?")
    assert "/v1/" not in search_path
    assert "/2/" not in search_path
    assert confluence_create_content_path(resolved) == "/rest/api/content"


def test_content_path_with_expand_includes_comma_separated_keys(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    path = confluence_content_path(resolved, "42", expand=["space", "version", "body.storage"])
    assert path == "/rest/api/content/42?expand=space,version,body.storage"


def test_search_path_encodes_cql_and_pins_default_expand(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    cql = 'type = page AND space = "ENG" AND text ~ "OAuth"'
    path = confluence_content_search_path(resolved, cql, limit=10)
    assert "cql=type%20%3D%20page%20AND%20space%20%3D%20%22ENG%22%20AND%20text%20~%20%22OAuth%22" in path
    assert "&limit=10" in path
    assert path.endswith("&expand=space,version")


def test_curl_base_config_prefers_bearer_personal_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CONFLUENCE_PERSONAL_TOKEN", "tok-1")
    monkeypatch.setenv("CONFLUENCE_USERNAME", "alice")
    monkeypatch.setenv("CONFLUENCE_PASSWORD", "secret")
    lines = _curl_base_config_lines()
    assert 'header = "Authorization: Bearer tok-1"' in lines
    assert not any(line.startswith("user =") for line in lines)


def test_curl_base_config_accepts_confluence_pat_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CONFLUENCE_PERSONAL_TOKEN", raising=False)
    monkeypatch.setenv("CONFLUENCE_PAT", "alias-tok")
    lines = _curl_base_config_lines()
    assert 'header = "Authorization: Bearer alias-tok"' in lines


def test_curl_base_config_falls_back_to_basic_auth(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CONFLUENCE_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("CONFLUENCE_PAT", raising=False)
    monkeypatch.setenv("CONFLUENCE_USERNAME", "alice")
    monkeypatch.setenv("CONFLUENCE_PASSWORD", "secret")
    lines = _curl_base_config_lines()
    assert 'user = "alice:secret"' in lines
    assert not any(line.startswith('header = "Authorization:') for line in lines)


def test_curl_base_config_accepts_confluence_user_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CONFLUENCE_PERSONAL_TOKEN", raising=False)
    monkeypatch.delenv("CONFLUENCE_PAT", raising=False)
    monkeypatch.delenv("CONFLUENCE_USERNAME", raising=False)
    monkeypatch.setenv("CONFLUENCE_USER", "bob")
    monkeypatch.setenv("CONFLUENCE_PASSWORD", "pw")
    lines = _curl_base_config_lines()
    assert 'user = "bob:pw"' in lines


def test_curl_base_config_with_no_credentials_emits_only_accept_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in (
        "CONFLUENCE_PERSONAL_TOKEN",
        "CONFLUENCE_PAT",
        "CONFLUENCE_USERNAME",
        "CONFLUENCE_USER",
        "CONFLUENCE_PASSWORD",
    ):
        monkeypatch.delenv(name, raising=False)
    assert _curl_base_config_lines() == ['header = "Accept: application/json"']


def test_get_json_invokes_curl_with_config_pipe(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "CONFLUENCE_PERSONAL_TOKEN",
        "CONFLUENCE_PAT",
        "CONFLUENCE_USERNAME",
        "CONFLUENCE_USER",
        "CONFLUENCE_PASSWORD",
    ):
        monkeypatch.delenv(name, raising=False)
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    url = "https://wiki.example.internal/rest/api/content/42"
    args = ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)
    runner = FakeRunner(
        {args: CommandResult(request=CommandRequest(args=args), returncode=0, stdout='{"id": "42"}')}
    )

    payload = confluence_get_json(resolved, "/rest/api/content/42", runner=runner)

    assert payload == {"id": "42"}
    assert runner.requests[0].input_text == 'header = "Accept: application/json"\n'


def test_get_json_raises_on_invalid_json(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    url = "https://wiki.example.internal/rest/api/content/42"
    args = ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)
    runner = FakeRunner(
        {args: CommandResult(request=CommandRequest(args=args), returncode=0, stdout="not-json")}
    )

    with pytest.raises(ConfluenceProviderError, match="not valid JSON"):
        confluence_get_json(resolved, "/rest/api/content/42", runner=runner)


def test_page_url_uses_viewpage_action_form(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    assert confluence_page_url(resolved, "42") == "https://wiki.example.internal/pages/viewpage.action?pageId=42"


def test_normalize_confluence_page_projects_contract_shape(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    page = {
        "id": "42",
        "title": "Page title",
        "space": {"key": "ENG"},
        "version": {"number": 7},
        "body": {"storage": {"value": "<p>body</p>", "representation": "storage"}},
        "metadata": {
            "labels": {
                "results": [
                    {"name": "design"},
                    {"name": "wip"},
                ]
            }
        },
    }

    payload = normalize_confluence_page(page, site=resolved)

    assert payload == {
        "provider": "confluence",
        "kind": "page",
        "page_id": "42",
        "title": "Page title",
        "space": "ENG",
        "version": 7,
        "url": "https://wiki.example.internal/pages/viewpage.action?pageId=42",
        "body": "<p>body</p>",
        "labels": ["design", "wip"],
        "confluence": {
            "deployment": "data_center",
            "site": "https://wiki.example.internal",
        },
    }


def test_normalize_confluence_page_without_body_omits_body(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    resolved = site(tmp_path)
    page = {
        "id": "42",
        "title": "Page title",
        "space": {"key": "ENG"},
        "version": {"number": 7},
        "metadata": {"labels": {"results": []}},
    }
    payload = normalize_confluence_page(page, site=resolved, include_body=False)
    assert "body" not in payload
    assert payload["labels"] == []


def test_site_from_provider_config_rejects_non_confluence_kind(tmp_path: Path) -> None:
    write_confluence_config(tmp_path)
    config = load_workflow_config(tmp_path)
    assert config is not None
    # Force a synthetic non-confluence config to exercise the guard.
    with pytest.raises(ConfluenceProviderError, match="not Confluence"):
        confluence_data_center_site_from_provider_config(
            type(config.knowledge)(role="knowledge", kind="github", settings={})
        )
