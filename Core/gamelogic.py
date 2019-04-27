from colorama import init
from termcolor import colored
from Core import graphics as graph


class GameLogic:

    def __init__(self, config):
        init()
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
        self.validate_answer(guess)
        self.reduce_retries(guess)
        self.mark_used_word(guess)

    def mark_used_word(self, guess):
        self.config.used_words.append(guess)

    def reduce_retries(self, guess):
        if self.config.is_guessed:
            print(format(colored("\n{}".format(self.config.answer), 'green')))
            print(format(colored("\nCONGRATULATIONS! You've guessed it!\n", 'green')))
            return
        if self.should_not_reduce_retry:
            self.print_info()
            return
        else:
            self.config.retries -= 1
            print("'{0}' isn't found in the answer\n".format(guess))
            self.graphics.print_hangman()
        if self.config.retries == 0:
            print("The correct answer was: {}".format(colored(self.config.answer, 'green')))
            print("Try another one? ;)\n")
            return
        self.print_info()

    def validate_answer(self, guess):
        if guess == self.config.answer or self.config.candidate == self.config.answer:
            self.config.is_guessed = True

    def print_info(self):
        print("Retries left: {0}".format(self.config.retries))
        str_builder = ""
        for letter in self.config.candidate:
            if letter.isspace():
                str_builder += "   "
            else:
                str_builder += "{0} ".format(letter)
        print(str_builder)
