#!/usr/bin/env python3
"""Provider-agnostic issue-key normalization.

Foundation layer: this module imports nothing else from the ``issue``
package or the provider backends, so session/hook state and provider
modules can normalize issue numbers without pulling in a backend (and
without reviving the ``session_state`` -> ``issue.github``
import cycle).
"""

from __future__ import annotations


class IssueKeyError(ValueError):
    """Raised when an issue number/key cannot be normalized."""


def normalize_issue_number(issue: int | str) -> str:
    """Normalize a same-repository issue number."""

    value = str(issue).strip()
    if value.startswith("#"):
        value = value[1:]
    if not value.isdigit():
        raise IssueKeyError(f"issue number must be numeric or #number: {issue}")
    return value
