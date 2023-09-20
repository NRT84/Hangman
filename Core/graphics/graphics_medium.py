from Core.graphics.graphics_base import GraphicsBase
from colorama import init
from termcolor import colored


class GraphicsMedium(GraphicsBase):

    def __init__(self):
        super().__init__()
        init()
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

    def print_hangman(self):
        self.function_list[self.index]()
        self.index += 1
        print("\n")

    def _print_try_1(self):
        print(colored("|\n|\n|\n|\n|\n|\n|", self.hangman_color))

    def _print_try_2(self):
        print(colored("|-------\n|      |\n|      O\n|\n|\n|\n|", self.hangman_color))

    def _print_try_3(self):
        print(colored("|-------\n|      |\n|      O\n|     / \\\n|\n|\n|", self.hangman_color))

    def _print_try_4(self):
        print(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|\n|", self.hangman_color))

    def _print_try_5(self):
        print(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     /\n|", self.hangman_color))

    def _print_try_6(self):
        print(colored("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     / \\\n|", self.hangman_color))

    def _print_try_7(self):
        print(colored("|-------\n|\n|      X\n|     /|\\    \n|      |\n|     / \\\n|\n", self.hangman_color))
        print(colored("YOU DIED!", self.hangman_death_color))
