#!/usr/bin/env python3
"""GitHub issue backend driver.

Ports the per-intent logic from the (now-deleted) ``github_issue_*.py``
CLI scripts onto a single :class:`GitHubIssueBackend` driver consumed by
the :mod:`issue.dispatch` dispatcher. The backend keeps the original
argument surface and emitted JSON payload shapes; the only moved seam is
the config-kind guard, which the dispatcher owns.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO

import frontmatter as frontmatter_lib

from workflow_cache import WorkflowCacheError
from workflow_command import CommandRunner
from workflow_config import WorkflowConfig
from workflow_github import (
    DEFAULT_ISSUE_FIELDS,  # noqa: F401  (imported for downstream tests)
    GitHubRepositoryError,
    get_github_login,
    resolve_github_repository,
)
from issue.backend import IssueBackendError
from issue.cli_output import (
    IssueFetchContext,
    cache_refreshed_from_payload,
    display_project_path,
    flatten_provider_envelope,
    format_issue_cache_json,
)
from issue.github.cache import GitHubIssueCache
from issue.github.provider import GitHubIssueNativeProvider
from issue.github.refs import issue_numbers_from_references
from workflow_providers import (
    CACHE_POLICY_DEFAULT,
    CACHE_POLICY_REFRESH,
    ProviderContext,
    ProviderRequest,
)


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()

_GITHUB_TYPE_LABELS = frozenset(
    {"task", "bug", "spike", "epic", "review", "usecase", "research"}
)

_CACHE_FETCH_POLICIES = (CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH)


class GitHubIssueBackend:
    """Drive GitHub-specific issue intents for the unified dispatchers."""

    kind = "github"

    # ------------------------------------------------------------------
    # fetch
    # ------------------------------------------------------------------

    def add_fetch_args(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--cache-policy",
            choices=_CACHE_FETCH_POLICIES,
            default=CACHE_POLICY_DEFAULT,
            help="provider cache policy",
        )
        parser.add_argument(
            "references",
            nargs="+",
            help="GitHub issue IDs or configured repository issue references",
        )

    def run_fetch(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            repo = resolve_github_repository(config.root, runner=runner)
        except GitHubRepositoryError as exc:
            print(f"GitHub issue fetch error: {exc}", file=stderr)
            return 2

        try:
            issue_numbers = issue_numbers_from_references(
                list(args.references),
                repo=repo,
                allow_bare_numbers=True,
            )
        except Exception as exc:  # noqa: BLE001 — surface as CLI error
            print(f"GitHub issue fetch error: {exc}", file=stderr)
            return 2
        if not issue_numbers:
            print(
                "GitHub issue fetch error: no configured GitHub issue references were found",
                file=stderr,
            )
            return 2

        provider = GitHubIssueNativeProvider(runner=runner)
        cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
        contexts: list[IssueFetchContext] = []
        try:
            for issue in issue_numbers:
                response = provider.call(
                    ProviderRequest(
                        role="issue",
                        kind="github",
                        operation="get",
                        context=ProviderContext(
                            project=config.root,
                            artifact_type="task",
                            cache_policy=args.cache_policy,
                        ),
                        payload={
                            "issue": issue,
                            "include_body": False,
                            "include_comments": False,
                            "include_relationships": False,
                        },
                    )
                )
                issue_dir = cache.issue_dir(repo, issue)
                comment_paths = tuple(
                    display_project_path(path, config.root)
                    for path in cache.comment_files(repo, issue)
                )
                relationships_path = cache.relationships_file(repo, issue)
                relationships_display = (
                    display_project_path(relationships_path, config.root)
                    if relationships_path.is_file()
                    else None
                )
                contexts.append(
                    IssueFetchContext(
                        number=issue,
                        issue_dir=display_project_path(
                            issue_dir, config.root, trailing_slash=True
                        ),
                        title=str(response.payload.get("title") or ""),
                        state=str(response.payload.get("state") or "").upper(),
                        cache_refreshed=cache_refreshed_from_payload(
                            response.payload, default=True
                        ),
                        provider_kind="github",
                        comments=comment_paths,
                        relationships=relationships_display,
                    )
                )
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue fetch error: {exc}", file=stderr)
            return 2

        payload = format_issue_cache_json(contexts)
        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        return 0

    # ------------------------------------------------------------------
    # comments
    # ------------------------------------------------------------------

    def add_comments_args(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="command", required=True)
        append = subparsers.add_parser(
            "append",
            help="append a comment to one GitHub issue from a body file",
        )
        append.add_argument("--type", default="task", help="workflow artifact type")
        append.add_argument(
            "--issue",
            required=True,
            help="GitHub issue id or configured reference",
        )
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
        append.add_argument(
            "--overwrite",
            action="store_true",
            help="replace the provider copy even if it changed since the last fetch",
        )

    def run_comments(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "append":
                payload = self._append_comment(
                    config=config,
                    artifact_type=args.type,
                    issue=args.issue,
                    body_file=args.body_file,
                    state=args.state,
                    state_reason=args.state_reason,
                    overwrite=args.overwrite,
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue comment append error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "conflict":
            return 3
        return 0

    def _append_comment(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        issue: str,
        body_file: Path,
        state: str | None,
        state_reason: str | None,
        overwrite: bool = False,
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        try:
            repo = resolve_github_repository(config.root, runner=runner)
        except GitHubRepositoryError as exc:
            raise IssueBackendError(str(exc)) from exc

        issue_numbers = issue_numbers_from_references(
            [issue], repo=repo, allow_bare_numbers=True
        )
        if len(issue_numbers) != 1:
            raise IssueBackendError(
                f"expected exactly one configured GitHub issue reference, got {len(issue_numbers)}"
            )
        issue_number = issue_numbers[0]

        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")
        body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

        payload: dict[str, object] = {"issue": issue_number, "body": body}
        if state:
            payload["state"] = state.strip().lower()
        if state_reason:
            payload["state_reason"] = state_reason.strip()
        if overwrite:
            payload["overwrite"] = True

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
        if provider_payload.get("status") == "conflict":
            provider_payload["body_file"] = str(body_path)
            provider_payload["body_file_removed"] = False
            return provider_payload

        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
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

    # ------------------------------------------------------------------
    # drafts (publish)
    # ------------------------------------------------------------------

    def add_drafts_args(self, parser: argparse.ArgumentParser) -> None:
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
        publish.add_argument(
            "--parent", help="add parent relationship after publish"
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
            help="add sub-issue after publish (repeatable)",
        )
        publish.add_argument(
            "--related",
            action="append",
            default=[],
            help="add related ref after publish (repeatable)",
        )

    def run_drafts(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "publish":
                payload = self._publish_issue(
                    config=config,
                    artifact_type=args.type,
                    title=args.title,
                    body_file=args.body_file,
                    labels=tuple(args.label),
                    state=args.state,
                    state_reason=args.state_reason,
                    assignee=args.assignee,
                    relationship_intent=self._publish_relationship_intent(args),
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue draft error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        relationships = payload.get("relationships") if isinstance(payload, dict) else None
        if isinstance(relationships, dict) and relationships.get("status") == "failed":
            return 1
        return 0

    @staticmethod
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

    def _publish_issue(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        title: str,
        body_file: Path,
        labels: tuple[str, ...],
        state: str,
        state_reason: str | None,
        assignee: str | None,
        relationship_intent: dict[str, object],
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        title = _required_text(title, "title")
        normalized_state = (state or "open").strip().lower()
        normalized_labels = tuple(label.strip() for label in labels if label.strip())
        if artifact_type not in normalized_labels:
            normalized_labels = (artifact_type, *normalized_labels)
        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")
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
        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
        issue_file = (
            cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
        )

        result: dict[str, object] = {
            "kind": "github",
            "issue": provider_payload.get("issue"),
            "issue_file": issue_file,
            "body_file": str(body_path),
            "body_file_removed": False,
            "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        }

        relationship_failed = False
        if relationship_intent:
            try:
                relationships_response = provider.call(
                    ProviderRequest(
                        role="issue",
                        kind="github",
                        operation="apply_relationships",
                        context=ProviderContext(
                            project=config.root, artifact_type=artifact_type
                        ),
                        payload={
                            "issue": provider_payload.get("issue"),
                            "relationship_intent": relationship_intent,
                        },
                    )
                )
                result["relationships"] = dict(relationships_response.payload)
            except Exception as exc:  # noqa: BLE001
                relationship_failed = True
                result["relationships"] = {
                    "operation": "apply_relationships",
                    "status": "failed",
                    "error": str(exc),
                    "intent": dict(relationship_intent),
                }

        if not relationship_failed:
            try:
                body_path.unlink()
            except OSError:
                pass
            else:
                result["body_file_removed"] = True

        return result

    # ------------------------------------------------------------------
    # writeback
    # ------------------------------------------------------------------

    def add_writeback_args(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="command", required=True)
        update = subparsers.add_parser(
            "update",
            help="update one GitHub issue body from a body file",
        )
        update.add_argument("--type", default="task", help="workflow artifact type")
        update.add_argument(
            "--issue", required=True, help="GitHub issue id or configured reference"
        )
        update.add_argument(
            "--body-file",
            type=Path,
            required=True,
            help="path to the opaque body content file (leading YAML frontmatter is stripped)",
        )
        update.add_argument("--title")
        update.add_argument(
            "--add-label",
            dest="add_label",
            action="append",
            default=[],
            help="add a label (repeatable; cannot be combined with --set-labels)",
        )
        update.add_argument(
            "--remove-label",
            dest="remove_label",
            action="append",
            default=[],
            help="remove a label (repeatable; cannot be combined with --set-labels)",
        )
        update.add_argument(
            "--set-labels",
            dest="set_labels",
            help="replace the label set with a comma-separated list",
        )
        update.add_argument("--state", choices=["open", "closed"])
        update.add_argument(
            "--state-reason",
            choices=["completed", "not_planned", "reopened"],
        )
        update.add_argument(
            "--overwrite",
            action="store_true",
            help="replace the provider copy even if it changed since the last fetch",
        )
        parent_group = update.add_mutually_exclusive_group()
        parent_group.add_argument(
            "--parent", help="add parent (errors if a parent already exists)"
        )
        parent_group.add_argument(
            "--replace-parent",
            dest="replace_parent",
            help="set parent, replacing any existing parent",
        )
        parent_group.add_argument(
            "--remove-parent",
            dest="remove_parent",
            action="store_true",
            help="remove the current parent (no-op when no parent exists)",
        )
        update.add_argument(
            "--child", action="append", default=[], help="add a sub-issue (repeatable)"
        )
        update.add_argument(
            "--remove-child",
            dest="remove_child",
            action="append",
            default=[],
            help="remove a sub-issue (repeatable)",
        )
        update.add_argument(
            "--blocked-by",
            action="append",
            default=[],
            help="add a blocked-by dependency (repeatable)",
        )
        update.add_argument(
            "--remove-blocked-by",
            dest="remove_blocked_by",
            action="append",
            default=[],
            help="remove a blocked-by dependency (repeatable)",
        )
        update.add_argument(
            "--blocking",
            action="append",
            default=[],
            help="add a blocking dependency (repeatable)",
        )
        update.add_argument(
            "--remove-blocking",
            dest="remove_blocking",
            action="append",
            default=[],
            help="remove a blocking dependency (repeatable)",
        )
        update.add_argument(
            "--related", action="append", default=[], help="add a related ref (repeatable)"
        )
        update.add_argument(
            "--remove-related",
            dest="remove_related",
            action="append",
            default=[],
            help="remove a related ref (repeatable)",
        )

    def run_writeback(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "update":
                set_labels: tuple[str, ...] | None = None
                if args.set_labels is not None:
                    set_labels = tuple(part for part in args.set_labels.split(","))
                payload = self._update_issue(
                    config=config,
                    artifact_type=args.type,
                    issue=args.issue,
                    body_file=args.body_file,
                    title=args.title,
                    add_labels=tuple(args.add_label),
                    remove_labels=tuple(args.remove_label),
                    set_labels=set_labels,
                    state=args.state,
                    state_reason=args.state_reason,
                    relationship_intent=self._writeback_relationship_intent(args),
                    overwrite=args.overwrite,
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue update error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "conflict":
            return 3
        return 0

    @staticmethod
    def _writeback_relationship_intent(args: argparse.Namespace) -> dict[str, object]:
        intent: dict[str, object] = {}
        if getattr(args, "parent", None):
            intent["parent_add"] = args.parent
        if getattr(args, "replace_parent", None):
            intent["parent_replace"] = args.replace_parent
        if getattr(args, "remove_parent", False):
            intent["parent_remove"] = True
        if getattr(args, "blocked_by", None):
            intent["blocked_by_add"] = list(args.blocked_by)
        if getattr(args, "remove_blocked_by", None):
            intent["blocked_by_remove"] = list(args.remove_blocked_by)
        if getattr(args, "blocking", None):
            intent["blocking_add"] = list(args.blocking)
        if getattr(args, "remove_blocking", None):
            intent["blocking_remove"] = list(args.remove_blocking)
        if getattr(args, "child", None):
            intent["child_add"] = list(args.child)
        if getattr(args, "remove_child", None):
            intent["child_remove"] = list(args.remove_child)
        if getattr(args, "related", None):
            intent["related_add"] = list(args.related)
        if getattr(args, "remove_related", None):
            intent["related_remove"] = list(args.remove_related)
        return intent

    def _update_issue(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        issue: str,
        body_file: Path,
        title: str | None,
        add_labels: tuple[str, ...],
        remove_labels: tuple[str, ...],
        set_labels: tuple[str, ...] | None,
        state: str | None,
        state_reason: str | None,
        relationship_intent: dict[str, object],
        overwrite: bool = False,
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        try:
            repo = resolve_github_repository(config.root, runner=runner)
        except GitHubRepositoryError as exc:
            raise IssueBackendError(str(exc)) from exc

        issue_numbers = issue_numbers_from_references(
            [issue], repo=repo, allow_bare_numbers=True
        )
        if len(issue_numbers) != 1:
            raise IssueBackendError(
                f"expected exactly one configured GitHub issue reference, got {len(issue_numbers)}"
            )
        issue_number = issue_numbers[0]

        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")
        body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

        normalized_add = tuple(label.strip() for label in add_labels if label.strip())
        normalized_remove = tuple(label.strip() for label in remove_labels if label.strip())
        normalized_set: tuple[str, ...] | None
        if set_labels is None:
            normalized_set = None
        else:
            normalized_set = tuple(label.strip() for label in set_labels if label.strip())
        if normalized_set is not None and (normalized_add or normalized_remove):
            raise IssueBackendError(
                "--set-labels cannot be combined with --add-label or --remove-label"
            )

        payload: dict[str, object] = {
            "issue": issue_number,
            "body": body,
            "freshness_check": True,
        }
        if overwrite:
            payload["overwrite"] = True
        if title is not None:
            payload["title"] = title
        if normalized_set is not None:
            payload["label_set"] = list(normalized_set)
        if normalized_add:
            payload["label_add"] = list(normalized_add)
        if normalized_remove:
            payload["label_remove"] = list(normalized_remove)
        if state:
            payload["state"] = state.strip().lower()
        if state_reason:
            payload["state_reason"] = state_reason.strip()

        provider = GitHubIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="update",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload=payload,
            )
        )

        provider_payload = dict(response.payload)
        if provider_payload.get("status") == "conflict":
            provider_payload["body_file"] = str(body_path)
            provider_payload["body_file_removed"] = False
            return provider_payload

        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
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
            "kind": "github",
            "issue": provider_payload.get("issue"),
            "state_changed": bool(provider_payload.get("state_changed")),
            "state": provider_payload.get("state"),
            "issue_file": issue_file,
            "body_file": str(body_path),
            "body_file_removed": body_removed,
            "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        }

        if relationship_intent:
            relationships_response = provider.call(
                ProviderRequest(
                    role="issue",
                    kind="github",
                    operation="apply_relationships",
                    context=ProviderContext(
                        project=config.root, artifact_type=artifact_type
                    ),
                    payload={
                        "issue": provider_payload.get("issue"),
                        "relationship_intent": relationship_intent,
                    },
                )
            )
            result["relationships"] = dict(relationships_response.payload)

        return result

    # ------------------------------------------------------------------
    # relationships
    # ------------------------------------------------------------------

    def add_relationships_args(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--type", default="task", help="workflow artifact type")
        parent_group = parser.add_mutually_exclusive_group()
        parent_group.add_argument(
            "--parent", help="add parent (errors if a parent already exists)"
        )
        parent_group.add_argument(
            "--replace-parent",
            dest="replace_parent",
            help="set parent, replacing any existing parent",
        )
        parent_group.add_argument(
            "--remove-parent",
            dest="remove_parent",
            action="store_true",
            help="remove the current parent (no-op when no parent exists)",
        )
        parser.add_argument(
            "--child", action="append", default=[], help="add a sub-issue (repeatable)"
        )
        parser.add_argument(
            "--remove-child",
            dest="remove_child",
            action="append",
            default=[],
            help="remove a sub-issue (repeatable)",
        )
        parser.add_argument(
            "--blocked-by",
            action="append",
            default=[],
            help="add a blocked-by dependency (repeatable)",
        )
        parser.add_argument(
            "--remove-blocked-by",
            dest="remove_blocked_by",
            action="append",
            default=[],
            help="remove a blocked-by dependency (repeatable)",
        )
        parser.add_argument(
            "--blocking",
            action="append",
            default=[],
            help="add a blocking dependency (repeatable)",
        )
        parser.add_argument(
            "--remove-blocking",
            dest="remove_blocking",
            action="append",
            default=[],
            help="remove a blocking dependency (repeatable)",
        )
        parser.add_argument(
            "--related",
            action="append",
            default=[],
            help="add a related ref (repeatable)",
        )
        parser.add_argument(
            "--remove-related",
            dest="remove_related",
            action="append",
            default=[],
            help="remove a related ref (repeatable)",
        )
        parser.add_argument(
            "issue", help="GitHub issue id or configured repository issue reference"
        )

    def run_relationships(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        intent = self._relationships_intent(args)
        try:
            payload = self._apply_relationships(
                config=config,
                issue_ref=args.issue,
                artifact_type=args.type,
                intent=intent,
                runner=runner,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue relationship error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        return 0

    @staticmethod
    def _relationships_intent(args: argparse.Namespace) -> dict[str, object]:
        intent: dict[str, object] = {}
        if args.parent:
            intent["parent_add"] = args.parent
        if args.replace_parent:
            intent["parent_replace"] = args.replace_parent
        if args.remove_parent:
            intent["parent_remove"] = True
        if args.blocked_by:
            intent["blocked_by_add"] = list(args.blocked_by)
        if args.remove_blocked_by:
            intent["blocked_by_remove"] = list(args.remove_blocked_by)
        if args.blocking:
            intent["blocking_add"] = list(args.blocking)
        if args.remove_blocking:
            intent["blocking_remove"] = list(args.remove_blocking)
        if args.child:
            intent["child_add"] = list(args.child)
        if args.remove_child:
            intent["child_remove"] = list(args.remove_child)
        if args.related:
            intent["related_add"] = list(args.related)
        if args.remove_related:
            intent["related_remove"] = list(args.remove_related)
        return intent

    def _apply_relationships(
        self,
        *,
        config: WorkflowConfig,
        issue_ref: str,
        artifact_type: str,
        intent: dict[str, object],
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        try:
            repo = resolve_github_repository(config.root, runner=runner)
        except GitHubRepositoryError as exc:
            raise IssueBackendError(str(exc)) from exc

        issue_numbers = issue_numbers_from_references(
            [issue_ref], repo=repo, allow_bare_numbers=True
        )
        if not issue_numbers:
            raise IssueBackendError(
                "no configured-repository GitHub issue references were found"
            )
        if len(issue_numbers) != 1:
            raise IssueBackendError(
                "relationship apply requires exactly one issue ref"
            )
        issue = issue_numbers[0]

        provider = GitHubIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue, "relationship_intent": intent},
            )
        )
        cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
        return flatten_provider_envelope(
            response.payload,
            project=config.root,
            issue_file=cache.issue_file(repo, issue),
        )

    # ------------------------------------------------------------------
    # fields
    # ------------------------------------------------------------------

    def add_fields_args(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--type", default="task", help="workflow artifact type")
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="replace the provider copy even if it changed since the last fetch",
        )
        subparsers = parser.add_subparsers(dest="verb", required=True)

        p_close = subparsers.add_parser("close", help="close an issue")
        p_close.add_argument("issue", help="GitHub issue reference")
        p_close.add_argument(
            "--reason", choices=("completed", "not_planned"), default="completed"
        )
        p_close.add_argument(
            "--comment", help="optional comment posted alongside the close"
        )

        p_reopen = subparsers.add_parser("reopen", help="reopen an issue")
        p_reopen.add_argument("issue", help="GitHub issue reference")
        p_reopen.add_argument(
            "--comment", help="optional comment posted alongside the reopen"
        )

        p_assign = subparsers.add_parser("assign", help="assign an issue to a user")
        p_assign.add_argument("issue", help="GitHub issue reference")
        p_assign.add_argument("user", help='GitHub login or the literal "me"')

        p_unassign = subparsers.add_parser("unassign", help="clear all assignees")
        p_unassign.add_argument("issue", help="GitHub issue reference")

        p_set_type = subparsers.add_parser(
            "set-type", help="swap the workflow type label"
        )
        p_set_type.add_argument("issue", help="GitHub issue reference")
        p_set_type.add_argument(
            "new_type", metavar="type", help="new workflow type label"
        )

    def run_fields(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            payload = self._fields_payload(
                config=config,
                artifact_type=args.type,
                verb=args.verb,
                issue=args.issue,
                reason=getattr(args, "reason", None),
                comment=getattr(args, "comment", None),
                user=getattr(args, "user", None),
                new_type=getattr(args, "new_type", None),
                overwrite=getattr(args, "overwrite", False),
                runner=runner,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"GitHub issue fields error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "conflict":
            return 3
        return 0

    def _fields_payload(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        verb: str,
        issue: str,
        reason: str | None,
        comment: str | None,
        user: str | None,
        new_type: str | None,
        overwrite: bool = False,
        runner: CommandRunner | None,
    ) -> dict[str, Any]:
        try:
            repo = resolve_github_repository(config.root, runner=runner)
        except GitHubRepositoryError as exc:
            raise IssueBackendError(str(exc)) from exc

        issue_numbers = issue_numbers_from_references(
            [issue], repo=repo, allow_bare_numbers=True
        )
        if len(issue_numbers) != 1:
            raise IssueBackendError(
                "fields update requires exactly one GitHub issue ref"
            )
        issue_number = issue_numbers[0]

        provider = GitHubIssueNativeProvider(runner=runner)

        if verb in {"close", "reopen"}:
            payload: dict[str, Any] = {
                "issue": issue_number,
                "freshness_check": True,
                "freshness_target": "issue",
            }
            if overwrite:
                payload["overwrite"] = True
            if verb == "close" and reason is not None:
                payload["reason"] = reason
            if comment is not None:
                payload["comment"] = comment
            response = provider.call(
                ProviderRequest(
                    role="issue",
                    kind="github",
                    operation=verb,
                    context=ProviderContext(
                        project=config.root, artifact_type=artifact_type
                    ),
                    payload=payload,
                )
            )
            return flatten_provider_envelope(response.payload, project=config.root)

        if verb == "assign":
            if not user:
                raise IssueBackendError("assign requires a user")
            resolved = user
            if resolved.strip().lower() == "me":
                resolved = get_github_login(project=config.root, runner=runner)
            payload = {
                "issue": issue_number,
                "freshness_check": True,
                "assignee": resolved,
            }
        elif verb == "unassign":
            payload = {
                "issue": issue_number,
                "freshness_check": True,
                "unassign": True,
            }
        elif verb == "set-type":
            if not new_type or not new_type.strip():
                raise IssueBackendError("set-type requires a non-empty type")
            cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
            try:
                cached = cache.read_issue(
                    repo,
                    issue_number,
                    include_body=False,
                    include_comments=False,
                    include_relationships=False,
                )
            except WorkflowCacheError as exc:
                raise IssueBackendError(
                    f"refresh the GitHub issue cache before set-type: {exc}"
                ) from exc
            current_labels = set(_string_list(cached.get("labels")))
            new_labels = _replace_github_type_label(current_labels, new_type)
            payload = {
                "issue": issue_number,
                "freshness_check": True,
                "label_set": sorted(new_labels),
            }
        else:
            raise IssueBackendError(f"unsupported verb: {verb}")

        if overwrite:
            payload["overwrite"] = True
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="update",
                context=ProviderContext(
                    project=config.root, artifact_type=artifact_type
                ),
                payload=payload,
            )
        )
        return flatten_provider_envelope(response.payload, project=config.root)


def _replace_github_type_label(labels: set[str], workflow_type: str) -> set[str]:
    desired = workflow_type.strip()
    if not desired:
        raise IssueBackendError("workflow type is empty")
    labels = {label for label in labels if label not in _GITHUB_TYPE_LABELS}
    labels.add(desired)
    return labels


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return _string_list(nodes)
        name = value.get("name")
        return [str(name)] if name else []
    if isinstance(value, list | tuple | set):
        result: list[str] = []
        for item in value:
            if isinstance(item, dict):
                name = item.get("name")
                if name:
                    result.append(str(name))
            elif item is not None:
                result.append(str(item))
        return result
    return [str(value)]


def _strip_body_frontmatter(body: str) -> str:
    if not _FRONTMATTER_HANDLER.detect(body):
        return body
    try:
        _frontmatter_text, remainder = _FRONTMATTER_HANDLER.split(body)
    except Exception:  # noqa: BLE001 — defensive
        return body
    return remainder.lstrip("\n")


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise IssueBackendError(f"{name} is required")
    return text


# ---------------------------------------------------------------------------
# Module-level helpers (call-site compatibility with the deleted ``github_issue_*.py``
# CLIs). These let library tests keep their existing signatures (``project=...``,
# ``runner=...``) without depending on dispatcher plumbing. The dispatcher
# itself does NOT use these helpers — it goes through the backend driver.
# ---------------------------------------------------------------------------


# Error aliases preserved so existing ``pytest.raises(GitHubIssueXxxError, ...)``
# assertions continue to work against the unified backend.
GitHubIssueFetchError = IssueBackendError
GitHubIssueCommentsError = IssueBackendError
GitHubIssueDraftError = IssueBackendError
GitHubIssueWritebackError = IssueBackendError
GitHubIssueRelationshipsError = IssueBackendError
GitHubIssueFieldsError = IssueBackendError


def _load_github_config(project: Path) -> WorkflowConfig:
    from workflow_config import WorkflowConfigError, load_workflow_config

    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise IssueBackendError(str(exc)) from exc
    if config is None:
        raise IssueBackendError(".workflow/config.yml was not found")
    if config.issues.kind != "github":
        raise IssueBackendError(
            f"GitHub issue dispatcher requires configured issue provider kind github, found {config.issues.kind}"
        )
    return config


def fetch_cache_payload(
    *,
    project: Path,
    references: list[str],
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Fetch configured GitHub issue references into the workflow cache."""

    config = _load_github_config(project)
    try:
        repo = resolve_github_repository(config.root, runner=runner)
    except GitHubRepositoryError as exc:
        raise IssueBackendError(str(exc)) from exc

    issue_numbers = issue_numbers_from_references(
        references, repo=repo, allow_bare_numbers=True
    )
    if not issue_numbers:
        raise IssueBackendError("no configured GitHub issue references were found")

    provider = GitHubIssueNativeProvider(runner=runner)
    cache = GitHubIssueCache.for_project(config.root, configured_repo=repo)
    contexts: list[IssueFetchContext] = []
    for issue in issue_numbers:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="github",
                operation="get",
                context=ProviderContext(
                    project=config.root,
                    artifact_type="task",
                    cache_policy=cache_policy,
                ),
                payload={
                    "issue": issue,
                    "include_body": False,
                    "include_comments": False,
                    "include_relationships": False,
                },
            )
        )
        issue_dir = cache.issue_dir(repo, issue)
        comment_paths = tuple(
            display_project_path(path, config.root)
            for path in cache.comment_files(repo, issue)
        )
        relationships_path = cache.relationships_file(repo, issue)
        relationships_display = (
            display_project_path(relationships_path, config.root)
            if relationships_path.is_file()
            else None
        )
        contexts.append(
            IssueFetchContext(
                number=issue,
                issue_dir=display_project_path(
                    issue_dir, config.root, trailing_slash=True
                ),
                title=str(response.payload.get("title") or ""),
                state=str(response.payload.get("state") or "").upper(),
                cache_refreshed=cache_refreshed_from_payload(
                    response.payload, default=True
                ),
                provider_kind="github",
                comments=comment_paths,
                relationships=relationships_display,
            )
        )

    return format_issue_cache_json(contexts)


def append_comment(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    state: str | None = None,
    state_reason: str | None = None,
    overwrite: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Post one comment from an opaque body file to one GitHub issue."""

    config = _load_github_config(project)
    return GitHubIssueBackend()._append_comment(
        config=config,
        artifact_type=artifact_type,
        issue=issue,
        body_file=body_file,
        state=state,
        state_reason=state_reason,
        overwrite=overwrite,
        runner=runner,
    )


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

    config = _load_github_config(project)
    return GitHubIssueBackend()._publish_issue(
        config=config,
        artifact_type=artifact_type,
        title=title,
        body_file=body_file,
        labels=labels,
        state=state,
        state_reason=state_reason,
        assignee=assignee,
        relationship_intent=relationship_intent or {},
        runner=runner,
    )


def update_issue(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    title: str | None = None,
    add_labels: tuple[str, ...] = (),
    remove_labels: tuple[str, ...] = (),
    set_labels: tuple[str, ...] | None = None,
    state: str | None = None,
    state_reason: str | None = None,
    relationship_intent: dict[str, object] | None = None,
    overwrite: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Update one GitHub issue body from an opaque caller-owned body file."""

    config = _load_github_config(project)
    return GitHubIssueBackend()._update_issue(
        config=config,
        artifact_type=artifact_type,
        issue=issue,
        body_file=body_file,
        title=title,
        add_labels=add_labels,
        remove_labels=remove_labels,
        set_labels=set_labels,
        state=state,
        state_reason=state_reason,
        relationship_intent=relationship_intent or {},
        overwrite=overwrite,
        runner=runner,
    )


def apply_relationships_payload(
    *,
    project: Path,
    issue_ref: str,
    artifact_type: str,
    intent: dict[str, object],
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply a single GitHub issue's relationship intent directly."""

    config = _load_github_config(project)
    return GitHubIssueBackend()._apply_relationships(
        config=config,
        issue_ref=issue_ref,
        artifact_type=artifact_type,
        intent=intent,
        runner=runner,
    )


def fields_payload(
    *,
    project: Path,
    artifact_type: str,
    verb: str,
    issue: str,
    reason: str | None = None,
    comment: str | None = None,
    user: str | None = None,
    new_type: str | None = None,
    overwrite: bool = False,
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Apply a body-less GitHub issue field mutation."""

    config = _load_github_config(project)
    return GitHubIssueBackend()._fields_payload(
        config=config,
        artifact_type=artifact_type,
        verb=verb,
        issue=issue,
        reason=reason,
        comment=comment,
        user=user,
        new_type=new_type,
        overwrite=overwrite,
        runner=runner,
    )


# ``sys`` is imported above so the backend module can dispatch friendly
# parser errors to stderr; ensure no unused-import warnings.
_ = sys
