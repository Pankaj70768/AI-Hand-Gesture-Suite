"""
camera.py

Camera Management Module
"""

import cv2

from utils.config import *


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)

        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        self.cap.set(cv2.CAP_PROP_FPS, FPS)

    def read(self):

        success, frame = self.cap.read()

        return success, frame

    def release(self):

        self.cap.release()