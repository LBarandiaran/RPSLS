from player import Player
from time import sleep

class Human(Player):

    def __init__(self,name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = input("Please choose your gesture: ")
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")