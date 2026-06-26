from controllers.gesture_mapper import GestureMapper

mapper = GestureMapper()

print("=" * 50)
print("AI UNIVERSAL MEDIA CONTROLLER")
print("=" * 50)

while True:

    print("""
Available Gestures

open_palm
thumb_up
thumb_down
peace
fist
mute

exit
""")

    gesture = input("Gesture : ").strip()

    if gesture == "exit":
        break

    mapper.execute(gesture)