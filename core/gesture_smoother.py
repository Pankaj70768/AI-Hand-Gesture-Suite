import time


class GestureSmoother:

    def __init__(self, hold_time=0.5):

        self.hold_time = hold_time

        self.current_gesture = None
        self.start_time = None

        self.last_executed = None

    def update(self, gesture):

        # No hand detected
        if gesture is None:
            self.current_gesture = None
            self.start_time = None
            self.last_executed = None
            return None

        current_time = time.time()

        # New gesture detected
        if gesture != self.current_gesture:

            self.current_gesture = gesture
            self.start_time = current_time

            return None

        # Wait until gesture is stable
        if current_time - self.start_time < self.hold_time:
            return None

        # Already executed
        if gesture == self.last_executed:
            return None

        self.last_executed = gesture

        return gesture