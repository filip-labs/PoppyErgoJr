"""Explicit opt-in launcher for the original hardware demo."""

import argparse
from pathlib import Path
import runpy
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Run the original Poppy color-sort demo on the robot."
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Initialize hardware and run motion after calibration review.",
    )
    args = parser.parse_args()
    if not args.execute:
        parser.error(
            "Motion is disabled. Review docs/CALIBRATION.md, then use --execute on the robot."
        )
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "ColorSort"), run_name="__main__")


if __name__ == "__main__":
    main()
