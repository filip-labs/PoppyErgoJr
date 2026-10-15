# Robot control and lifecycle

Use the [setup guide](SETUP.md) and [calibration checklist](CALIBRATION.md) first.
The controller runs locally on the robot's Raspberry Pi. Ethernet/SSH provides
operator access; this application does not implement a remote robot protocol.
Pypot and the installed Poppy creature configuration handle motor communication.
No custom serial port, baud rate, motor IDs or firmware are specified here.

## Start

From the repository on the robot:

```bash
python3 scripts/check_environment.py
python3 scripts/run_color_sort.py --help
python3 scripts/run_color_sort.py --execute
```

`--help`, missing arguments and invalid arguments do not initialize the robot.
`--execute` constructs `PoppyErgoJr()` and sets all six motor speeds to 40.
The legacy `python3 ColorSort` entry point still starts hardware immediately.
Import only `poppy_sort.vision` for offline work; do not import or execute
`ColorSort` as a utility module.

## Sorting cycle

1. Start and immediately stop the upstream base-posture primitive, then wait.
2. Capture an RGB frame and display it with matplotlib; close the window to continue.
3. Apply fixed HSV masks and find contours. Red takes priority over blue.
4. Map the largest contour's x centroid to m1. The y centroid is unused.
5. Lower m3, close m6, check load once and retry if needed, then lift.
6. Rotate m4 left for red or right for blue, then open m6.
7. Capture again. Exit if neither mask contains pixels, otherwise repeat.

See the calibration table for the exact existing values. The script does not
verify that base posture has completed, that an object was successfully picked
up after the retry, or that the next frame contains a different object.

## Stop and disconnect

Remain with the robot and use the upstream documented physical stop/power
procedure for your assembly if motion must stop. Ctrl+C interrupts Python but
is not an emergency stop: previously submitted goals may still be active.
Support the arm and remove loads as required by the hardware procedure before
removing power; releasing torque can let an unsupported arm fall.

The current controller has no `try/finally` shutdown path. Upstream Pypot exposes
[`Robot.close()`](https://github.com/poppy-project/pypot/blob/master/pypot/robot/robot.py)
to stop synchronization and close controller I/O, but this is not proof of torque
disable or a physical emergency stop. No automatic return pose, compliance
command, or new shutdown motion has been added without hardware validation.
After stopping the controller, shut down the Raspberry Pi using the image's
normal OS shutdown procedure before removing its power. Do not launch another
controller until the previous process is stopped and resources are released.
