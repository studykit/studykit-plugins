import base64
from pathlib import Path
import struct
import sys
import tempfile
import time
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import diagram_preview as puml
from ui import Navigator


def png(width, height, body=b""):
    header = struct.pack(">II", width, height) + b"\x08\x06\x00\x00\x00"
    return puml.PNG_SIGNATURE + b"\x00\x00\x00\x0dIHDR" + header + b"crc0" + body + b"\x00\x00\x00\x00IEND\xaeB`\x82"


class RendererTests(unittest.TestCase):
    def test_file_and_fence_languages(self):
        files = {"a.puml": "plantuml", "dir/B.PlantUML": "plantuml", "c.wsd": "plantuml", "flow.mmd": "mermaid",
                 "net.d2": "d2", "deps.dot": "graphviz", "g.gv": "graphviz", "p.pikchr": "pikchr",
                 "art.bob": "svgbob", "chart.vl.json": "vega-lite", "docs/workspace.dsl": "structurizr"}
        for name, language in files.items():
            self.assertEqual(puml.file_language(name), language, name)
        for name in ("a.md", "puml", "a.puml.txt", "data.json", "other.dsl"):
            self.assertIsNone(puml.file_language(name), name)
        fences = {"plantuml": "plantuml", "PUML": "plantuml", "mermaid {theme}": "mermaid", "dot": "graphviz",
                  "bob": "svgbob", "vegalite": "vega-lite", "wavedrom": "wavedrom", "structurizr": "structurizr"}
        for info, language in fences.items():
            self.assertEqual(puml.fence_language(info), language, info)
        self.assertIsNone(puml.fence_language("python"))
        self.assertIsNone(puml.fence_language(""))

    def test_tools_and_available_languages(self):
        with tempfile.NamedTemporaryFile(suffix=".jar") as jar:
            with patch("shutil.which", side_effect=lambda name: "/bin/" + name):
                found = puml.tools({"PLANTUML_JAR": jar.name})
                self.assertEqual(found["plantuml"], ["/bin/plantuml"])
                self.assertEqual(puml.available(found), set(puml.LANGUAGES))
            with patch("shutil.which", side_effect=lambda name: "/bin/" + name if name in ("java", "d2") else None):
                found = puml.tools({"PLANTUML_JAR": jar.name})
                self.assertEqual(found["plantuml"][-2:], ["-jar", jar.name])
                # d2 also needs rsvg-convert to turn its SVG into PNG.
                self.assertEqual(puml.available(found), {"plantuml"})
                self.assertNotIn("plantuml", puml.tools({"PLANTUML_JAR": jar.name + ".missing"}))

    def test_plantuml_pipes_wrapped_source_and_keeps_first_image(self):
        first, second = png(10, 20), png(30, 40)
        script = ("import sys; data = sys.stdin.buffer.read(); assert data.startswith(b'@startuml\\nA'); "
                  f"sys.stdout.buffer.write({first + second!r})")
        with tempfile.TemporaryDirectory() as cwd:
            found = {"plantuml": [sys.executable, "-c", script]}
            self.assertEqual(puml.render("plantuml", "A -> B\n", Path(cwd), found), first)

    def test_plantuml_reports_last_stderr_line_without_image(self):
        script = "import sys; sys.stderr.write('warning\\nsyntax error at line 2\\n'); sys.exit(1)"
        with tempfile.TemporaryDirectory() as cwd:
            with self.assertRaisesRegex(RuntimeError, "syntax error at line 2"):
                puml.render("plantuml", "x", Path(cwd), {"plantuml": [sys.executable, "-c", script]})

    def test_svg_tools_are_flattened_through_rsvg(self):
        svg = "import sys; sys.stdin.read(); sys.stdout.write('<svg/>')"
        rsvg = (f"import sys; assert sys.stdin.buffer.read() == b'<svg/>'; assert '-b' in sys.argv; "
                f"sys.stdout.buffer.write({png(4, 5)!r})")
        with tempfile.TemporaryDirectory() as cwd:
            found = {"svgbob_cli": [sys.executable, "-c", svg], "rsvg-convert": [sys.executable, "-c", rsvg]}
            self.assertEqual(puml.image_size(puml.render("svgbob", "-->", Path(cwd), found)), (4, 5))

    def test_error_summary_skips_stack_traces_and_temp_paths(self):
        trace = b"/usr/lib/node/cli.js:10\n    throw e\nError: Parse error on line 4:\n    at fromText (x.js:1)\n"
        self.assertEqual(puml.summary(trace), "Error: Parse error on line 4:")
        work = Path("/tmp/lens-diagram-x")
        self.assertEqual(puml.summary(b"err: /tmp/lens-diagram-x/in.d2:1:1: missing\n", work), "err: in.d2:1:1: missing")

    def test_installed_renderers_produce_png(self):
        samples = {"plantuml": "A -> B\n", "graphviz": "digraph { a -> b }\n", "mermaid": "graph TD\nA-->B\n",
                   "d2": "a -> b\n", "pikchr": 'box "A"; arrow; box "B"\n', "svgbob": "+--+\n|A |-->\n+--+\n",
                   "wavedrom": '{ signal: [{ name: "clk", wave: "p..." }] }\n',
                   "vega-lite": '{"data":{"values":[{"a":1}]},"mark":"bar","encoding":{"x":{"field":"a"}}}',
                   "structurizr": 'workspace {\n model {\n s = softwareSystem "S"\n }\n views {\n systemContext s {\n include *\n }\n }\n}\n'}
        found = puml.tools({})
        with tempfile.TemporaryDirectory() as cwd:
            for language in sorted(puml.available(found)):
                with self.subTest(language=language):
                    width, height = puml.image_size(puml.render(language, samples[language], Path(cwd), found))
                    self.assertGreater(width * height, 0)

    def test_image_size_and_fit_keep_aspect_ratio(self):
        self.assertEqual(puml.image_size(png(800, 600)), (800, 600))
        with self.assertRaises(ValueError):
            puml.image_size(b"GIF89a")
        # 800x600 into 100 cols x 20 rows of 10x20 px cells is height-bound.
        self.assertEqual(puml.fit((800, 600), 100, 20, (10, 20)), (53, 20))
        # Tiny images grow at most MAX_UPSCALE times.
        self.assertEqual(puml.fit((100, 40), 100, 50, (10, 20)), (20, 4))
        self.assertEqual(puml.fit((1, 10000), 5, 5, (10, 20)), (1, 5))

    def test_alignment_offsets_and_saved_preference(self):
        self.assertEqual([puml.offset(a, 50, 20) for a in puml.ALIGNMENTS], [0, 15, 30])
        self.assertEqual(puml.offset("right", 10, 20), 0)  # Wider than the panel: no shift.
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory)
            self.assertEqual(puml.load_alignment(config), "center")
            self.assertEqual(puml.load_alignment(None), "center")
            puml.save_alignment(config, "right")
            self.assertEqual(puml.load_alignment(config), "right")
            (config / "diagrams.json").write_text('{"align": "diagonal"}')
            self.assertEqual(puml.load_alignment(config), "center")
            with self.assertRaises(ValueError):
                puml.save_alignment(config, "diagonal")

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


