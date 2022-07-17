from word import Word
from terminal_functions import build_output_string, build_letter_list, build_output_stats, build_opening_scene
from random import choice


class Terminle(object):
    def __init__(self, guesses=6, word_length=5):
        self.word_length = word_length
        self.word = None
        self.wordlist = []
        self.guesses = guesses
        self.stats = {num_guesses: 0 for num_guesses in range(guesses + 1)}
        self.guess_list = []

    def get_word_list(self, input_file="words.txt") -> None:
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        with open(input_file) as f:
            word_database = f.readlines()
            word_database = [word[:-1] for word in word_database]
            for word in word_database:
                if len(word) == self.word_length and word[0] in alphabet:
                    self.wordlist.append(word.lower())
        assert len(self.wordlist) > 0

    def play(self) -> None:
        print("\n" + "_" * 100 + "\n\n" + "\t\t\t\t\t\t Word: \t" + "_ " * self.word_length + "\n")
        self.word = Word(choice(self.wordlist))
        guess_number = 0
        won = False
        self.guess_list = []
        while guess_number < self.guesses:
            guess = input("Enter a guess: ")
            word_tags = self.word.compare(guess)
            if guess not in self.wordlist:
                print("Your guess is not a valid word.")
                word_tags = []
            if word_tags:
                guess_string = build_output_string(guess, word_tags)
                self.guess_list.append(guess_string)
                print(guess_string)
                if guess == self.word.get_word():
                    print(f"Congratulations! You got the answer in {guess_number + 1} tries!")
                    won = True
                    self.stats[guess_number + 1] += 1
                    break
                guess_str = build_letter_list(self.word.get_guessed())
                guess_number += 1
                print(f"Guessed Letters: \t{guess_str}\nYou have {self.guesses - guess_number} guesses remaining")
                print("\033[38;5;255;255;255m_" * 100)
        if not won:
            print(f"You lost! The word was {self.word.get_word()}")
            self.stats[0] += 1

    def post_game(self, recursed=False) -> bool:
        if not recursed:
            for guess in self.guess_list:
                print(guess)
        response = input("Play again (y/n)?\t")
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response. Enter either y or n.")
            return self.post_game(recursed=False)

    def opening_response(self, recursed=False) -> bool:
        if not recursed:
            print(build_opening_scene())
        response = input("Would you like to play Terminle?\t")
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response. Enter either y or n.")
            return self.post_game(recursed=False)


if __name__ == "__main__":
    game = Terminle()
    game.get_word_list()
    play_again = True
    print(build_opening_scene())
    while play_again:
        game.play()
        play_again = game.post_game()
        if not play_again:
            break
    print(build_output_stats(game.stats))
