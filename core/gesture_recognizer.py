class GestureRecognizer:

    TIP_IDS = [4, 8, 12, 16, 20]

    def recognize(self, landmarks):

        if not landmarks:
            return None

        fingers = []

        # Thumb
        if landmarks[4][0] > landmarks[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Index
        for tip in [8, 12, 16, 20]:

            if landmarks[tip][1] < landmarks[tip - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Open Palm
        if fingers == [1, 1, 1, 1, 1]:
            return "open_palm"

        # Fist
        if fingers == [0, 0, 0, 0, 0]:
            return "fist"

        # Thumb Up
        if fingers == [1, 0, 0, 0, 0]:
            return "thumb_up"

        # Peace
        if fingers == [0, 1, 1, 0, 0]:
            return "peace"

        return None