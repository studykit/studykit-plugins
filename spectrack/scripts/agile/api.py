"""Jira Software Cloud Agile REST operations.

Paths and payloads follow the Jira Software Cloud REST API. The site and runner
are explicit so this module is shared by Claude Code, Codex, and a shell.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import quote, urlencode

from command import CommandRunner
from issue.jira.client import JiraDataCenterSite, jira_delete, jira_get_json, jira_send_json

AGILE = "/rest/agile/1.0"
SOFTWARE = "/rest/software/1.0"


class AgileError(ValueError):
    """Invalid agile operation input."""


def segment(value: object) -> str:
    return quote(str(value).strip(), safe="")


def with_query(path: str, **params: object) -> str:
    values = {key: str(value).lower() if isinstance(value, bool) else value
              for key, value in params.items() if value is not None}
    return f"{path}{'&' if '?' in path else '?'}{urlencode(values, doseq=True)}" if values else path


def get(site: JiraDataCenterSite, path: str, runner: CommandRunner | None = None) -> Any:
    return jira_get_json(site, path, runner=runner)


def send(site: JiraDataCenterSite, method: str, path: str, body: Mapping[str, Any], runner: CommandRunner | None = None) -> Any:
    return jira_send_json(site, method, path, body, runner=runner)


def delete(site: JiraDataCenterSite, path: str, runner: CommandRunner | None = None) -> Any:
    return jira_delete(site, path, runner=runner)


def pages(site: JiraDataCenterSite, path: str, *, runner: CommandRunner | None = None,
          max_results: int = 50, page_token: str | None = None, start_at: int | None = None,
          all_pages: bool = False, token_paged: bool = False) -> Any:
    if max_results < 1:
        raise AgileError("--max-results must be positive")
    if page_token and not token_paged:
        raise AgileError("--page-token is only valid for enhanced issue lists")
    if start_at is not None and token_paged:
        raise AgileError("--start-at is only valid for offset-paged lists")
    collected: list[Any] = []
    seen: set[object] = set()
    while True:
        query = {"maxResults": max_results}
        query["nextPageToken" if token_paged else "startAt"] = page_token if token_paged else start_at
        result = get(site, with_query(path, **query), runner)
        if not all_pages or not isinstance(result, dict):
            return result
        collected.extend(result.get("issues", result.get("values", [])))
        if token_paged:
            next_token = result.get("nextPageToken")
            if not next_token or next_token in seen:
                break
            seen.add(next_token)
            page_token = next_token
        else:
            if result.get("isLast") is True:
                break
            values = result.get("issues", result.get("values", []))
            if not values:
                break
            start_at = int(result.get("startAt", start_at or 0)) + len(values)
            if start_at in seen:
                break
            seen.add(start_at)
    return {"issues" if "issues" in result else "values": collected, "isLast": True}


def issue_batch(issues: list[str], *, before: str | None = None, after: str | None = None) -> dict[str, Any]:
    if not 1 <= len(issues) <= 50:
        raise AgileError("1 to 50 issues are required")
    if before and after:
        raise AgileError("choose --before or --after")
    body: dict[str, Any] = {"issues": issues}
    if before:
        body["rankBeforeIssue"] = before
    if after:
        body["rankAfterIssue"] = after
    return body


def sprint_name(name: str) -> str:
    if not name or len(name) >= 30:
        raise AgileError("sprint name must be shorter than 30 characters")
    return name


def board_create(site: JiraDataCenterSite, *, name: str, board_type: str, jql: str | None,
                 filter_id: int | None, project: str | None, user_location: bool,
                 runner: CommandRunner | None = None) -> Any:
    if bool(jql) == (filter_id is not None):
        raise AgileError("choose exactly one of --jql or --filter-id")
    if project and user_location:
        raise AgileError("choose --project or --user-location")
    if board_type not in {"scrum", "kanban"}:
        raise AgileError("board type must be scrum or kanban")
    created_filter = None
    if jql:
        created_filter = send(site, "POST", "/rest/api/3/filter", {"name": name, "jql": jql, "sharePermissions": []}, runner)
        filter_id = int(created_filter["id"])
    body: dict[str, Any] = {"name": name, "type": board_type, "filterId": filter_id}
    if project:
        body["location"] = {"type": "project", "projectKeyOrId": project}
    elif user_location:
        body["location"] = {"type": "user"}
    try:
        return send(site, "POST", f"{AGILE}/board", body, runner)
    except Exception as board_error:
        if created_filter:
            try:
                delete(site, f"/rest/api/3/filter/{segment(filter_id)}", runner)
            except Exception as cleanup_error:
                raise AgileError(f"board creation failed: {board_error}; filter {filter_id} cleanup failed: {cleanup_error}") from board_error
        raise


def board_delete(site: JiraDataCenterSite, board_id: str, *, delete_filter: bool,
                 runner: CommandRunner | None = None) -> Any:
    filter_id = None
    if delete_filter:
        config = get(site, f"{AGILE}/board/{segment(board_id)}/configuration", runner)
        filter_id = config["filter"]["id"]
    result = delete(site, f"{AGILE}/board/{segment(board_id)}", runner)
    if filter_id:
        delete(site, f"/rest/api/3/filter/{segment(filter_id)}", runner)
    return result


def board_add(site: JiraDataCenterSite, board_id: str, issues: list[str], *, before: str | None,
              after: str | None, runner: CommandRunner | None = None) -> Any:
    body = issue_batch(issues, before=before, after=after)
    board = get(site, f"{AGILE}/board/{segment(board_id)}", runner)
    if board.get("type") != "kanban":
        raise AgileError("board add requires a kanban board")
    return send(site, "POST", f"{AGILE}/board/{segment(board_id)}/issue", body, runner)


def property_op(site: JiraDataCenterSite, kind: str, object_id: str, action: str,
                key: str | None = None, value: Any = None, runner: CommandRunner | None = None) -> Any:
    base = f"{AGILE}/{kind}/{segment(object_id)}/properties"
    if action == "list":
        return get(site, base, runner)
    if not key:
        raise AgileError("property key is required")
    path = f"{base}/{segment(key)}"
    if action == "get":
        return get(site, path, runner)
    if action == "set":
        return send(site, "PUT", path, value, runner)
    return delete(site, path, runner)
