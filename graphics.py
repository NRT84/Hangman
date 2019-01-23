
class Graphics:

    def __init__(self):
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
        print("|\n|\n|\n|\n|\n|\n|")

    def _print_try_2(self):
        print("|-------\n|\n|\n|\n|\n|\n|")

    def _print_try_3(self):
        print("|-------\n|      |\n|\n|\n|\n|\n|")

    def _print_try_4(self):
        print("|-------\n|      |\n|      O\n|\n|\n|\n|")

    def _print_try_5(self):
        print("|-------\n|      |\n|      O\n|     /\n|\n|\n|")

    def _print_try_6(self):
        print("|-------\n|      |\n|      O\n|     / \\\n|\n|\n|")

    def _print_try_7(self):
        print("|-------\n|      |\n|      O\n|     /|\\\n|\n|\n|")

    def _print_try_8(self):
        print("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|\n|")

    def _print_try_9(self):
        print("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     /\n|")

    def _print_try_10(self):
        print("|-------\n|      |\n|      O\n|     /|\\\n|      |\n|     / \\\n|")

    def _print_try_11(self):
        print("|-------\n|\n|      X\n|     /|\\    YOU DIED!\n|      |\n|     / \\\n|")
