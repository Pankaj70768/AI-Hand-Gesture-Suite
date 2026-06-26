import cv2

from core.camera import Camera
from core.hand_detector import HandDetector
from core.predictor import GesturePredictor
from controllers.gesture_mapper import GestureMapper


camera = Camera()

detector = HandDetector()

predictor = GesturePredictor()
mapper = GestureMapper()


while True:

    success, frame = camera.read()

    if not success:
        break

    hands = detector.get_hands(frame)

    frame = detector.draw(
        frame,
        hands,
    )

    if hands:

        gesture, confidence = predictor.predict(
            hands[0]["landmarks"]
        )
        print(gesture)
        if confidence > 0.90:
         mapper.execute(gesture)

        cv2.putText(
            frame,
            f"{gesture} ({confidence:.2f})",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    cv2.imshow(
        "ML Gesture Prediction",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()

cv2.destroyAllWindows()