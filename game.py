import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []
        self.max_guesses = 6

    def print_history(self):
        print("\nGuess history:")
        for guess, feedback in self.history:
            print(f"{guess}  {' '.join(feedback)}")

    def run(self):
        print(f"\nWordle — {self.length} letters, 6 guesses.")
        print("Enter q to quit.")

        while len(self.history) < self.max_guesses:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("\nGame quit.")
                self.print_history()
                print(f"Target word: {self.target}")
                print(f"Guesses used: {len(self.history)}/{self.max_guesses}")
                return

            if len(guess) != self.length or not guess.isalpha():
                print(f"Enter a valid {self.length}-letter word.")
                continue

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            self.print_history()

            if guess == self.target:
                print(f"\nSolved in {len(self.history)}/{self.max_guesses} guesses!")
                return

        print("\nGame over.")
        print(f"The word was: {self.target}")
        print(f"Guesses used: {len(self.history)}/{self.max_guesses}")