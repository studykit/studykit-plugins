#!/usr/bin/env python3
"""Confluence Data Center site config and REST client helpers."""

from __future__ import annotations

import json
import os
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

from workflow_command import CommandRunner, run_command
from workflow_config import ProviderConfig, WorkflowConfigError, load_workflow_config

DEPLOYMENT_DATA_CENTER = "data_center"


class ConfluenceProviderError(RuntimeError):
    """Raised when Confluence provider data or configuration cannot be handled."""


@dataclass(frozen=True)
class ConfluenceDataCenterSite:
    """Resolved Confluence Data Center / Server site configuration."""

    base_url: str
    authority: str
    space: str | None = None
    space_id: str | None = None
    parent_page_id: str | None = None

    @property
    def deployment(self) -> str:
        return DEPLOYMENT_DATA_CENTER

    def to_json(self) -> dict[str, str]:
        result = {
            "base_url": self.base_url,
            "authority": self.authority,
            "deployment": self.deployment,
        }
        if self.space:
            result["space"] = self.space
        if self.space_id:
            result["space_id"] = self.space_id
        if self.parent_page_id:
            result["parent_page_id"] = self.parent_page_id
        return result


def resolve_confluence_data_center_site(project: Path) -> ConfluenceDataCenterSite:
    """Resolve Confluence Data Center knowledge provider settings from ``.workflow/config.yml``."""

    try:
        config = load_workflow_config(project, require=True)
    except WorkflowConfigError as exc:
        raise ConfluenceProviderError(str(exc)) from exc
    if config is None or config.knowledge.kind != "confluence":
        raise ConfluenceProviderError("workflow knowledge provider is not configured as Confluence")
    return confluence_data_center_site_from_provider_config(config.knowledge)


def confluence_data_center_site_from_provider_config(provider: ProviderConfig) -> ConfluenceDataCenterSite:
    """Resolve normalized Confluence Data Center settings from a knowledge provider config."""

    if provider.kind != "confluence":
        raise ConfluenceProviderError(f"provider config is not Confluence: {provider.kind}")

    settings = dict(provider.settings)
    deployment = _string_setting(settings, "deployment", "type", "edition")
    if deployment is not None and _normalize_deployment(deployment) != DEPLOYMENT_DATA_CENTER:
        raise ConfluenceProviderError(
            "confluence cloud is not supported by this provider; use deployment: data_center"
        )

    raw_site = _string_setting(settings, "site", "base_url", "url", "host", "hostname")
    if raw_site is None:
        raise ConfluenceProviderError(
            "Confluence knowledge provider requires a site, base_url, url, host, or hostname setting"
        )
    base_url, authority = _normalize_base_url(raw_site)

    space = _string_setting(settings, "space", "space_key")
    space_id = _string_setting(settings, "space_id", "spaceId")
    parent_page_id = _string_setting(settings, "parent_page_id", "parentPageId", "parent")

    return ConfluenceDataCenterSite(
        base_url=base_url,
        authority=authority,
        space=space,
        space_id=space_id,
        parent_page_id=parent_page_id,
    )


def confluence_content_path(
    site: ConfluenceDataCenterSite,
    page_id: str,
    *,
    expand: Sequence[str] | None = None,
) -> str:
    """REST path for ``GET /rest/api/content/{id}`` with an optional expand list."""

    escaped_id = quote(_require_page_id(page_id), safe="")
    base = f"/rest/api/content/{escaped_id}"
    if expand:
        return f"{base}?expand={','.join(expand)}"
    return base


def confluence_content_search_path(
    site: ConfluenceDataCenterSite,
    cql: str,
    *,
    limit: int = 25,
    expand: Sequence[str] | None = None,
) -> str:
    """REST path for ``GET /rest/api/content/search`` with URL-encoded CQL."""

    if not cql or not cql.strip():
        raise ConfluenceProviderError("Confluence search requires a non-empty CQL string")
    encoded_cql = quote(cql, safe="")
    expand_value = ",".join(expand) if expand else "space,version"
    return f"/rest/api/content/search?cql={encoded_cql}&limit={int(limit)}&expand={expand_value}"


def confluence_create_content_path(site: ConfluenceDataCenterSite) -> str:
    """REST path for ``POST /rest/api/content``."""

    return "/rest/api/content"


