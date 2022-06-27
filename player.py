# parent Player class #

class Player:

    def __init__(self):
        self.gestures = str["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture()
        self.win_count = 0



