"""Host-specific configuration, explicit reviewers, and file/plan switches.

Reviewer objects select a user-installed agent or skill. Missing configuration uses
defaults; invalid non-empty reviewer objects are reported by their dispatchers.
Settings preserves unknown and retired keys until the user explicitly removes them.
"""

from __future__ import annotations

import json
import os
import re

from pathlib import Path
from typing import Any, NamedTuple



# Codex adapters set GUARD_HOST before importing this module. Keep the historical
# Claude paths intact while preventing one host from interpreting the other's state.
# Read once into a constant: the Codex adapter imports this module, so anything below
# asking "which host" must get the same answer the paths were chosen from.
_HOST_IS_CODEX = os.environ.get("GUARD_HOST") == "codex"


if _HOST_IS_CODEX:
    STATE_DIR_REL = ".codex/guard"
    CONFIG_REL = ".codex/guard.local.json"
else:
    STATE_DIR_REL = ".claude/guard"
    CONFIG_REL = ".claude/guard.local.json"


TRACE_FILE_NAME = "trace.log"


TRACE_ENV_VAR = "GUARD_TRACE"


TRACE_TRUTHY = {"1", "true", "yes", "on"}


# Marker user-invoked Guard configuration skills set on config-mutating CLI verbs. See
# _cli_write_allowed for what this does and does not buy.
CLI_WRITE_ENV_VAR = "GUARD_SETTINGS_SKILL"


ORPHAN_MAX_AGE_SECONDS = 7 * 24 * 60 * 60


# How long a `/clear` handoff record stays usable. The record is not a guess about which
# session preceded which — `SessionEnd` names the ending session outright, measured 55ms
# before the replacing `SessionStart` arrives — so this is not a confidence window. It is the
# expiry on a record that was never consumed: the new session's hook failing to run, or the
# process dying between the two events, leaves a file behind, and without an expiry that file
# would arm some unrelated `/clear` hours later. Five minutes is enormous next to 55ms and
# still far too short to become the persistent gate that was deleted.
CLEAR_INHERIT_MAX_AGE_SECONDS = 5 * 60


# The words that mean armed and muted, for BOTH ways a two-valued switch is written: the
# `audit-plan` value in guard.local.json and the argument to the `guard` /
# `guard-plan` shell commands. One vocabulary, because a word the config file accepts and the
# shell command rejects is a difference the user has no way to predict.
_ON_WORDS = frozenset({"on", "true", "yes", "1", "resume", "enable", "arm", "unmute"})


_OFF_WORDS = frozenset({"off", "false", "no", "0", "pause", "disable", "mute"})


# The audit switch, keyed the way the agent switches are: the key is what the user reads, and
# it names the audit it opens. Values are `_ON_WORDS` / `_OFF_WORDS` words.
AUDIT_PLAN_KEY = "audit-plan"


# A tuple of one, and it stays a tuple. The settings verb reads it to decide which keys are
# two-valued rather than modes, and that is a property of the key's TYPE — a second one would
# be added here and nowhere else.
AUDIT_SWITCHES = (AUDIT_PLAN_KEY,)


# Keys guard used to honor and no longer does, with what to tell a user who still has one in
# their config file. `_load_config` ignores an unknown key in silence, which is right for a typo
# and wrong for a key that USED to decide something: a project carrying `"audit-turn": "off"`
# opens armed from now on with nothing saying why. `cmd_settings` reads this map so the change
# is stated where the user is already looking at the file.
RETIRED_KEYS: dict[str, str] = {
    "claims-auditor": "retired in v0.153.0 — configure answer_review or turn_review instead.",
    "deferrals-auditor": "retired in v0.153.0 — configure answer_review or turn_review instead.",
    "clarity-auditor": "retired in v0.153.0 — configure answer_review or turn_review instead.",
    "audit-turn": (
        "retired in v0.124.0 — `/guard:audit-turn` uses turn_review when invoked; "
        "`/guard:answer` runs when invoked. Edited-file audits now run only at "
        "an explicit `/guard:audit-files` checkpoint."
    ),
}


