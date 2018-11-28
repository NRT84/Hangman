import random


class Configuration:

    def __init__(self, game_data):
        self.game_data = game_data
        self.difficulty_number = None
        self.answer = None
        self.retries = None
        self.used_words = None
        self.is_guessed = None
        self.candidate = ""

    def setup(self):
        self.init_difficulty_number()
        self.init_answer()
        self.init_candidate()
        self.init_retries()
        self.init_used_words()
        self.init_is_guessed()

    def init_difficulty_number(self):
        self.difficulty_number = int(input("Select difficulty level (input number):\n1. Easy\n2. Normal\n3. Hard\n\n"))
        if self.difficulty_number not in range(1, 4):
            raise ValueError("Difficulty should be of value 1, 2 or 3")

    def init_answer(self):
        self.answer = random.choice(self.game_data.words[self.difficulty_number])

    def init_candidate(self):
        for letter in self.answer:
            if not(letter.isspace()):
                self.candidate += "_"
            else:
                self.candidate += letter

    def init_retries(self):
        self.retries = self.game_data.retries[self.difficulty_number]

    def init_used_words(self):
        self.used_words = []

    def init_is_guessed(self):
        self.is_guessed = False
