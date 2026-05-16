#!/usr/bin/env python3
"""Jira issue reference parsing helpers."""

from __future__ import annotations

import re
from typing import Any

JIRA_KEY_RE = re.compile(r"^(?P<project>[A-Z][A-Z0-9]+)-(?P<number>[1-9]\d*)$", re.IGNORECASE)


class JiraProviderError(RuntimeError):
    """Raised when Jira provider data or configuration cannot be handled."""


def normalize_jira_issue_key(value: Any) -> str:
    """Normalize a Jira issue key such as ``test-1234`` to ``TEST-1234``."""

    text = str(value).strip()
    match = JIRA_KEY_RE.match(text)
    if not match:
        raise JiraProviderError(f"invalid Jira issue key: {value}")
    return f"{match.group('project').upper()}-{int(match.group('number'))}"
