"""Check imports only; never initialize the robot or send motor commands."""

import importlib
import sys


def main():
    print("Python:", sys.version.split()[0])
    failed = False
    for name in ("numpy", "matplotlib.pyplot", "cv2", "pypot.creatures"):
        try:
            module = importlib.import_module(name)
            if name == "pypot.creatures":
                getattr(module, "PoppyErgoJr")
            print("OK:", name)
        except Exception as error:
            failed = True
            print("FAIL:", name, "-", error)
    print("Import checks only: hardware, camera, and calibration were not tested.")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
