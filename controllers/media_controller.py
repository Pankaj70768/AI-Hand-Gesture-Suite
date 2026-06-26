import keyboard
import time


class MediaController:

    def __init__(self):

        self.last_action = 0
        self.cooldown = 1.2

    def _execute(self, action, message):

        current_time = time.time()

        if current_time - self.last_action < self.cooldown:
            return

        self.last_action = current_time

        keyboard.send(action)

        print(f"[ACTION] {message}")

    def play_pause(self):
        self._execute("play/pause media", "Play / Pause")

    def next_track(self):
        self._execute("next track", "Next Track")

    def previous_track(self):
        self._execute("previous track", "Previous Track")

    def volume_up(self):
        self._execute("volume up", "Volume Up")

    def volume_down(self):
        self._execute("volume down", "Volume Down")

    def mute(self):
        self._execute("volume mute", "Mute")