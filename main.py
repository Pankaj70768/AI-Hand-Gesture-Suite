import cv2
import time

from core.hand_detector import HandDetector


cap = cv2.VideoCapture(0)

detector = HandDetector()

previous_time = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame, results = detector.detect_hands(frame)

    frame = detector.draw_landmarks(frame, results)

    landmarks = detector.get_landmarks(frame, results)

    frame = detector.draw_bounding_box(frame, landmarks)

    current_time = time.time()

    fps = 1 / (current_time - previous_time) if previous_time else 0

    previous_time = current_time

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2,
    )

    cv2.imshow("AI Hand Gesture Suite", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()