DEFAULT_CONFIG: dict[str, Any] = {
    # Only the Claude post-approval gate can start a review automatically.
    AUDIT_PLAN_KEY: "on",
    # WHO reviews a held plan, as one `{"kind": "agent"|"skill", "name": "..."}` action —
    # the same shape `file_review_rules` uses per glob, without the glob, because there is
    # exactly one plan under review at a time.
    #
    # Empty means no plan review. An invalid non-empty object blocks rather than
    # silently dropping the review the user requested; see `_plan_review_action`.
    "plan_review": {},
    "turn_review": {},
    "answer_review": {},
    # A matching rule is the only opt-in for an explicit file checkpoint.
    "file_review_rules": [],
    "files_exclude": [],
    # Which directories hold those documents, relative to the project dir. Empty (the
    # default) means the whole project — a project that turned the audit on meant its
    # documents, and guard picking a subset from directory names would be guessing at a
    # repository it has never read. Set it where the non-document markdown outnumbers the
    # documents.
    "doc_dir": [],
    # Where this project writes down what its DEPLOYED system looks like — topology,
    # environments, runbooks. Exposed to audit inputs and user-supplied reviewers;
    # guard never writes here. Empty means the project has none.
    #
    # NOT confined to the project. The material it points at is frequently a knowledge base
    # kept outside the repository, and nothing derives a write from it. See
    # `paths._knowledge_dirs`.
    #
    # A LIST — this knowledge is normally split across directories rather than centralized,
    # and order is precedence. A bare string is still accepted (one directory), since that
    # is what a user with one will write.
    "knowledge_dir": [],
}

_ACTION_NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9:_-]*")


class FileReviewRule(NamedTuple):
    """One project-relative file glob and its agent or skill action."""

    glob: str
    kind: str
    name: str


class ReviewAction(NamedTuple):
    """An agent or skill a review is handed to, with no path condition in front of it.

    Deliberately not a base class `FileReviewRule` inherits: the two share a validator
    (``_review_action_name``) and nothing else. A document action is selected by matching a
    glob and is one of many; this one is the whole answer to "who reviews the plan".
    """

    kind: str
    name: str


def _review_action_name(value: Any) -> str | None:
    """Return a configured review action name, if it is safe to inject."""

    if not isinstance(value, str):
        return None
    normalized = value.strip()
    return normalized if _ACTION_NAME_RE.fullmatch(normalized) else None


def _plan_review_action(cfg: dict[str, Any]) -> tuple[ReviewAction | None, bool]:
    """Who reviews a held plan: ``(action, configured)``.

    ``(None, False)`` is unset and skips plan review. ``(None, True)`` is an invalid
    configured action and blocks approval: silently ignoring it would drop a requested
    review. The flag keeps those outcomes distinct.

    A value of the wrong JSON TYPE never reaches here: ``_load_config`` compares against this
    key's ``{}`` default and drops a non-object, which lands it in the unset case. Only an
    object with an unusable ``kind`` or ``name`` is "configured but invalid".
    """
    return _single_review_action(cfg.get("plan_review"), "audit-plan")


def _turn_review_action(cfg: dict[str, Any]) -> tuple[ReviewAction | None, bool]:
    """User-configured turn reviewer; unset skips, malformed objects report an error."""
    return _single_review_action(cfg.get("turn_review"), "audit-turn")


def _answer_review_action(cfg: dict[str, Any]) -> tuple[ReviewAction | None, bool]:
    """User-configured answer reviewer, excluding the answer dispatcher itself."""
    return _single_review_action(cfg.get("answer_review"), "answer")


def _single_review_action(raw: Any, dispatcher: str) -> tuple[ReviewAction | None, bool]:
    if not isinstance(raw, dict) or not raw:
        return None, False
    kind = raw.get("kind")
    name = _review_action_name(raw.get("name"))
    if kind not in ("agent", "skill") or name is None:
        return None, True
    # A dispatcher cannot act as its own reviewer.
    if kind == "skill" and name in {f"guard:{dispatcher}", dispatcher}:
        return None, True
    return ReviewAction(kind, name), True


def _file_review_rules(cfg: dict[str, Any]) -> tuple[FileReviewRule, ...]:
    """Return only valid per-file agent or skill rules, in declared order."""

    raw_rules = cfg.get("file_review_rules", [])
    if not isinstance(raw_rules, list):
        return ()
    rules: list[FileReviewRule] = []
    for raw_rule in raw_rules:
        if not isinstance(raw_rule, dict):
            continue
        pattern = raw_rule.get("glob")
        if not isinstance(pattern, str) or not (pattern := pattern.strip()):
            continue
        if "action" not in raw_rule:
            continue
        action = raw_rule["action"]
        if not isinstance(action, dict):
            continue
        kind = action.get("kind")
        name = _review_action_name(action.get("name"))
        if kind in ("agent", "skill") and name is not None:
            if kind == "skill" and name in {"guard:audit-files", "audit-files"}:
                continue
            rules.append(FileReviewRule(pattern, kind, name))
    return tuple(rules)


