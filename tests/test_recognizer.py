import cv2

from core.camera import Camera
from core.hand_detector import HandDetector
from core.gesture_recognizer import GestureRecognizer
from core.gesture_smoother import GestureSmoother

from controllers.gesture_mapper import GestureMapper


camera = Camera()
detector = HandDetector()
recognizer = GestureRecognizer()
smoother = GestureSmoother()
mapper = GestureMapper()


while True:

    success, frame = camera.read()

    if not success:
        break

    hands = detector.get_hands(frame)

    frame = detector.draw(frame, hands)

    if hands:

        gesture = recognizer.recognize(
            hands[0]["landmarks"]
        )

        stable_gesture = smoother.update(gesture)

        if stable_gesture:

            mapper.execute(stable_gesture)

        cv2.putText(
            frame,
            f"Gesture : {gesture}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Stable : {stable_gesture}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2,
        )

    cv2.imshow("AI Universal Media Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()