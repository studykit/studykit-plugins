#!/usr/bin/env python3
"""Confluence Data Center native knowledge provider."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from workflow_command import CommandRunner, WorkflowCommandError
from workflow_confluence_data_center_client import (
    ConfluenceDataCenterSite,
    ConfluenceProviderError,
    confluence_content_path,
    confluence_content_search_path,
    confluence_create_content_path,
    confluence_get_json,
    confluence_send_json,
    normalize_confluence_page,
    resolve_confluence_data_center_site,
)
from workflow_providers import (
    TRANSPORT_NATIVE,
    KnowledgeProvider,
    ProviderOperationError,
    ProviderRequest,
)


DEFAULT_SEARCH_LIMIT = 25
_METADATA_LABEL_EXPAND = ("space", "version", "metadata.labels")
_FULL_PAGE_EXPAND = ("space", "version", "body.storage", "metadata.labels")
_PRE_FETCH_EXPAND = ("space", "version", "body.storage")
_SEARCH_RESULT_EXPAND = ("space", "version")


class ConfluenceDataCenterKnowledgeNativeProvider(KnowledgeProvider):
    """Native Confluence Data Center knowledge provider backed by REST."""

    def __init__(self, *, runner: CommandRunner | None = None):
        super().__init__(kind="confluence", transport=TRANSPORT_NATIVE)
        self.runner = runner

    def get(self, request: ProviderRequest) -> Mapping[str, Any]:
        page_id = _require_page_id(request, "get")
        include_body = _truthy_default(request.payload.get("include_body"), default=True)
        site = self._resolve_site(request, "get")

        expand = _FULL_PAGE_EXPAND if include_body else _METADATA_LABEL_EXPAND
        page = self._read_page(site, page_id, expand=expand, op="get")
        return normalize_confluence_page(page, site=site, include_body=include_body)

    def metadata(self, request: ProviderRequest) -> Mapping[str, Any]:
        page_id = _require_page_id(request, "metadata")
        site = self._resolve_site(request, "metadata")
        page = self._read_page(site, page_id, expand=_METADATA_LABEL_EXPAND, op="metadata")
        return normalize_confluence_page(page, site=site, include_body=False)

    def search(self, request: ProviderRequest) -> Mapping[str, Any]:
        payload = request.payload
        raw_query = _optional_string(payload.get("query"))
        raw_cql = _optional_string(payload.get("cql"))
        if raw_query and raw_cql:
            raise ProviderOperationError(
                "confluence:search: provide either query or cql, not both"
            )

        limit = _normalize_limit(payload.get("limit"), default=DEFAULT_SEARCH_LIMIT)
        site = self._resolve_site(request, "search")
        resolved_space = (
            _optional_string(payload.get("space"))
            or _optional_string(payload.get("space_key"))
            or site.space
        )
        global_search = _truthy(payload.get("global_search"))
        expand = _expand_list(payload.get("expand"), default=_SEARCH_RESULT_EXPAND)

        if raw_cql:
            cql = raw_cql
            if resolved_space and f'space = "{resolved_space}"' not in cql:
                raise ProviderOperationError(
                    'confluence:search: raw cql must include explicit space = "'
                    f'{resolved_space}" constraint when a space is configured'
                )
            if not resolved_space and not global_search:
                raise ProviderOperationError(
                    "confluence:search: missing space scope "
                    "(set space in config/payload or pass global_search=true)"
                )
        else:
            if raw_query is None:
                raise ProviderOperationError("confluence:search: missing query or cql")
            escaped = _cql_quote(raw_query)
            if resolved_space:
                cql = f'type = page AND space = "{resolved_space}" AND text ~ "{escaped}"'
            elif global_search:
                cql = f'type = page AND text ~ "{escaped}"'
            else:
                raise ProviderOperationError(
                    "confluence:search: missing space scope "
                    "(set space in config/payload or pass global_search=true)"
                )

        path = confluence_content_search_path(site, cql, limit=limit, expand=expand)
        response = self._call_get(site, path, op="search")
        if not isinstance(response, Mapping):
            raise ProviderOperationError("confluence:search: invalid response")

        raw_results = response.get("results")
        results: list[dict[str, Any]] = []
        if isinstance(raw_results, list):
            for entry in raw_results:
                if isinstance(entry, Mapping):
                    results.append(normalize_confluence_page(entry, site=site, include_body=False))

        return {
            "provider": "confluence",
            "kind": "search",
            "cql": cql,
            "start": _int_or(response.get("start"), 0),
            "limit": _int_or(response.get("limit"), limit),
            "size": _int_or(response.get("size"), len(results)),
            "results": results,
            "confluence": {"deployment": site.deployment, "site": site.base_url},
        }

    def create(self, request: ProviderRequest) -> Mapping[str, Any]:
        title = _optional_string(request.payload.get("title"))
        body = _optional_string(request.payload.get("body"))
        if title is None:
            raise ProviderOperationError("confluence:create: missing title")
        if body is None:
            raise ProviderOperationError("confluence:create: missing body")

        site = self._resolve_site(request, "create")
        space_key = (
            _optional_string(request.payload.get("space"))
            or _optional_string(request.payload.get("space_key"))
            or site.space
        )
        if not space_key:
            raise ProviderOperationError(
                "confluence:create: missing space (space_id is not a valid create selector)"
            )

        parent_page_id = (
            _optional_string(request.payload.get("parent_page_id"))
            or site.parent_page_id
        )

        payload: dict[str, Any] = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {"storage": {"value": body, "representation": "storage"}},
        }
        if parent_page_id:
            payload["ancestors"] = [{"id": parent_page_id}]

        path = confluence_create_content_path(site)
        response = self._call_send(site, "POST", path, payload, op="create")
        if not isinstance(response, Mapping):
            raise ProviderOperationError("confluence:create: invalid response")
        return normalize_confluence_page(response, site=site, include_body=True)

    def update(self, request: ProviderRequest) -> Mapping[str, Any]:
        page_id = _require_page_id(request, "update")
        payload_title = _optional_string(request.payload.get("title"))
        payload_body = _optional_string(request.payload.get("body"))
        if payload_title is None and payload_body is None:
            raise ProviderOperationError(
                "confluence:update: nothing to update (provide title and/or body)"
            )

        site = self._resolve_site(request, "update")
        current = self._read_page(site, page_id, expand=_PRE_FETCH_EXPAND, op="update")
        version_obj = current.get("version") if isinstance(current.get("version"), Mapping) else None
        if not isinstance(version_obj, Mapping) or _coerce_int(version_obj.get("number")) is None:
            raise ProviderOperationError("confluence:update: response missing current version")
        current_version = _coerce_int(version_obj.get("number"))
        assert current_version is not None
        space_obj = current.get("space") if isinstance(current.get("space"), Mapping) else None
        space_key = (
            _optional_string(space_obj.get("key")) if isinstance(space_obj, Mapping) else None
        )
        if not space_key:
            raise ProviderOperationError("confluence:update: response missing space")

        current_title = _optional_string(current.get("title"))
        current_body = _extract_storage_value(current.get("body"))

        new_title = payload_title or current_title or ""
        new_body = payload_body if payload_body is not None else (current_body or "")

        put_payload: dict[str, Any] = {
            "id": page_id,
            "type": "page",
            "title": new_title,
            "space": {"key": space_key},
            "version": {"number": current_version + 1},
            "body": {"storage": {"value": new_body, "representation": "storage"}},
        }
        path = confluence_content_path(site, page_id)
        try:
            response = confluence_send_json(site, "PUT", path, put_payload, runner=self.runner)
        except WorkflowCommandError as exc:
            if _is_conflict(exc):
                raise ProviderOperationError("confluence:update: version conflict") from exc
            raise ProviderOperationError(f"confluence:update: request failed: {exc}") from exc
        except ConfluenceProviderError as exc:
            raise ProviderOperationError(f"confluence:update: {exc}") from exc

        if not isinstance(response, Mapping):
            raise ProviderOperationError("confluence:update: invalid response")
        return normalize_confluence_page(response, site=site, include_body=True)

    def _resolve_site(self, request: ProviderRequest, op: str) -> ConfluenceDataCenterSite:
        try:
            return resolve_confluence_data_center_site(request.context.project)
        except ConfluenceProviderError as exc:
            message = str(exc)
            if message.startswith("confluence cloud is not supported"):
                raise ProviderOperationError(message) from exc
            raise ProviderOperationError(f"confluence:{op}: {message}") from exc

    def _read_page(
        self,
        site: ConfluenceDataCenterSite,
        page_id: str,
        *,
        expand: Sequence[str],
        op: str,
    ) -> Mapping[str, Any]:
        path = confluence_content_path(site, page_id, expand=expand)
        response = self._call_get(site, path, op=op)
        if not isinstance(response, Mapping):
            raise ProviderOperationError(f"confluence:{op}: invalid response")
        return response

    def _call_get(self, site: ConfluenceDataCenterSite, path: str, *, op: str) -> Any:
        try:
            return confluence_get_json(site, path, runner=self.runner)
        except ConfluenceProviderError as exc:
            raise ProviderOperationError(f"confluence:{op}: {exc}") from exc
        except WorkflowCommandError as exc:
            raise ProviderOperationError(f"confluence:{op}: request failed: {exc}") from exc

    def _call_send(
        self,
        site: ConfluenceDataCenterSite,
        method: str,
        path: str,
        payload: Mapping[str, Any],
        *,
        op: str,
    ) -> Any:
        try:
            return confluence_send_json(site, method, path, payload, runner=self.runner)
        except ConfluenceProviderError as exc:
            raise ProviderOperationError(f"confluence:{op}: {exc}") from exc
        except WorkflowCommandError as exc:
            raise ProviderOperationError(f"confluence:{op}: request failed: {exc}") from exc


def _require_page_id(request: ProviderRequest, op: str) -> str:
    raw = (
        request.payload.get("page_id")
        if request.payload.get("page_id") is not None
        else request.payload.get("page")
        if request.payload.get("page") is not None
        else request.payload.get("id")
    )
    text = _optional_string(raw)
    if not text:
        raise ProviderOperationError(f"confluence:{op}: missing page_id")
    return text


def _optional_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _truthy_default(value: Any, *, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "on"}:
            return True
        if normalized in {"0", "false", "no", "off"}:
            return False
        return default
    return bool(value)


def _normalize_limit(value: Any, *, default: int) -> int:
    if value is None:
        return default
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ProviderOperationError("confluence:search: limit must be an integer") from exc
    if parsed <= 0:
        raise ProviderOperationError("confluence:search: limit must be positive")
    return parsed


def _expand_list(value: Any, *, default: Sequence[str]) -> Sequence[str]:
    if value is None:
        return tuple(default)
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    if isinstance(value, (list, tuple)):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return tuple(default)


def _cql_quote(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _int_or(value: Any, default: int) -> int:
    parsed = _coerce_int(value)
    return parsed if parsed is not None else default


def _coerce_int(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def _extract_storage_value(body: Any) -> str | None:
    if not isinstance(body, Mapping):
        return None
    storage = body.get("storage")
    if not isinstance(storage, Mapping):
        return None
    value = storage.get("value")
    if value is None:
        return None
    return str(value)


def _is_conflict(exc: WorkflowCommandError) -> bool:
    result = exc.result
    if result is None:
        return False
    stderr = result.stderr or ""
    stdout = result.stdout or ""
    return "409" in stderr or "409" in stdout