def _file_review_rule(path: str, rules: tuple[FileReviewRule, ...]) -> FileReviewRule | None:
    """Return the most-specific configured rule whose glob matches ``path``.

    ``*`` stays within one directory, while ``**`` may cross directories. Paths are already
    project-relative before reaching here, so a rule can never widen the document scope.

    **The FILENAME decides first, and that ordering is the fix for a real misroute.** Ranking
    literal directory depth first — as this did until v0.141.1 — sent
    `Github/ticket/AGENTS.md` to `Github/**/*.md`'s reviewer instead of to `**/AGENTS.md`'s,
    because one literal directory segment outranked an exactly named file. A rule that names
    the file is a rule about THAT file wherever it lives; a rule with a wildcard basename is a
    rule about an area, and an area rule that captured a file named by another rule leaves no
    trace — the wrong auditor reports on the document and its report looks like any other.
    So: a fully literal last segment beats a partly literal one (`AGENTS.md` over `*.md`),
    which beats a bare wildcard (`*.md` over `*`). Only then does literal directory depth
    decide, so `Github/AGENTS.md` still wins over `**/AGENTS.md`. Literal detail and fewer
    wildcards follow, and configuration order breaks an exact tie.
    """

    normalized = path.replace("\\", "/")
    matches: list[tuple[tuple[int, int, int, int, int, int, int], FileReviewRule]] = []
    for rule_index, rule in enumerate(rules):
        pattern = rule.glob.replace("\\", "/")
        if _doc_glob_regex(pattern).fullmatch(normalized):
            segments = [segment for segment in pattern.split("/") if segment]
            basename = segments[-1] if segments else ""
            basename_wildcards = sum(basename.count(char) for char in "*?[")
            if not basename_wildcards:
                basename_rank = 2
            elif any(char not in "*?[]" for char in basename):
                basename_rank = 1
            else:
                basename_rank = 0
            prefix_depth = 0
            for segment in segments:
                if "*" in segment or "?" in segment or "[" in segment:
                    break
                prefix_depth += 1
            literal_segments = sum(
                not any(char in segment for char in "*?[") for segment in segments)
            literal_chars = sum(1 for char in pattern if char not in "*?[]/")
            wildcard_count = sum(pattern.count(char) for char in "*?[")
            matches.append(((basename_rank, prefix_depth, literal_segments, literal_chars,
                             -wildcard_count, len(segments), -rule_index), rule))
    return max(matches, key=lambda match: match[0])[1] if matches else None


def _doc_glob_regex(pattern: str) -> re.Pattern[str]:
    """Compile Guard's project-relative glob syntax (`*` one level, `**` any depth)."""
    regex_parts: list[str] = []
    cursor = 0
    while cursor < len(pattern):
        char = pattern[cursor]
        if char == "*" and cursor + 1 < len(pattern) and pattern[cursor + 1] == "*":
            cursor += 2
            if cursor < len(pattern) and pattern[cursor] == "/":
                regex_parts.append("(?:.*/)?")
                cursor += 1
            else:
                regex_parts.append(".*")
            continue
        if char == "*":
            regex_parts.append("[^/]*")
        elif char == "?":
            regex_parts.append("[^/]")
        elif char == "[":
            # Character classes are not part of Guard's small glob language. Treat `[` as
            # literal so a malformed pattern cannot unexpectedly widen an exclusion.
            regex_parts.append(re.escape(char))
        else:
            regex_parts.append(re.escape(char))
        cursor += 1
    return re.compile("".join(regex_parts))


def _doc_glob_matches(path: str, pattern: str) -> bool:
    """Whether a project-relative path matches the shared document glob syntax."""
    return _doc_glob_regex(pattern.replace("\\", "/")).fullmatch(
        path.replace("\\", "/")) is not None


def _file_excluded(path: str, patterns: Any) -> bool:
    """Apply ordered exclusion globs; ! restores a file and the last match wins."""
    if isinstance(patterns, str):
        patterns = [patterns]
    if not isinstance(patterns, list):
        return False
    excluded = False
    for pattern in patterns:
        if not isinstance(pattern, str) or not (pattern := pattern.strip()):
            continue
        restore = pattern.startswith("!")
        if restore or pattern.startswith("\\!"):
            pattern = pattern[1:]
        if pattern and _doc_glob_matches(path, pattern):
            excluded = not restore
    return excluded


