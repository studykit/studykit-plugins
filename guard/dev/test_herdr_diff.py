"""Git snapshot and terminal handoff regressions for the Herdr diff viewer."""

from contextlib import ExitStack
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "herdr"))
import guard_diff
import guard_herdr
import guard_settings


class DiffTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-diff-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.git("init", "-q")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args],
                              capture_output=True, check=True)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def commit(self):
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "-qm", "baseline")

    def test_head_to_worktree_includes_staged_and_unstaged_edits(self):
        path = self.write("file.py", b"original\n")
        self.commit()
        path.write_bytes(b"staged\n")
        self.git("add", ".")
        path.write_bytes(b"current\n")
        self.assertEqual(guard_diff.snapshots(self.root, path),
                         ("file.py", b"original\n", b"current\n"))

    def test_new_file_before_and_after_first_commit(self):
        path = self.write("new.txt", b"new\n")
        self.assertEqual(guard_diff.snapshots(self.root, path)[1:], (b"", b"new\n"))
        self.commit()
        other = self.write("untracked.txt", b"untracked\n")
        self.assertEqual(guard_diff.snapshots(self.root, other)[1:], (b"", b"untracked\n"))

    def test_deleted_file(self):
        path = self.write("removed.txt", b"removed\n")
        self.commit()
        path.unlink()
        self.assertEqual(guard_diff.snapshots(self.root, path)[1:], (b"removed\n", b""))

    def test_staged_rename_uses_original_head_blob(self):
        self.write("before.txt", b"original\n")
        self.commit()
        self.git("mv", "before.txt", "after.txt")
        self.assertEqual(guard_diff.snapshots(self.root, self.root / "after.txt")[1:],
                         (b"original\n", b"original\n"))

    def test_nested_project_and_literal_filename(self):
        path = self.write("nested/[file] name.txt", b"original\n")
        self.commit()
        path.write_bytes(b"current\n")
        self.assertEqual(guard_diff.snapshots(path.parent, path),
                         ("nested/[file] name.txt", b"original\n", b"current\n"))

    def test_non_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "outside a Git repository"):
                guard_diff.snapshots(Path(directory), Path(directory) / "file")

    def test_outside_path_and_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory) / "file"
            outside.write_text("outside")
            with self.assertRaisesRegex(ValueError, "inside the project"):
                guard_diff.snapshots(self.root, outside)
            link = self.root / "link"
            link.symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "inside the project"):
                guard_diff.snapshots(self.root, link)

    def test_fifo_and_directory_rejected_without_blocking(self):
        fifo = self.root / "fifo"
        os.mkfifo(fifo)
        for path in (fifo, self.root):
            with self.subTest(path=path), self.assertRaises((ValueError, IsADirectoryError)):
                guard_diff.snapshots(self.root, path)

    def test_binary_and_limits_on_both_sides(self):
        path = self.write("file", b"binary\0")
        with self.assertRaisesRegex(ValueError, "Binary"):
            guard_diff.snapshots(self.root, path)
        self.commit()
        path.write_bytes(b"text\n")
        with self.assertRaisesRegex(ValueError, "Binary"):
            guard_diff.snapshots(self.root, path)
        self.commit()
        with patch.object(guard_diff, "MAX_DIFF_BYTES", 4):
            with self.assertRaisesRegex(ValueError, "8 MiB"):
                guard_diff.snapshots(self.root, path)
            new = self.write("large", b"12345")
            with self.assertRaisesRegex(ValueError, "8 MiB"):
                guard_diff.snapshots(self.root, new)

    def test_snapshots_are_disposable_even_on_launch_failure(self):
        path = self.write("file name.py", b"original\n")
        self.commit()
        path.write_bytes(b"changed\n")
        with patch.object(guard_diff.shutil, "which", return_value="/usr/bin/vimdiff"):
            with self.assertRaisesRegex(OSError, "launch failed"):
                with guard_diff.comparison(self.root, path) as (command, cwd):
                    self.assertEqual((cwd / command[-2]).read_bytes(), b"original\n")
                    self.assertEqual((cwd / command[-1]).read_bytes(), b"changed\n")
                    (cwd / command[-1]).write_bytes(b"forced save\n")
                    raise OSError("launch failed")
        self.assertEqual(path.read_bytes(), b"changed\n")
        self.assertFalse(cwd.exists())

    def test_missing_vim_and_vim_fallback(self):
        path = self.write("file", b"new\n")
        with patch.object(guard_diff.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "Install Vim"):
                with guard_diff.comparison(self.root, path):
                    self.fail("Vim is unavailable")
        with patch.object(guard_diff.shutil, "which", side_effect=[None, "/usr/bin/vim"]):
            with guard_diff.comparison(self.root, path) as (command, _):
                self.assertEqual(command[0], "/usr/bin/vim")
                self.assertIn("-d", command)

    @unittest.skipUnless(shutil.which("vimdiff") or shutil.which("vim"), "Vim unavailable")
    def test_configured_tool_receives_snapshot_paths(self):
        path = self.write("dir/file name.py", b"before\n")
        self.commit()
        path.write_bytes(b"after\n")
        with patch.object(guard_diff.shutil, "which", return_value="/usr/bin/difft"):
            with guard_diff.comparison(self.root, path, "difft --title {name}") as (command, cwd):
                self.assertEqual(command[:3], ["difft", "--title", "dir/file name.py"])
                self.assertEqual(Path(command[3]).read_bytes(), b"before\n")
                self.assertEqual(Path(command[4]).read_bytes(), b"after\n")
            with guard_diff.comparison(self.root, path, "meld {after} {before}") as (command, _):
                self.assertEqual(Path(command[1]).read_bytes(), b"after\n")
                self.assertEqual(len(command), 3)
        with patch.object(guard_diff.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "not found on PATH"):
                with guard_diff.comparison(self.root, path, "missing-tool"):
                    self.fail("The tool is unavailable")

    @unittest.skipUnless(shutil.which("vimdiff") or shutil.which("vim"), "Vim unavailable")
    def test_real_vim_has_two_read_only_vertical_diff_windows(self):
        path = self.write("file.py", b"before\n")
        self.commit()
        path.write_bytes(b"after\n")
        with guard_diff.comparison(self.root, path) as (command, cwd):
            separator = command.index("--")
            command[separator:separator] = [
                "-es", "-c", "if winnr('$') != 2 || winlayout()[0] != 'row' | cquit 2 | endif",
                "-c", "windo if !&diff || !&readonly || &modifiable || &modeline | cquit 3 | endif",
                "-c", "if maparg('q', 'n') != ':qa!<CR>' | cquit 4 | endif",
                "-c", "qa!",
            ]
            result = subprocess.run(command, cwd=cwd, capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)


