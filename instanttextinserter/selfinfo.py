# encoding: shift-jis

import os
import sys

# Program Information
PROGRAM_NAME = "InstantTextInserter"
VERSION = "0.2.1"
AUTHOR = "shouh"
PROGRAM_INFO = PROGRAM_NAME + " " + "v" + VERSION + " (c) " + AUTHOR

# GUI information
WINDOWCLASSNAME = "itiwnd"
TRAYICON_TOOLTIP = PROGRAM_NAME + " v" + VERSION

# Program pathes
PROGRAM_FULLPATH = sys.argv[0]
PROGRAM_DIRECTORY = os.path.dirname(PROGRAM_FULLPATH)

# Files path
# ここに置くべきかどうか迷ったけど
# 一元管理できるのでとりあえずここで...
SNIPPETFOLDER_FULLPATH = os.path.join(PROGRAM_DIRECTORY, "snippet")
HOTKEYCONFIG_FULLPATH = os.path.join(PROGRAM_DIRECTORY, "hotkey.ini")
