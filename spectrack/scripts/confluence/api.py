"""Confluence Cloud page REST operations.

Pages, spaces, and children use REST v2. CQL search and positional moves have
no v2 equivalent (v2 page update can only re-parent within one space), so those
two stay on v1. Confluence shares the Jira Cloud site and credentials: both
products live on the same ``*.atlassian.net`` host.

Bodies travel as ADF. Markdown is converted with the same transformer the Jira
Cloud provider uses, so a Markdown round trip drops what that converter cannot
express (macros, layouts, panels); ``adf`` keeps the page lossless.
"""
from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any
from urllib.parse import quote, urlencode

from command import CommandRunner
from issue.jira.adf import adf_to_markdown, is_adf_document, markdown_to_adf
from issue.jira.client import JiraDataCenterSite, jira_get_json, jira_send_json

V2 = "/wiki/api/v2"
V1 = "/wiki/rest/api"
FORMATS = ("markdown", "adf", "storage")
MOVE_POSITIONS = {"parent": "append", "before": "before", "after": "after"}


class ConfluenceError(ValueError):
    """Invalid Confluence operation input or unexpected response."""


def segment(value: object) -> str:
    return quote(str(value).strip(), safe="")


def with_query(path: str, **params: object) -> str:
    values = {key: value for key, value in params.items() if value is not None}
    return f"{path}{'&' if '?' in path else '?'}{urlencode(values, doseq=True)}" if values else path


def collect(site: JiraDataCenterSite, path: str, *, runner: CommandRunner | None = None,
            all_pages: bool = False) -> Any:
    """Read one page of results, or follow ``_links.next`` cursors to the end."""

    result = jira_get_json(site, path, runner=runner)
    if not all_pages or not isinstance(result, dict):
        return result
    collected = list(result.get("results", []))
    seen: set[str] = set()
    while True:
        next_path = (result.get("_links") or {}).get("next")
        if not next_path or next_path in seen:
            break
        seen.add(next_path)
        # v2 links carry the /wiki prefix; v1 links are relative to it.
        result = jira_get_json(site, next_path if next_path.startswith("/wiki/") else f"/wiki{next_path}", runner=runner)
        collected.extend(result.get("results", []))
    return {"results": collected}


def space_id(site: JiraDataCenterSite, key: str, runner: CommandRunner | None = None) -> str:
    result = jira_get_json(site, with_query(f"{V2}/spaces", keys=key), runner=runner)
    spaces = result.get("results", []) if isinstance(result, dict) else []
    if not spaces:
        raise ConfluenceError(f"no Confluence space with key {key}")
    return str(spaces[0]["id"])


def get_page(site: JiraDataCenterSite, page_id: str, *, body_format: str | None = None,
             version: int | None = None, runner: CommandRunner | None = None) -> dict[str, Any]:
    wire = None if body_format is None else "storage" if body_format == "storage" else "atlas_doc_format"
    path = with_query(f"{V2}/pages/{segment(page_id)}", **{"body-format": wire, "version": version})
    page = jira_get_json(site, path, runner=runner)
    if not isinstance(page, dict):
        raise ConfluenceError(f"unexpected Confluence page response for {page_id}")
    return page


def read_body(site: JiraDataCenterSite, page: Mapping[str, Any], body_format: str,
              runner: CommandRunner | None = None) -> Any:
    """Return the page body as Markdown text, an ADF object, or storage XHTML."""

    body = page.get("body") or {}
    if body_format == "storage":
        return (body.get("storage") or {}).get("value", "")
    document = _adf_value(body)
    if body_format == "adf":
        return document
    return adf_to_markdown(site, document, runner=runner)


def write_body(text: str, body_format: str, runner: CommandRunner | None = None) -> dict[str, str]:
    if body_format == "storage":
        return {"representation": "storage", "value": text}
    if body_format == "adf":
        try:
            document = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ConfluenceError(f"ADF body is not valid JSON: {exc}") from exc
        if not is_adf_document(document):
            raise ConfluenceError('ADF body must be a document object ({"type": "doc", ...})')
    else:
        document = markdown_to_adf(text, runner=runner)
    return {"representation": "atlas_doc_format", "value": json.dumps(document, ensure_ascii=False)}


def summarize(page: Mapping[str, Any]) -> dict[str, Any]:
    links = page.get("_links") or {}
    summary = {key: page.get(key) for key in ("id", "title", "status", "spaceId", "parentId")}
    summary["version"] = (page.get("version") or {}).get("number")
    if links.get("webui"):
        summary["url"] = f"{links.get('base', '')}{links['webui']}"
    return summary


def create_page(site: JiraDataCenterSite, *, space: str, title: str, parent: str | None,
                body: dict[str, str] | None, draft: bool, runner: CommandRunner | None = None) -> Any:
    payload: dict[str, Any] = {"spaceId": space, "status": "draft" if draft else "current", "title": title}
    if parent:
        payload["parentId"] = parent
    if body:
        payload["body"] = body
    return jira_send_json(site, "POST", f"{V2}/pages", payload, runner=runner)


def update_page(site: JiraDataCenterSite, page_id: str, *, title: str | None, body: dict[str, str] | None,
                expected_version: int | None, message: str | None,
                runner: CommandRunner | None = None) -> Any:
    """Publish a new page version; v2 requires a body, so an unchanged one is resent."""

    if title is None and body is None:
        raise ConfluenceError("page update requires --title or --body")
    current = get_page(site, page_id, body_format=None if body else "adf", runner=runner)
    number = (current.get("version") or {}).get("number")
    if not isinstance(number, int):
        raise ConfluenceError(f"page {page_id} has no version number")
    if expected_version is not None and number != expected_version:
        raise ConfluenceError(
            f"page {page_id} is at version {number}, not {expected_version}; re-read it before updating"
        )
    if body is None:
        body = {"representation": "atlas_doc_format",
                "value": json.dumps(_adf_value(current.get("body") or {}), ensure_ascii=False)}
    version: dict[str, Any] = {"number": number + 1}
    if message:
        version["message"] = message
    payload = {"id": str(current.get("id", page_id)), "status": current.get("status") or "current",
               "title": title if title is not None else current.get("title"), "body": body, "version": version}
    return jira_send_json(site, "PUT", f"{V2}/pages/{segment(page_id)}", payload, runner=runner)


def move_page(site: JiraDataCenterSite, page_id: str, relation: str, target: str,
              runner: CommandRunner | None = None) -> Any:
    position = MOVE_POSITIONS[relation]
    path = f"{V1}/content/{segment(page_id)}/move/{position}/{segment(target)}"
    return jira_send_json(site, "PUT", path, {}, runner=runner)


def _adf_value(body: Mapping[str, Any]) -> dict[str, Any]:
    value = (body.get("atlas_doc_format") or {}).get("value")
    if not value:
        return {"type": "doc", "version": 1, "content": []}
    document = json.loads(value) if isinstance(value, str) else value
    if not is_adf_document(document):
        raise ConfluenceError("Confluence returned a body that is not an ADF document")
    return document
