#!/usr/bin/env python3
"""Jira Data Center site config and REST client helpers."""

from __future__ import annotations

import json
import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

from workflow_command import CommandRunner, run_command
from workflow_config import ProviderConfig, WorkflowConfigError, load_workflow_config
from issue.jira.refs import JiraProviderError, normalize_jira_issue_key

DEPLOYMENT_DATA_CENTER = "data_center"


@dataclass(frozen=True)
class JiraDataCenterSite:
    """Resolved Jira Data Center or Server site configuration."""

    base_url: str
    authority: str
    api_version: str = "2"
    project: str | None = None
    issue_type: str | None = None
    cache_site: str | None = None

    @property
    def deployment(self) -> str:
        return DEPLOYMENT_DATA_CENTER

    @property
    def cache_site_segment(self) -> str:
        return self.cache_site or self.authority

    def to_json(self) -> dict[str, str]:
        result = {
            "base_url": self.base_url,
            "authority": self.authority,
            "deployment": self.deployment,
            "api_version": self.api_version,
        }
        if self.project:
            result["project"] = self.project
        if self.issue_type:
            result["issue_type"] = self.issue_type
        return result


def resolve_jira_data_center_site(project: Path) -> JiraDataCenterSite:
    """Resolve Jira Data Center issue provider settings from ``.workflow/config.yml``."""

    try:
        config = load_workflow_config(project, require=True)
    except WorkflowConfigError as exc:
        raise JiraProviderError(str(exc)) from exc
    if config is None or config.issues.kind != "jira":
        raise JiraProviderError("workflow issue provider is not configured as Jira")
    return jira_data_center_site_from_provider_config(config.issues)


def jira_data_center_site_from_provider_config(provider: ProviderConfig) -> JiraDataCenterSite:
    """Resolve normalized Jira Data Center settings from an issue provider config."""

    if provider.kind != "jira":
        raise JiraProviderError(f"provider config is not Jira: {provider.kind}")

    settings = dict(provider.settings)
    deployment = _string_setting(settings, "deployment", "type", "edition")
    if deployment is not None and _normalize_deployment(deployment) != DEPLOYMENT_DATA_CENTER:
        raise JiraProviderError("Jira Cloud is out of scope for this provider; use a Data Center/on-premise site")

    raw_site = _string_setting(settings, "site", "base_url", "url", "host", "hostname")
    if raw_site is None:
        raise JiraProviderError("Jira issue provider requires a site, base_url, url, host, or hostname setting")
    base_url, authority, cache_site = _normalize_base_url(raw_site)

    api_version = _string_setting(settings, "api_version", "apiVersion", "rest_api_version") or "2"
    project = _string_setting(settings, "project", "project_key", "projectKey")
    issue_type = _string_setting(settings, "issue_type", "issueType", "issuetype", "issue_type_name")
    return JiraDataCenterSite(
        base_url=base_url,
        authority=authority,
        api_version=api_version.strip().strip("/") or "2",
        project=project.upper() if project else None,
        issue_type=issue_type,
        cache_site=cache_site,
    )


def jira_data_center_issue_path(site: JiraDataCenterSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}"


