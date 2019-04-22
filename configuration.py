import opentdb
from colorama import init
from termcolor import colored


class Configuration:

    def __init__(self, game_data):
        init()
        self.game_data = game_data
        self.tdb = opentdb.Opentdb()
        self.category = None
        self.difficulty = None
        self.question = None
        self.answer = None
        self.retries = None
        self.used_words = None
        self.is_guessed = None
        self.candidate = ""

    def setup(self):
        self.init_category()
        self.init_difficulty()
        self.init_trivia_item()
        self.init_candidate()
        self.init_retries()
        self.init_used_words()
        self.init_is_guessed()

    def init_category(self):
        print("Select category (input number):\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n"
                            "{10}\n{11}\n{12}\n{13}\n""{14}\n{15}\n{16}\n{17}\n{18}\n\n"
                            .format(self.game_data.categories[1].description, self.game_data.categories[2].description,
                            self.game_data.categories[3].description, self.game_data.categories[4].description,
                            self.game_data.categories[5].description, self.game_data.categories[6].description,
                            self.game_data.categories[7].description, self.game_data.categories[8].description,
                            self.game_data.categories[9].description, self.game_data.categories[10].description,
                            self.game_data.categories[11].description, self.game_data.categories[12].description,
                            self.game_data.categories[13].description, self.game_data.categories[14].description,
                            self.game_data.categories[15].description, self.game_data.categories[16].description,
                            self.game_data.categories[17].description, self.game_data.categories[18].description,
                            self.game_data.categories[19].description))
        option = 0
        while option not in range(1, 20):
            option = int(input("Your choice: "))
            try:
                if option not in range(1, 20):
                    raise ValueError()
            except ValueError:
                print("Category should be a value between 1-19 (are you deliberately trying to crash the game?)\n")
        self.category = option

    def init_difficulty(self):
        print("Select difficulty level (input number):\n1. Easy\n2. Medium\n3. Hard\n\n")
        option = 0
        while option not in range(1, 4):
            option = int(input("Your choice: "))
            try:
                if option not in range(1, 4):
                    raise ValueError
            except ValueError:
                print("Difficulty should be a value between 1-3 (stop it..)")
        self.difficulty = option

    def init_trivia_item(self):
        trivia_item = self.tdb.get_trivia_item(self.game_data.categories[self.category].opentdb_number, self.game_data.difficulties[self.difficulty])
        self.question = "Question: {}".format(colored(trivia_item.question, 'yellow'))
        self.answer = trivia_item.answer

    def init_candidate(self):
        for letter in self.answer:
            if not(letter.isspace()):
                self.candidate += "_"
            else:
                self.candidate += letter

    def init_retries(self):
        self.retries = 11

    def init_used_words(self):
        self.used_words = []

    def init_is_guessed(self):
        self.is_guessed = False
