import opentdb


class Configuration:

    def __init__(self, game_data):
        self.game_data = game_data
        self.tdb = opentdb.Opentdb()
        self.difficulty = None
        self.answer = None
        self.retries = None
        self.used_words = None
        self.is_guessed = None
        self.candidate = ""

    def setup(self):
        self.init_difficulty()
        self.init_answer()
        self.init_candidate()
        self.init_retries()
        self.init_used_words()
        self.init_is_guessed()

    def init_difficulty(self):
        self.difficulty = int(input("Select difficulty level (input number):\n1. Easy\n2. Medium\n3. Hard\n\n"))
        if self.difficulty not in range(1, 4):
            raise ValueError("Difficulty should be of value 1, 2 or 3")

    def init_answer(self):
        trivia_item = self.tdb.get_trivia_item(9, self.game_data.difficulty[self.difficulty])
        self.answer = trivia_item.answer
        print(trivia_item.question)

    def init_candidate(self):
        for letter in self.answer:
            if not(letter.isspace()):
                self.candidate += "_"
            else:
                self.candidate += letter

    def init_retries(self):
        self.retries = self.game_data.retries[self.difficulty]

    def init_used_words(self):
        self.used_words = []

    def init_is_guessed(self):
        self.is_guessed = False
