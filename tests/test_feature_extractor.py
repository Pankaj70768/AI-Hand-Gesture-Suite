from core.camera import Camera
from core.hand_detector import HandDetector
from core.feature_extractor import FeatureExtractor

import cv2

camera = Camera()
detector = HandDetector()

while True:

    success, frame = camera.read()

    if not success:
        break

    hands = detector.get_hands(frame)

    if hands:

        features = FeatureExtractor.extract_features(
            hands[0]["landmarks"]
        )

        cv2.putText(
            frame,
            f"Features : {len(features)}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    frame = detector.draw(frame, hands)

    cv2.imshow("Feature Extractor", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()