def jira_data_center_remote_links_path(site: JiraDataCenterSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink"


def jira_data_center_remote_link_global_id_path(site: JiraDataCenterSite, issue_key: str, global_id: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink?globalId={quote(global_id, safe='')}"


def jira_data_center_remote_link_path(site: JiraDataCenterSite, issue_key: str, link_id: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    escaped_link_id = quote(str(link_id).strip(), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink/{escaped_link_id}"


def jira_data_center_issue_links_path(site: JiraDataCenterSite) -> str:
    return f"/rest/api/{site.api_version}/issueLink"


def jira_data_center_issue_link_path(site: JiraDataCenterSite, link_id: str) -> str:
    escaped_link_id = quote(str(link_id).strip(), safe="")
    return f"/rest/api/{site.api_version}/issueLink/{escaped_link_id}"


def jira_data_center_comments_path(site: JiraDataCenterSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/comment"


def jira_data_center_transitions_path(site: JiraDataCenterSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/transitions"


def jira_data_center_createmeta_path(
    site: JiraDataCenterSite,
    *,
    project_key: str,
    expand_fields: bool = False,
) -> str:
    escaped_project = quote(project_key.strip().upper(), safe="")
    suffix = "&expand=projects.issuetypes.fields" if expand_fields else ""
    return f"/rest/api/{site.api_version}/issue/createmeta?projectKeys={escaped_project}{suffix}"


def jira_get_json(
    site: JiraDataCenterSite,
    path: str,
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Read one Jira REST resource with curl and parse JSON."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url),
        input_text=_curl_config(),
        runner=runner,
    )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def jira_send_json(
    site: JiraDataCenterSite,
    method: str,
    path: str,
    payload: Mapping[str, Any],
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Send one Jira REST JSON mutation with curl and parse any JSON response."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail", "--config", "-"),
        input_text=_curl_json_config(method=method, url=url, payload=payload),
        runner=runner,
    )
    stdout = result.stdout.strip()
    if not stdout:
        return {}
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def jira_delete(
    site: JiraDataCenterSite,
    path: str,
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Send one Jira REST DELETE mutation and parse any JSON response."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail", "--config", "-"),
        input_text=_curl_method_config(method="DELETE", url=url),
        runner=runner,
    )
    stdout = result.stdout.strip()
    if not stdout:
        return {}
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def _normalize_base_url(value: str) -> tuple[str, str, str]:
    raw = value.strip().rstrip("/")
    if not raw:
        raise JiraProviderError("Jira site setting is empty")
    if "://" not in raw:
        raw = f"https://{raw}"
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise JiraProviderError(f"unsupported Jira site URL: {value}")
    base_path = parsed.path.rstrip("/")
    base_url = f"{parsed.scheme}://{parsed.netloc}{base_path}"
    authority = parsed.netloc.lower()
    cache_site = authority if not base_path else f"{authority}{base_path.replace('/', '-')}"
    return base_url, authority, cache_site


def _normalize_deployment(value: str) -> str:
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
    if normalized in {"", "auto", "on_premise", "on_prem", "onprem", "premise", "server", "datacenter", "data_center", "dc"}:
        return DEPLOYMENT_DATA_CENTER
    if normalized in {"cloud", "jira_cloud"}:
        return "cloud"
    raise JiraProviderError(f"unsupported Jira deployment: {value}")


def _string_setting(settings: Mapping[str, Any], *names: str) -> str | None:
    for name in names:
        value = settings.get(name)
        if value is not None and str(value).strip():
            return str(value).strip()
    return None


def _curl_config() -> str:
    lines = _curl_base_config_lines()
    return "\n".join(lines) + "\n"


def _curl_json_config(*, method: str, url: str, payload: Mapping[str, Any]) -> str:
    lines = _curl_method_config(method=method, url=url).rstrip("\n").splitlines()
    lines.extend(
        [
            'header = "Content-Type: application/json"',
            f'data-binary = "{_curl_quote(_format_json_compact(payload))}"',
        ]
    )
    return "\n".join(lines) + "\n"


def _curl_method_config(*, method: str, url: str) -> str:
    lines = _curl_base_config_lines()
    lines.extend(
        [
            f'request = "{_curl_quote(method.upper())}"',
            f'url = "{_curl_quote(url)}"',
        ]
    )
    return "\n".join(lines) + "\n"


def _curl_base_config_lines() -> list[str]:
    lines = ['header = "Accept: application/json"']
    personal_token = _first_env("JIRA_PERSONAL_TOKEN", "JIRA_PAT")
    username = _first_env("JIRA_USERNAME", "JIRA_USER")
    password = _first_env("JIRA_PASSWORD")
    if personal_token:
        lines.append(f'header = "Authorization: Bearer {_curl_quote(personal_token)}"')
    elif username and password:
        lines.append(f'user = "{_curl_quote(username)}:{_curl_quote(password)}"')
    return lines


def _first_env(*names: str) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


def _curl_quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _format_json_compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
