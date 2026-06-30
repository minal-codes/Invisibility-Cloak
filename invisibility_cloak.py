










import subprocess, sys, importlib.util

REQUIRED = {
    "cv2": "opencv-python",
    "numpy": "numpy",
    "mediapipe": "mediapipe"
}

def _auto_install():
    missing = [
        pkg for mod, pkg in REQUIRED.items()
        if importlib.util.find_spec(mod) is None
    ]

    if missing:
        print(f"\n[AUTO-INSTALL] Installing: {', '.join(missing)}\n")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet"] + missing
        )
        print("[AUTO-INSTALL] Done.\n")

_auto_install()

import cv2
import numpy as np
import time

BANNER = """
Ghost / Invisibility Mode
"""

WINDOW = "Ghost / Invisibility Mode"

def _detect_device():

    def run_calibration():

        cap = cv2.VideoCapture(...)

from engine import (
    BackgroundModel,
    SegmentationEngine,
    HandTracker,
    PortalBox,
    HUD
)

while True:

    ret, frame = cap.read()

    if not ret:
        time.sleep(0.02)
        continue

    # Update FPS
    hud.tick()

    # -------------------------------
    # Segmentation
    # -------------------------------
    seg_mask = seg.get_mask(frame)

    # -------------------------------
    # Hand Tracking
    # -------------------------------
    results = tracker.process(frame)

    info = tracker.get_info(results, w, h)

    # -------------------------------
    # Portal Update
    # -------------------------------
    portal.update(info)
    portal.update_alpha()

    # -------------------------------
    # Render Invisibility
    # -------------------------------
    out = portal.render(
        frame,
        seg_mask,
        bg_model.get(),
        info["all_points"]
    )

    # -------------------------------
    # Draw HUD
    # -------------------------------
    out = hud.draw(
        out,
        portal,
        info
    )

    cv2.imshow(WINDOW, out)

    key = cv2.waitKey(1) & 0xFF

    if key in (ord("q"), 27):
        break