def _trace_enabled() -> bool:
    return os.environ.get(TRACE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _cli_write_allowed() -> bool:
    """True when a config-mutating CLI verb may write.

    guard never gates Bash, so the model can invoke this script directly — and the
    config-mutating verbs can weaken guard itself: `settings set audit-plan off`
    disables the automatic plan gate by default. The `guard:settings` skill is
    `disable-model-invocation: true` (user-invoked only) and sets this marker; a bare
    model-issued Bash call does not have it.

    This is a SPEED BUMP, NOT A SECURITY BOUNDARY: the variable name is in this file,
    which the model can read, so a model that decides to defeat guard can set it. What
    it buys is (a) the unreflective path — "this gate is in my way, let me widen it" —
    fails closed, (b) the refusal names the user as the only legitimate widener, and
    (c) the attempt lands in the trace as `refused_no_skill_marker`. A model that
    deliberately sets the marker is outside guard's threat model, and either way the
    Bash call is visible to the user in the transcript.
    """
    return os.environ.get(CLI_WRITE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _load_config(project_dir: Path) -> dict[str, Any]:
    """Load the JSON config at guard.local.json, if present. Fail-open to defaults.

    Only keys present in DEFAULT_CONFIG are honored, and only when the supplied value
    matches the default's JSON type — a list for file-review rules,
    (or a bare str) for ``knowledge_dir`` — so a malformed value can never change a setting
    by accident.
    """
    config = dict(DEFAULT_CONFIG)
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return config
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return config
    if not isinstance(data, dict):
        return config
    for key, default in DEFAULT_CONFIG.items():
        want: type | tuple[type, ...]
        if key in AUDIT_SWITCHES:
            # `"off"` and `false` are the same instruction written two ways, and a two-valued
            # switch is the one setting a user reasonably writes as a JSON boolean. Rejecting
            # one of the two spellings would silently ignore an intention that is not
            # ambiguous; `_audit_on` reads both.
            want = (str, bool)
        elif isinstance(default, list):
            # A list default accepts a bare string too — `knowledge_dir` takes one
            # directory written plainly. The resolver normalizes; this only checks shape.
            want = (list, str)
        else:
            want = type(default)
        if key in data and isinstance(data[key], want):
            config[key] = data[key]
    return config


def _load_raw_config(project_dir: Path) -> dict[str, Any]:
    """Read guard.local.json as a raw dict (unmerged, no defaults applied), or {} if
    missing/malformed. Used by the ``settings`` CLI so it can edit one key in place
    while preserving every other key the user has set."""
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_config(project_dir: Path, data: dict[str, Any]) -> bool:
    """Atomically write guard.local.json. Returns True on success."""
    path = project_dir / CONFIG_REL
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.parent / (path.name + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        tmp.replace(path)
        return True
    except OSError:
        return False


def _parse_switch(value: str) -> bool | None:
    """Parse an on/off word: True armed, False muted, None when it is neither.

    The caller reports the error rather than guessing — this is what the ``settings`` CLI
    validates a written value with, and guessing there would record a switch the user did not
    ask for in a file that outlives the session.
    """
    v = value.strip().lower()
    if v in _ON_WORDS:
        return True
    if v in _OFF_WORDS:
        return False
    return None


def _audit_on(cfg: dict[str, Any], key: str) -> bool:
    """Does this project's config open a session with ``key``'s audit armed?

    A CONFIG reader, never a state reader: the live answer for a session is
    ``state._plan_audit_paused``, which this seeds and the shell toggle then overrides. Absent,
    malformed, or written as a JSON boolean all resolve here — and anything unrecognized
    resolves to THAT KEY's own default (see ``DEFAULT_CONFIG``), so a mistyped switch lands
    where an absent one would, which is the only fallback a project can predict. Written
    per-key, though ``audit-plan`` is currently the only key: the rule is about what a
    misspelling costs, not about how many switches there happen to be.

    The retired automatic edited-file audit has no switch here; current file reviews begin at
    an explicit checkpoint.
    """
    raw = cfg.get(key, DEFAULT_CONFIG[key])
    if isinstance(raw, bool):
        return raw
    parsed = _parse_switch(str(raw))
    if parsed is None:
        return _parse_switch(str(DEFAULT_CONFIG[key])) is True
    return parsed
