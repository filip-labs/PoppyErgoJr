"""Run the real legacy script with fake hardware, display and clock."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
import sys
import types
import unittest
from unittest.mock import Mock, patch

import numpy as np


class SortingTests(unittest.TestCase):
    def run_sort(self, frame, load=20):
        robot = Mock()
        robot.m6.present_load = load
        camera = Mock()
        type(camera).frame = property(lambda _: next(frames))
        frames = iter([frame, np.zeros_like(frame)])
        robot.camera = camera
        creatures = types.ModuleType("pypot.creatures")
        creatures.PoppyErgoJr = Mock(return_value=robot)
        pypot = types.ModuleType("pypot")
        pypot.creatures = creatures
        plotting = types.ModuleType("matplotlib.pyplot")
        plotting.imshow = Mock()
        plotting.show = Mock()
        matplotlib = types.ModuleType("matplotlib")
        matplotlib.pyplot = plotting
        with (
            patch.dict(
                sys.modules,
                {
                    "pypot": pypot,
                    "pypot.creatures": creatures,
                    "matplotlib": matplotlib,
                    "matplotlib.pyplot": plotting,
                },
            ),
            patch("time.sleep"),
            redirect_stdout(io.StringIO()),
        ):
            runpy.run_path(
                str(Path(__file__).resolve().parents[1] / "ColorSort"), run_name="__main__"
            )
        creatures.PoppyErgoJr.assert_called_once_with()
        return robot

    def test_red_takes_priority_over_blue(self):
        frame = np.zeros((20, 40, 3), dtype=np.uint8)
        frame[2:12, 2:12] = [255, 0, 0]
        frame[2:12, 22:32] = [0, 0, 255]
        robot = self.run_sort(frame)
        self.assertEqual(robot.m4.goal_position, 90)
        self.assertEqual(robot.m6.goal_position, 45)
        self.assertEqual(robot.m3.goal_position, 0)
        self.assertEqual(robot.m1.moving_speed, 40)
        self.assertAlmostEqual(robot.m1.goal_position, (6 / 640.0) * 60 - 30)

    def test_blue_uses_right_drop(self):
        frame = np.zeros((20, 20, 3), dtype=np.uint8)
        frame[2:12, 2:12] = [0, 0, 255]
        self.assertEqual(self.run_sort(frame).m4.goal_position, -90)

    def test_no_color_has_no_pickup_or_drop(self):
        robot = self.run_sort(np.zeros((20, 20, 3), dtype=np.uint8))
        self.assertNotIn("goal_position", vars(robot.m4))
        self.assertNotIn("goal_position", vars(robot.m6))
        robot.base_posture.start.assert_called_once_with()

    def test_failed_grasp_still_drops_existing_limitation(self):
        frame = np.zeros((20, 20, 3), dtype=np.uint8)
        frame[2:12, 2:12] = [255, 0, 0]
        self.assertEqual(self.run_sort(frame, load=0).m4.goal_position, 90)

    def test_largest_red_contour_controls_mapping(self):
        frame = np.zeros((30, 50, 3), dtype=np.uint8)
        frame[2:5, 2:5] = [255, 0, 0]
        frame[10:21, 30:41] = [255, 0, 0]
        robot = self.run_sort(frame)
        self.assertAlmostEqual(robot.m1.goal_position, (35 / 640.0) * 60 - 30)
