#!/usr/bin/env python3
"""Jira Cloud site config and REST client helpers."""

from __future__ import annotations

import functools
import json
import os
import subprocess
import sys
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

from command import CommandRunner, run_command
from config import ProviderConfig, WorkflowConfigError, load_workflow_config
from issue.jira.refs import JiraProviderError, normalize_jira_issue_key

# Issue bodies are ADF, which only REST v3 speaks.
API_VERSION = "3"
DEFAULT_KEYCHAIN_SERVICE = "jira-api-token"
CLOUD_ONLY_MESSAGE = "spectrack supports Jira Cloud only"
_CLOUD_DEPLOYMENT_ALIASES = frozenset({"cloud", "jira_cloud", "atlassian_cloud"})


@dataclass(frozen=True)
class JiraSite:
    """Resolved Jira Cloud site configuration."""

    base_url: str
    authority: str
    api_version: str = API_VERSION
    project: str | None = None
    issue_type: str | None = None
    cache_site: str | None = None
    email: str | None = None

    @property
    def cache_site_segment(self) -> str:
        return self.cache_site or self.authority

    def to_json(self) -> dict[str, str]:
        result = {
            "base_url": self.base_url,
            "authority": self.authority,
        }
        if self.project:
            result["project"] = self.project
        if self.issue_type:
            result["issue_type"] = self.issue_type
        return result


def resolve_jira_site(project: Path) -> JiraSite:
    """Resolve Jira issue provider settings from ``.spectrack/config.yml``."""

    try:
        config = load_workflow_config(project, require=True)
    except WorkflowConfigError as exc:
        raise JiraProviderError(str(exc)) from exc
    if config is None or config.issues.kind != "jira":
        raise JiraProviderError("workflow issue provider is not configured as Jira")
    return jira_site_from_provider_config(config.issues)


def jira_site_from_provider_config(provider: ProviderConfig) -> JiraSite:
    """Resolve normalized Jira settings from an issue provider config.

    Settings left over from a Jira Data Center config fail here rather than
    being ignored, so a stale config cannot silently reach a Cloud site.
    """

    if provider.kind != "jira":
        raise JiraProviderError(f"provider config is not Jira: {provider.kind}")

    settings = dict(provider.settings)
    raw_site = _string_setting(settings, "site", "base_url", "url", "host", "hostname")
    if raw_site is None:
        raise JiraProviderError("Jira issue provider requires a site, base_url, url, host, or hostname setting")
    reject_non_cloud_settings(settings)
    base_url, authority, cache_site = _normalize_base_url(raw_site)
    project = _string_setting(settings, "project", "project_key", "projectKey")
    issue_type = _string_setting(settings, "issue_type", "issueType", "issuetype", "issue_type_name")
    email = _string_setting(settings, "email", "account_email", "accountEmail")
    return JiraSite(
        base_url=base_url,
        authority=authority,
        project=project.upper() if project else None,
        issue_type=issue_type,
        cache_site=cache_site,
        email=email,
    )


def reject_non_cloud_settings(settings: Mapping[str, Any]) -> None:
    """Raise when provider settings describe anything but a Jira Cloud site."""

    deployment = _string_setting(settings, "deployment", "type", "edition")
    if deployment is not None:
        normalized = deployment.strip().lower().replace("-", "_").replace(" ", "_")
        if normalized not in _CLOUD_DEPLOYMENT_ALIASES:
            raise JiraProviderError(f"{CLOUD_ONLY_MESSAGE}: unsupported deployment {deployment!r}")
    raw_api_version = _string_setting(settings, "api_version", "apiVersion", "rest_api_version")
    if raw_api_version is not None and raw_api_version.strip().strip("/") != API_VERSION:
        raise JiraProviderError(
            f"{CLOUD_ONLY_MESSAGE}: REST API version must be {API_VERSION}; got {raw_api_version}"
        )
    raw_site = _string_setting(settings, "site", "base_url", "url", "host", "hostname")
    if raw_site is not None and not is_atlassian_cloud_host(raw_site):
        raise JiraProviderError(f"{CLOUD_ONLY_MESSAGE}: site must be an *.atlassian.net host; got {raw_site}")
    if settings.get("epic_fields") is not None or settings.get("epicFields") is not None:
        raise JiraProviderError(
            f"{CLOUD_ONLY_MESSAGE}: remove providers.issues.epic_fields; epics link through the native parent field"
        )


