#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass


HEX_RE = re.compile(r"^#?[0-9a-fA-F]{6}$")


def parse_hex(s: str) -> tuple[int, int, int] | None:
    s = s.strip()
    if not HEX_RE.match(s):
        return None
    if s.startswith("#"):
        s = s[1:]
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


@dataclass
class Theme:
    background: tuple[int, int, int] | None = None
    foreground: tuple[int, int, int] | None = None
    cursor: tuple[int, int, int] | None = None
    colors: dict[int, tuple[int, int, int]] | None = None


def parse_theme(path: str) -> Theme:
    theme = Theme(colors={})
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            # ghostty theme format:
            # palette = 0=#RRGGBB
            # background = RRGGBB
            if line.startswith("palette"):
                m = re.match(r"^palette\s*=\s*(\d+)=(#?[0-9a-fA-F]{6})$", line)
                if not m:
                    continue
                idx = int(m.group(1))
                rgb = parse_hex(m.group(2))
                if rgb is not None:
                    theme.colors[idx] = rgb
                continue

            if "=" in line:
                key, value = [p.strip() for p in line.split("=", 1)]
            else:
                continue

            if key == "background":
                theme.background = parse_hex(value) or theme.background
            elif key == "foreground":
                theme.foreground = parse_hex(value) or theme.foreground
            elif key in {"cursor-color", "cursor_color"}:
                theme.cursor = parse_hex(value) or theme.cursor

    return theme


def bg(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\x1b[48;2;{r};{g};{b}m"


def fg(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\x1b[38;2;{r};{g};{b}m"


RESET = "\x1b[0m"


def block(rgb: tuple[int, int, int], width: int = 6) -> str:
    return f"{bg(rgb)}{' ' * width}{RESET}"


def safe(rgb: tuple[int, int, int] | None, fallback: tuple[int, int, int]) -> tuple[int, int, int]:
    return rgb if rgb is not None else fallback


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: theme_preview.py /path/to/ghostty_theme", file=sys.stderr)
        return 2

    path = sys.argv[1]
    theme = parse_theme(path)

    default_bg = (0, 0, 0)
    default_fg = (255, 255, 255)
    background = safe(theme.background, default_bg)
    foreground = safe(theme.foreground, default_fg)

    title = path.split("/")[-1]
    print(f"{title}")
    print()

    sample = " The quick brown fox jumps over the lazy dog "
    print(f"{bg(background)}{fg(foreground)}{sample}{RESET}")
    print()

    colors = theme.colors or {}
    row0 = [colors.get(i) for i in range(0, 8)]
    row1 = [colors.get(i) for i in range(8, 16)]

    def render_row(items: list[tuple[int, int, int] | None]) -> str:
        out = []
        for item in items:
            if item is None:
                out.append("\x1b[48;2;64;64;64m      \x1b[0m")
            else:
                out.append(block(item))
        return " ".join(out)

    print("ANSI 0-7")
    print(render_row(row0))
    print()
    print("ANSI 8-15")
    print(render_row(row1))
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
