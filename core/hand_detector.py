"""
Professional Hand Detector
AI Hand Gesture Recognition Suite
Author: Pankaj
"""

from typing import List, Dict, Optional

import cv2
import mediapipe as mp

from utils.config import *


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.mp_draw = mp.solutions.drawing_utils

        self.mp_styles = mp.solutions.drawing_styles

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE,
        )

    def process(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return self.hands.process(rgb)

    def get_hands(self, frame):

        results = self.process(frame)

        hands = []

        if not results.multi_hand_landmarks:
            return hands

        h, w, _ = frame.shape

        for index, hand_landmarks in enumerate(results.multi_hand_landmarks):

            landmark_list = []

            x_points = []

            y_points = []

            for landmark in hand_landmarks.landmark:

                x = int(landmark.x * w)

                y = int(landmark.y * h)

                z = landmark.z

                landmark_list.append((x, y, z))

                x_points.append(x)

                y_points.append(y)

            x_min = min(x_points)

            x_max = max(x_points)

            y_min = min(y_points)

            y_max = max(y_points)

            bbox = (
                x_min,
                y_min,
                x_max - x_min,
                y_max - y_min,
            )

            hand_label = "Unknown"

            if results.multi_handedness:

                hand_label = (
                    results
                    .multi_handedness[index]
                    .classification[0]
                    .label
                )

            hands.append(
                {
                    "id": index,
                    "label": hand_label,
                    "bbox": bbox,
                    "landmarks": landmark_list,
                    "raw": hand_landmarks,
                }
            )

        return hands

    def draw(self, frame, hands):

        for hand in hands:

            self.mp_draw.draw_landmarks(
                frame,
                hand["raw"],
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_styles.get_default_hand_landmarks_style(),
                self.mp_styles.get_default_hand_connections_style(),
            )

            x, y, w, h = hand["bbox"]

            cv2.rectangle(
                frame,
                (x - 15, y - 15),
                (x + w + 15, y + h + 15),
                GREEN,
                2,
            )

            cv2.putText(
                frame,
                hand["label"],
                (x, y - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                YELLOW,
                2,
            )

        return frame