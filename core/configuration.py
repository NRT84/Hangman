from colorama import init
from termcolor import colored


class Configuration:

    def __init__(self, game_data, open_tdb):
        init()
        self.game_data = game_data
        self.tdb = open_tdb
        self.category = None
        self.difficulty = None
        self.question = None
        self.answer = None
        self.retries_config = None
        self.retries = None
        self.used_words = None
        self.is_guessed = None
        self.candidate = ""
        self.setup()

    def setup(self):
        self.init_category()
        self.init_difficulty()
        self.init_trivia_item()
        self.init_candidate()
        self.retries_config = {1: 10, 2: 7, 3: 4}
        self.init_retries(self.retries_config, self.difficulty)
        self.init_used_words()
        self.init_is_guessed()

    def init_category(self):
        print(f"Select category (input number):\n{self.game_data.categories[1].description}\n{self.game_data.categories[2].description}\n"
              f"{self.game_data.categories[3].description}\n{self.game_data.categories[4].description}\n"
              f"{self.game_data.categories[5].description}\n{self.game_data.categories[6].description}\n"
              f"{self.game_data.categories[7].description}\n{self.game_data.categories[8].description}\n"
              f"{self.game_data.categories[9].description}\n{self.game_data.categories[10].description}\n"
              f"{self.game_data.categories[11].description}\n{self.game_data.categories[12].description}\n"
              f"{self.game_data.categories[13].description}\n{self.game_data.categories[14].description}\n"
              f"{self.game_data.categories[15].description}\n{self.game_data.categories[16].description}\n"
              f"{self.game_data.categories[17].description}\n{self.game_data.categories[18].description}\n"
              f"{self.game_data.categories[19].description}\n\n")

        option = 0
        while option not in range(1, 20):
            try:
                option = int(input("Your choice: "))
                if option not in range(1, 20):
                    raise ValueError()
            except ValueError:
                print("Category should be a value between 1-19 (are you deliberately trying to crash the game?)\n")
        self.category = option

    def init_difficulty(self):
        print("Select difficulty level (input number):\n1. Easy\n2. Medium\n3. Hard\n\n")
        option = 0
        while option not in range(1, 4):
            try:
                option = int(input("Your choice: "))
                if option not in range(1, 4):
                    raise ValueError
            except ValueError:
                print("Difficulty should be a value between 1-3 (stop it..)")
        self.difficulty = option

    def init_trivia_item(self):
        trivia_item = self.tdb.get_trivia_item(self.game_data.categories[self.category].opentdb_number,
                                               self.game_data.difficulties[self.difficulty])
        self.question = f"Question: {colored(trivia_item.question, 'yellow')}"
        self.answer = trivia_item.answer

    def init_candidate(self):
        for letter in self.answer:
            if not (letter.isspace()):
                self.candidate += "_"
            else:
                self.candidate += letter

    def init_retries(self, retries_config, difficulty):
        self.retries = retries_config[difficulty]

    def init_used_words(self):
        self.used_words = []

    def init_is_guessed(self):
        self.is_guessed = False
