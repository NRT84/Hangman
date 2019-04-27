from colorama import init
from termcolor import colored


class Graphics:

    def __init__(self):
        init()
        self.hangman_color = "blue"
        self.hangman_death_color = "red"
        self.function_list = None
        self.index = 0
        self._init_function_list()

    def _init_function_list(self):
        self.function_list = []
        self.function_list.append(self._print_try_1)
        self.function_list.append(self._print_try_2)
        self.function_list.append(self._print_try_3)
        self.function_list.append(self._print_try_4)
        self.function_list.append(self._print_try_5)
        self.function_list.append(self._print_try_6)
        self.function_list.append(self._print_try_7)
        self.function_list.append(self._print_try_8)
        self.function_list.append(self._print_try_9)
        self.function_list.append(self._print_try_10)
        self.function_list.append(self._print_try_11)

    def print_hangman(self):
        self.function_list[self.index]()
        self.index += 1
        print("\n")

    def _print_try_1(self):
        print(format(colored("|\n|\n|\n|\n|\n|\n|", self.hangman_color)))

    def _print_try_2(self):
        print(format(colored("|-------\n|\n|\n|\n|\n|\n|", self.hangman_color)))

    def _print_try_3(self):
        print(format(colored("|-------\n|      |\n|\n|\n|\n|\n|", self.hangman_color)))

    def _print_try_4(self):
        print(format(colored("|-------\n|      |\n|      O\n|\n|\n|\n|", self.hangman_color)))

    def _print_try_5(self):
        print(format(colored("|-------\n|      |\n|      O\n|     /\n|\n|\n|", self.hangman_color)))

    def _print_try_6(self):
        print(format(colored("|-------\n|      |\n|      O\n|     / \\\n|\n|\n|", self.hangman_color)))

    def _print_try_7(self):
        print(format(colored("|-------\n|      |\n|      O\n|     /|\\\n|\n|\n|", self.hangman_color)))

    def _print_try_8(self):
        print(format(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|\n|", self.hangman_color)))

    def _print_try_9(self):
        print(format(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     /\n|", self.hangman_color)))

    def _print_try_10(self):
        print(format(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     / \\\n|", self.hangman_color)))

    def _print_try_11(self):
        print(format(colored("|-------\n|\n|      X\n|     /|\\    \n|      |\n|     / \\\n|\n", self.hangman_color)))
        print(format(colored("YOU DIED!", self.hangman_death_color)))
