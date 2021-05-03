import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
packages = ["os", "requests", "tekore",
"lxml", "bs4", "PyQt5", "spotify", "webbrowser", "shiboken2",
"sys", "platform", "ctypes", "subprocess", "datetime", "base64",
"re", "random", "spotipy", "flask", "ui_vs", "UserInterfaceFunctions", "PySide2"]

includefiles = ["vs_app_rc.py", "ui_vs.py", "UserInterfaceFunctions.py",
 "vs.ui", "vs_app.qrc"]
includes = []
excludes = []
# GUI applications require a different base on Windows (the default is for
# a console application).

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Vibeshare Playlist Generator",
    version = "1.3",
    description = "Spotify Playlist Generator",
    options = {"build_exe": {"include_files":includefiles, "packages":packages}},
    executables = [Executable("splash_screen.py", base=None, targetName = "VibeShare Playlist Generator.exe", icon="vs.ico")]
)
