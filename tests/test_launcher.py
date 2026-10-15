"""Exercise the real CLI gate; mock dispatch to avoid robot imports."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts" / "run_color_sort.py"


class LauncherTests(unittest.TestCase):
    def test_help_and_refusal_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            for arguments, expected in ((["--help"], 0), ([], 2), (["--unknown"], 2)):
                with self.subTest(arguments=arguments):
                    result = subprocess.run(
                        [sys.executable, "-I", str(LAUNCHER), *arguments],
                        cwd=directory,
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(result.returncode, expected, result.stderr)
                    self.assertNotIn("ModuleNotFoundError", result.stderr)

    def test_execute_dispatches_only_after_opt_in(self):
        spec = importlib.util.spec_from_file_location("launcher", LAUNCHER)
        launcher = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(launcher)
        with (
            patch.object(sys, "argv", [str(LAUNCHER), "--execute"]),
            patch.object(launcher.runpy, "run_path") as dispatch,
            patch.object(sys, "path", list(sys.path)),
        ):
            launcher.main()
            dispatch.assert_called_once_with(str(ROOT / "ColorSort"), run_name="__main__")
            self.assertEqual(sys.path[0], str(ROOT))
