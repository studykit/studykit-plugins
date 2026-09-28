"""Command-line interface for Jira Software Cloud Agile REST operations."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from agile import api
from command import CommandRunner, WorkflowCommandError
from config import WorkflowConfigError, load_workflow_config
from env import workflow_project_dir_from_env
from issue.jira.client import jira_data_center_site_from_provider_config
from issue.jira.refs import JiraProviderError


def _pagination(parser: argparse.ArgumentParser, *, token: bool = False) -> None:
    parser.add_argument("--max-results", type=int, default=50)
    parser.add_argument("--page-token" if token else "--start-at", type=str if token else int)
    parser.add_argument("--all", action="store_true", help="fetch every page")


def _issue_options(parser: argparse.ArgumentParser) -> None:
    _pagination(parser, token=True)
    parser.add_argument("--jql")
    parser.add_argument("--fields", help="comma-separated fields")
    parser.add_argument("--reconcile", help="comma-separated issue IDs")
    parser.add_argument("--expand")


def _position(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--before")
    group.add_argument("--after")


def _property(parent: argparse.ArgumentParser, kind: str) -> None:
    commands = parent.add_subparsers(dest="property_action", required=True)
    for action in ("list", "get", "set", "delete"):
        sub = commands.add_parser(action, help=f"{action} {kind} property")
        sub.add_argument("id")
        if action != "list":
            sub.add_argument("key")
        if action == "set":
            sub.add_argument("json", help="JSON value or @file containing JSON")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="agile", description="Jira Software Cloud agile operations")
    root.add_argument("--project", dest="project_dir", type=Path, default=workflow_project_dir_from_env(), help="workflow project directory")
    groups = root.add_subparsers(dest="group", required=True)

    board = groups.add_parser("board", help="boards, their issues and properties")
    b = board.add_subparsers(dest="action", required=True)
    p = b.add_parser("list", help="list boards")
    _pagination(p)
    for flag in ("type", "name", "project"):
        p.add_argument(f"--{flag}")
    p.add_argument("--include-private", action="store_true")
    for action in ("get", "config", "by-filter"):
        p = b.add_parser(action)
        p.add_argument("id")
        if action == "by-filter":
            _pagination(p)
    p = b.add_parser("create", help="create a scrum or kanban board and optionally a private filter")
    p.add_argument("--name", required=True)
    p.add_argument("--type", required=True, choices=("scrum", "kanban"))
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--jql")
    source.add_argument("--filter-id", type=int)
    location = p.add_mutually_exclusive_group()
    location.add_argument("--project")
    location.add_argument("--user-location", action="store_true")
    p = b.add_parser("delete")
    p.add_argument("id")
    p.add_argument("--yes", action="store_true", help="confirm deletion")
    p.add_argument("--delete-filter", action="store_true", help="also delete the board's filter")
    for action in ("issues", "backlog", "epic-issues", "sprint-issues"):
        p = b.add_parser(action)
        p.add_argument("id")
        if action in ("epic-issues", "sprint-issues"):
            p.add_argument("child_id")
        _issue_options(p)
    p = b.add_parser("count", help="approximate issue count")
    p.add_argument("id")
    p.add_argument("--backlog", action="store_true")
    p.add_argument("--jql")
    p = b.add_parser("epics")
    p.add_argument("id")
    p.add_argument("--done", choices=("true", "false"))
    _pagination(p)
    p = b.add_parser("projects")
    p.add_argument("id")
    p.add_argument("--full", action="store_true")
    _pagination(p)
    p = b.add_parser("versions")
    p.add_argument("id")
    p.add_argument("--released", choices=("true", "false"))
    _pagination(p)
    p = b.add_parser("quickfilters")
    p.add_argument("id")
    p.add_argument("child_id", nargs="?")
    _pagination(p)
    p = b.add_parser("features", help="Team-managed boards only")
    p.add_argument("id")
    toggle = p.add_mutually_exclusive_group()
    toggle.add_argument("--enable")
    toggle.add_argument("--disable")
    p = b.add_parser("reports", help="Team-managed boards only")
    p.add_argument("id")
    p = b.add_parser("add", help="move issues onto a kanban board only")
    p.add_argument("id")
    p.add_argument("keys", nargs="+")
    _position(p)
    _property(b.add_parser("property"), "board")

    sprint = groups.add_parser("sprint", help="sprints and their properties")
    s = sprint.add_subparsers(dest="action", required=True)
    p = s.add_parser("list")
    p.add_argument("board")
    p.add_argument("--state", help="future,active,closed")
    _pagination(p)
    p = s.add_parser("get")
    p.add_argument("id")
    p = s.add_parser("issues")
    p.add_argument("id")
    _issue_options(p)
    p = s.add_parser("create")
    p.add_argument("board")
    p.add_argument("--name", required=True)
    for flag in ("start", "end", "goal"):
        p.add_argument(f"--{flag}")
    for action in ("update", "start", "close", "replace"):
        p = s.add_parser(action, help="closed sprints accept only name and goal changes" if action == "update" else None)
        p.add_argument("id")
        if action == "update":
            for flag in ("name", "goal", "start", "end", "state"):
                p.add_argument(f"--{flag}")
        elif action == "start":
            p.add_argument("--start", required=True, help="ISO start date")
            p.add_argument("--end", required=True, help="ISO end date")
        elif action == "replace":
            p.add_argument("--json", required=True, type=Path, help="complete sprint JSON; omitted fields become null")
    for action in ("swap", "add", "delete"):
        p = s.add_parser(action)
        p.add_argument("id")
        if action == "swap":
            p.add_argument("other_id")
        elif action == "add":
            p.add_argument("keys", nargs="+")
            _position(p)
        else:
            p.add_argument("--yes", action="store_true")
    _property(s.add_parser("property"), "sprint")

    backlog = groups.add_parser("backlog")
    bl = backlog.add_subparsers(dest="action", required=True)
    p = bl.add_parser("add")
    p.add_argument("keys", nargs="+")
    p.add_argument("--board")
    _position(p)

    epic = groups.add_parser("epic")
    e = epic.add_subparsers(dest="action", required=True)
    p = e.add_parser("get")
    p.add_argument("id")
    for action in ("issues", "orphans"):
        p = e.add_parser(action)
        if action == "issues":
            p.add_argument("id")
        _issue_options(p)
    p = e.add_parser("update")
    p.add_argument("id")
    for flag in ("name", "summary", "color"):
        p.add_argument(f"--{flag}")
    p.add_argument("--done", choices=("true", "false"))
    for action in ("add", "remove"):
        p = e.add_parser(action)
        if action == "add":
            p.add_argument("id")
        p.add_argument("keys", nargs="+")
    p = e.add_parser("rank")
    p.add_argument("id")
    _position(p)

    issue = groups.add_parser("issue")
    i = issue.add_subparsers(dest="action", required=True)
    p = i.add_parser("get")
    p.add_argument("id")
    p.add_argument("--fields")
    p = i.add_parser("rank")
    p.add_argument("keys", nargs="+")
    _position(p)
    p = i.add_parser("estimate", help="the issue must be on the selected board")
    p.add_argument("id")
    p.add_argument("--board", required=True)
    p.add_argument("value", nargs="?")
    return root


def _list(site: Any, path: str, args: argparse.Namespace, runner: CommandRunner | None, *, token: bool = False) -> Any:
    return api.pages(site, path, runner=runner, max_results=args.max_results,
                     page_token=getattr(args, "page_token", None), start_at=getattr(args, "start_at", None),
                     all_pages=args.all, token_paged=token)


def _issue_path(path: str, args: argparse.Namespace) -> str:
    params: dict[str, Any] = {}
    for arg, param in (("jql", "jql"), ("fields", "fields"), ("reconcile", "reconcileIssues"), ("expand", "expand")):
        value = getattr(args, arg, None)
        if value:
            params[param] = value.split(",") if arg in {"fields", "reconcile"} else value
    return api.with_query(path, **params)


def _json_arg(value: str) -> Any:
    return json.loads(Path(value[1:]).read_text(encoding="utf-8") if value.startswith("@") else value)


def _error_text(exc: Exception) -> str:
    if isinstance(exc, WorkflowCommandError) and exc.result and exc.result.stdout.strip():
        try:
            body = json.loads(exc.result.stdout)
        except json.JSONDecodeError:
            return str(exc)
        if isinstance(body, dict) and (body.get("errorMessages") or body.get("errors")):
            return json.dumps({key: body[key] for key in ("errorMessages", "errors") if body.get(key)}, ensure_ascii=False)
    return str(exc)


def dispatch(site: Any, args: argparse.Namespace, runner: CommandRunner | None = None) -> Any:
    g, a = args.group, args.action
    ag, sw, seg = api.AGILE, api.SOFTWARE, api.segment
    if g == "board":
        if a == "list":
            path = api.with_query(f"{ag}/board", type=args.type, name=args.name, projectKeyOrId=args.project, includePrivate=args.include_private or None)
            return _list(site, path, args, runner)
        if a == "by-filter":
            return _list(site, f"{ag}/board/filter/{seg(args.id)}", args, runner)
        if a == "create":
            return api.board_create(site, name=args.name, board_type=args.type, jql=args.jql,
                                    filter_id=args.filter_id, project=args.project, user_location=args.user_location, runner=runner)
        if a == "delete":
            if not args.yes:
                raise api.AgileError("board delete requires --yes")
            return api.board_delete(site, args.id, delete_filter=args.delete_filter, runner=runner)
        if a == "add":
            return api.board_add(site, args.id, args.keys, before=args.before, after=args.after, runner=runner)
        if a == "property":
            return api.property_op(site, "board", args.id, args.property_action, getattr(args, "key", None),
                                   _json_arg(args.json) if args.property_action == "set" else None, runner)
        base = f"{ag}/board/{seg(args.id)}"
        if a == "get": return api.get(site, base, runner)
        if a == "config": return api.get(site, base + "/configuration", runner)
        if a in {"issues", "backlog", "epic-issues", "sprint-issues"}:
            suffix = "/issue" if a == "issues" else "/backlog" if a == "backlog" else f"/{'epic' if a == 'epic-issues' else 'sprint'}/{seg(args.child_id)}/issue"
            return _list(site, _issue_path(f"{sw}/board/{seg(args.id)}{suffix}", args), args, runner, token=True)
        if a == "count":
            suffix = "/backlog" if args.backlog else "/issue"
            return api.get(site, api.with_query(f"{sw}/board/{seg(args.id)}{suffix}/approximate-count", jql=args.jql), runner)
        if a == "epics": return _list(site, api.with_query(base + "/epic", done=args.done), args, runner)
        if a == "projects": return _list(site, base + ("/project/full" if args.full else "/project"), args, runner)
        if a == "versions": return _list(site, api.with_query(base + "/version", released=args.released), args, runner)
        if a == "quickfilters":
            if args.child_id: return api.get(site, base + f"/quickfilter/{seg(args.child_id)}", runner)
            return _list(site, base + "/quickfilter", args, runner)
        if a == "features":
            feature = args.enable or args.disable
            if feature:
                return api.send(site, "PUT", base + "/features", {"boardId": int(args.id), "feature": feature, "enabling": bool(args.enable)}, runner)
            return api.get(site, base + "/features", runner)
        if a == "reports": return api.get(site, base + "/reports", runner)
    if g == "sprint":
        if a == "list": return _list(site, api.with_query(f"{ag}/board/{seg(args.board)}/sprint", state=args.state), args, runner)
        if a == "create":
            body = {"originBoardId": int(args.board), "name": api.sprint_name(args.name)}
            body.update({key: value for key, value in (("startDate", args.start), ("endDate", args.end), ("goal", args.goal)) if value is not None})
            return api.send(site, "POST", ag + "/sprint", body, runner)
        if a == "property":
            return api.property_op(site, "sprint", args.id, args.property_action, getattr(args, "key", None),
                                   _json_arg(args.json) if args.property_action == "set" else None, runner)
        base = f"{ag}/sprint/{seg(args.id)}"
        if a == "get": return api.get(site, base, runner)
        if a == "issues": return _list(site, _issue_path(f"{sw}/sprint/{seg(args.id)}/issue", args), args, runner, token=True)
        if a == "update":
            body = {key: value for key, value in (("name", args.name), ("goal", args.goal), ("startDate", args.start), ("endDate", args.end), ("state", args.state)) if value is not None}
            if "name" in body: api.sprint_name(body["name"])
            if not body: raise api.AgileError("sprint update requires at least one field")
            return api.send(site, "POST", base, body, runner)
        if a == "replace":
            body = json.loads(args.json.read_text(encoding="utf-8"))
            if not isinstance(body, dict): raise api.AgileError("sprint JSON must be an object")
            if "name" in body and body["name"] is not None: api.sprint_name(body["name"])
            return api.send(site, "PUT", base, body, runner)
        if a == "start": return api.send(site, "POST", base, {"state": "active", "startDate": args.start, "endDate": args.end}, runner)
        if a == "close": return api.send(site, "POST", base, {"state": "closed"}, runner)
        if a == "swap": return api.send(site, "POST", base + "/swap", {"sprintToSwapWith": int(args.other_id)}, runner)
        if a == "add": return api.send(site, "POST", base + "/issue", api.issue_batch(args.keys, before=args.before, after=args.after), runner)
        if a == "delete":
            if not args.yes: raise api.AgileError("sprint delete requires --yes")
            return api.delete(site, base, runner)
    if g == "backlog" and a == "add":
        if (args.before or args.after) and not args.board: raise api.AgileError("ranking backlog issues requires --board")
        path = f"{ag}/backlog/{seg(args.board)}/issue" if args.board else f"{ag}/backlog/issue"
        return api.send(site, "POST", path, api.issue_batch(args.keys, before=args.before, after=args.after), runner)
    if g == "epic":
        base = f"{ag}/epic/{seg(args.id)}" if hasattr(args, "id") else f"{ag}/epic/none"
        if a == "get": return api.get(site, base, runner)
        if a == "issues": return _list(site, _issue_path(f"{sw}/epic/{seg(args.id)}/issue", args), args, runner, token=True)
        if a == "orphans": return _list(site, _issue_path(f"{sw}/epic/none/issue", args), args, runner, token=True)
        if a == "update":
            body = {key: value for key, value in (("name", args.name), ("summary", args.summary)) if value is not None}
            if args.color:
                if args.color not in {f"color_{i}" for i in range(1, 10)}: raise api.AgileError("color must be color_1 through color_9")
                body["color"] = {"key": args.color}
            if args.done is not None: body["done"] = args.done == "true"
            if not body: raise api.AgileError("epic update requires at least one field")
            return api.send(site, "POST", base, body, runner)
        if a == "add": return api.send(site, "POST", base + "/issue", api.issue_batch(args.keys), runner)
        if a == "remove": return api.send(site, "POST", f"{ag}/epic/none/issue", api.issue_batch(args.keys), runner)
        if a == "rank":
            if not (args.before or args.after): raise api.AgileError("epic rank requires --before or --after")
            return api.send(site, "PUT", base + "/rank", {"rankBeforeEpic" if args.before else "rankAfterEpic": args.before or args.after}, runner)
    if g == "issue":
        base = f"{ag}/issue/{seg(args.id)}" if hasattr(args, "id") else f"{ag}/issue"
        if a == "get": return api.get(site, api.with_query(base, fields=args.fields), runner)
        if a == "rank":
            if not (args.before or args.after): raise api.AgileError("issue rank requires --before or --after")
            return api.send(site, "PUT", ag + "/issue/rank", api.issue_batch(args.keys, before=args.before, after=args.after), runner)
        if a == "estimate":
            path = api.with_query(base + "/estimation", boardId=args.board)
            return api.send(site, "PUT", path, {"value": args.value}, runner) if args.value is not None else api.get(site, path, runner)
    raise api.AgileError("unknown agile operation")


def main(argv: list[str] | None = None, *, stdout: TextIO | None = None, stderr: TextIO | None = None,
         runner: CommandRunner | None = None) -> int:
    out, err = stdout or sys.stdout, stderr or sys.stderr
    try:
        args = parser().parse_args(argv)
        config = load_workflow_config(args.project_dir, require=True)
        if config is None or config.issues.kind != "jira":
            raise api.AgileError("agile requires a Jira Cloud issue provider")
        site = jira_data_center_site_from_provider_config(config.issues)
        if not site.is_cloud:
            raise api.AgileError("agile supports Jira Cloud only")
        result = dispatch(site, args, runner)
        print(json.dumps(result, indent=2, ensure_ascii=False), file=out)
        return 0
    except (api.AgileError, JiraProviderError, WorkflowConfigError, WorkflowCommandError, OSError, ValueError) as exc:
        print(f"agile: {_error_text(exc)}", file=err)
        return 1
