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