words = ["madrid", "barcelona", "valencia", "sevilla", "bilbao", "zaragoza", "vigo", "pamplona", "murcia", "santander"]
import random as Random

class Game():
    def __init__(self, args):
        self.rWord = args["rWord"]
        self.Lives = args["Lives"]

    def create_string(self):
        self.empty_string = []
        for i in range(len(self.rWord)):
            self.empty_string.append("_")
        self.rWord = list(self.rWord)
    
    def print_string(self, _):
        if "rWord" in _: print(self.rWord)
        if "eWord" in _: print(self.empty_string)
        if "Lives" in _: print(self.Lives)

    def get_guess(self):
        guess = input("Guess letter: ")
        return guess.upper()

    def game_round(self):
        self.print_string("eWord")
        guess = self.get_guess()
        if guess in self.rWord:
            print(f"Letter {guess.upper()} found.")
            index = 0
            for l in self.rWord:
                if self.rWord[index] == guess:
                    self.empty_string[index] = guess.upper()
                index += 1
        else:
            print(f"Letter {guess.upper()} not found.")
            self.Lives -= 1
            self.print_string("Lives")

    def start(self):
        self.create_string()
        while self.Lives > 0 and "_" in self.empty_string:
            self.game_round()
        else:
            if self.Lives <= 0:
                print("No more lives.")
                self.print_string(["rWord", "eWord", "Lives"])
            if "_" not in self.empty_string:
                print("You won!")
                self.print_string("eWord")

game_args = {
    "rWord":words[Random.randint(0, len(words) - 1)].upper(),
    "Lives":10
    }

game = Game(game_args).start()