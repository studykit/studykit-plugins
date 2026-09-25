"""Render diagram sources to PNG and place them with the Kitty graphics protocol."""
# Lens writes Kitty escapes itself instead of calling Herdr's pane graphics API:
# popups have no pane ID, but Herdr parses Kitty graphics from popup output too.
from __future__ import annotations

import base64
from dataclasses import dataclass
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
# Kitty requires base64 payload chunks of at most 4096 bytes.
CHUNK = 4096
# Small diagrams stay legible on high-density cells without turning into blur.
MAX_UPSCALE = 2.0
TIMEOUT = 60  # Mermaid starts a headless browser for every render.
ALIGNMENTS = ("left", "center", "right")
ZOOMS = (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0)  # Relative to fitting the panel.


@dataclass(frozen=True)
class Language:
    title: str
    fences: tuple[str, ...]
    names: tuple[str, ...]  # Filename suffixes, or whole names such as workspace.dsl.
    tools: tuple[str, ...]


LANGUAGES = {
    "plantuml": Language("PlantUML", ("plantuml", "puml"), (".puml", ".plantuml", ".pu", ".iuml", ".wsd"), ("plantuml",)),
    "mermaid": Language("Mermaid", ("mermaid", "mmd"), (".mmd", ".mermaid"), ("mmdc",)),
    "d2": Language("D2", ("d2",), (".d2",), ("d2", "rsvg-convert")),
    "graphviz": Language("Graphviz", ("dot", "graphviz", "gv"), (".dot", ".gv"), ("dot",)),
    "pikchr": Language("Pikchr", ("pikchr",), (".pikchr", ".pik"), ("pikchr", "rsvg-convert")),
    "svgbob": Language("Svgbob", ("bob", "svgbob"), (".bob",), ("svgbob_cli", "rsvg-convert")),
    "wavedrom": Language("WaveDrom", ("wavedrom",), (), ("wavedrom-cli", "rsvg-convert")),
    "vega-lite": Language("Vega-Lite", ("vega-lite", "vegalite"), (".vl.json",), ("vl2svg", "rsvg-convert")),
    "structurizr": Language("Structurizr", ("structurizr",), ("workspace.dsl",), ("structurizr-cli", "plantuml")),
    # Obsidian image embeds; the source is the file, its |size and mtime, one per line.
    "image": Language("Image", (), (), ()),
}
MAX_IMAGE_BYTES = 32 * 1024 * 1024
FENCES = {fence: language for language, spec in LANGUAGES.items() for fence in spec.fences}


def fence_language(info: str) -> str | None:
    words = info.split()
    return FENCES.get(words[0].lower()) if words else None


def file_language(name: str) -> str | None:
    lowered = Path(name).name.lower()
    for language, spec in LANGUAGES.items():
        if any(lowered == item if not item.startswith(".") else lowered.endswith(item) for item in spec.names):
            return language
    return None


def tools(env) -> dict[str, list[str]]:
    """Commands found on PATH, by tool name; PLANTUML_JAR can stand in for plantuml."""
    found = {name: [path] for spec in LANGUAGES.values() for name in spec.tools
             if (path := shutil.which(name))}
    jar = env.get("PLANTUML_JAR")
    if "plantuml" not in found and jar and Path(jar).is_file() and shutil.which("java"):
        found["plantuml"] = ["java", "-Djava.awt.headless=true", "-jar", jar]
    return found


def available(found: dict[str, list[str]]) -> set[str]:
    return {language for language, spec in LANGUAGES.items() if all(name in found for name in spec.tools)}


def first_image(data: bytes) -> bytes:
    # A file with several @startuml blocks pipes one PNG after another.
    end = data.find(b"IEND")
    return data[:end + 8] if end >= 0 else data


def summary(output: bytes, work: Path | None = None) -> str:
    text = output.decode(errors="replace")
    if work is not None:
        text = text.replace(f"{work}/", "")  # Temporary input paths mean nothing to the reader.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # Node tools end with a stack trace; the message is the line naming the error.
    named = [line for line in lines if "error" in line.lower() and not line.startswith("at ")]
    return (named or [line for line in lines if not line.startswith("at ")] or [""])[0]


def run(argv, cwd, data=None, work=None) -> bytes:
    result = subprocess.run(argv, cwd=cwd, input=data, capture_output=True, timeout=TIMEOUT)
    if result.returncode:
        detail = summary(result.stderr or result.stdout, work)
        raise RuntimeError(detail or f"{Path(argv[0]).name} exited with status {result.returncode}")
    return result.stdout


