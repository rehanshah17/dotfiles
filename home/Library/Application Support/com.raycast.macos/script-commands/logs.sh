#!/usr/bin/env bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Kitty: Tail Log
# @raycast.mode silent
# @raycast.packageName Terminal
#
# Optional parameters:
# @raycast.icon 🧾
# @raycast.description Pick a file and tail -F in Kitty

exec "$HOME/.local/bin/klog"

