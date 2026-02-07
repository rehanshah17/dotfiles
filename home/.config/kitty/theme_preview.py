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
            # kitty-themes uses: key value
            parts = line.split()
            if len(parts) < 2:
                continue
            key = parts[0]
            value = parts[1]

            if key in {"background", "foreground", "cursor", "cursor_color", "cursor-color"}:
                rgb = parse_hex(value)
                if rgb is None:
                    continue
                if key == "background":
                    theme.background = rgb
                elif key == "foreground":
                    theme.foreground = rgb
                else:
                    theme.cursor = rgb
                continue

            m = re.match(r"^color(\d+)$", key)
            if m:
                idx = int(m.group(1))
                rgb = parse_hex(value)
                if rgb is None:
                    continue
                theme.colors[idx] = rgb
                continue

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
        print("usage: theme_preview.py /path/to/theme.conf", file=sys.stderr)
        return 2

    path = sys.argv[1]
    theme = parse_theme(path)

    default_bg = (0, 0, 0)
    default_fg = (255, 255, 255)
    background = safe(theme.background, default_bg)
    foreground = safe(theme.foreground, default_fg)

    title = path.split("/")[-1].removesuffix(".conf")
    print(f"{title}")
    print()

    sample = " The quick brown fox jumps over the lazy dog "
    print(f"{bg(background)}{fg(foreground)}{sample}{RESET}")
    print()

    colors = theme.colors or {}
    # Prefer 0-15, but tolerate missing keys.
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