def png(data: bytes, tool: str) -> bytes:
    if not data.startswith(PNG_SIGNATURE):
        raise RuntimeError(f"{tool} produced no image")
    return first_image(data)


def plantuml(source: str, cwd: Path, found) -> bytes:
    if "@start" not in source:
        source = f"@startuml\n{source}@enduml\n"
    result = subprocess.run([*found["plantuml"], "-tpng", "-pipe", "-charset", "UTF-8"], cwd=cwd,
                            input=source.encode(), capture_output=True, timeout=TIMEOUT)
    if not result.stdout.startswith(PNG_SIGNATURE):
        detail = result.stderr.decode(errors="replace").strip().splitlines()
        raise RuntimeError(detail[-1] if detail else "PlantUML produced no image")
    # On syntax errors PlantUML still pipes an image that describes the error.
    return first_image(result.stdout)


def image(source: str, cwd: Path, found) -> bytes:
    path = Path(source.split("\n")[0])
    if path.stat().st_size > MAX_IMAGE_BYTES:
        raise ValueError("The image is too large to preview")
    data = path.read_bytes()
    if data.startswith(PNG_SIGNATURE):
        return first_image(data)
    if path.suffix.lower() == ".svg":
        if "rsvg-convert" not in found:
            raise RuntimeError("SVG images need rsvg-convert")
        return png(run([*found["rsvg-convert"], "-f", "png", "-b", "white", "-z", "2"], cwd, data), "rsvg-convert")
    # Kitty graphics take PNG, so other formats go through whichever converter is installed.
    with tempfile.TemporaryDirectory(prefix="lens-image-") as directory:
        out = Path(directory) / "out.png"
        if tool := shutil.which("sips"):
            run([tool, "-s", "format", "png", str(path), "--out", str(out)], cwd, work=Path(directory))
            return png(out.read_bytes(), "sips")
        if tool := shutil.which("magick") or shutil.which("convert"):
            return png(run([tool, f"{path}[0]", "png:-"], cwd), Path(tool).name)
    raise RuntimeError(f"{path.suffix} images need sips or ImageMagick")


def render(language: str, source: str, cwd: Path, found: dict[str, list[str]]) -> bytes:
    """Render one diagram; cwd is the source file's folder, for relative includes."""
    if language == "image":
        return image(source, cwd, found)
    if language == "plantuml":
        return plantuml(source, cwd, found)
    if language == "graphviz":
        return png(run([*found["dot"], "-Tpng", "-Gdpi=144"], cwd, source.encode()), "dot")
    with tempfile.TemporaryDirectory(prefix="lens-diagram-") as directory:
        work = Path(directory)
        if language == "mermaid":
            (work / "in.mmd").write_text(source)
            run([*found["mmdc"], "-i", str(work / "in.mmd"), "-o", str(work / "out.png"),
                 "-b", "white", "-s", "2", "-q"], cwd, work=work)
            return png((work / "out.png").read_bytes(), "mmdc")
        if language == "structurizr":
            # The CLI cannot draw diagrams; it exports each view as PlantUML.
            (work / "workspace.dsl").write_text(source)
            run([*found["structurizr-cli"], "export", "-w", str(work / "workspace.dsl"),
                 "-f", "plantuml/c4plantuml", "-o", str(work / "out")], cwd, work=work)
            views = sorted((work / "out").glob("*.puml"))
            if not views:
                raise RuntimeError("The workspace defines no views")
            return plantuml(views[0].read_text(), cwd, found)
        if language == "d2":
            (work / "in.d2").write_text(source)
            run([*found["d2"], "--pad", "20", str(work / "in.d2"), str(work / "out.svg")], cwd, work=work)
            svg = (work / "out.svg").read_bytes()
        elif language == "pikchr":
            svg = run([*found["pikchr"], "--svg-only", "-"], cwd, source.encode())
            if b"<svg" not in svg:
                raise RuntimeError(summary(svg) or "pikchr produced no image")
        elif language == "svgbob":
            svg = run(found["svgbob_cli"], cwd, source.encode())
        elif language == "wavedrom":
            (work / "in.json").write_text(source)
            run([*found["wavedrom-cli"], "-i", str(work / "in.json"), "-s", str(work / "out.svg")], cwd, work=work)
            svg = (work / "out.svg").read_bytes()
        elif language == "vega-lite":
            (work / "in.json").write_text(source)
            run([*found["vl2svg"], str(work / "in.json"), str(work / "out.svg")], cwd, work=work)
            svg = (work / "out.svg").read_bytes()
        else:
            raise ValueError(f"Unknown diagram language: {language}")
        # Transparent SVGs would vanish on dark themes, so flatten onto white.
        return png(run([*found["rsvg-convert"], "-f", "png", "-b", "white", "-z", "2"], cwd, svg), "rsvg-convert")


