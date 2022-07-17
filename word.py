class Word(object):
    def __init__(self, string) -> None:
        self.word = string
        self.length = len(string)
        self.letter_pos = {}
        for ind, x in enumerate(string):
            if x not in self.letter_pos:
                self.letter_pos[x] = set()
            self.letter_pos[x].add(ind)
        self.guessed = {}

    def compare(self, string) -> list[int]:
        try:
            assert (len(string) == self.length) is True
        except AssertionError:
            print(f"Inputted word ({string}) was not correct length.")
            return []
        res = [0 for _ in range(self.length)]
        guess_map = {}
        for ind, x in enumerate(string):
            if x not in guess_map:
                guess_map[x] = set()
            guess_map[x].add(ind)

        for x in guess_map:
            s1 = set(guess_map[x])
            s2 = set(self.letter_pos[x]) if x in self.letter_pos else set()
            inter = s1.intersection(s2)
            num_yellow_letters = min(len(s1), len(s2)) - len(inter)
            for q in inter:
                res[q] = 1
                self.guessed[x] = 1
            if num_yellow_letters > 0:
                for y in s1:
                    if y not in inter:
                        res[y] = 2
                        if x not in self.guessed:
                            self.guessed[x] = 2
                        num_yellow_letters -= 1
                    if num_yellow_letters == 0:
                        break
            if x not in self.guessed:
                self.guessed[x] = 0
        return res

    def get_word(self) -> str:
        return self.word

    def get_guessed(self):
        return self.guessed
