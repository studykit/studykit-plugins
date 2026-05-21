#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Append a GitHub-backed issue comment from an opaque caller-owned body file."""

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
from workflow_github import GitHubRepositoryError, resolve_github_repository
from issue.github.provider import GitHubIssueNativeProvider
from issue.github.refs import issue_numbers_from_references
from workflow_providers import ProviderContext, ProviderRequest


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()


class GitHubIssueCommentsError(RuntimeError):
    """Raised when a GitHub issue comment append cannot proceed."""


def append_comment(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    state: str | None = None,
    state_reason: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Post one comment from an opaque body file to one GitHub issue."""

    config = _load_github_issue_config(project)
    artifact_type = _required_text(artifact_type, "artifact type")
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise GitHubIssueCommentsError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references([issue], repo=repo, allow_bare_numbers=True)
    if len(issue_numbers) != 1:
        raise GitHubIssueCommentsError(
            f"expected exactly one configured GitHub issue reference, got {len(issue_numbers)}"
        )
    issue_number = issue_numbers[0]

    body_path = body_file.expanduser()
    if not body_path.is_file():
        raise GitHubIssueCommentsError(f"body file does not exist: {body_path}")
    body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

    payload: dict[str, object] = {"issue": issue_number, "body": body}
    if state:
        payload["state"] = state.strip().lower()
    if state_reason:
        payload["state_reason"] = state_reason.strip()

    provider = GitHubIssueNativeProvider(runner=runner)
    response = provider.call(
        ProviderRequest(
            role="issue",
            kind="github",
            operation="add_comment",
            context=ProviderContext(project=config.root, artifact_type=artifact_type),
            payload=payload,
        )
    )

    provider_payload = dict(response.payload)
    if provider_payload.get("status") == "blocked":
        provider_payload["body_file"] = str(body_path)
        provider_payload["body_file_removed"] = False
        return provider_payload

    cache_payload = provider_payload.get("cache") if isinstance(provider_payload.get("cache"), dict) else {}
    issue_file = cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
    body_removed = False
    try:
        body_path.unlink()
    except OSError:
        body_removed = False
    else:
        body_removed = True

    return {
        "operation": "append_comment",
        "kind": "github",
        "issue": provider_payload.get("issue"),
        "comment": provider_payload.get("comment"),
        "state_changed": bool(provider_payload.get("state_changed")),
        "state": provider_payload.get("state"),
        "issue_file": issue_file,
        "body_file": str(body_path),
        "body_file_removed": body_removed,
        "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
    }


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

    append = subparsers.add_parser(
        "append",
        help="append a comment to one GitHub issue from a body file",
    )
    append.add_argument("--type", default="task", help="workflow artifact type")
    append.add_argument("--issue", required=True, help="GitHub issue id or configured reference")
    append.add_argument(
        "--body-file",
        type=Path,
        required=True,
        help="path to the opaque body content file (leading YAML frontmatter is stripped)",
    )
    append.add_argument("--state", choices=["open", "closed"])
    append.add_argument(
        "--state-reason",
        choices=["completed", "not_planned", "reopened"],
    )

    return parser


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
        if args.command == "append":
            payload = append_comment(
                project=args.project,
                artifact_type=args.type,
                issue=args.issue,
                body_file=args.body_file,
                state=args.state,
                state_reason=args.state_reason,
                runner=runner,
            )
        else:
            raise GitHubIssueCommentsError(f"unsupported command: {args.command}")
    except Exception as exc:
        print(f"GitHub issue comment append error: {exc}", file=errors)
        return 2

    print(json.dumps(payload, indent=2, sort_keys=False), file=output)
    if payload.get("status") == "blocked":
        return 3
    return 0


def _load_github_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise GitHubIssueCommentsError(str(exc)) from exc
    if config is None:
        raise GitHubIssueCommentsError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise GitHubIssueCommentsError(
            f"GitHub issue comment append requires configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise GitHubIssueCommentsError(f"{name} is required")
    return text


if __name__ == "__main__":
    raise SystemExit(main())