def image_size(png: bytes) -> tuple[int, int]:
    if not png.startswith(PNG_SIGNATURE) or png[12:16] != b"IHDR":
        raise ValueError("Not a PNG image")
    return struct.unpack(">II", png[16:24])


def fit(size: tuple[int, int], cols: int, rows: int, cell: tuple[int, int]) -> tuple[int, int]:
    (width, height), (cell_width, cell_height) = size, cell
    scale = min(cols * cell_width / width, rows * cell_height / height, MAX_UPSCALE)
    return (max(1, min(cols, round(width * scale / cell_width))),
            max(1, min(rows, round(height * scale / cell_height))))


def scaled(size: tuple[int, int], cols: int, rows: int, cell: tuple[int, int], zoom: float,
           max_cols: int | None = None) -> tuple[int, int]:
    """Cells for an image drawn at `zoom` times its fit into cols x rows; unlike fit,
    the result may exceed the box. max_cols caps the width."""
    (width, height), (cell_width, cell_height) = size, cell
    scale = min(cols * cell_width / width, rows * cell_height / height, MAX_UPSCALE) * zoom
    if max_cols is not None:
        scale = min(scale, max_cols * cell_width / width)
    return max(1, round(width * scale / cell_width)), max(1, round(height * scale / cell_height))


def offset(alignment: str, width: int, cols: int) -> int:
    """Columns to shift an image `cols` wide within `width` for the alignment."""
    gap = max(0, width - cols)
    return {"left": 0, "center": gap // 2, "right": gap}.get(alignment, gap // 2)


def load_alignment(config_dir: Path | None) -> str:
    if config_dir is not None:
        try:
            value = json.loads((config_dir / "diagrams.json").read_text())
            if isinstance(value, dict) and value.get("align") in ALIGNMENTS:
                return value["align"]
        except (OSError, ValueError):
            pass
    return "center"


def save_alignment(config_dir: Path, alignment: str):
    if alignment not in ALIGNMENTS:
        raise ValueError("Unknown diagram alignment")
    config_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".diagrams-", dir=config_dir)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump({"align": alignment}, stream)
            stream.write("\n")
        os.replace(temporary, config_dir / "diagrams.json")
    finally:
        Path(temporary).unlink(missing_ok=True)


def apc(control: str, payload: bytes = b"") -> bytes:
    return b"\x1b_G" + control.encode() + (b";" + payload if payload else b"") + b"\x1b\\"


def transmit(image_id: int, png: bytes) -> bytes:
    data = base64.standard_b64encode(png)
    chunks = [data[i:i + CHUNK] for i in range(0, len(data), CHUNK)] or [b""]
    out = []
    for number, chunk in enumerate(chunks):
        more = int(number < len(chunks) - 1)
        control = f"a=t,f=100,i={image_id},q=2,m={more}" if number == 0 else f"m={more}"
        out.append(apc(control, chunk))
    return b"".join(out)


def place(image_id: int, placement: int, y: int, x: int, cols: int, rows: int, crop=None) -> bytes:
    # crop is (x, y, width, height) in image pixels, for a partly visible image.
    source = ",x={},y={},w={},h={}".format(*crop) if crop else ""
    # Save and restore the cursor so curses' idea of its position stays true.
    return (b"\x1b7" + f"\x1b[{y + 1};{x + 1}H".encode()
            + apc(f"a=p,i={image_id},p={placement}{source},c={cols},r={rows},C=1,q=2") + b"\x1b8")


def hide(image_id: int, placement: int | None = None) -> bytes:
    # Without a placement ID, every placement of the image is removed.
    target = f",p={placement}" if placement is not None else ""
    return apc(f"a=d,d=i,i={image_id}{target},q=2")


def delete(image_id: int) -> bytes:
    return apc(f"a=d,d=I,i={image_id},q=2")


def write(data: bytes, fd: int = 1):
    view = memoryview(data)
    while view:
        view = view[os.write(fd, view):]
