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
        self.assertEqual(settings.chord("ctrl+;"), "ctrl+;")
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
        self.config = self.base / "config" / "lens" / "config.toml"
        self.root = self.base / "project"
        self.root.mkdir()
        (self.root / "code.py").write_text("\n".join(f"x = {i}" for i in range(50)))

    def write(self, text):
        self.config.parent.mkdir(parents=True, exist_ok=True)
        self.config.write_text(text)

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

    def test_tree_padding_is_one_by_default_and_bounded(self):
        self.assertEqual(self.navigator().tree_padding, 1)
        self.write("[ui]\ntree_padding = 3\n")
        self.assertEqual(self.navigator().tree_padding, 3)
        for bad in ("-1", "9", "true", '"2"'):
            self.write(f"[ui]\ntree_padding = {bad}\n")
            nav = self.navigator()
            self.assertEqual(nav.tree_padding, 1)
            self.assertIn("ui.tree_padding", nav.message)

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

    def test_when_bindings_override_global_only_in_the_matching_state(self):
        self.write('''[keys]
"g" = ":icons nerd"
[[keybindings]]
key = "g"
command = ":icons plain"
when = "tree && !history"
[[keybindings]]
key = "g"
command = "top"
when = "preview && file"
''')
        nav = self.navigator()
        self.assertEqual(len(nav.binding_rules), 2)
        self.assertIn(("g", ":icons plain"), nav.key_groups()[-1][1])
        nav.key("g", None)
        self.assertEqual(nav.icons, "plain")
        nav.load("code.py")
        nav.preview_focus = True
        nav.body = 10
        nav.preview_scroll = 20
        self.assertIn(("g", "top"), nav.key_groups()[-1][1])
        nav.key("g", None)
        self.assertEqual(nav.preview_scroll, 0)
        self.assertEqual(nav.icons, "plain")

    def test_when_rule_can_disable_a_key_only_in_one_state(self):
        self.write('''[[keybindings]]
key = "g"
command = "none"
when = "preview"
''')
        nav = self.navigator()
        nav.load("code.py")
        nav.preview_focus = True
        nav.body = 10
        nav.preview_scroll = 20
        nav.key("g", None)
        self.assertEqual(nav.preview_scroll, 20)
        self.assertFalse(any("g" in key.split() for _, rows in nav.key_groups() for key, _ in rows))

    def test_when_expression_parsing_and_invalid_rules(self):
        expression = settings.parse_when("tree && (git || !file)")
        self.assertTrue(settings.when_matches(expression, {"tree", "git"}))
        self.assertFalse(settings.when_matches(expression, {"tree", "file"}))
        for source in ("tree &&", "(git", "tree + git", "mystery"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                settings.parse_when(source)
        self.write('''[[keybindings]]
key = "ctrl+q"
command = ":git.history"
when = "mystery"
''')
        nav = self.navigator()
        self.assertEqual(nav.binding_rules, [])
        self.assertIn("unknown when context", nav.message)

    def test_config_command_creates_template_and_reloads(self):
        nav = self.navigator()
        def fake_editor(screen, command, cwd):
            Path(command[-1]).write_text('[ui]\nicons = "nerd"\n')
            return type("Result", (), {"returncode": 0})()
        with patch("ui.editor_command", side_effect=lambda editor, path, line=1: [editor, str(path)]), \
                patch.object(nav, "run_terminal", side_effect=fake_editor) as run:
            nav.run_command("config", None)
        self.assertEqual(run.call_args.args[1], ["env-editor", str(self.config)])
        self.assertEqual((nav.icons, nav.message), ("nerd", "Settings reloaded"))

    def test_location_follows_xdg_and_override(self):
        self.assertEqual(settings.location({"XDG_CONFIG_HOME": "/x"}), Path("/x/lens/config.toml"))
        self.assertEqual(settings.location({"LENS_CONFIG": "/y/lens.toml", "XDG_CONFIG_HOME": "/x"}),
                         Path("/y/lens.toml"))
        self.assertEqual(settings.location({}), Path.home() / ".config" / "lens" / "config.toml")

    def test_template_is_valid_and_fully_commented(self):
        settings.ensure(self.config)
        loaded = settings.load(self.config)
        self.assertEqual((loaded.editor, loaded.icons, loaded.keys, loaded.errors), ("", None, {}, []))


class DiffCommandTests(unittest.TestCase):
    def test_placeholders_and_appended_paths(self):
        import diff_tool
        before, after = Path("/t/HEAD/a b.py"), Path("/t/WORKTREE/a b.py")
        with patch("diff_tool.shutil.which", return_value="/bin/tool"):
            self.assertEqual(diff_tool.configured_command("difft", before, after, "a b.py"),
                             ["difft", "/t/HEAD/a b.py", "/t/WORKTREE/a b.py"])
            self.assertEqual(diff_tool.configured_command(
                "emacsclient --eval '(ediff-files \"{before}\" \"{after}\")'", before, after, "a b.py"),
                ["emacsclient", "--eval", '(ediff-files "/t/HEAD/a b.py" "/t/WORKTREE/a b.py")'])
        with patch("diff_tool.shutil.which", return_value=None):
            with self.assertRaises(ValueError):
                diff_tool.configured_command("missing-tool", before, after, "a b.py")

    def test_settings_and_template_parse(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "config.toml"
            file.write_text(settings.TEMPLATE.replace("# command = \"difft", "command = \"difft")
                            .replace("# pause = true", "pause = true"))
            loaded = settings.load(file)
        self.assertEqual((loaded.diff, loaded.diff_pause, loaded.errors), ("difft {before} {after}", True, []))


class EditorCommandTests(unittest.TestCase):
    def test_placeholders_stay_single_arguments(self):
        path = Path("/tmp/a b; rm.txt")
        with patch("core.shutil.which", return_value="/bin/editor"):
            self.assertEqual(core.editor_command("code --goto {file}:{line}", path, 12),
                             ["code", "--goto", "/tmp/a b; rm.txt:12"])
            self.assertEqual(core.editor_command("nvim +{line}", path, 3), ["nvim", "+3", "/tmp/a b; rm.txt"])
            self.assertEqual(core.editor_command("nvim +{line}", path, None), ["nvim", "/tmp/a b; rm.txt"])
            self.assertEqual(core.editor_command("code --goto {file}:{line}", path, None),
                             ["code", "--goto", "/tmp/a b; rm.txt"])
            self.assertEqual(core.editor_command("vim", path, 3), ["vim", "/tmp/a b; rm.txt"])


if __name__ == "__main__":
    unittest.main()
