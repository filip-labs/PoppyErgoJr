# Calibration and troubleshooting

## Review before running

The original script is retained unchanged. Its poses belong to a particular demonstration layout and have not been validated on your hardware by the documentation update.

| Setting | Current implementation | What to check |
| --- | --- | --- |
| Motor speed | 40 for m1–m6 | Suitable speed for your assembly |
| Horizontal mapping | 0–640 px → -30–30 degrees on m1 | Frame size, orientation, reachable workspace |
| Lowering | m3 = -55; retry = -45 | Direction, clearance, object height |
| Lift | m3 = 0 | Clear path before rotation |
| Gripper | m6 = -15 closed; 45 open | Attachment orientation and mechanical limits |
| Drop rotation | m4 = 90 left; -90 right | Both bins reachable without collision |
| Grip heuristic | m6.present_load > 10 | Load units/sign and reliable threshold |
| Base posture | start then immediately stop | Whether this reaches a useful pose on your stack |

The retry comment says “lower further,” but the code changes -55 to -45. Do not assume the comment matches the physical movement. Also, a failed second grasp still proceeds to the lift/drop sequence. Validate these behaviors before relying on the demo.

Begin with an empty gripper and test one pose at a time. Place small red/blue objects on a plain contrasting surface under consistent lighting. Check image orientation and RGB/BGR ordering before tuning HSV ranges. Do not infer a general camera-to-world calibration from the simple horizontal mapping.

## Common problems

| Symptom | Checks |
| --- | --- |
| `poppy.local` cannot be reached | Same network, robot boot, Ethernet link, mDNS support; try the IP address |
| Import error | Run the environment checker in the robot image's Python environment |
| Camera frame missing | Enable/test camera through upstream tools; check wiring and competing processes |
| Serial or motor connection error | Stop other controllers; verify supply, cables, IDs, and upstream initialization |
| Script waits after capturing | Close the matplotlib window; check plotting backend/display availability |
| False red/blue detections | Remove colored background, inspect masks, tune thresholds; no area filter exists yet |
| Wrong pickup position | Check 640-pixel assumption, camera orientation and m1 mapping; y is unused |
| Gripper misses but continues | Current load heuristic and retry do not guarantee successful pickup |

When reporting an issue, include board model, OS image filename, Python version, dependency versions, attachment, camera frame dimensions, and the full traceback. State whether the issue occurred without hardware or during a supervised hardware run.
