#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Publish Jira-backed issues from an opaque caller-owned body file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

import frontmatter as frontmatter_lib

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import JiraProviderError, normalize_jira_issue_key
from workflow_providers import ProviderContext, ProviderRequest


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()


class JiraIssueDraftError(RuntimeError):
    """Raised when Jira issue publish operations cannot proceed."""


def publish_issue(
    *,
    project: Path,
    artifact_type: str,
    title: str,
    body_file: Path,
    labels: tuple[str, ...] = (),
    issue_type: str | None = None,
    subtask_parent: str | None = None,
    project_key: str | None = None,
    epic_name: str | None = None,
    relationship_intent: dict[str, object] | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Create a Jira issue from an opaque caller-owned body file."""

    config = _load_jira_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    title = _required_text(title, "title")
    normalized_labels = tuple(label.strip() for label in labels if label.strip())
    normalized_subtask_parent = _jira_issue_key(subtask_parent, "subtask parent")
    normalized_issue_type = _optional_text(issue_type)
    normalized_epic_name = _optional_text(epic_name)

    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise JiraIssueDraftError(f"body file does not exist: {body_path}")
    body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

    payload: dict[str, object] = {
        "title": title,
        "body": body,
        "labels": list(normalized_labels),
    }
    if normalized_issue_type:
        payload["jira_issue_type"] = normalized_issue_type
    if normalized_subtask_parent:
        payload["subtask_parent_key"] = normalized_subtask_parent
    normalized_project_key = _optional_text(project_key)
    if normalized_project_key:
        payload["project_key"] = normalized_project_key
    if normalized_epic_name is not None:
        payload["epic_name"] = normalized_epic_name

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="jira",
            operation="create",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )

    provider_payload = dict(response.payload)
    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = (
        cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
    )
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    result: dict[str, object] = {
        "operation": "publish_issue",
        "kind": "jira",
        "issue": provider_payload.get("issue") or provider_payload.get("key"),
        "key": provider_payload.get("key"),
        "verified": bool(provider_payload.get("verified")),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        "subtask_parent": provider_payload.get("subtask_parent"),
    }

    if relationship_intent:
        new_key = provider_payload.get("key") or provider_payload.get("issue")
        relationships_response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": new_key, "relationship_intent": relationship_intent},
            )
        )
        result["relationships"] = dict(relationships_response.payload)

    return result


def _strip_body_frontmatter(body: str) -> str:
    if not _FRONTMATTER_HANDLER.detect(body):
        return body
    try:
        _frontmatter_text, remainder = _FRONTMATTER_HANDLER.split(body)
    except Exception:
        return body
    return remainder.lstrip("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    subparsers = parser.add_subparsers(dest="command", required=True)

    publish = subparsers.add_parser(
        "publish",
        help="publish a new Jira issue from a body file",
    )
    publish.add_argument("--type", required=True, help="workflow artifact type")
    publish.add_argument("--title", required=True)
    publish.add_argument("--label", action="append", default=[])
    publish.add_argument("--issue-type", help="Jira provider issue type")
    publish.add_argument(
        "--subtask-parent",
        help="Jira parent issue key when publishing a Sub-task",
    )
    publish.add_argument(
        "--project-key",
        help="override the Jira project key for this create",
    )
    publish.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (leading YAML frontmatter is stripped)",
    )
    publish.add_argument(
        "--epic-name",
        help="Epic Name customfield value (epic only; defaults to --title)",
    )
    publish.add_argument("--parent", help="add parent relationship after publish")
    publish.add_argument(
        "--epic",
        help="add Epic Link after publish (rejected when --type epic)",
    )
    publish.add_argument(
        "--blocked-by",
        action="append",
        default=[],
        help="add blocked-by dependency after publish (repeatable)",
    )
    publish.add_argument(
        "--blocking",
        action="append",
        default=[],
        help="add blocking dependency after publish (repeatable)",
    )
    publish.add_argument(
        "--child",
        action="append",
        default=[],
        help="add child after publish (repeatable)",
    )
    publish.add_argument(
        "--related",
        action="append",
        default=[],
        help="add related ref after publish (repeatable)",
    )

    for child in subparsers.choices.values():
        child.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    return parser


def _publish_relationship_intent(args: argparse.Namespace) -> dict[str, object]:
    intent: dict[str, object] = {}
    if getattr(args, "parent", None):
        intent["parent_add"] = args.parent
    if getattr(args, "epic", None):
        if getattr(args, "type", None) and args.type.strip().lower() == "epic":
            raise JiraIssueDraftError("publish --epic cannot be combined with --type epic")
        intent["epic_add"] = args.epic
    if getattr(args, "blocked_by", None):
        intent["blocked_by_add"] = list(args.blocked_by)
    if getattr(args, "blocking", None):
        intent["blocking_add"] = list(args.blocking)
    if getattr(args, "child", None):
        intent["child_add"] = list(args.child)
    if getattr(args, "related", None):
        intent["related_add"] = list(args.related)
    return intent


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    output = stdout or sys.stdout
    errors = stderr or sys.stderr

    try:
        if args.command == "publish":
            payload = publish_issue(
                project=args.project,
                artifact_type=args.type,
                title=args.title,
                body_file=args.body_file,
                labels=tuple(args.label),
                issue_type=args.issue_type,
                subtask_parent=args.subtask_parent,
                project_key=args.project_key,
                epic_name=args.epic_name,
                relationship_intent=_publish_relationship_intent(args),
                runner=runner,
            )
        else:
            raise JiraIssueDraftError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"Jira issue draft error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    else:
        _print_plain(payload, output)
    return 0


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueDraftError(str(exc)) from exc
    if config is None:
        raise JiraIssueDraftError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueDraftError(
            f"Jira issue draft commands require configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise JiraIssueDraftError(f"{name} is required")
    return text


def _optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _jira_issue_key(value: str | None, name: str) -> str | None:
    parent = _optional_text(value)
    if parent is None:
        return None
    try:
        return normalize_jira_issue_key(parent)
    except JiraProviderError as exc:
        raise JiraIssueDraftError(f"invalid {name}: {exc}") from exc


def _print_plain(payload: dict[str, object], output: TextIO) -> None:
    issue = payload.get("issue") or payload.get("key")
    print(
        f"published issue {issue} verified={payload.get('verified')} cache={payload.get('issue_file')}",
        file=output,
    )


if __name__ == "__main__":
    raise SystemExit(main())
