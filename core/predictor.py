"""
ML Gesture Predictor
Author : Pankaj
"""

import joblib
import numpy as np


class GesturePredictor:

    def __init__(self):

        self.model = joblib.load(
            "trained_models/gesture_model.pkl"
        )

        self.encoder = joblib.load(
            "trained_models/label_encoder.pkl"
        )

    def preprocess(self, landmarks):

        data = []

        for x, y, z in landmarks:

            data.extend([
                x,
                y,
                z,
            ])

        return np.array(data).reshape(1, -1)

    def predict(self, landmarks):

        sample = self.preprocess(
            landmarks
        )

        prediction = self.model.predict(
            sample
        )[0]

        probabilities = self.model.predict_proba(
            sample
        )[0]

        confidence = np.max(
            probabilities
        )

        gesture = self.encoder.inverse_transform(
            [prediction]
        )[0]

        return gesture, confidence