def is_atlassian_cloud_host(value: str) -> bool:
    raw = value.strip()
    if "://" not in raw:
        raw = f"https://{raw}"
    hostname = urlparse(raw).hostname
    return bool(hostname and hostname.lower().endswith(".atlassian.net"))


def jira_issue_path(site: JiraSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}"


def jira_remote_links_path(site: JiraSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink"


def jira_remote_link_global_id_path(site: JiraSite, issue_key: str, global_id: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink?globalId={quote(global_id, safe='')}"


def jira_remote_link_path(site: JiraSite, issue_key: str, link_id: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    escaped_link_id = quote(str(link_id).strip(), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/remotelink/{escaped_link_id}"


def jira_search_path(
    site: JiraSite,
    *,
    jql: str,
    max_results: int,
    fields: Iterable[str] = (),
) -> str:
    params = [
        f"jql={quote(jql, safe='')}",
        f"maxResults={int(max_results)}",
    ]
    field_list = [field for field in fields if field]
    if field_list:
        params.append(f"fields={quote(','.join(field_list), safe='')}")
    return f"/rest/api/{site.api_version}/search/jql?{'&'.join(params)}"


def jira_issue_links_path(site: JiraSite) -> str:
    return f"/rest/api/{site.api_version}/issueLink"


def jira_issue_link_path(site: JiraSite, link_id: str) -> str:
    escaped_link_id = quote(str(link_id).strip(), safe="")
    return f"/rest/api/{site.api_version}/issueLink/{escaped_link_id}"


def jira_comments_path(site: JiraSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/comment"


def jira_comment_path(site: JiraSite, issue_key: str, comment_id: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    escaped_comment = quote(str(comment_id).strip(), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/comment/{escaped_comment}"


def jira_attachments_path(site: JiraSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/attachments"


def jira_transitions_path(site: JiraSite, issue_key: str) -> str:
    escaped_key = quote(normalize_jira_issue_key(issue_key), safe="")
    return f"/rest/api/{site.api_version}/issue/{escaped_key}/transitions"


def jira_get_json(
    site: JiraSite,
    path: str,
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Read one Jira REST resource with curl and parse JSON."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail-with-body", "--request", "GET", "--config", "-", url),
        input_text=_curl_config(site),
        runner=runner,
    )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def jira_send_json(
    site: JiraSite,
    method: str,
    path: str,
    payload: Mapping[str, Any],
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Send one Jira REST JSON mutation with curl and parse any JSON response."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail-with-body", "--config", "-"),
        input_text=_curl_json_config(site, method=method, url=url, payload=payload),
        runner=runner,
    )
    stdout = result.stdout.strip()
    if not stdout:
        return {}
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def jira_upload_attachments(
    site: JiraSite,
    issue_key: str,
    file_paths: Iterable[str],
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Upload one or more local files to a Jira issue as multipart attachments.

    Jira's attachment endpoint is multipart/form-data (form field ``file``,
    repeatable) and requires the ``X-Atlassian-Token: no-check`` header to
    bypass the XSRF guard — neither fits the JSON mutation helper above.
    """

    paths = [str(path) for path in file_paths]
    if not paths:
        raise JiraProviderError("at least one attachment file is required")
    url = f"{site.base_url}{jira_attachments_path(site, issue_key)}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail", "--config", "-"),
        input_text=_curl_multipart_config(site, url=url, file_paths=paths),
        runner=runner,
    )
    stdout = result.stdout.strip()
    if not stdout:
        return []
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Jira response was not valid JSON for {url}: {exc}") from exc


def jira_download_attachment(
    site: JiraSite,
    content_url: str,
    out_path: str,
    *,
    runner: CommandRunner | None = None,
) -> None:
    """Download one Jira attachment by its absolute content URL to ``out_path``.

    The attachment ``content`` URL is an absolute Jira link (often a redirect
    to a streaming endpoint), so this follows redirects (``--location``) and
    writes the raw bytes out (``--output``). Auth reuses the same basic
    credentials as the JSON helpers; the JSON ``Accept`` header is dropped so
    the binary body is not negotiated away.
    """

    run_command(
        ("curl", "--silent", "--show-error", "--fail", "--location", "--config", "-"),
        input_text=_curl_download_config(site, url=content_url, out_path=out_path),
        runner=runner,
    )


def jira_delete(
    site: JiraSite,
    path: str,
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Send one Jira REST DELETE mutation and parse any JSON response."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail-with-body", "--config", "-"),
        input_text=_curl_method_config(site, method="DELETE", url=url),
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


def _string_setting(settings: Mapping[str, Any], *names: str) -> str | None:
    for name in names:
        value = settings.get(name)
        if value is not None and str(value).strip():
            return str(value).strip()
    return None


def _curl_config(site: JiraSite) -> str:
    lines = _curl_base_config_lines(site)
    return "\n".join(lines) + "\n"


def _curl_json_config(site: JiraSite, *, method: str, url: str, payload: Mapping[str, Any]) -> str:
    lines = _curl_method_config(site, method=method, url=url).rstrip("\n").splitlines()
    lines.extend(
        [
            'header = "Content-Type: application/json"',
            f'data-binary = "{_curl_quote(_format_json_compact(payload))}"',
        ]
    )
    return "\n".join(lines) + "\n"


def _curl_multipart_config(site: JiraSite, *, url: str, file_paths: Iterable[str]) -> str:
    lines = _curl_base_config_lines(site)
    lines.extend(
        [
            'header = "X-Atlassian-Token: no-check"',
            'request = "POST"',
            f'url = "{_curl_quote(url)}"',
        ]
    )
    lines.extend(f'form = "file=@{_curl_quote(path)}"' for path in file_paths)
    return "\n".join(lines) + "\n"


def _curl_download_config(site: JiraSite, *, url: str, out_path: str) -> str:
    lines = _curl_auth_lines(site)
    lines.extend(
        [
            f'output = "{_curl_quote(out_path)}"',
            f'url = "{_curl_quote(url)}"',
        ]
    )
    return "\n".join(lines) + "\n"


def _curl_method_config(site: JiraSite, *, method: str, url: str) -> str:
    lines = _curl_base_config_lines(site)
    lines.extend(
        [
            f'request = "{_curl_quote(method.upper())}"',
            f'url = "{_curl_quote(url)}"',
        ]
    )
    return "\n".join(lines) + "\n"


def _curl_base_config_lines(site: JiraSite) -> list[str]:
    return ['header = "Accept: application/json"', *_curl_auth_lines(site)]


def _curl_auth_lines(site: JiraSite) -> list[str]:
    email, token = _cloud_credentials(site.email)
    return [f'user = "{_curl_quote(email)}:{_curl_quote(token)}"']


def _cloud_credentials(config_email: str | None = None) -> tuple[str, str]:
    """Resolve Jira Cloud basic-auth credentials (account email + API token).

    ``JIRA_EMAIL`` wins over the config ``email`` setting: the config is usually
    committed and shared, so each user must be able to override it. The token
    comes from ``JIRA_API_TOKEN`` or, on macOS, from the login
    Keychain entry for service ``JIRA_KEYCHAIN_SERVICE`` (default
    ``jira-api-token``) and the email as account, so it never has to sit in a
    shell profile.
    """

    email = _first_env("JIRA_EMAIL", "JIRA_USERNAME", "JIRA_USER") or config_email
    if not email:
        raise JiraProviderError(
            "Jira Cloud requires the Atlassian account email: set providers.issues.email or JIRA_EMAIL"
        )
    token = _first_env("JIRA_API_TOKEN") or _keychain_token(
        _first_env("JIRA_KEYCHAIN_SERVICE") or DEFAULT_KEYCHAIN_SERVICE, email
    )
    if not token:
        raise JiraProviderError(
            "Jira Cloud requires an API token: set JIRA_API_TOKEN, or on macOS store it with "
            f"`security add-generic-password -s {DEFAULT_KEYCHAIN_SERVICE} -a <email> -w`"
        )
    return email, token


@functools.cache
def _keychain_token(service: str, account: str) -> str | None:
    if sys.platform != "darwin":
        return None
    try:
        completed = subprocess.run(
            ("security", "find-generic-password", "-s", service, "-a", account, "-w"),
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if completed.returncode != 0:
        return None
    return completed.stdout.strip() or None


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
