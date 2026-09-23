import base64
from pathlib import Path
import struct
import sys
import tempfile
import time
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import plantuml_preview as puml
from ui import Navigator


def png(width, height, body=b""):
    header = struct.pack(">II", width, height) + b"\x08\x06\x00\x00\x00"
    return puml.PNG_SIGNATURE + b"\x00\x00\x00\x0dIHDR" + header + b"crc0" + body + b"\x00\x00\x00\x00IEND\xaeB`\x82"


class PlantUMLTests(unittest.TestCase):
    def test_supported_suffixes(self):
        for name in ("a.puml", "dir/B.PlantUML", "c.pu", "d.iuml", "e.wsd"):
            self.assertTrue(puml.supported(name))
        for name in ("a.md", "puml", "a.puml.txt"):
            self.assertFalse(puml.supported(name))

    def test_command_prefers_path_then_jar(self):
        with tempfile.NamedTemporaryFile(suffix=".jar") as jar:
            with patch("shutil.which", side_effect=lambda name: "/bin/" + name):
                self.assertEqual(puml.command({"PLANTUML_JAR": jar.name}), ["plantuml"])
            with patch("shutil.which", side_effect=lambda name: "/bin/java" if name == "java" else None):
                self.assertEqual(puml.command({"PLANTUML_JAR": jar.name})[-2:], ["-jar", jar.name])
                self.assertIsNone(puml.command({"PLANTUML_JAR": jar.name + ".missing"}))
                self.assertIsNone(puml.command({}))

    def test_render_pipes_source_and_keeps_first_image(self):
        first, second = png(10, 20), png(30, 40)
        script = ("import sys; data = sys.stdin.buffer.read(); assert b'@startuml' in data; "
                  f"sys.stdout.buffer.write({first + second!r})")
        with tempfile.TemporaryDirectory() as cwd:
            self.assertEqual(puml.render("@startuml\n@enduml\n", Path(cwd), [sys.executable, "-c", script]), first)

    def test_render_reports_last_stderr_line_without_image(self):
        script = "import sys; sys.stderr.write('warning\\nsyntax error at line 2\\n'); sys.exit(1)"
        with tempfile.TemporaryDirectory() as cwd:
            with self.assertRaisesRegex(RuntimeError, "syntax error at line 2"):
                puml.render("x", Path(cwd), [sys.executable, "-c", script])

    def test_image_size_and_fit_keep_aspect_ratio(self):
        self.assertEqual(puml.image_size(png(800, 600)), (800, 600))
        with self.assertRaises(ValueError):
            puml.image_size(b"GIF89a")
        # 800x600 into 100 cols x 20 rows of 10x20 px cells is height-bound.
        self.assertEqual(puml.fit((800, 600), 100, 20, (10, 20)), (53, 20))
        # Tiny images grow at most MAX_UPSCALE times.
        self.assertEqual(puml.fit((100, 40), 100, 50, (10, 20)), (20, 4))
        self.assertEqual(puml.fit((1, 10000), 5, 5, (10, 20)), (1, 5))

    def test_transmit_chunks_base64_payload(self):
        data = puml.transmit(7, b"x" * 10000)
        chunks = data.split(b"\x1b\\")[:-1]
        self.assertTrue(chunks[0].startswith(b"\x1b_Ga=t,f=100,i=7,q=2,m=1;"))
        self.assertTrue(chunks[-1].startswith(b"\x1b_Gm=0;"))
        payload = b"".join(chunk.split(b";", 1)[1] for chunk in chunks)
        self.assertEqual(base64.standard_b64decode(payload), b"x" * 10000)
        self.assertTrue(all(len(chunk.split(b";", 1)[1]) <= puml.CHUNK for chunk in chunks))

    def test_place_restores_cursor_and_crops(self):
        self.assertEqual(puml.place(3, 1, 6, 9, 20, 10),
                         b"\x1b7\x1b[7;10H\x1b_Ga=p,i=3,p=1,c=20,r=10,C=1,q=2\x1b\\\x1b8")
        self.assertIn(b"a=p,i=3,p=2,x=0,y=40,w=200,h=60,c=20,r=3,", puml.place(3, 2, 0, 0, 20, 3, (0, 40, 200, 60)))
        self.assertEqual(puml.hide(3), b"\x1b_Ga=d,d=i,i=3,q=2\x1b\\")
        self.assertEqual(puml.hide(3, 2), b"\x1b_Ga=d,d=i,i=3,p=2,q=2\x1b\\")


class NavigatorDiagramTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "flow.puml").write_text("@startuml\nA -> B\n@enduml\n")
        (self.root / "code.py").write_text("x = 1\n")
        self.writes = []
        self.image = png(200, 100)
        render = patch("plantuml_preview.render", return_value=self.image)
        self.render = render.start()
        self.addCleanup(render.stop)
        self.nav = Navigator(self.root, "pane", False, "", plantuml=["plantuml"],
                             graphics=self.writes.append, cell_size=lambda: (10, 20))

    def rendered(self, name="docs/flow.puml"):
        self.nav.load(name)
        deadline = time.monotonic() + 5
        while self.nav.diagram_job is not None and time.monotonic() < deadline:
            self.nav.diagram_job[1].exception(timeout=5)
            self.nav.poll_diagram()

    def draw(self):
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        with patch.object(self.nav, "span_style", return_value=0):
            self.nav.draw(screen)
        self.nav.sync_image()
        return screen

    def test_renders_in_file_directory_and_places_image(self):
        self.rendered()
        self.render.assert_called_once_with("@startuml\nA -> B\n@enduml\n", self.root / "docs", ["plantuml"])
        self.draw()
        data = b"".join(self.writes)
        self.assertIn(b"a=t,f=100,i=1", data)
        self.assertIn(b"a=p,i=1,p=1", data)
        self.writes.clear()
        self.draw()
        self.assertEqual(self.writes, [])  # Unchanged frames send nothing.

    def test_toggle_source_hides_and_reuses_transmitted_image(self):
        self.rendered()
        self.draw()
        self.writes.clear()
        self.assertTrue(self.nav.preview_key("v"))
        self.draw()
        self.assertEqual(self.writes, [puml.hide(1, 1)])
        self.writes.clear()
        self.nav.preview_key("v")
        self.draw()
        self.assertNotIn(b"a=t", b"".join(self.writes))
        self.assertIn(b"a=p,i=1", b"".join(self.writes))

    def test_dialogs_and_other_files_hide_image(self):
        self.rendered()
        self.draw()
        self.writes.clear()
        self.nav.layout_dialog = True
        self.draw()
        self.assertEqual(self.writes, [puml.hide(1, 1)])
        self.nav.layout_dialog = False
        self.nav.load("code.py")
        self.writes.clear()
        self.draw()
        self.assertEqual(self.writes, [puml.delete(1)])  # Leaving the file frees its image.
        self.assertFalse(self.nav.preview_key("v"))

    def test_edited_source_rerenders_and_frees_old_image(self):
        self.rendered()
        self.draw()
        self.nav.refresh()
        self.assertIsNone(self.nav.diagram_job)  # Unchanged source keeps its image.
        (self.root / "docs" / "flow.puml").write_text("@startuml\nB -> A\n@enduml\n")
        self.writes.clear()
        self.rendered()
        self.draw()
        data = b"".join(self.writes)
        self.assertIn(puml.delete(1), data)
        self.assertIn(b"a=t,f=100,i=2", data)

    def test_render_failure_is_shown_and_release_frees_image(self):
        self.render.side_effect = RuntimeError("boom")
        self.rendered()
        screen = self.draw()
        self.assertIn("Could not render PlantUML: boom",
                      [call.args[2] for call in screen.addstr.call_args_list])
        self.assertEqual(self.writes, [])
        self.render.side_effect = None
        (self.root / "docs" / "flow.puml").write_text("@startuml\nC -> D\n@enduml\n")
        self.rendered()
        self.draw()
        self.writes.clear()
        self.nav.release_image()
        self.assertEqual(self.writes, [puml.delete(1)])

    def test_without_graphics_puml_uses_source_preview(self):
        nav = Navigator(self.root, "pane", False, "", plantuml=["plantuml"])
        nav.load("docs/flow.puml")
        self.assertIsNone(nav.diagram_job)
        self.assertFalse(nav.diagram_view())
        self.render.assert_not_called()


