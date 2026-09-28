"""Command-line interface for Confluence Cloud page operations."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

from command import CommandRunner, WorkflowCommandError
from config import WorkflowConfigError, load_workflow_config
from confluence import api
from env import workflow_project_dir_from_env
from issue.jira.client import jira_data_center_site_from_provider_config, jira_get_json
from issue.jira.refs import JiraProviderError

FORMAT_HELP = ("body format: markdown (default; converted through ADF, so macros and layouts "
               "the converter cannot express are dropped), adf (lossless JSON), or storage (XHTML)")


def _pagination(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--all", action="store_true", help="follow cursors and fetch every page of results")


def _format(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=api.FORMATS, default="markdown", help=FORMAT_HELP)


def _space(parser: argparse.ArgumentParser, *, required: bool) -> None:
    group = parser.add_mutually_exclusive_group(required=required)
    group.add_argument("--space", help="space key")
    group.add_argument("--space-id", help="numeric space ID")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="confluence", description="Confluence Cloud pages on the Jira Cloud site",
        epilog="Page IDs are the numeric IDs in page URLs (/pages/<id>/...). Output is JSON.")
    root.add_argument("--project", dest="project_dir", type=Path, default=workflow_project_dir_from_env(), help="workflow project directory")
    groups = root.add_subparsers(dest="group", required=True)

    space = groups.add_parser("space", help="find spaces and their IDs")
    s = space.add_subparsers(dest="action", required=True)
    p = s.add_parser("list")
    p.add_argument("--keys", help="comma-separated space keys")
    _pagination(p)
    p = s.add_parser("get")
    p.add_argument("key")

    page = groups.add_parser("page", help="read, search, create, update, and move pages")
    g = page.add_subparsers(dest="action", required=True)
    p = g.add_parser("get", help="page metadata and body")
    p.add_argument("id")
    _format(p)
    p.add_argument("--version", type=int, help="read a historical version")
    p.add_argument("--output", type=Path, help="write the body to this file and print only metadata")
    p = g.add_parser("search", help="search content with CQL", epilog='example: \'space = DOC and type = page and title ~ "setup"\'')
    p.add_argument("cql")
    _pagination(p)
    p = g.add_parser("children", help="direct children of a page")
    p.add_argument("id")
    _pagination(p)
    p = g.add_parser("create")
    _space(p, required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--parent", help="parent page ID; defaults to the space homepage")
    p.add_argument("--body", help="body file, or - for stdin")
    _format(p)
    p.add_argument("--draft", action="store_true", help="create an unpublished draft")
    p = g.add_parser(
        "update", help="publish a new version with a new title and/or body",
        description="Publish a new page version. Pass --expected-version with the version you read "
                    "so a concurrent edit is refused instead of overwritten.")
    p.add_argument("id")
    p.add_argument("--title")
    p.add_argument("--body", help="body file, or - for stdin; omit to keep the current body")
    _format(p)
    p.add_argument("--expected-version", type=int, help="refuse unless the page is still at this version")
    p.add_argument("--message", help="version comment")
    p = g.add_parser("move", help="re-parent or reorder a page, across spaces too")
    p.add_argument("id")
    target = p.add_mutually_exclusive_group(required=True)
    target.add_argument("--parent", help="make the page the last child of this page")
    target.add_argument("--before", help="place the page just before this sibling")
    target.add_argument("--after", help="place the page just after this sibling")
    return root


def _read_text(value: str) -> str:
    return sys.stdin.read() if value == "-" else Path(value).read_text(encoding="utf-8")


def _error_text(exc: Exception) -> str:
    if isinstance(exc, WorkflowCommandError) and exc.result and exc.result.stdout.strip():
        try:
            body = json.loads(exc.result.stdout)
        except json.JSONDecodeError:
            return str(exc)
        if isinstance(body, dict):
            if body.get("errors"):
                return json.dumps(body["errors"], ensure_ascii=False)
            if body.get("message"):
                return str(body["message"])
    return str(exc)


def dispatch(site: Any, args: argparse.Namespace, runner: CommandRunner | None = None) -> Any:
    g, a = args.group, args.action
    if getattr(args, "limit", 1) < 1:
        raise api.ConfluenceError("--limit must be positive")
    if g == "space":
        if a == "get":
            return jira_get_json(site, f"{api.V2}/spaces/{api.space_id(site, args.key, runner)}", runner=runner)
        keys = args.keys.split(",") if args.keys else None
        return api.collect(site, api.with_query(f"{api.V2}/spaces", keys=keys, limit=args.limit), runner=runner, all_pages=args.all)
    if a == "get":
        page = api.get_page(site, args.id, body_format=args.format, version=args.version, runner=runner)
        body = api.read_body(site, page, args.format, runner)
        result = api.summarize(page)
        if args.output:
            args.output.write_text(json.dumps(body, indent=2, ensure_ascii=False) if args.format == "adf" else body, encoding="utf-8")
            result["body_file"] = str(args.output)
        else:
            result["body"] = body
        return {**result, "format": args.format}
    if a == "search":
        return api.collect(site, api.with_query(f"{api.V1}/search", cql=args.cql, limit=args.limit), runner=runner, all_pages=args.all)
    if a == "children":
        return api.collect(site, api.with_query(f"{api.V2}/pages/{api.segment(args.id)}/direct-children", limit=args.limit), runner=runner, all_pages=args.all)
    if a == "create":
        space = args.space_id or api.space_id(site, args.space, runner)
        body = api.write_body(_read_text(args.body), args.format, runner) if args.body else None
        return api.summarize(api.create_page(site, space=space, title=args.title, parent=args.parent, body=body, draft=args.draft, runner=runner))
    if a == "update":
        body = api.write_body(_read_text(args.body), args.format, runner) if args.body else None
        return api.summarize(api.update_page(site, args.id, title=args.title, body=body, expected_version=args.expected_version,
                                             message=args.message, runner=runner))
    if a == "move":
        relation = "parent" if args.parent else "before" if args.before else "after"
        api.move_page(site, args.id, relation, args.parent or args.before or args.after, runner)
        return api.summarize(api.get_page(site, args.id, runner=runner))
    raise api.ConfluenceError("unknown confluence operation")


def main(argv: list[str] | None = None, *, stdout: TextIO | None = None, stderr: TextIO | None = None,
         runner: CommandRunner | None = None) -> int:
    out, err = stdout or sys.stdout, stderr or sys.stderr
    try:
        args = parser().parse_args(argv)
        config = load_workflow_config(args.project_dir, require=True)
        if config is None or config.issues.kind != "jira":
            raise api.ConfluenceError("confluence requires a Jira Cloud issue provider")
        site = jira_data_center_site_from_provider_config(config.issues)
        if not site.is_cloud:
            raise api.ConfluenceError("confluence supports Confluence Cloud only")
        result = dispatch(site, args, runner)
        print(json.dumps(result, indent=2, ensure_ascii=False), file=out)
        return 0
    except (api.ConfluenceError, JiraProviderError, WorkflowConfigError, WorkflowCommandError, OSError, ValueError) as exc:
        print(f"confluence: {_error_text(exc)}", file=err)
        return 1
