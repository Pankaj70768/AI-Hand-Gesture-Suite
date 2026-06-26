import cv2

from core.camera import Camera
from core.hand_detector import HandDetector
from utils.config import GREEN   # <-- missing import

camera = Camera()
detector = HandDetector()

while True:

    success, frame = camera.read()

    if not success:
        break

    hands = detector.get_hands(frame)

    frame = detector.draw(frame, hands)

    cv2.putText(
        frame,
        f"Hands : {len(hands)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        GREEN,
        2,
    )

    cv2.imshow("Hand Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()