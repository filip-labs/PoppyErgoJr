"""Synthetic images exercise the actual vision helpers, without Pypot."""

import unittest

import cv2
import numpy as np

from poppy_sort.vision import centroid, color_masks, image_x_to_motor


class VisionTests(unittest.TestCase):
    def test_rgb_masks_and_background(self):
        frame = np.array([[[255, 0, 0], [0, 0, 255], [0, 255, 0], [0, 0, 0]]], dtype=np.uint8)
        red, blue = color_masks(frame)
        np.testing.assert_array_equal(red, [[255, 0, 0, 0]])
        np.testing.assert_array_equal(blue, [[0, 255, 0, 0]])

    def test_hue_wraparound_remains_excluded(self):
        hsv = np.array([[[179, 255, 255]]], dtype=np.uint8)
        red, blue = color_masks(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))
        self.assertFalse(red.any())
        self.assertFalse(blue.any())

    def test_rectangle_centroid(self):
        contour = np.array([[[2, 4]], [[10, 4]], [[10, 12]], [[2, 12]]], dtype=np.int32)
        self.assertEqual(centroid(contour), (6, 8))

    def test_zero_area_centroid(self):
        self.assertEqual(centroid(np.array([[[3, 7]]], dtype=np.int32)), (0, 0))

    def test_mapping_endpoints_and_midpoint(self):
        for pixel, angle in ((0, -30), (320, 0), (640, 30)):
            with self.subTest(pixel=pixel):
                self.assertEqual(image_x_to_motor(pixel), angle)

    def test_mapping_is_not_a_safety_clamp(self):
        self.assertEqual(image_x_to_motor(1280), 90)
