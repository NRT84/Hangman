from colorama import Fore
import graphics as graph


class GameLogic:

    def __init__(self, config):
        self.graphics = graph.Graphics()
        self.config = config
        self.should_not_reduce_retry = None

    def guess(self, guess):
        self.should_not_reduce_retry = False
        if not(len(guess) == 1 or len(guess) == len(self.config.answer)):
            print("Not a legal guess, either guess one character at a time or guess the whole phrase exactly")
            return
        if guess in self.config.used_words:
            self.should_not_reduce_retry = True
            print("You've already used that letter. Try again..")
        elif guess in self.config.answer:
            self.handle_positive_guess(guess)

        self.handle_end_turn(guess)
        self.validate_answer(guess)

    def evaluate_new_candidate(self, old_candidate, new_found_letter, answer):
        new_candidate = ""
        for index, letter in enumerate(old_candidate):
            if letter == "_" and answer[index] == new_found_letter:
                new_candidate += new_found_letter
            else:
                new_candidate += letter
        return new_candidate

    def handle_positive_guess(self, guess):
        self.should_not_reduce_retry = True
        for letter in self.config.answer:
            if letter == guess:
                self.config.candidate = self.evaluate_new_candidate(self.config.candidate, letter, self.config.answer)

    def handle_end_turn(self, guess):
        self.mark_used_word(guess)
        self.reduce_retries(guess)

    def mark_used_word(self, guess):
        self.config.used_words.append(guess)

    def reduce_retries(self, guess):
        if self.should_not_reduce_retry or self.config.is_guessed:
            self.print_info()
            return
        else:
            self.config.retries -= 1
            print("'{0}' isn't found in the answer\n".format(guess))
            self.graphics.print_hangman()
        if self.config.retries == 0:
            print("The correct answer was: {}".format(Fore.LIGHTGREEN_EX + self.config.answer))
            print(Fore.RESET)
            print("Try another one? ;)\n")
            return
        self.print_info()

    def validate_answer(self, guess):
        if guess == self.config.answer or self.config.candidate == self.config.answer:
            print("\nCONGRATULATIONS! You've guessed it!\n")
            self.config.is_guessed = True

    def pretty_print(self, text):
        str_builder = ""
        for letter in text:
            if letter.isspace():
                str_builder += "   "
            else:
                str_builder += "{0} ".format(letter)
        print(str_builder)

    def print_info(self):
        print("Retries left: {0}".format(self.config.retries))
        self.pretty_print(self.config.candidate)