def confluence_get_json(
    site: ConfluenceDataCenterSite,
    path: str,
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Read one Confluence REST resource with curl and parse JSON."""

    url = f"{site.base_url}{path}"
    result = run_command(
        ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url),
        input_text=_curl_config(),
        runner=runner,
    )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ConfluenceProviderError(f"Confluence response was not valid JSON for {url}: {exc}") from exc


def confluence_send_json(
    site: ConfluenceDataCenterSite,
    method: str,
    path: str,
    payload: Mapping[str, Any],
    *,
    runner: CommandRunner | None = None,
) -> Any:
    """Send one Confluence REST JSON mutation with curl and parse any JSON response."""

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
        raise ConfluenceProviderError(f"Confluence response was not valid JSON for {url}: {exc}") from exc


def confluence_page_url(site: ConfluenceDataCenterSite, page_id: str) -> str:
    """Return the canonical Confluence UI URL for one page."""

    return f"{site.base_url}/pages/viewpage.action?pageId={_require_page_id(page_id)}"


def normalize_confluence_page(
    page: Mapping[str, Any],
    *,
    site: ConfluenceDataCenterSite,
    include_body: bool = True,
) -> dict[str, Any]:
    """Project a Confluence REST page object into the provider payload contract."""

    if not isinstance(page, Mapping):
        raise ConfluenceProviderError("Confluence page response was not an object")

    page_id = _string_value(page.get("id"))
    if page_id is None:
        raise ConfluenceProviderError("Confluence page response missing id")
    title = _string_value(page.get("title")) or ""

    space = page.get("space") if isinstance(page.get("space"), Mapping) else {}
    assert isinstance(space, Mapping)
    space_key = _string_value(space.get("key"))

    version_obj = page.get("version") if isinstance(page.get("version"), Mapping) else {}
    assert isinstance(version_obj, Mapping)
    version_number = _int_value(version_obj.get("number"))

    labels = _extract_labels(page.get("metadata"))

    payload: dict[str, Any] = {
        "provider": "confluence",
        "kind": "page",
        "page_id": page_id,
        "title": title,
        "url": confluence_page_url(site, page_id),
        "labels": labels,
        "confluence": {
            "deployment": site.deployment,
            "site": site.base_url,
        },
    }
    if space_key is not None:
        payload["space"] = space_key
    if version_number is not None:
        payload["version"] = version_number
    if include_body:
        body = _extract_storage_body(page.get("body"))
        if body is not None:
            payload["body"] = body
    return payload


def _normalize_base_url(value: str) -> tuple[str, str]:
    raw = value.strip().rstrip("/")
    if not raw:
        raise ConfluenceProviderError("Confluence site setting is empty")
    if "://" not in raw:
        raw = f"https://{raw}"
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ConfluenceProviderError(f"unsupported Confluence site URL: {value}")
    base_path = parsed.path.rstrip("/")
    base_url = f"{parsed.scheme}://{parsed.netloc}{base_path}"
    authority = parsed.netloc.lower()
    return base_url, authority


def _normalize_deployment(value: str) -> str:
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
    if normalized in {
        "",
        "auto",
        "on_premise",
        "on_prem",
        "onprem",
        "premise",
        "server",
        "datacenter",
        "data_center",
        "dc",
    }:
        return DEPLOYMENT_DATA_CENTER
    if normalized in {"cloud", "confluence_cloud"}:
        return "cloud"
    raise ConfluenceProviderError(f"unsupported Confluence deployment: {value}")


def _string_setting(settings: Mapping[str, Any], *names: str) -> str | None:
    for name in names:
        value = settings.get(name)
        if value is not None and str(value).strip():
            return str(value).strip()
    return None


def _require_page_id(value: Any) -> str:
    text = str(value).strip() if value is not None else ""
    if not text:
        raise ConfluenceProviderError("Confluence page id is empty")
    return text


def _string_value(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _int_value(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    text = str(value).strip()
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _extract_storage_body(body: Any) -> str | None:
    if not isinstance(body, Mapping):
        return None
    storage = body.get("storage")
    if not isinstance(storage, Mapping):
        return None
    value = storage.get("value")
    if value is None:
        return None
    return str(value)


def _extract_labels(metadata: Any) -> list[str]:
    if not isinstance(metadata, Mapping):
        return []
    labels = metadata.get("labels")
    if isinstance(labels, Mapping):
        results = labels.get("results")
        labels = results if isinstance(results, list) else []
    if not isinstance(labels, list):
        return []
    extracted: list[str] = []
    for entry in labels:
        if isinstance(entry, Mapping):
            name = entry.get("name") or entry.get("label")
            if name is not None and str(name).strip():
                extracted.append(str(name).strip())
        elif entry is not None and str(entry).strip():
            extracted.append(str(entry).strip())
    return extracted


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
    personal_token = _first_env("CONFLUENCE_PERSONAL_TOKEN", "CONFLUENCE_PAT")
    username = _first_env("CONFLUENCE_USERNAME", "CONFLUENCE_USER")
    password = _first_env("CONFLUENCE_PASSWORD")
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
