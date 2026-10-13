# Hardware and OS setup

## 1. Assemble and initialize the robot

Follow the upstream [parts list](https://github.com/poppy-project/poppy-ergo-jr/blob/master/doc/bom.md) and [assembly guide](https://docs.poppy-project.org/en/assembly-guides/ergo-jr/index.html). Use the gripper attachment and a working camera for this application. Follow the upstream motor-ID and initialization procedure before using sorting poses.

## 2. Prepare the microSD card

The project presentation references Poppy image **4.0.2**. Its [official release](https://github.com/poppy-project/poppy-ergo-jr/releases/tag/4.0.2) is marked as a **prerelease**. It is a historical reference, not a claim of compatibility with every Raspberry Pi model or a verified environment for this repository. Confirm board support with the release documentation before flashing.

1. Back up the target SD card: flashing overwrites it.
2. Download `2022-01-07-poppy-ergo-jr.img.7z` from the official release. The archive is approximately 2.15 GB; allow additional space for the extracted image.
3. Extract the `.7z` archive with a compatible archive tool.
4. Optionally compare the files against the published MD5 values in [os-image.json](os-image.json). MD5 detects accidental corruption here; it is not proof of authenticity.
5. Flash the extracted `.img` using [balenaEtcher](https://etcher.balena.io/) or the upstream [image flashing guide](https://docs.poppy-project.org/en/installation/burn-an-image-file.html).
6. Insert the card and boot the robot following the official power and wiring instructions.

The image stays upstream rather than being committed to this repository. Do not substitute a generic Raspberry Pi OS installation and assume that motor communication, camera support, and Poppy services are already configured.

## 3. Connect

Connect the robot and computer to the same local network using Ethernet. Try `http://poppy.local`; if name resolution fails, use the robot's IP address from your router or network tools. Open the image's interface to initialize motors and enable or check the camera. Exact interface options depend on the image.

For a terminal, use the image's documented SSH account, or a terminal exposed by its interface. Do not assume a username or password. Stop other notebooks and robot-control services before creating another controller.

## 4. Check dependencies

Run these commands **on the Raspberry Pi**, not on a laptop expecting remote hardware access:

```bash
python3 --version
python3 scripts/check_environment.py
python3 -m pip freeze > environment-local.txt
```

The checker imports packages but never constructs `PoppyErgoJr`. It cannot validate camera access, motor IDs, power, or calibration.

[requirements.txt](../requirements.txt) lists direct dependencies, deliberately without guessed pins. Prefer the versions already configured by the official image. If imports are missing, inspect the active Python environment first. Only in a compatible environment that you intend to modify:

```bash
python3 -m pip install -r requirements.txt
```

Do not blindly upgrade the preconfigured robot stack. No dependency lockfile is provided because the exact working hardware environment has not been recorded in the repository.

## 5. First run

Read [CALIBRATION.md](CALIBRATION.md), test individual poses through the robot's tools, and prepare a clear workspace. The original script opens a matplotlib figure for each captured frame; close it to continue. A headless SSH session may require a suitable display or a deliberate plotting change.

```bash
python3 scripts/run_color_sort.py --execute
```

Stay with the robot while it runs. Interrupting Python is not a guaranteed physical stop; use the robot's documented power-stop procedure when necessary. This repository does not autostart motion on boot.

## Simulation

Upstream Poppy software offers simulation tools, but this script requires `poppy.camera.frame` and physical gripper-load feedback. It is not a ready-to-run camera sorting simulation. See [upstream samples](https://github.com/poppy-project/poppy-ergo-jr/tree/master/software/samples) for separate simulator examples.
