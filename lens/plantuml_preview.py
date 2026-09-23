"""Render PlantUML sources to PNG and place them with the Kitty graphics protocol."""
# Lens writes Kitty escapes itself instead of calling Herdr's pane graphics API:
# popups have no pane ID, but Herdr parses Kitty graphics from popup output too.
from __future__ import annotations

import base64
import os
from pathlib import Path
import shutil
import struct
import subprocess


SUFFIXES = (".puml", ".plantuml", ".pu", ".iuml", ".wsd")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
# Kitty requires base64 payload chunks of at most 4096 bytes.
CHUNK = 4096
# Small diagrams stay legible on high-density cells without turning into blur.
MAX_UPSCALE = 2.0


def supported(name: str) -> bool:
    return Path(name).suffix.lower() in SUFFIXES


def command(env) -> list[str] | None:
    if shutil.which("plantuml"):
        return ["plantuml"]
    jar = env.get("PLANTUML_JAR")
    if jar and Path(jar).is_file() and shutil.which("java"):
        return ["java", "-Djava.awt.headless=true", "-jar", jar]
    return None


def first_image(data: bytes) -> bytes:
    # A file with several @startuml blocks pipes one PNG after another.
    end = data.find(b"IEND")
    return data[:end + 8] if end >= 0 else data


def render(source: str, cwd: Path, argv: list[str], timeout: float = 30) -> bytes:
    result = subprocess.run([*argv, "-tpng", "-pipe", "-charset", "UTF-8"], cwd=cwd,
                            input=source.encode(), capture_output=True, timeout=timeout)
    if not result.stdout.startswith(PNG_SIGNATURE):
        detail = result.stderr.decode(errors="replace").strip().splitlines()
        raise RuntimeError(detail[-1] if detail else "PlantUML produced no image")
    # On syntax errors PlantUML still pipes an image that describes the error.
    return first_image(result.stdout)


def image_size(png: bytes) -> tuple[int, int]:
    if not png.startswith(PNG_SIGNATURE) or png[12:16] != b"IHDR":
        raise ValueError("Not a PNG image")
    return struct.unpack(">II", png[16:24])


def fit(size: tuple[int, int], cols: int, rows: int, cell: tuple[int, int]) -> tuple[int, int]:
    (width, height), (cell_width, cell_height) = size, cell
    scale = min(cols * cell_width / width, rows * cell_height / height, MAX_UPSCALE)
    return (max(1, min(cols, round(width * scale / cell_width))),
            max(1, min(rows, round(height * scale / cell_height))))


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
