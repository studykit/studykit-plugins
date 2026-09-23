"""Decode terminal mouse reports without relying on ncurses mouse ABI versions."""
from __future__ import annotations

import curses
from dataclasses import dataclass
import os
import re
import sys


@dataclass(frozen=True)
class Mouse:
    x: int
    y: int
    action: str


@dataclass(frozen=True)
class Appearance:
    mode: str


def mouse_event(button: int, x: int, y: int, released=False):
    # Only the left button drags; its motion and release end a divider drag.
    if released or (button & 3 == 3 and not button & 64):
        return Mouse(x, y, "release") if not button & 64 else None
    if button & 32:
        return Mouse(x, y, "drag") if button & 3 == 0 else None
    if button & 64 and button & 3 in (0, 1):
        return Mouse(x, y, "up" if button & 3 == 0 else "down")
    if button & 3 == 0:
        return Mouse(x, y, "click")
    return None


def decode(sequence: str):
    appearance = re.fullmatch(r"\x1b\[\?997;([12])n", sequence)
    if appearance:
        return Appearance("light" if appearance[1] == "2" else "dark")
    mouse = re.fullmatch(r"\x1b\[<(\d+);(\d+);(\d+)([Mm])", sequence)
    if mouse:
        return mouse_event(int(mouse[1]), int(mouse[2]) - 1, int(mouse[3]) - 1, mouse[4] == "m")
    if sequence.startswith("\x1b[M") and len(sequence) == 6:
        return mouse_event(ord(sequence[3]) - 32, ord(sequence[4]) - 33, ord(sequence[5]) - 33)
    key = re.fullmatch(r"\x1b(?:\[|O)(?:1;\d+)?([ABCDHFZ])", sequence)
    if key:
        return {"A": curses.KEY_UP, "B": curses.KEY_DOWN, "C": curses.KEY_RIGHT,
                "D": curses.KEY_LEFT, "H": curses.KEY_HOME, "F": curses.KEY_END,
                "Z": curses.KEY_BTAB}[key[1]]
    numbered = re.fullmatch(r"\x1b\[(\d+)(?:;\d+)?~", sequence)
    if numbered:
        return {1: curses.KEY_HOME, 3: curses.KEY_DC, 4: curses.KEY_END, 5: curses.KEY_PPAGE,
                6: curses.KEY_NPAGE, 7: curses.KEY_HOME, 8: curses.KEY_END}.get(int(numbered[1]))
    return None


def read(screen):
    key = screen.get_wch()
    if key != "\x1b":
        return key
    sequence = key
    screen.timeout(60)
    try:
        while len(sequence) < 64:
            try:
                char = screen.get_wch()
            except curses.error:
                return "\x1b" if sequence == "\x1b" else None
            if not isinstance(char, str):
                return char
            sequence += char
            if len(sequence) == 2 and char not in "[O":
                return sequence  # Alt+key arrives as Escape then the key.
            if sequence.startswith("\x1b[M"):
                if len(sequence) == 6:
                    return decode(sequence)
            elif len(sequence) >= 3 and "@" <= char <= "~":
                return decode(sequence)
    finally:
        screen.timeout(-1)
    return None


def enable(screen):
    # Deliver control keys to the navigator instead of terminal signal handling.
    curses.raw()
    # keypad(False) prevents older ncurses from swallowing button-five reports.
    screen.keypad(False)
    curses.mousemask(0)
    sys.stdout.write("\x1b[?1000h\x1b[?1002h\x1b[?1006h\x1b[?996n")
    sys.stdout.flush()


def sync_size(screen):
    # A terminal surface can settle to its final size while curses is still initializing.
    # Consult the PTY as well as SIGWINCH so a missed early resize can recover.
    try:
        columns, lines = os.get_terminal_size()
        if lines > 0 and columns > 0 and screen.getmaxyx() != (lines, columns):
            curses.resizeterm(lines, columns)
            screen.clearok(True)
    except (OSError, curses.error):
        pass


def disable():
    sys.stdout.write("\x1b[?1000l\x1b[?1002l\x1b[?1006l")
    sys.stdout.flush()
