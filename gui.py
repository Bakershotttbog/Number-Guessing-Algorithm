import tkinter as tk
from game import Game
from player import Player

class NumberGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        # create the game and player objects
        self.game = Game(1, 1000)
        self.player = Player(self.game.min_num, self.game.max_num)

        # create the GUI elements
        self.title_label = tk.Label(master, text="Think of a number between 1 and 1000")
        self.title_label.pack(pady=10)

        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()

        self.higher_button = tk.Button(master, text="Higher", command=self.update_range_higher)
        self.higher_button.pack(pady=10)

        self.lower_button = tk.Button(master, text="Lower", command=self.update_range_lower)
        self.lower_button.pack(pady=10)

        self.correct_button = tk.Button(master, text="Correct", command=self.check_guess)
        self.correct_button.pack(pady=10)

        # start the game loop
        self.play_game()

    def play_game(self):
        while not self.game.is_over():
            guess = self.player.make_guess()
            self.guess_label.config(text=f"Computer's guess: {guess}")
            self.master.update()
            result = self.game.check_guess(guess)
            self.player.update_stats(guess, result)
            if result == "Correct!":
                num_guesses = self.player.num_guesses
                message = f"The computer guessed the number in {num_guesses} tries!"
                tk.messagebox.showinfo("Game Over", message)
                self.master.quit()
            else:
                self.update_buttons()

    def update_buttons(self):
        if self.player.min_num == self.player.max_num:
            self.higher_button.config(state="disabled")
            self.lower_button.config(state="disabled")
        else:
            self.higher_button.config(state="normal")
            self.lower_button.config(state="normal")

    def update_range_higher(self):
        self.player.update_range(self.player.make_guess(), "Too low")
        self.update_buttons()

    def update_range_lower(self):
        self.player.update_range(self.player.make_guess(), "Too high")
        self.update_buttons()

    def check_guess(self):
        guess = self.player.make_guess()
        result = self.game.check_guess(guess)
        self.player.update_stats(guess, result)
        if result == "Correct!":
            num_guesses = self.player.num_guesses
            message = f"The computer guessed the number in {num_guesses} tries!"
            tk.messagebox.showinfo("Game Over", message)
            self.master.quit()
        else:
            self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop()