#!/usr/bin/env python3
"""Issue backend driver protocol and factory.

The :mod:`issue.dispatch` dispatcher resolves the active backend via
:func:`get_backend` and delegates intent-specific argparse registration
plus execution to the returned driver. Drivers wrap the body of the
(now-deleted) per-backend CLI scripts; the dispatcher owns the shared
parser, the config guard, and the JSON emission policy.
"""

from __future__ import annotations

import argparse
from typing import Protocol, TextIO

from command import CommandRunner
from config import WorkflowConfig


class IssueBackendError(RuntimeError):
    """Raised when an issue backend driver cannot proceed."""


class IssueBackend(Protocol):
    """Backend driver contract used by the dispatcher scripts.

    Every intent (``fetch``, ``comments``, ``drafts``, ``writeback``,
    ``relationships``, ``fields``) is split into two halves on each driver:

    - ``add_<intent>_args(parser)`` registers backend-specific options on a
      pre-built shared parser. The dispatcher already supplies the common
      flags (``--project`` and any other intent-shared arguments) before
      handing the parser to the driver.
    - ``run_<intent>(args, *, runner, stdout, stderr)`` reads the parsed
      namespace, calls the configured provider, prints the JSON payload to
      ``stdout``, and returns the process exit code.

    The dispatcher passes a loaded :class:`WorkflowConfig` via the
    ``config`` keyword on every ``run_*`` call so the driver does not have
    to re-load it. Backend implementations may raise
    :class:`IssueBackendError` to communicate a clean, descriptive failure
    that the dispatcher converts into a non-zero exit and stderr message.
    """

    kind: str

    # --- fetch ----------------------------------------------------------

    def add_fetch_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_fetch(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...

    # --- comments -------------------------------------------------------

    def add_comments_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_comments(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...

    # --- drafts ---------------------------------------------------------

    def add_drafts_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_drafts(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...

    # --- writeback ------------------------------------------------------

    def add_writeback_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_writeback(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...

    # --- relationships --------------------------------------------------

    def add_relationships_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_relationships(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...

    # --- fields ---------------------------------------------------------

    def add_fields_args(self, parser: argparse.ArgumentParser) -> None: ...

    def run_fields(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int: ...


def get_backend(kind: str) -> IssueBackend:
    """Resolve an :class:`IssueBackend` driver for the configured kind.

    Imports are deferred so each dispatcher only pays for the active
    backend (the inactive backend's module is never loaded).
    """

    normalized = str(kind or "").strip().lower()
    if normalized == "github":
        from issue.github.backend import GitHubIssueBackend

        return GitHubIssueBackend()
    if normalized == "jira":
        from issue.jira.backend import JiraIssueBackend

        return JiraIssueBackend()
    raise IssueBackendError(
        f"issue dispatcher requires configured issue provider kind github or jira, found {normalized or 'unset'}"
    )
