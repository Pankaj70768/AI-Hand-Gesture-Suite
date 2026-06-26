from controllers.media_controller import MediaController


class GestureMapper:

    def __init__(self):

        self.media = MediaController()

    def execute(self, gesture):

        gesture = gesture.lower()

        if gesture == "open_palm":
            self.media.play_pause()

        elif gesture == "thumb_up":
            self.media.volume_up()

        elif gesture == "thumb_down":
            self.media.volume_down()

        elif gesture == "peace":
            self.media.next_track()

        elif gesture == "fist":
            self.media.previous_track()

        elif gesture == "ok":
            self.media.mute()

        else:
            print(f"[INFO] Unknown Gesture : {gesture}")