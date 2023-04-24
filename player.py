import random

class Player:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.num_guesses = 0

    def make_guess(self):
        self.num_guesses += 1
        return random.randint(self.min_num, self.max_num)

    def update_stats(self, guess, result):
        pass

    def update_range(self, guess, feedback):
        while True:
            if feedback == "higher":
                self.min_num = guess + 1
            elif feedback == "lower":
                self.max_num = guess - 1
            guess = self.make_guess()
            feedback = input(f"Is {guess} higher or lower than your number? ")
            if feedback == "correct":
                break
