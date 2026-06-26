"""
config.py
-----------------------------------
Global configuration for
AI Hand Gesture Recognition Suite
"""

from pathlib import Path

# ==============================
# PROJECT PATHS
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"
RAW_DATASET_DIR = DATASET_DIR / "raw"
LANDMARK_DATASET_DIR = DATASET_DIR / "landmarks"

MODEL_DIR = BASE_DIR / "model"

LOG_DIR = BASE_DIR / "logs"

RESULT_DIR = BASE_DIR / "results"

ASSET_DIR = BASE_DIR / "assets"


# ==============================
# CAMERA SETTINGS
# ==============================

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

FPS = 30


# ==============================
# HAND DETECTION
# ==============================

MAX_HANDS = 1

DETECTION_CONFIDENCE = 0.70

TRACKING_CONFIDENCE = 0.70


# ==============================
# DATASET
# ==============================

SAMPLES_PER_GESTURE = 500


# ==============================
# GESTURES
# ==============================

GESTURES = {

    ord("1"): "open_palm",

    ord("2"): "fist",

    ord("3"): "thumb_up",

    ord("4"): "thumb_down",

    ord("5"): "ok",

    ord("6"): "peace",

    ord("7"): "swipe_left",

    ord("8"): "swipe_right",

}


# ==============================
# UI COLORS
# ==============================

GREEN = (0,255,0)

RED = (0,0,255)

BLUE = (255,0,0)

YELLOW = (0,255,255)

WHITE = (255,255,255)


# ==============================
# FONT
# ==============================

FONT_SCALE = 0.8

FONT_THICKNESS = 2
