from ai import AI
from human import Human
from time import sleep

class Game:
    def __init__(self):
        self.human_player = human_player
        self.ai_player = ai_player

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print()
        print()
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print()
        sleep(5)
        print("The first to win two rounds is the winner")
        sleep(2)
        print("Please use number keys to enter your selections")
        print(3 * "\n")
        sleep(5)
        print("Scissors cut Paper")
        sleep(1)
        print("Paper covers Rock")
        sleep(1)
        print("Rock crushes Lizard")
        sleep(1)
        print("Lizard poisons Spock")
        sleep(1)
        print("Spock smashes Scissors")
        sleep(1)
        print("Scissors decapitates Lizard")
        sleep(1)
        print("Lizard eats Paper")
        sleep(1)
        print("Paper disproves Spock")
        sleep(1)
        print("Spock vaporizes Rock")
        sleep(1)
        print("Rock crushes Scissors")

    
    


        
