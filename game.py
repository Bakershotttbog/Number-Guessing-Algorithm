import random

class Game:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.answer = random.randint(min_num, max_num)
        self.num_guesses = 0

    def check_guess(self, guess):
        self.num_guesses += 1
        if guess < self.answer:
            return "Too low"
        elif guess > self.answer:
            return "Too high"
        else:
            return "Correct!"

    def is_over(self):
        return self.num_guesses > 0 and self.check_guess(self.answer) == "Correct!"