class MarkdownDiagramTests(unittest.TestCase):
    TEXT = ("# Title\n\n```plantuml\nA -> B\n```\n\n" + "filler\n\n" * 30
            + "```puml\n@startuml\nC -> D\n@enduml\n```\n\n````md\n```plantuml\nX\n```\n````\n")

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "notes.md").write_text(self.TEXT)
        self.writes = []
        render = patch("plantuml_preview.render", return_value=png(200, 100))
        self.render = render.start()
        self.addCleanup(render.stop)
        self.nav = Navigator(self.root, "pane", False, "", plantuml=["plantuml"],
                             graphics=self.writes.append, cell_size=lambda: (10, 20))

    def settle(self):
        while self.nav.diagram_job is not None:
            self.nav.diagram_job[1].exception(timeout=5)
            self.nav.poll_diagram()

    def draw(self):
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        with patch.object(self.nav, "span_style", return_value=0):
            self.nav.draw(screen)
        self.nav.sync_image()

    def test_blocks_ignore_fences_nested_in_other_code(self):
        from markdown_preview import plantuml_blocks
        self.assertEqual(plantuml_blocks(self.TEXT), ["A -> B\n", "@startuml\nC -> D\n@enduml\n"])

    def test_render_replaces_fences_with_blank_rows(self):
        from markdown_preview import render_diagrams
        lines, placements = render_diagrams(self.TEXT, 60, None, {"A -> B\n": 4})
        (line, source, rows), = placements
        self.assertEqual((source, rows), ("A -> B\n", 4))
        self.assertEqual(lines[line:line + 4], [[], [], [], []])
        text = ["".join(span.text for span in row) for row in lines]
        self.assertFalse(any("LD" in row for row in text))
        self.assertTrue(any("C -> D" in row for row in text))  # Not yet rendered: stays code.

    def test_renders_each_block_and_wraps_bare_sources(self):
        self.nav.load("notes.md")
        self.settle()
        sources = [call.args[0] for call in self.render.call_args_list]
        self.assertEqual(sources, ["@startuml\nA -> B\n@enduml\n", "@startuml\nC -> D\n@enduml\n"])
        self.nav.preview_focus = True
        self.draw()
        data = b"".join(self.writes)
        self.assertIn(b"a=t,f=100,i=1", data)
        self.assertIn(b"a=p,i=1,p=1", data)
        self.assertNotIn(b"a=p,i=2", data)  # The second diagram is below the fold.

    def test_scrolling_crops_then_hides_images(self):
        self.nav.load("notes.md")
        self.settle()
        self.nav.preview_focus = True
        self.draw()
        line, _, (cols, rows) = self.nav.markdown_diagrams[0]
        self.writes.clear()
        self.nav.preview_scroll = line + 1
        self.draw()
        data = b"".join(self.writes)
        self.assertIn(f"a=p,i=1,p=1,x=0,y={round(100 / rows)},".encode(), data)
        self.assertIn(f"r={rows - 1},".encode(), data)
        self.writes.clear()
        self.nav.preview_scroll = line + rows
        self.draw()
        self.assertIn(puml.hide(1, 1), b"".join(self.writes))

    def test_toggle_shows_source_blocks(self):
        self.nav.load("notes.md")
        self.settle()
        self.nav.preview_focus = True
        self.draw()
        self.writes.clear()
        self.assertTrue(self.nav.preview_key("v"))
        self.draw()
        self.assertEqual(self.nav.markdown_diagrams, [])
        self.assertTrue(any("A -> B" in line for line in self.nav.content))
        self.assertIn(puml.hide(1, 1), b"".join(self.writes))

    def test_render_errors_keep_code_block_and_report(self):
        self.render.side_effect = RuntimeError("bad")
        self.nav.load("notes.md")
        self.settle()
        self.draw()
        self.assertEqual(self.nav.message, "Could not render PlantUML: bad")
        self.assertEqual(self.nav.markdown_diagrams, [])
        self.assertTrue(any("A -> B" in line for line in self.nav.content))


if __name__ == "__main__":
    unittest.main()
