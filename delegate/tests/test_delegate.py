"""Behavioral checks for the self-contained Delegate plugin."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest


PLUGIN = Path(__file__).resolve().parents[1]


class DelegateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="delegate-plugin-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / "codex"
        self.env = os.environ.copy()
        self.data = self.root / "plugin-data"
        self.env.update(CODEX_HOME=str(self.home), PLUGIN_DATA=str(self.data))
        self.env.pop("DELEGATE_LEDGER", None)

    def run_script(self, script, *args, ok=True, plugin=PLUGIN):
        result = subprocess.run([sys.executable, str(plugin / "scripts" / script), *args],
                                env=self.env, cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return result.stdout

    def add(self, verdict="pass", cause=None, **kwargs):
        args = ["add", "--category", "lookup", "--task", "Locate settings ownership",
                "--agent-type", "worker", "--model", "gpt-6-luna", "--effort", "low",
                "--verdict", verdict, "--reason", "Verified source"]
        if cause:
            args += ["--cause", cause]
        return self.run_script("ledger.py", *args, **kwargs).strip()

    def test_ledger_amend_and_recall_preserve_append_history(self):
        record = self.add("fail", "instruction")
        path = self.data / "ledger.jsonl"
        original = path.read_bytes()
        self.run_script("ledger.py", "amend", record, "--verdict", "pass", "--reason", "User verified")
        self.assertTrue(path.read_bytes().startswith(original))
        self.assertEqual(len(path.read_text().splitlines()), 2)
        output = self.run_script("ledger.py", "recall", "--category", "lookup")
        self.assertIn("1 pass, 0 partial, 0 fail", output)

    def test_recall_reports_average_duration_and_dispatcher_amendment(self):
        record = self.add("pass")
        self.add("pass")
        self.run_script("ledger.py", "add", "--category", "lookup", "--task", "Find x",
                        "--agent-type", "worker", "--model", "gpt-6-luna", "--effort", "low",
                        "--verdict", "pass", "--reason", "Verified", "--duration-ms", "180000")
        self.run_script("ledger.py", "amend", record, "--by", "dispatcher", "--verdict", "fail",
                        "--cause", "capability", "--reason", "Evidence contradicted the pass")
        output = self.run_script("ledger.py", "recall", "--category", "lookup")
        self.assertIn("avg 3.0 min", output)
        self.assertIn("(amended by dispatcher)", output)

    def test_ledger_override(self):
        path = self.root / "alternate/ledger.jsonl"
        self.env["DELEGATE_LEDGER"] = str(path)
        self.add()
        self.assertTrue(path.exists())
        self.assertFalse((self.data / "ledger.jsonl").exists())

    def test_invalid_verdict_does_not_record(self):
        self.run_script("ledger.py", "add", "--category", "lookup", "--task", "Find x",
                        "--agent-type", "worker", "--model", "gpt-6-luna", "--effort", "low",
                        "--verdict", "fail", "--reason", "No cause", ok=False)
        self.assertFalse((self.data / "ledger.jsonl").exists())

    def test_setup_installs_durable_agent_and_preserves_config_bytes(self):
        self.home.mkdir()
        config = self.home / "config.toml"
        original = b'# User config\r\nmodel = "gpt-6-luna"\r\n'
        config.write_bytes(original)
        result = json.loads(self.run_script("setup.py"))
        self.assertTrue(result["configured"])
        self.assertTrue(config.read_bytes().startswith(original))
        agent = Path(result["agent"])
        self.assertEqual(agent.read_bytes(), (PLUGIN / "agents/delegate-sizer.toml").read_bytes())
        self.assertEqual(tomllib.loads(config.read_text())["agents"]["delegate-sizer"]["config_file"], str(agent))
        self.assertFalse(str(agent).startswith(str(PLUGIN)))
        snapshot = config.read_bytes()
        self.run_script("setup.py")
        self.assertEqual(snapshot, config.read_bytes())
        status = json.loads(self.run_script("setup.py", "status"))
        self.assertTrue(status["configured"] and status["up_to_date"])
        self.add()
        history = (self.data / "ledger.jsonl").read_bytes()
        (self.data / "sizer-lessons.md").write_text("A supported sizing lesson with record IDs.\n")
        self.run_script("setup.py", "remove")
        self.assertEqual(config.read_bytes(), original)
        self.assertFalse(agent.exists())
        self.assertEqual((self.data / "ledger.jsonl").read_bytes(), history)
        self.assertTrue((self.data / "sizer-lessons.md").exists())

    def test_user_role_conflict_changes_nothing(self):
        self.home.mkdir()
        config = self.home / "config.toml"
        original = '[agents.delegate-sizer]\ndescription="Mine"\nconfig_file="mine.toml"\n'
        config.write_text(original)
        self.run_script("setup.py", ok=False)
        self.assertEqual(config.read_text(), original)
        self.assertFalse(self.data.exists())

    def test_edited_agent_is_preserved_on_update_and_remove(self):
        result = json.loads(self.run_script("setup.py"))
        agent = Path(result["agent"])
        agent.write_text(agent.read_text() + "\n# User change\n")
        config = (self.home / "config.toml").read_bytes()
        self.run_script("setup.py", ok=False)
        self.run_script("setup.py", "remove", ok=False)
        self.assertTrue(agent.read_text().endswith("# User change\n"))
        self.assertEqual((self.home / "config.toml").read_bytes(), config)

    def test_edited_role_is_preserved_on_remove(self):
        result = json.loads(self.run_script("setup.py"))
        config = self.home / "config.toml"
        config.write_text(config.read_text().replace("Do not invoke otherwise.", "Customized."))
        original = config.read_bytes()
        self.run_script("setup.py", "remove", ok=False)
        self.assertEqual(config.read_bytes(), original)
        self.assertTrue(Path(result["agent"]).exists())

    def test_relocated_package_and_upgrade_use_no_checkout_dependency(self):
        copied = self.root / "installed-plugin"
        shutil.copytree(PLUGIN, copied, ignore=shutil.ignore_patterns("__pycache__"))
        result = json.loads(self.run_script("setup.py", plugin=copied))
        agent = Path(result["agent"])
        copied.rename(self.root / "old-plugin-cache")
        self.assertTrue(agent.is_file())
        copied = self.root / "new-plugin-cache"
        shutil.copytree(PLUGIN, copied, ignore=shutil.ignore_patterns("__pycache__"))
        source = copied / "agents/delegate-sizer.toml"
        source.write_text(source.read_text() + "\n# Updated bundled definition\n")
        self.run_script("setup.py", plugin=copied)
        self.assertEqual(agent.read_bytes(), source.read_bytes())
        self.add(plugin=copied)

    def test_config_symlink_preserved(self):
        self.home.mkdir()
        real = self.root / "real-config.toml"
        real.write_text('model="gpt-6-luna"\n')
        config = self.home / "config.toml"
        config.symlink_to(real)
        self.run_script("setup.py")
        self.assertTrue(config.is_symlink())
        self.run_script("setup.py", "remove")
        self.assertEqual(real.read_text(), 'model="gpt-6-luna"\n')

    def test_explicit_plugin_data_without_shell_environment(self):
        self.env.pop("PLUGIN_DATA")
        result = json.loads(self.run_script("setup.py", "install", "--data-dir", str(self.data)))
        self.assertTrue(result["configured"])
        output = self.run_script("ledger.py", "--data-dir", str(self.data), "recall", "--category", "lookup")
        self.assertIn("No recorded runs", output)

    def test_missing_plugin_data_does_not_guess_a_directory(self):
        self.env.pop("PLUGIN_DATA")
        self.run_script("setup.py", ok=False)
        self.run_script("ledger.py", "recall", ok=False)
        self.assertFalse(self.home.exists())

    def test_hook_normalizes_storage_without_writing(self):
        script = PLUGIN / "hooks/scripts/hook_codex.py"
        result = subprocess.run([sys.executable, str(script)], input=json.dumps({"hook_event_name": "SessionStart"}),
                                env=self.env, cwd=self.root, text=True, capture_output=True, check=True)
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn(str(self.data.resolve()), context)
        self.assertIn("sizer-lessons.md", context)
        self.assertFalse(self.data.exists())

    def test_claude_ledger_uses_explicit_data_dir_and_claude_models(self):
        self.env.pop("PLUGIN_DATA")
        data = self.root / "claude-data"
        args = ["--data-dir", str(data), "add", "--category", "lookup", "--task", "Find x",
                "--agent-type", "general-purpose", "--model", "haiku", "--effort", "low",
                "--verdict", "pass", "--reason", "Verified"]
        record = self.run_script("ledger_claude.py", *args).strip()
        self.assertIn(record, (data / "ledger.jsonl").read_text())
        args[args.index("haiku")] = "gpt-6-luna"
        self.run_script("ledger_claude.py", *args, ok=False)
        self.run_script("ledger_claude.py", "recall", ok=False)

    def test_each_host_loads_only_its_own_entry_points(self):
        # Claude Code always scans skills/ and hooks/hooks.json, so neither may exist:
        # the Codex skills and hook would load in Claude too.
        self.assertFalse((PLUGIN / "skills").exists())
        self.assertFalse((PLUGIN / "hooks/hooks.json").exists())
        codex = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
        for key in ("skills", "hooks"):
            self.assertTrue((PLUGIN / codex[key]).exists(), key)
        self.assertTrue((PLUGIN / codex["extensions"]["com.openai"]["onboardingSkill"]).is_file())
        claude = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(claude["version"], codex["version"])
        for path in claude["skills"]:
            self.assertTrue((PLUGIN / path).is_dir(), path)
        self.assertTrue((PLUGIN / "claude/skills/delegate/SKILL.md").is_file())
        self.assertTrue((PLUGIN / "agents/delegate-sizer.md").is_file())
        self.assertTrue((PLUGIN / "agents/delegate-verifier.md").is_file())


if __name__ == "__main__":
    unittest.main()
