#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Publish GitHub-backed issues from an opaque caller-owned body file."""

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
from workflow_github_issue_provider import GitHubIssueNativeProvider
from workflow_providers import ProviderContext, ProviderRequest


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()


class GitHubIssueDraftError(RuntimeError):
    """Raised when GitHub issue publish operations cannot proceed."""


def publish_issue(
    *,
    project: Path,
    artifact_type: str,
    title: str,
    body_file: Path,
    labels: tuple[str, ...] = (),
    state: str = "open",
    state_reason: str | None = None,
    assignee: str | None = None,
    relationship_intent: dict[str, object] | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Create a GitHub issue from an opaque caller-owned body file."""

    config = _load_github_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    title = _required_text(title, "title")
    normalized_state = (state or "open").strip().lower()
    normalized_labels = tuple(label.strip() for label in labels if label.strip())
    if artifact_type not in normalized_labels:
        normalized_labels = (artifact_type, *normalized_labels)
    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise GitHubIssueDraftError(f"body file does not exist: {body_path}")
    body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

    payload: dict[str, object] = {
        "title": title,
        "body": body,
        "labels": list(normalized_labels),
        "state": normalized_state,
    }
    if state_reason:
        payload["state_reason"] = state_reason.strip()
    normalized_assignee = (assignee or "").strip()
    if normalized_assignee:
        payload["assignee"] = normalized_assignee

    provider = GitHubIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="create",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )

    provider_payload = dict(response.payload)
    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    result: dict[str, object] = {
        "operation": "publish_issue",
        "kind": "github",
        "issue": provider_payload.get("issue"),
        "verified": bool(provider_payload.get("verified")),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
    }

    if relationship_intent:
        try:
            relationships_response = provider.call(
                ProviderRequest(
                    role="issue",
                    kind="github",
                    operation="apply_relationships",
                    context=ProviderContext(project=config.root, artifact_type=artifact_type),
                    payload={
                        "issue": provider_payload.get("issue"),
                        "relationship_intent": relationship_intent,
                    },
                )
            )
            result["relationships"] = dict(relationships_response.payload)
        except Exception as exc:
            result["relationships"] = {
                "operation": "apply_relationships",
                "status": "failed",
                "error": str(exc),
                "intent": dict(relationship_intent),
            }

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
    subparsers = parser.add_subparsers(dest="command", required=True)

    publish = subparsers.add_parser(
        "publish",
        help="publish a new GitHub issue from a body file",
    )
    publish.add_argument("--type", required=True, help="workflow artifact type")
    publish.add_argument("--title", required=True)
    publish.add_argument("--label", action="append", default=[])
    publish.add_argument("--state", default="open")
    publish.add_argument("--state-reason")
    publish.add_argument(
        "--assignee",
        help='GitHub login or the literal "me" to resolve via `gh api user`',
    )
    publish.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (leading YAML frontmatter is stripped)",
    )
    publish.add_argument("--parent", help="add parent relationship after publish")
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
        help="add sub-issue after publish (repeatable)",
    )
    publish.add_argument(
        "--related",
        action="append",
        default=[],
        help="add related ref after publish (repeatable)",
    )

    return parser


def _publish_relationship_intent(args: argparse.Namespace) -> dict[str, object]:
    intent: dict[str, object] = {}
    if getattr(args, "parent", None):
        intent["parent_add"] = args.parent
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
                state=args.state,
                state_reason=args.state_reason,
                assignee=args.assignee,
                relationship_intent=_publish_relationship_intent(args),
                runner=runner,
            )
        else:
            raise GitHubIssueDraftError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"GitHub issue draft error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueDraftError(str(exc)) from exc
    if config is None:
        raise GitHubIssueDraftError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueDraftError(
            f"GitHub issue draft commands require configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise GitHubIssueDraftError(f"{name} is required")
    return text


if __name__ == "__main__":
    raise SystemExit(main())
