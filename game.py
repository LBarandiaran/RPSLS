from readline import replace_history_item
from ai import AI
from human import Human
from time import sleep

class Game:
    def __init__(self):
        self.player_one = player_one
        self.player_two = player_two

    def run_game(self):
        self.display_welcome()
        self.game_format()
        self.battle_phase()
        self.display_winner()
        self.replay()

    def display_welcome(self):
        print()
        print()
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print()
        sleep(4)
        print("The first to win two rounds is the winner")
        sleep(2)
        print("Please use number keys to enter your selections")
        print(3 * "\n")
        sleep(4)
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

    
## Game Format method which includes logic for bad user input ##

    def game_format(self):
        self.game_format = int(input("How many players? 1, 2, or 3 for an all AI battle"))
        if self.game_format == 1:
            self.player_one = "Player One"
            self.player_two = "AI"          

        elif self.game_format == 2:
            self.player_one = "Player One"
            self.player_two = "Player Two"

        elif self.game_format == 3:
            self.player_one = "AI One"
            self.player_two = "AI Two"

        else print("Please enter a number as instructed")

    

    def battle_phase(self):
        pass

    def display_winner(self):
        if self.player_one.score == 2:
            print("Player One is the winner!")
        elif self.player_two.score == 2:
            print("Player Two is the winner!")




        


        


        
