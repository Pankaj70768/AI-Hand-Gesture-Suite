import cv2

from core.camera import Camera


def run_camera_test():

    camera = Camera()

    while True:

        success, frame = camera.read()

        if not success:
            print("Unable to access camera.")
            break

        cv2.putText(
            frame,
            "Camera Test",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Camera Test", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_camera_test()