class PanelTests(unittest.TestCase):
    def test_diff_shortcuts_preserve_selection_without_checkpoint_mutation(self):
        for shortcut in ("d", "D", "\x04"):
            with self.subTest(shortcut=shortcut), ExitStack() as stack:
                screen = Mock()
                screen.getmaxyx.return_value = (30, 120)
                screen.get_wch.side_effect = [" ", "j", shortcut, "a", "q"]
                pane = {"cwd": "/project", "agent": "codex"}
                pending = {"files": {"/project/first": "1", "/project/second": "2"}}
                stack.enter_context(patch.object(guard_herdr, "_pending", return_value=(pane, pending)))
                settings = guard_settings.Settings()
                stack.enter_context(patch.object(guard_herdr, "_settings", return_value=settings))
                for name in ("curs_set", "use_default_colors", "init_pair", "color_pair"):
                    stack.enter_context(patch.object(guard_herdr.curses, name, return_value=0))
                diff = stack.enter_context(patch.object(guard_herdr, "_open_diff", return_value="Returned"))
                checkpoint = stack.enter_context(patch.object(
                    guard_herdr, "_checkpoint", return_value={"files": {"/project/first": "1"}, "token": "t"}))
                audit = stack.enter_context(patch.object(guard_herdr, "_prompt_audit", return_value=True))
                self.assertEqual(guard_herdr._panel(screen), 0)
                diff.assert_called_once_with(screen, Path("/project"), "/project/second", settings)
                checkpoint.assert_called_once_with(pane, "show", "--paths-json", '["/project/first"]')
                audit.assert_called_once_with(pane, "t")

    def test_terminal_restored_when_child_fails(self):
        with ExitStack() as stack:
            screen = Mock()
            for name in ("def_prog_mode", "endwin", "curs_set"):
                stack.enter_context(patch.object(guard_herdr.curses, name))
            restore = stack.enter_context(patch.object(guard_herdr.curses, "reset_prog_mode"))
            stack.enter_context(patch.object(guard_herdr.subprocess, "run", side_effect=OSError("unavailable")))
            with self.assertRaises(OSError):
                guard_herdr._run_terminal(screen, ["vimdiff"], Path("/tmp"))
            restore.assert_called_once()
            screen.keypad.assert_called_once_with(True)
            screen.refresh.assert_called_once()

    def test_configured_diff_pauses_and_tolerates_differences_status(self):
        settings = guard_settings.Settings(diff="difft", diff_pause=True)
        with patch.object(guard_herdr, "comparison") as comparison, \
                patch.object(guard_herdr, "_run_terminal", return_value=1) as run:
            comparison.return_value.__enter__.return_value = (["/usr/bin/difft", "a", "b"], Path("/tmp"))
            message = guard_herdr._open_diff(Mock(), Path("/tmp"), "/tmp/file", settings)
        comparison.assert_called_once_with(Path("/tmp"), Path("/tmp/file"), "difft")
        self.assertTrue(run.call_args.kwargs["pause"])
        self.assertEqual(message, "Returned from difft.")

    def test_editor_setting_overrides_environment(self):
        with patch.dict(guard_herdr.os.environ, {"VISUAL": "vim"}), \
                patch.object(guard_herdr.shutil, "which", return_value="/usr/bin/x"):
            self.assertEqual(guard_herdr._editor_command("/p/a b", "code --wait --goto {file}:{line}"),
                             ["code", "--wait", "--goto", "/p/a b:1"])
            self.assertEqual(guard_herdr._editor_command("/p/f", "hx"), ["hx", "/p/f"])
            self.assertEqual(guard_herdr._editor_command("/p/f"), ["vim", "/p/f"])
        with patch.object(guard_herdr.shutil, "which", return_value=None):
            self.assertEqual(guard_herdr._open_editor(Mock(), "/p/f", "missing"),
                             "Configured editor was not found on PATH")

    def test_keyboard_mode_reset_after_screen_restore(self):
        # Emacs's tty frames push a kitty keyboard mode and can exit without popping it.
        events = []
        screen = Mock()
        screen.refresh.side_effect = lambda: events.append("refresh")
        stdout = Mock()
        stdout.write.side_effect = lambda text: events.append(text)
        with ExitStack() as stack:
            for name in ("def_prog_mode", "endwin", "reset_prog_mode", "curs_set"):
                stack.enter_context(patch.object(guard_herdr.curses, name))
            stack.enter_context(patch.object(guard_herdr.subprocess, "run", return_value=Mock(returncode=0)))
            stack.enter_context(patch.object(guard_herdr.sys, "stdout", stdout))
            guard_herdr._run_terminal(screen, ["emacsclient"], Path("/tmp"))
        self.assertEqual(events, ["refresh", guard_herdr.KEYBOARD_RESET])

    def test_diff_preparation_error_remains_in_panel(self):
        with patch.object(guard_herdr, "comparison", side_effect=ValueError("Binary file")), \
                patch.object(guard_herdr, "_run_terminal") as run:
            self.assertEqual(guard_herdr._open_diff(Mock(), Path("/tmp"), "/tmp/file"), "Binary file")
            run.assert_not_called()


class SettingsTests(unittest.TestCase):
    def test_location_and_partial_errors(self):
        self.assertEqual(guard_settings.location({"GUARD_HERDR_CONFIG": "/x/g.toml"}), Path("/x/g.toml"))
        self.assertEqual(guard_settings.location({"XDG_CONFIG_HOME": "/cfg"}), Path("/cfg/guard/herdr.toml"))
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "herdr.toml"
            self.assertEqual(guard_settings.load(file), guard_settings.Settings())
            file.write_text('[editor]\ncommand = " hx "\n[diff]\ncommand = 3\npause = true\n')
            settings = guard_settings.load(file)
            self.assertEqual((settings.editor, settings.diff, settings.diff_pause), ("hx", "", True))
            self.assertEqual(settings.errors, ["herdr.toml: diff.command must be a string"])
            file.write_text("[editor")
            self.assertEqual(len(guard_settings.load(file).errors), 1)


if __name__ == "__main__":
    unittest.main()