TOOLS = {"plantuml": ["plantuml"], "mmdc": ["mmdc"]}


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
        render = patch("diagram_preview.render", return_value=self.image)
        self.render = render.start()
        self.addCleanup(render.stop)
        self.nav = Navigator(self.root, "pane", False, "", diagram_tools=TOOLS,
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
        self.render.assert_called_once_with("plantuml", "@startuml\nA -> B\n@enduml\n", self.root / "docs", TOOLS)
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

    def test_zoom_pans_a_diagram_file_larger_than_the_panel(self):
        self.rendered()
        self.nav.preview_focus = True
        self.draw()
        fitted = self.nav.placements[0]
        self.assertIsNone(fitted[6])
        key = self.nav.diagram_list[0]
        for _ in range(10):
            self.assertTrue(self.nav.preview_key("+"))
        self.assertEqual(self.nav.zoom_of(key), puml.ZOOMS[-1])
        self.assertEqual(self.nav.message, "PlantUML zoom 400%")
        self.draw()
        full_cols, full_rows = self.nav.diagram_extent
        self.assertEqual((full_cols, full_rows), (fitted[4] * 4, fitted[5] * 4))
        self.writes.clear()
        self.nav.preview_key("j")
        self.nav.key(__import__("curses").KEY_RIGHT, None)
        self.draw()
        _, _, _, _, cols, rows, crop = self.nav.placements[0]
        self.assertEqual((self.nav.preview_scroll, self.nav.horizontal), (1, 8))
        self.assertEqual(rows, self.nav.body)
        self.assertEqual(crop[:2], (round(8 * 200 / full_cols), round(100 / full_rows)))
        self.assertIn(b",x=", b"".join(self.writes))
        self.nav.preview_key("0")
        self.draw()
        self.assertEqual((self.nav.zoom_of(key), self.nav.preview_scroll, self.nav.horizontal), (1.0, 0, 0))
        self.assertEqual(self.nav.placements[0], fitted)
        for _ in range(20):
            self.nav.preview_key("-")
        self.assertEqual(self.nav.zoom_of(key), puml.ZOOMS[0])

    def test_a_cycles_alignment_and_saves_it(self):
        saved = []
        self.nav.on_alignment = saved.append
        self.rendered()
        self.nav.preview_focus = True
        self.draw()
        _, _, _, center, cols, _, _ = self.nav.placements[0]
        edges = {}
        for expected in ("right", "left", "center"):
            self.assertTrue(self.nav.preview_key("a"))
            self.assertEqual(self.nav.alignment, expected)
            self.draw()
            edges[expected] = self.nav.placements[0][3]
        self.assertEqual(saved, ["right", "left", "center"])
        self.assertEqual(edges["center"], center)
        self.assertLess(edges["left"], center)
        self.assertGreater(edges["right"], center)
        self.assertEqual(center - edges["left"], (edges["right"] - edges["left"]) // 2)
        self.nav.on_alignment = Mock(side_effect=OSError("read-only"))
        self.nav.preview_key("a")
        self.assertEqual(self.nav.message, "Diagram alignment: Right (not saved: read-only)")

    def test_resize_resends_images_after_the_screen_clear(self):
        self.rendered()
        self.nav.track_size((40, 120))
        self.draw()
        self.writes.clear()
        self.nav.track_size((40, 120))
        self.draw()
        self.assertEqual(self.writes, [])
        self.nav.track_size((30, 100))
        self.draw()
        data = b"".join(self.writes)
        self.assertTrue(data.startswith(puml.delete(1)))
        self.assertIn(b"a=t,f=100,i=1", data)
        self.assertIn(b"a=p,i=1,p=1", data)

    def test_without_graphics_puml_uses_source_preview(self):
        nav = Navigator(self.root, "pane", False, "", diagram_tools=TOOLS)
        nav.load("docs/flow.puml")
        self.assertIsNone(nav.diagram_job)
        self.assertFalse(nav.diagram_view())
        self.render.assert_not_called()


class MarkdownDiagramTests(unittest.TestCase):
    TEXT = ("# Title\n\n```plantuml\nA -> B\n```\n\n" + "filler\n\n" * 30
            + "```puml\n@startuml\nC -> D\n@enduml\n```\n\n````md\n```plantuml\nX\n```\n````\n\n"
            + "```mermaid\ngraph TD\nE-->F\n```\n\n```d2\ng -> h\n```\n")

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "notes.md").write_text(self.TEXT)
        self.writes = []
        render = patch("diagram_preview.render", return_value=png(200, 100))
        self.render = render.start()
        self.addCleanup(render.stop)
        self.nav = Navigator(self.root, "pane", False, "", diagram_tools=TOOLS,
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
        from markdown_preview import diagram_blocks
        self.assertEqual(diagram_blocks(self.TEXT), [("plantuml", "A -> B\n"),
                                                     ("plantuml", "@startuml\nC -> D\n@enduml\n"),
                                                     ("mermaid", "graph TD\nE-->F\n"), ("d2", "g -> h\n")])

    def test_render_replaces_fences_with_blank_rows(self):
        from markdown_preview import render_diagrams
        lines, placements = render_diagrams(self.TEXT, 60, None, {("plantuml", "A -> B\n"): 4})
        (line, source, rows), = placements
        self.assertEqual((source, rows), (("plantuml", "A -> B\n"), 4))
        self.assertEqual(lines[line:line + 4], [[], [], [], []])
        text = ["".join(span.text for span in row) for row in lines]
        self.assertFalse(any("LD" in row for row in text))
        self.assertTrue(any("C -> D" in row for row in text))  # Not yet rendered: stays code.

    def test_renders_each_available_language_block(self):
        self.nav.load("notes.md")
        self.settle()
        sources = [call.args[:2] for call in self.render.call_args_list]
        # d2 is not in TOOLS, so its block stays as code.
        self.assertEqual(sources, [("plantuml", "A -> B\n"), ("plantuml", "@startuml\nC -> D\n@enduml\n"),
                                   ("mermaid", "graph TD\nE-->F\n")])
        self.assertTrue(any("g -> h" in line for line in self.nav.content))
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

    def test_zoom_changes_only_the_chosen_markdown_diagram(self):
        self.nav.load("notes.md")
        self.settle()
        self.nav.preview_focus = True
        self.draw()
        sizes = lambda: [size for _, _, size in self.nav.markdown_diagrams]
        first, second = sizes()[:2]
        # The first diagram on screen is the default target.
        self.nav.preview_key("-")
        self.draw()
        self.assertLess(sizes()[0][1], first[1])
        self.assertEqual(sizes()[1], second)
        self.assertTrue(self.nav.preview_key("]"))
        self.draw()
        self.assertEqual(self.nav.current_diagram(), self.nav.markdown_diagrams[1][1])
        self.assertIn("Diagram 2/3", self.nav.message)
        for _ in range(10):
            self.nav.preview_key("+")
        self.draw()
        self.assertEqual(sizes()[1][0], self.nav.render_width)  # Capped at the panel width.
        self.assertGreater(sizes()[1][1], second[1])
        self.assertLess(sizes()[0][1], first[1])  # The first keeps its own zoom.
        self.nav.preview_key("[")
        self.draw()
        self.assertEqual(self.nav.current_diagram(), self.nav.markdown_diagrams[0][1])
        self.nav.preview_key("0")
        self.draw()
        self.assertEqual(sizes()[0], first)

    def test_selected_diagram_is_marked(self):
        self.nav.load("notes.md")
        self.settle()
        self.nav.preview_focus = True
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        with patch.object(self.nav, "span_style", return_value=0):
            self.nav.draw(screen)
        marks = [call for call in screen.addstr.call_args_list if call.args[2] == "▌"]
        line, _, (_, rows) = self.nav.markdown_diagrams[0]
        self.assertEqual(len(marks), rows)

    def test_markdown_diagrams_follow_alignment(self):
        self.nav.load("notes.md")
        self.settle()
        self.nav.preview_focus = True
        self.draw()
        center = self.nav.placements[0][3]
        self.nav.preview_key("a")  # right
        self.nav.preview_key("a")  # left
        self.draw()
        left, cols = self.nav.placements[0][3], self.nav.placements[0][4]
        self.assertEqual(center - left, (self.nav.render_width - cols) // 2)

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
        self.assertEqual(self.nav.message, "Could not render Mermaid: bad")  # The last failure.
        self.assertEqual(self.nav.markdown_diagrams, [])
        self.assertTrue(any("A -> B" in line for line in self.nav.content))


if __name__ == "__main__":
    unittest.main()
