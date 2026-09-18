import curses
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core
import herdr_main
from diff_tool import comparison, snapshots
from ui import Navigator, clean


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def init(self):
        self.git("init", "-q")
        self.git("config", "user.name", "Navigator Test")
        self.git("config", "user.email", "navigator@example.invalid")

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def test_git_ignored_hidden_and_deleted_files(self):
        self.init()
        self.write(".gitignore", "ignored/\n")
        self.write("gone.txt", "before\n")
        self.commit()
        (self.root / "gone.txt").unlink()
        self.write("ignored/cache.txt", "hidden")
        self.write("new.txt", "new")
        self.write(".settings", "visible")
        index = core.scan(self.root)
        self.assertIn("gone.txt", index.files)
        self.assertIn("D", index.status["gone.txt"])
        self.assertIn(".settings", index.files)
        self.assertNotIn("ignored/cache.txt", index.files)
        self.assertNotIn(".git/HEAD", index.files)
        self.assertEqual(index.status["new.txt"], "??")
        self.assertEqual(snapshots(index, "gone.txt"), (b"before\n", b""))

    def test_nested_root_stays_inside_source_pane(self):
        self.init()
        self.write("outside.txt", "outside")
        self.write("nested/inside.txt", "before\n")
        self.commit()
        self.write("nested/inside.txt", "after\n")
        index = core.scan(self.root / "nested")
        self.assertEqual(index.files, ["inside.txt"])
        self.assertEqual(index.status, {"inside.txt": " M"})
        self.assertEqual(snapshots(index, "inside.txt"), (b"before\n", b"after\n"))

    def test_staged_and_unstaged_combined(self):
        self.init()
        self.write("file.txt", "original\n")
        self.commit()
        self.write("file.txt", "staged\n")
        self.git("add", "file.txt")
        self.write("file.txt", "unstaged\n")
        self.assertEqual(snapshots(core.scan(self.root), "file.txt"), (b"original\n", b"unstaged\n"))

    def test_untracked_and_unborn_repository(self):
        self.init()
        self.write("new.txt", "new content\n")
        self.assertEqual(snapshots(core.scan(self.root), "new.txt"), (b"", b"new content\n"))
        self.git("add", ".")
        self.assertEqual(snapshots(core.scan(self.root), "new.txt"), (b"", b"new content\n"))

    def test_literal_pathspec_and_unusual_names(self):
        self.init()
        for name in ("[abc].txt", "a.txt", "space name.txt", "line\nbreak.txt", "한글.txt"):
            self.write(name, "before\n")
        self.commit()
        self.write("[abc].txt", "literal\n")
        self.write("a.txt", "must not match\n")
        index = core.scan(self.root)
        self.assertIn("line\nbreak.txt", index.files)
        self.assertEqual(snapshots(index, "[abc].txt"), (b"before\n", b"literal\n"))

    def test_staged_rename(self):
        self.init()
        self.write("old name", "content\n")
        self.commit()
        self.git("mv", "old name", "new name")
        index = core.scan(self.root)
        self.assertIn("R", index.status["new name"])
        self.assertNotIn("old name", index.files)
        self.assertEqual(snapshots(index, "new name"), (b"content\n", b"content\n"))

    def test_non_git_and_symlinks(self):
        self.write("src/file.txt", "hello\n")
        self.write("node_modules/dep.txt", "skip")
        (self.root / "loop").symlink_to(self.root, target_is_directory=True)
        (self.root / "outside").symlink_to(self.root.parent, target_is_directory=True)
        index = core.scan(self.root)
        self.assertEqual(index.files, ["src/file.txt"])
        self.assertEqual(core.preview(index, "src/file.txt"), "hello\n")
        with self.assertRaisesRegex(ValueError, "unavailable"):
            snapshots(index, "src/file.txt")
        with self.assertRaises(ValueError):
            core.checked_path(self.root, "../escape")
        with self.assertRaises(ValueError):
            core.checked_path(self.root, "outside/escape")

    def test_large_binary_and_special_files(self):
        self.write("large.txt", "a" * (core.PREVIEW_BYTES + 1))
        self.write("binary", "a\0b")
        os.mkfifo(self.root / "pipe")
        index = core.scan(self.root)
        self.assertIn("truncated", core.preview(index, "large.txt"))
        with self.assertRaisesRegex(ValueError, "Binary"):
            core.preview(index, "binary")
        with self.assertRaisesRegex(ValueError, "regular"):
            core.preview(index, "pipe")

    def test_ui_search_enter_diff_clear_and_changes(self):
        self.init()
        self.write("nested/README.md", "known preview\n")
        nav = Navigator(self.root, "source-pane", False, "")
        self.assertTrue(nav.items[0].directory)
        nav.key("/", None)
        for char in "rdm":
            nav.key(char, None)
        self.assertEqual(nav.items[0].path, "nested/README.md")
        nav.narrow = False
        nav.key("\n", None)
        nav.key("\n", None)
        self.assertEqual(nav.content, ["known preview"])
        self.assertTrue(nav.preview_focus)
        with patch.object(nav, "show_diff") as show:
            nav.key("\x04", None)
            show.assert_called_once_with(None)
        nav.key("/", None)
        nav.key("\x15", None)
        nav.key("\n", None)
        self.assertEqual(nav.query, "")
        nav.key("\x07", None)
        self.assertTrue(nav.changes)
        self.assertFalse(nav.key("\x1b", None))

    def test_mouse_opens_file_and_wheel_scrolls_preview(self):
        self.write("click.txt", "click opened\n")
        nav = Navigator(self.root, "source-pane", False, "")
        nav.narrow, nav.divider, nav.body = False, 30, 10
        with patch("curses.getmouse", return_value=(0, 5, 9, 0, curses.BUTTON1_CLICKED)):
            nav.mouse()
        self.assertEqual(nav.active, "click.txt")
        self.assertEqual(nav.content, ["click opened"])
        nav.content = [str(i) for i in range(50)]
        nav.preview_scroll = 10
        with patch("curses.getmouse", return_value=(0, 40, 4, 0, curses.BUTTON4_PRESSED)):
            nav.mouse()
        self.assertEqual(nav.preview_scroll, 7)

    def test_vimdiff_uses_disposable_snapshots_and_cleans_up(self):
        self.init()
        self.write("file name.py", "original\n")
        self.commit()
        self.write("file name.py", "changed\n")
        with patch("diff_tool.shutil.which", return_value="/usr/bin/vimdiff"):
            with comparison(core.scan(self.root), "file name.py") as (command, cwd):
                self.assertIn("-R", command)
                self.assertIn("-O", command)
                self.assertEqual((cwd / command[-2]).read_bytes(), b"original\n")
                self.assertEqual((cwd / command[-1]).read_bytes(), b"changed\n")
                (cwd / command[-1]).write_text("changed snapshot")
                self.assertEqual((self.root / "file name.py").read_text(), "changed\n")
            self.assertFalse(cwd.exists())

    def test_diff_size_limit_and_binary(self):
        self.init()
        self.write("file", "0123456789")
        with patch("diff_tool.MAX_DIFF_BYTES", 5):
            with self.assertRaisesRegex(ValueError, "8 MiB"):
                snapshots(core.scan(self.root), "file")
        self.write("file", "binary\0")
        with self.assertRaisesRegex(ValueError, "Binary"):
            snapshots(core.scan(self.root), "file")

    @unittest.skipUnless(shutil.which("vimdiff") or shutil.which("vim"), "Vim is not installed")
    def test_vim_configuration_opens_two_read_only_diff_windows(self):
        self.init()
        self.write("file.py", "before\n")
        self.commit()
        self.write("file.py", "after\n")
        with comparison(core.scan(self.root), "file.py") as (command, cwd):
            separator = command.index("--")
            command[separator:separator] = [
                "-es", "-c", "if winnr('$') != 2 || winlayout()[0] != 'row' | cquit 2 | endif",
                "-c", "windo if !&diff || !&readonly || &modifiable | cquit 3 | endif",
                "-c", "qa!",
            ]
            result = subprocess.run(command, cwd=cwd, capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_changes_enter_opens_vimdiff_and_tab_changes_focus(self):
        self.init()
        self.write("file.txt", "new\n")
        nav = Navigator(self.root, "pane", True, "")
        nav.selected = next(i for i, row in enumerate(nav.items) if row.path == "file.txt")
        with patch.object(nav, "show_diff") as show:
            nav.key("\n", None)
            show.assert_called_once_with(None)
        self.assertTrue(nav.preview_focus)
        nav.key("\t", None)
        self.assertFalse(nav.preview_focus)
        nav.key(curses.KEY_BTAB, None)
        self.assertTrue(nav.preview_focus)
        self.assertTrue(nav.key("\x1b", None))
        self.assertFalse(nav.preview_focus)

    def test_content_focus_uses_displayed_file_not_tree_selection(self):
        self.write("a", "a")
        self.write("b", "b")
        nav = Navigator(self.root, "pane", False, "")
        nav.selected = next(i for i, row in enumerate(nav.items) if row.path == "a")
        nav.activate()
        nav.selected = next(i for i, row in enumerate(nav.items) if row.path == "b")
        self.assertEqual(nav.current_file(), "a")
        nav.key("\t", None)
        self.assertEqual(nav.current_file(), "b")

    def test_mouse_release_does_not_steal_content_focus(self):
        self.write("a", "a")
        nav = Navigator(self.root, "pane", False, "")
        nav.divider = 30
        nav.preview_focus = True
        with patch("curses.getmouse", return_value=(0, 5, 8, 0, curses.BUTTON1_RELEASED)):
            nav.mouse()
        self.assertTrue(nav.preview_focus)


class PureTests(unittest.TestCase):
    def test_search_ranking_and_fuzzy(self):
        files = ["readme/other.txt", "README.md", "src/my-readme.md", "src/readme.md"]
        self.assertEqual(core.search(files, "README.md")[0], "README.md")
        self.assertEqual(core.search(files, "rdm")[0], "README.md")
        self.assertEqual(core.search(files, "src/rdm"), ["src/readme.md", "src/my-readme.md"])

    def test_tree_and_collapsed_search(self):
        files = ["src/deep/file.py", "README.md"]
        tree = core.rows(files, set())
        self.assertEqual([(row.path, row.directory) for row in tree], [("src", True), ("README.md", False)])
        self.assertEqual(core.rows(files, set(), "file")[0].path, "src/deep/file.py")
        self.assertEqual(core.rows(files, {"src", "src/deep"})[2].depth, 2)

    def test_porcelain_rename_and_newline(self):
        self.assertEqual(core.parse_status(b"R  new name\0old name\0?? line\nbreak\0"),
                         {"new name": "R ", "line\nbreak": "??"})

    def test_editor_argv_does_not_invoke_shell(self):
        with patch("core.shutil.which", return_value="/bin/editor"):
            command = core.editor_command('editor --wait "an argument"', Path("/tmp/$(touch nope).txt"))
        self.assertEqual(command, ["editor", "--wait", "an argument", "/tmp/$(touch nope).txt"])

    def test_control_sequences_are_not_rendered(self):
        self.assertNotIn("\x1b", clean("\x1b[31muntrusted\ttext"))


class AdapterTests(unittest.TestCase):
    def test_manifest_entrypoint_runs_from_project_directory(self):
        plugin = Path(__file__).resolve().parents[1]
        manifest = tomllib.loads((plugin / "herdr-plugin.toml").read_text())
        command = manifest["panes"][0]["command"]
        with tempfile.TemporaryDirectory() as directory:
            env = dict(os.environ)
            env.pop("HERDR_ENV", None)
            result = subprocess.run([str(plugin / command[0]), *command[1:]],
                                    cwd=directory, env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Run File Navigator from inside Herdr", result.stderr)

    def test_context_precedes_caller_and_uses_foreground_cwd(self):
        with tempfile.TemporaryDirectory() as directory:
            env = {"HERDR_PLUGIN_CONTEXT_JSON": json.dumps({"focused_pane_id": "focused"}), "HERDR_PANE_ID": "caller"}
            with patch("herdr_main.call", return_value={"pane": {"foreground_cwd": directory, "cwd": "/"}}) as call:
                pane, root = herdr_main.source(env, "herdr-binary")
            self.assertEqual(pane, "focused")
            self.assertEqual(root, Path(directory).resolve())
            call.assert_called_once_with("herdr-binary", "pane", "get", "focused")

    def test_action_defaults_to_popup_and_forwards_source(self):
        env = {"HERDR_ENV": "1", "HERDR_PLUGIN_ID": "studykit.file-nav"}
        with patch("herdr_main.source", return_value=("w1:p9", Path("/tmp/project"))), patch("herdr_main.call") as call:
            herdr_main.main(env, "changes")
        argv = call.call_args.args
        self.assertIn("FILE_NAV_SOURCE_PANE=w1:p9", argv)
        self.assertIn("FILE_NAV_CHANGES=1", argv)
        self.assertEqual(argv[argv.index("--entrypoint") + 1], "popup")
        self.assertNotIn("--placement", argv)
        self.assertNotIn("--target-pane", argv)
        self.assertIn("--width", argv)
        self.assertIn("--height", argv)

    def test_missing_or_invalid_context_does_not_browse_plugin_directory(self):
        for env in ({}, {"HERDR_PLUGIN_CONTEXT_JSON": "[]"}, {"HERDR_PLUGIN_CONTEXT_JSON": "bad"}):
            with self.assertRaises(ValueError):
                herdr_main.source(env, "herdr")

    def test_requires_herdr(self):
        with self.assertRaisesRegex(ValueError, "inside Herdr"):
            herdr_main.main({}, "browse")


if __name__ == "__main__":
    unittest.main()
