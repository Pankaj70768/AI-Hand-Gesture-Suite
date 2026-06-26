"""
Feature Extraction Module
Converts MediaPipe landmarks into ML feature vectors.
"""

from typing import List
import math


class FeatureExtractor:

    @staticmethod
    def normalize_landmarks(landmarks: List[tuple]) -> List[float]:
        """
        Normalize landmarks using wrist as origin.
        """

        if not landmarks:
            return []

        wrist_x, wrist_y, wrist_z = landmarks[0]

        normalized = []

        for x, y, z in landmarks:
            normalized.extend([
                x - wrist_x,
                y - wrist_y,
                z - wrist_z
            ])

        return normalized

    @staticmethod
    def calculate_distance(p1, p2):

        return math.sqrt(
            (p1[0]-p2[0])**2 +
            (p1[1]-p2[1])**2
        )

    @staticmethod
    def extract_features(landmarks):

        features = FeatureExtractor.normalize_landmarks(landmarks)

        # Thumb - Index
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[4],
                landmarks[8]
            )
        )

        # Thumb - Middle
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[4],
                landmarks[12]
            )
        )

        # Thumb - Ring
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[4],
                landmarks[16]
            )
        )

        # Thumb - Pinky
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[4],
                landmarks[20]
            )
        )

        # Index - Middle
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[8],
                landmarks[12]
            )
        )

        # Middle - Ring
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[12],
                landmarks[16]
            )
        )

        # Ring - Pinky
        features.append(
            FeatureExtractor.calculate_distance(
                landmarks[16],
                landmarks[20]
            )
        )

        return features