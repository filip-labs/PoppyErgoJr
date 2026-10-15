"""Image processing only: importing this module never initializes hardware.

Thresholds and the 640-pixel mapping preserve the original demo assumptions.
They are not a calibrated camera-to-world transform.
"""

import cv2
import numpy as np


def color_masks(rgb_frame):
    """Return red and blue masks using the original RGB/HSV thresholds."""
    hsv = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2HSV)
    red = cv2.inRange(hsv, np.array([0, 120, 70]), np.array([10, 255, 255]))
    blue = cv2.inRange(hsv, np.array([94, 80, 2]), np.array([126, 255, 255]))
    return red, blue


def centroid(contour):
    """Return integer image coordinates, or (0, 0) for zero-area contours."""
    moments = cv2.moments(contour)
    if moments["m00"] != 0:
        return int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"])
    return 0, 0


def image_x_to_motor(cx):
    """Preserve the legacy linear mapping; no clamping or limit validation."""
    return (cx / 640.0) * 60 - 30
