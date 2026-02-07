#!/usr/bin/env bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Inbox: Move Items
# @raycast.mode silent
# @raycast.packageName Inbox
#
# Optional parameters:
# @raycast.icon 🚚
# @raycast.description Pick files from Inbox/Downloads and move them into PARA folders

exec "$HOME/.local/bin/inbox-mv"

