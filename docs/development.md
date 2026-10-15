# Offline development

Use a separate environment on a workstation. Hardware dependencies and the robot
OS image are not required. Python 3.9 and 3.12 are the CI targets; this does not
establish compatibility with the historical robot image's Python environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
ruff check .
ruff format --check .
```

`opencv-python-headless` supports synthetic-image checks without a display.
Do not install it alongside `opencv-python` in the robot environment: both
provide `cv2`. Development dependency ranges are separate from the unpinned
historical hardware requirements; they are not a hardware lockfile.

Tests cover RGB masks, the known red hue limitation, centroid edge cases, mapping,
launcher refusal/dispatch, and the actual sorting script with a fake robot,
camera, matplotlib and clock. They cover red priority, blue routing, no-color
handling, and the existing failed-grasp behavior. No Pypot package is installed
in CI, and no motors, serial devices, network robot or physical camera are used.
Mocks validate software decisions only; they do not verify kinematics, timing,
load measurement, collision clearance or safe shutdown.

The formatter excludes the legacy `ColorSort` file to keep its motion-code diff
small. Lint and syntax checks still include it. Run `ruff format .` for maintained
Python modules and scripts. GitHub Actions runs the same checks on pushes and PRs.
