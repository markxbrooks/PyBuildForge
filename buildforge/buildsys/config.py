import sys
from pathlib import Path

from elmo.project import __version__, __project__, __program__, __author__
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

APP_NAME = "elmo"
DESCRIPTION = "An extremely lightweight molecular graphics program"
MAINTAINER = "Mark Brooks <mark.x.brooks@gmail.com>"
HOMEPAGE = "https://github.com/markxbrooks/JDXI-Editor"
LICENSE = "MIT"
CATEGORIES = "AudioVideo;Audio;Midi;Music;"


PROJECT_ROOT = SCRIPT_DIR.parent.parent
PROGRAM_DISPLAY_NAME = "elmo"
PROGRAM_SRC_DIR = "elmo"
PROGRAM_RESOURCES_DIR = "resources"
PROGRAM_WINDOWS_ICON = "icon.ico"
APP_DMG_BUILD_DIR  = "elmo_dmg"

# Build configuration
APP_NAME = "elmo"
APP_DISPLAY_NAME = __program__
VERSION = __version__
PKG_IDENTIFIER = "com.elmo.app"
INSTALL_LOCATION = "/Applications"

# Directories
BUILD_DIR = PROJECT_ROOT / "build" / "macos"
DIST_DIR = PROJECT_ROOT / "dist"
VENV_PATH = PROJECT_ROOT / "venv"
PYTHON_PATH = VENV_PATH / "bin" / "python"

