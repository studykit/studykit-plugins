import curses
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
import settings
from ui import Navigator


class ChordTests(unittest.TestCase):
    def test_chords(self):
        self.assertEqual(settings.chord("ctrl+a"), "\x01")
        self.assertEqual(settings.chord("alt+x"), "\x1bx")
        self.assertEqual(settings.chord("shift+a"), "A")
        self.assertEqual(settings.chord("N"), "N")
        self.assertEqual(settings.chord("+"), "+")
        self.assertEqual(settings.chord("pagedown"), curses.KEY_NPAGE)
        self.assertIsNone(settings.chord("ctrl+f5"))
        self.assertIsNone(settings.chord("hyper+a"))


class SettingsTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name)
        self.config = self.base / "config"
        self.root = self.base / "project"
        self.root.mkdir()
        (self.root / "code.py").write_text("\n".join(f"x = {i}" for i in range(50)))

    def write(self, text):
        self.config.mkdir(exist_ok=True)
        settings.path(self.config).write_text(text)

    def navigator(self):
        return Navigator(self.root, "pane", False, "env-editor",
                         settings_loader=lambda: settings.load(self.config),
                         settings_file=lambda: settings.ensure(self.config))

    def test_missing_file_keeps_defaults(self):
        nav = self.navigator()
        self.assertEqual((nav.editor, nav.icons, nav.bindings), ("env-editor", "plain", {}))
        self.assertNotIn("config.toml", nav.message)

    def test_values_apply_and_mistakes_are_reported(self):
        self.write('''[editor]
command = "nvim +{line} {file}"
[ui]
icons = "nerd"
align = "left"
[keys]
"ctrl+f" = "search"
"alt+z" = ":zoom fit"
"ctrl+q" = "nonsense"
"hyper+q" = "quit"
"ctrl+b" = ":bogus"
''')
        nav = self.navigator()
        self.assertEqual((nav.editor, nav.icons, nav.alignment), ("nvim +{line} {file}", "nerd", "left"))
        self.assertEqual(nav.bindings, {"\x06": "search", "\x1bz": ":zoom fit"})
        for mistake in ("'ctrl+q' needs an action", "unknown key 'hyper+q'", "unknown command in 'ctrl+b'"):
            self.assertIn(mistake, nav.message)

    def test_invalid_toml_is_reported(self):
        self.write("[ui\n")
        self.assertIn("config.toml:", self.navigator().message)

    def test_bindings_run_actions_and_commands_but_not_while_typing(self):
        self.write('[keys]\n"ctrl+f" = "search"\n"ctrl+l" = ":icons nerd"\n"q" = "quit"\n')
        nav = self.navigator()
        nav.key("\x0c", None)
        self.assertEqual(nav.icons, "nerd")
        nav.key("\x06", None)
        self.assertTrue(nav.searching)
        self.assertTrue(nav.key("q", None))  # Typed into the search, not a quit.
        self.assertEqual(nav.query, "q")
        nav.key("\x1b", None)
        self.assertFalse(nav.key("q", None))

    def test_config_command_creates_template_and_reloads(self):
        nav = self.navigator()
        def fake_editor(screen, command, cwd):
            Path(command[-1]).write_text('[ui]\nicons = "nerd"\n')
            return type("Result", (), {"returncode": 0})()
        with patch("ui.editor_command", side_effect=lambda editor, path, line=1: [editor, str(path)]), \
                patch.object(nav, "run_terminal", side_effect=fake_editor) as run:
            nav.run_command("config", None)
        self.assertEqual(run.call_args.args[1], ["env-editor", str(self.config / "config.toml")])
        self.assertEqual((nav.icons, nav.message), ("nerd", "Settings reloaded"))

    def test_template_is_valid_and_fully_commented(self):
        settings.ensure(self.config)
        loaded = settings.load(self.config)
        self.assertEqual((loaded.editor, loaded.icons, loaded.keys, loaded.errors), ("", None, {}, []))


class EditorCommandTests(unittest.TestCase):
    def test_placeholders_stay_single_arguments(self):
        path = Path("/tmp/a b; rm.txt")
        with patch("core.shutil.which", return_value="/bin/editor"):
            self.assertEqual(core.editor_command("code --goto {file}:{line}", path, 12),
                             ["code", "--goto", "/tmp/a b; rm.txt:12"])
            self.assertEqual(core.editor_command("nvim +{line}", path, 3), ["nvim", "+3", "/tmp/a b; rm.txt"])
            self.assertEqual(core.editor_command("vim", path, 3), ["vim", "/tmp/a b; rm.txt"])


if __name__ == "__main__":
    unittest.main()
