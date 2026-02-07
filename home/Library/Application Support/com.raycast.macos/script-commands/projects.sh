#!/usr/bin/env bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Kitty: Open Project
# @raycast.mode silent
# @raycast.packageName Terminal
#
# Optional parameters:
# @raycast.icon 📁
# @raycast.description Pick a directory and open it in Kitty

exec "$HOME/.local/bin/kproj"

