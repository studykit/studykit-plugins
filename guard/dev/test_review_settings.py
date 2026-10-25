#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Project-scoped settings adapter and per-rule Stop policy regressions."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
SETTINGS = PLUGIN / "skills/settings/scripts/settings.py"


class ReviewSettingsTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-review-settings-")
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name) / "project"
        self.project.mkdir()
        self.outside = Path(temporary.name) / "outside"
        self.outside.mkdir()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        self.env.update(PYTHONDONTWRITEBYTECODE="1", GUARD_SETTINGS_SKILL="1",
                        GUARD_PROJECT_DIR=str(self.outside),
                        CLAUDE_PROJECT_DIR=str(self.outside))

    def call(self, host, *arguments, marker=True, session="native-session"):
        env = dict(self.env, GUARD_HOST="claude" if host == "codex" else "codex")
        if not marker:
            env.pop("GUARD_SETTINGS_SKILL", None)
        return subprocess.run(
            [sys.executable, str(SETTINGS), "--host", host,
             "--project", str(self.project), "--session", session, *arguments],
            cwd=self.outside, env=env, capture_output=True, text=True, timeout=15)

    def config(self, host):
        path = self.project / f".{host}/guard.local.json"
        return json.loads(path.read_text()) if path.exists() else None

    def seed(self, host, value):
        path = self.project / f".{host}/guard.local.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(value))

    def test_explicit_host_and_project_override_inherited_environment(self):
        for host in ("claude", "codex"):
            result = self.call(host, "set", "turn_review",
                               '{"kind":"agent","name":"project-turn-check"}')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.config(host)["turn_review"]["name"], "project-turn-check")
            self.assertEqual(list(self.outside.iterdir()), [])

    def test_rules_round_trip_stop_policy_and_preserve_unrelated_values(self):
        rules = [
            {"glob": "src/**", "action": {"kind": "agent", "name": "source-reviewer"},
             "on_stop": "ask"},
            {"glob": "config/*.json", "action": {"kind": "skill", "name": "review-config"}},
            {"glob": "docs/**", "action": {"kind": "agent", "name": "docs-reviewer"},
             "on_stop": "manual"},
        ]
        for host in ("claude", "codex"):
            self.seed(host, {"future-setting": {"keep": True}, "files_exclude": ["vendor/**"]})
            result = self.call(host, "set", "file_review_rules", json.dumps(rules))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.config(host)["file_review_rules"], rules)
            self.assertEqual(self.config(host)["future-setting"], {"keep": True})
            self.assertEqual(self.config(host)["files_exclude"], ["vendor/**"])
            self.assertIn("src/** -> agent:source-reviewer (on_stop: ask)", result.stdout)
            self.assertIn("config/*.json -> skill:review-config (on_stop: manual)", result.stdout)
            self.assertNotIn("actions (built in)", result.stdout)

    def test_invalid_stop_policy_is_rejected_without_a_write(self):
        for host in ("claude", "codex"):
            original = {"file_review_rules": []}
            self.seed(host, original)
            for policy in ("automatic", "ASK", True, {}, None):
                rules = [{"glob": "**", "action": {"kind": "agent", "name": "reviewer"},
                          "on_stop": policy}]
                result = self.call(host, "set", "file_review_rules", json.dumps(rules))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("on_stop", result.stderr)
                self.assertEqual(self.config(host), original)

    def test_configured_reviewer_names_are_exact_without_builtin_aliases(self):
        for host in ("claude", "codex"):
            rules = [{"glob": "**/*.txt", "action": {"kind": "agent", "name": "my-plugin:reviewer_2"},
                      "on_stop": "ask"}]
            result = self.call(host, "set", "file_review_rules", json.dumps(rules))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.config(host)["file_review_rules"][0]["action"]["name"], "my-plugin:reviewer_2")

    def test_a_settings_write_requires_user_skill_marker(self):
        for host in ("claude", "codex"):
            result = self.call(host, "set", "files_exclude", "vendor/**", marker=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("refusing", result.stderr)
            self.assertIsNone(self.config(host))
            shown = self.call(host, "show", marker=False)
            self.assertEqual(shown.returncode, 0, shown.stderr)

    def test_bad_session_or_argument_shape_cannot_change_settings(self):
        for host in ("claude", "codex"):
            for session in ("../other", "", "with/slash"):
                result = self.call(host, "set", "files_exclude", "vendor/**", session=session)
                self.assertNotEqual(result.returncode, 0)
            result = self.call(host, "set", "files_exclude", "vendor/**", "extra")
            self.assertNotEqual(result.returncode, 0)
            self.assertIsNone(self.config(host))

    def test_unset_changes_only_requested_key(self):
        for host in ("claude", "codex"):
            self.seed(host, {"turn_review": {"kind": "agent", "name": "custom"},
                             "files_exclude": ["vendor/**"]})
            result = self.call(host, "unset", "turn_review")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.config(host), {"files_exclude": ["vendor/**"]})


if __name__ == "__main__":
    unittest.main()
