#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


HEX_RE = re.compile(r"^#?[0-9a-fA-F]{6}$")


def parse_hex(s: str) -> str | None:
    s = s.strip()
    if not HEX_RE.match(s):
        return None
    if s.startswith("#"):
        s = s[1:]
    return s.lower()


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: kitty_to_ghostty.py /path/to/kitty_theme.conf /path/to/ghostty_theme", file=sys.stderr)
        return 2

    kitty_path = Path(sys.argv[1]).expanduser()
    ghostty_path = Path(sys.argv[2]).expanduser()

    colors: dict[int, str] = {}
    background: str | None = None
    foreground: str | None = None
    cursor: str | None = None

    for raw in kitty_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        key, value = parts[0], parts[1]

        if key == "background":
            background = parse_hex(value) or background
            continue
        if key == "foreground":
            foreground = parse_hex(value) or foreground
            continue
        if key in {"cursor", "cursor_color"}:
            cursor = parse_hex(value) or cursor
            continue

        m = re.match(r"^color(\d+)$", key)
        if m:
            idx = int(m.group(1))
            hx = parse_hex(value)
            if hx is not None:
                colors[idx] = hx

    # Ghostty expects palette entries 0-15. If missing, skip.
    out: list[str] = []
    for i in range(16):
        if i in colors:
            out.append(f"palette = {i}=#{colors[i]}")

    if background:
        out.append(f"background = {background}")
    if foreground:
        out.append(f"foreground = {foreground}")
    if cursor:
        out.append(f"cursor-color = {cursor}")

    ghostty_path.parent.mkdir(parents=True, exist_ok=True)
    ghostty_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

