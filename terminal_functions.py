def yellow_text(text: str) -> str:
    return f"\033[38;2;255;255;0m{text} \033[38;5;255;255;255m"


def green_text(text: str) -> str:
    return f"\033[38;2;0;255;0m{text} \033[38;5;255;255;255m"


def gray_text(text: str) -> str:
    return f"\033[38;2;100;100;150m{text} \033[38;5;255;255;255m"


def white_text(text: str) -> str:
    return f"\033[38;2;255;255;255m{text} \033[38;5;255;255;255m"


def build_output_string(guess_string: str, nums: list[int]) -> str:
    r_string = ""
    for ind, letter in enumerate(guess_string):
        if nums[ind] == 0:
            r_string += gray_text(letter) + " "
        elif nums[ind] == 1:
            r_string += green_text(letter) + " "
        elif nums[ind] == 2:
            r_string += yellow_text(letter) + " "
    return r_string


def build_letter_list(guessed: dict[str: int]) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    r = ""
    for letter in alphabet:
        if letter in guessed:
            if guessed[letter] == 0:
                r += gray_text(letter)
            elif guessed[letter] == 1:
                r += green_text(letter)
            elif guessed[letter] == 2:
                r += yellow_text(letter)
        else:
            r += letter + " "
    return r


def build_output_stats(stats_dict: dict[int:int]) -> str:
    block_pixel = "|"
    played = sum(stats_dict.values())
    return_string = f"\nPlayed:\t{played}\nWon:\t{played - stats_dict[0]}\n\n"
    for num_guesses in sorted(stats_dict):
        if num_guesses == 0:
            return_string += f"X\t{block_pixel * stats_dict[num_guesses]}\n"
        else:
            return_string += f"{num_guesses}\t{block_pixel * stats_dict[num_guesses]}\n"
    return return_string


def build_opening_scene() -> str:
    block_pixel = u"\u2586"
    return_string = "\n"
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for line in array:
        return_string += "\t\t\t\t\t\t"
        for cell in line:
            if cell == 1:
                return_string += white_text(block_pixel)
            else:
                return_string += green_text(block_pixel)
        return_string += "\n"
    return_string += "\n\n\t\t\t\t" + green_text("Terminle: A terminal-based Wordle game")
    return return_string
