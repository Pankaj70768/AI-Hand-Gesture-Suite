import time

from core.gesture_smoother import GestureSmoother

smoother = GestureSmoother()

print("=" * 50)
print("GESTURE SMOOTHER TEST")
print("=" * 50)

while True:

    gesture = input("Gesture (or exit): ").strip()

    if gesture == "exit":
        break

    result = smoother.update(gesture)

    if result:
        print(f"✅ Triggered : {result}")

    else:
        print("Waiting...")

    time.sleep(0.2)