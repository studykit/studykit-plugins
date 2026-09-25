import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import herdr_main


class PopupShellTests(unittest.TestCase):
    def test_action_uses_the_focused_panes_foreground_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.shellbox",
                   "HERDR_SOCKET_PATH": "/tmp/herdr.sock",
                   "HERDR_PLUGIN_CONTEXT_JSON": json.dumps({"focused_pane_id": "w1:p2"})}
            def host_call(_env, method, **params):
                if method == "pane.get":
                    self.assertEqual(params["pane_id"], "w1:p2")
                    return {"pane": {"cwd": "/tmp", "foreground_cwd": str(root),
                                     "terminal_id": "terminal-2",
                                     "terminal_title_stripped": "Editor #1\nproject"}}
                self.assertEqual(method, "plugin.pane.open")
                self.assertEqual(params["plugin_id"], "studykit.shellbox")
                self.assertEqual(params["entrypoint"], "shell")
                self.assertEqual(params["cwd"], str(root))
                self.assertTrue(params["focus"])
                self.assertEqual(params["env"]["POPUP_SHELL_SESSION"],
                                 herdr_main.shell_identity(env, "w1:p2", "terminal-2")[1])
                self.assertEqual(params["env"]["SHELLBOX_SOURCE_LABEL"],
                                 "Herdr w1:p2 · Editor 1 project")
                return {"plugin_pane": {}}
            with patch("herdr_main.call", side_effect=host_call) as call:
                self.assertEqual(herdr_main.main(env, "open"), 0)
            self.assertEqual(call.call_count, 2)

    def test_session_identity_is_per_server_pane_and_terminal(self):
        env = {"HERDR_SOCKET_PATH": "/tmp/herdr.sock"}
        first = herdr_main.shell_identity(env, "w1:p1", "terminal-a")
        self.assertEqual(first, herdr_main.shell_identity(env, "w1:p1", "terminal-a"))
        self.assertNotEqual(first, herdr_main.shell_identity(env, "w1:p2", "terminal-a"))
        self.assertNotEqual(first, herdr_main.shell_identity(env, "w1:p1", "terminal-b"))
        self.assertNotEqual(first, herdr_main.shell_identity(
            {"HERDR_SOCKET_PATH": "/tmp/other.sock"}, "w1:p1", "terminal-a"))

    def test_source_label_replaces_the_hash_in_this_sessions_status(self):
        env = {"SHELLBOX_SOURCE_LABEL": "Herdr w1:p2 · Editor"}
        with patch("herdr_main.subprocess.run") as run:
            herdr_main.show_source_label(["tmux", "-L", "test"], env, "session-id")
        calls = [call.args[0] for call in run.call_args_list]
        self.assertEqual(calls[0][-4:],
                         ["-t", "session-id", "@shellbox_source_label", "Herdr w1:p2 · Editor"])
        self.assertEqual(calls[1][-3:],
                         ["session-id", "status-left", "#{@shellbox_source_label} "])
        self.assertEqual(calls[2][-3:], ["session-id", "status-left-length", "70"])

    def test_popup_attaches_to_a_persistent_shell(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_ENV": "1", "SHELL": "/bin/zsh", "PWD": "/old",
                   "TMUX": "other-server", "POPUP_SHELL_SERVER": "popup-shell-123",
                   "POPUP_SHELL_SESSION": "abc123", "HERDR_PLUGIN_STATE_DIR": directory,
                   "HOME": directory}
            with patch("herdr_main.shutil.which", side_effect=lambda name: "/bin/tmux" if name == "tmux" else name), \
                 patch("herdr_main.os.access", return_value=True), \
                 patch("herdr_main.subprocess.run") as run, \
                 patch("herdr_main.os.execvpe") as exec_shell:
                run.return_value.returncode = 1
                run.return_value.stdout = b""
                self.assertEqual(herdr_main.main(env, "panel"), 0)
            executable, argv, shell_env = exec_shell.call_args.args
            self.assertEqual(executable, "/bin/tmux")
            self.assertEqual(argv[-3:], ["attach-session", "-t", "abc123"])
            self.assertEqual(shell_env["PWD"], os.getcwd())
            self.assertNotIn("TMUX", shell_env)
            self.assertEqual(run.call_args_list[1].args[0][-2:], ["/bin/zsh", "-i"])
            self.assertTrue(any(call.args[0][-3:] == ["root", "C-q", "detach-client"]
                                for call in run.call_args_list))

    def test_indicator_prefixes_the_source_agent_label(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_PLUGIN_ID": "studykit.shellbox", "HERDR_PLUGIN_CONFIG_DIR": directory}
            def host_call(_env, method, **params):
                if method == "pane.get":
                    return {"pane": {"agent": "claude"}}
                reports.append(params)
                return {}
            reports = []
            with patch("herdr_main.call", side_effect=host_call):
                herdr_main.mark_pane(env, "w1:p2")
                (Path(directory) / "config.toml").write_text('indicator = ""\n')
                herdr_main.mark_pane(env, "w1:p2")
            self.assertEqual(reports, [{"pane_id": "w1:p2", "source": "studykit.shellbox",
                                        "agent": "claude",
                                        "display_agent": " claude"}])

    def test_closed_shell_clears_its_source_panes_indicator(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.shellbox",
                   "HERDR_PLUGIN_STATE_DIR": directory}
            herdr_main.session_record(env, "abc123").write_text("w1:p2")
            with patch("herdr_main.call") as call:
                self.assertEqual(herdr_main.main(env, "closed", "abc123"), 0)
                herdr_main.main(env, "closed", "abc123")
            call.assert_called_once_with(env, "pane.report_metadata", pane_id="w1:p2",
                                         source="studykit.shellbox", clear_display_agent=True)
            self.assertFalse(herdr_main.session_record(env, "abc123").exists())

    def test_agent_detection_marks_only_panes_with_a_shell(self):
        env = {"HERDR_PLUGIN_EVENT_JSON": json.dumps({"event": "pane.agent_detected",
                                                      "data": {"pane_id": "w1:p2"}})}
        with patch("herdr_main.pane_has_shell", return_value=True) as has_shell, \
             patch("herdr_main.mark_pane") as mark:
            herdr_main.on_agent_detected(env)
            has_shell.return_value = False
            herdr_main.on_agent_detected(env)
        self.assertEqual(has_shell.call_args.args[1], "w1:p2")
        mark.assert_called_once_with(env, "w1:p2")

    def test_reopening_reuses_the_existing_session(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_ENV": "1", "SHELL": "/bin/zsh",
                   "POPUP_SHELL_SERVER": "popup-shell-123",
                   "POPUP_SHELL_SESSION": "abc123", "HERDR_PLUGIN_STATE_DIR": directory,
                   "HOME": directory}
            with patch("herdr_main.shutil.which", side_effect=lambda name: "/bin/tmux" if name == "tmux" else name), \
                 patch("herdr_main.os.access", return_value=True), \
                 patch("herdr_main.subprocess.run") as run, \
                 patch("herdr_main.os.execvpe"):
                run.return_value.returncode = 0
                run.return_value.stdout = b""
                self.assertEqual(herdr_main.main(env, "panel"), 0)
            self.assertEqual(run.call_args_list[0].args[0][-3:], ["has-session", "-t", "abc123"])
            self.assertFalse(any("new-session" in call.args[0] for call in run.call_args_list))

    def test_existing_session_loads_user_tmux_config_once(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / ".tmux.conf"
            config.write_text("set -g prefix C-s\n")
            env = {"HERDR_ENV": "1", "SHELL": "/bin/zsh", "HOME": directory,
                   "POPUP_SHELL_SERVER": "popup-shell-123",
                   "POPUP_SHELL_SESSION": "abc123", "HERDR_PLUGIN_STATE_DIR": directory}
            with patch("herdr_main.shutil.which", side_effect=lambda name: "/bin/tmux" if name == "tmux" else name), \
                 patch("herdr_main.os.access", return_value=True), \
                 patch("herdr_main.subprocess.run") as run, \
                 patch("herdr_main.os.execvpe"):
                run.return_value.returncode = 0
                run.return_value.stdout = b""
                herdr_main.main(env, "panel")
            calls = [item.args[0] for item in run.call_args_list]
            self.assertEqual([item[-2:] for item in calls if "source-file" in item],
                             [["source-file", str(config)]])
            self.assertTrue(any(item[-3:] == ["show-option", "-gqv", "@popup_shell_config"]
                                for item in calls))
            self.assertTrue(any(item[-3:] == ["root", "C-q", "detach-client"]
                                for item in calls))

    def test_close_key_can_use_tmux_prefix_or_be_disabled(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "config.toml"
            env = {"HERDR_PLUGIN_CONFIG_DIR": directory}
            config.write_text('close_key = "prefix+q"\n')
            self.assertEqual(herdr_main.close_binding(env), ("prefix", "q"))
            config.write_text('close_key = "none"\n')
            self.assertIsNone(herdr_main.close_binding(env))
            with patch("herdr_main.subprocess.run") as run:
                run.return_value.stdout = b""
                herdr_main.apply_close_binding(["tmux", "-L", "test"], env)
            self.assertFalse(any("unbind-key" in call.args[0] or "bind-key" in call.args[0]
                                 for call in run.call_args_list))
            config.write_text('close_key = 42\n')
            with self.assertRaisesRegex(ValueError, "close_key"):
                herdr_main.close_binding(env)

    def test_changed_close_key_replaces_the_previous_binding(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "config.toml").write_text('close_key = "prefix+q"\n')
            env = {"HERDR_PLUGIN_CONFIG_DIR": directory}
            with patch("herdr_main.subprocess.run") as run:
                run.return_value.stdout = b"root:C-q\n"
                herdr_main.apply_close_binding(["tmux", "-L", "test"], env)
            calls = [call.args[0] for call in run.call_args_list]
            self.assertTrue(any(item[-5:] == ["unbind-key", "-q", "-T", "root", "C-q"]
                                for item in calls))
            self.assertTrue(any(item[-3:] == ["prefix", "q", "detach-client"]
                                for item in calls))

    def test_toggle_uses_the_configured_herdr_shortcut(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "herdr.toml"
            env = {"HERDR_CONFIG_PATH": str(config), "HERDR_PLUGIN_ID": "studykit.shellbox"}
            config.write_text('''[keys]
prefix = "ctrl+s"
[[keys.command]]
key = "ctrl+h"
type = "plugin_action"
command = "studykit.shellbox.open"
''')
            self.assertEqual(herdr_main.toggle_chord(env), ("C-h",))
            with patch("herdr_main.subprocess.run") as run:
                run.return_value.stdout = b""
                herdr_main.apply_toggle_binding(["tmux", "-L", "test"], env)
            self.assertTrue(any(call.args[0][-3:] == ["root", "C-h", "detach-client"]
                                for call in run.call_args_list))
            config.write_text(config.read_text().replace('key = "ctrl+h"', 'key = "prefix+s"'))
            self.assertEqual(herdr_main.toggle_chord(env), ("C-s", "s"))
            with patch("herdr_main.subprocess.run") as run:
                run.return_value.stdout = b""
                herdr_main.apply_toggle_binding(["tmux", "-L", "test"], env)
            calls = [call.args[0] for call in run.call_args_list]
            self.assertTrue(any(item[-5:] == ["root", "C-s", "switch-client", "-T", "popup-shell-toggle"]
                                for item in calls))
            self.assertTrue(any(item[-3:] == ["popup-shell-toggle", "s", "detach-client"]
                                for item in calls))


if __name__ == "__main__":
    unittest.main()
