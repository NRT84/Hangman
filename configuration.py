import opentdb
import categories


class Configuration:

    def __init__(self, game_data):
        self.game_data = game_data
        self.tdb = opentdb.Opentdb()
        self.category = None
        self.difficulty = None
        self.answer = None
        self.retries = None
        self.used_words = None
        self.is_guessed = None
        self.candidate = ""

    def setup(self):
        self.init_category()
        self.init_difficulty()
        self.init_answer()
        self.init_candidate()
        self.init_retries()
        self.init_used_words()
        self.init_is_guessed()

    def init_category(self):
        self.category = int(input("Select category (input number):\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n"
                                  "{10}\n{11}\n{12}\n{13}\n""{14}\n{15}\n{16}\n{17}\n{18}\n\nYour choice: "
                                  .format(categories.general_knowledge, categories.entertainment_books,
                                          categories.entertainment_film, categories.entertainment_music,
                                          categories.entertainment_musicals_and_theatres,
                                          categories.entertainment_television, categories.entertainment_video_games,
                                          categories.entertainment_board_games, categories.science_and_nature,
                                          categories.science_computers, categories.science_mathematics,
                                          categories.mythology, categories.sports, categories.geography,
                                          categories.history, categories.politics, categories.art,
                                          categories.celebrities, categories.animals)))
        if self.category not in range(1, 19):
            raise ValueError("Category should be a value between 1-19")

    def init_difficulty(self):
        self.difficulty = int(input("Select difficulty level (input number):\n1. Easy\n2. Medium\n3. Hard\n\nYour choice: "))
        if self.difficulty not in range(1, 4):
            raise ValueError("Difficulty should be a value between 1-3")

    def init_answer(self):
        trivia_item = self.tdb.get_trivia_item(self.game_data.categories[self.category], self.game_data.difficulties[self.difficulty])
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
