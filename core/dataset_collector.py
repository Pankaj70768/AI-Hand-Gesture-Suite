import os
import csv
import cv2
import time

from core.camera import Camera
from core.hand_detector import HandDetector


class DatasetCollector:

    def __init__(self):

        self.camera = Camera()
        self.detector = HandDetector()

        self.current_label = None
        self.sample_count = 0

        self.auto_save = False
        self.last_save_time = 0
        self.save_interval = 0.10

        self.dataset_path = "dataset/landmarks"
        os.makedirs(self.dataset_path, exist_ok=True)

        self.csv_path = os.path.join(
            self.dataset_path,
            "gesture_dataset.csv"
        )

        self.create_csv()

    def create_csv(self):

        if os.path.exists(self.csv_path):
            return

        header = []

        for i in range(21):
            header.extend([
                f"x{i}",
                f"y{i}",
                f"z{i}"
            ])

        header.append("label")

        with open(
            self.csv_path,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)
            writer.writerow(header)

    def save_sample(self, landmarks):

        row = []

        for x, y, z in landmarks:
            row.extend([x, y, z])

        row.append(self.current_label)

        with open(
            self.csv_path,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)
            writer.writerow(row)

        self.sample_count += 1
        print(f"Saved : {self.sample_count}")

    def run(self):

        print("=" * 50)
        print("AI HAND GESTURE DATASET COLLECTOR")
        print("=" * 50)

        print("""
1 -> open_palm
2 -> fist
3 -> thumb_up
4 -> thumb_down
5 -> peace
6 -> ok
7 -> swipe_left
8 -> swipe_right

S -> Save Current Sample
Q -> Quit
""")

        labels = {
            ord("1"): "open_palm",
            ord("2"): "fist",
            ord("3"): "thumb_up",
            ord("4"): "thumb_down",
            ord("5"): "peace",
            ord("6"): "ok",
            ord("7"): "swipe_left",
            ord("8"): "swipe_right",
        }

        while True:

            success, frame = self.camera.read()

            if not success:
                break

            hands = self.detector.get_hands(frame)

            frame = self.detector.draw(frame, hands)

            if self.current_label:

                cv2.putText(
                    frame,
                    f"Label : {self.current_label}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

            cv2.putText(
                frame,
                f"Samples : {self.sample_count}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 0),
                2,
            )

            cv2.imshow(
                "Dataset Collector",
                frame,
            )

            key = cv2.waitKey(1) & 0xFF
            current_time = time.time()

            if (
                self.auto_save
                and hands
                and self.current_label
                and current_time - self.last_save_time > self.save_interval
            ):
                

                self.save_sample(
                    hands[0]["landmarks"]
                )

                self.last_save_time = current_time
            

            if key in labels:

                self.current_label = labels[key]
                print(f"Current Label : {self.current_label}")

            elif key == ord("s"):

                if hands and self.current_label:

                    self.save_sample(
                        hands[0]["landmarks"]
                    )

                    print(
                        f"Saved : {self.sample_count}"
                    )

            elif key == ord("a"):

                self.auto_save = not self.auto_save

                print(
                    f"Auto Save : {'ON' if self.auto_save else 'OFF'}"
                )

            elif key == ord("q"):
                break
    
        self.camera.release()
        cv2.destroyAllWindows()