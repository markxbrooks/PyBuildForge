from pathlib import Path
import sys

class BuildContext:
    def __init__(self):
        self.project_root = self._find_project_root()
        self.venv_python = self._find_venv_python()

    def _find_project_root(self) -> Path:
        here = Path(__file__).resolve()
        for parent in here.parents:
            if (parent / "pyproject.toml").exists():
                return parent
            if (parent / "elmo").exists():
                return parent
        raise RuntimeError("Could not locate project root")

    def _find_venv_python(self) -> Path:
        # Prefer project-local envs first so builds are reproducible.
        possible_venv_dirs = ["venv", ".venv"]
        for venv in possible_venv_dirs:
            if sys.platform == "win32":
                python = self.project_root / venv / "Scripts" / "python.exe"
            else:
                python = self.project_root / venv / "bin" / "python"

            if python.exists():
                return python

        # If already running inside a virtual environment, reuse it.
        if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
            return Path(sys.executable).resolve()

        raise RuntimeError("Virtualenv missing (expected ./venv or ./.venv)")
