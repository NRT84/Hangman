
class Graphics:

    def __init__(self):
        self.function_list = self.init_function_list()
        self.index = 0

    def init_function_list(self):
        func_list = []
        func_list.append(self._print_try_1)
        func_list.append(self._print_try_2)
        func_list.append(self._print_try_3)
        func_list.append(self._print_try_4)
        func_list.append(self._print_try_5)
        func_list.append(self._print_try_6)
        func_list.append(self._print_try_7)
        func_list.append(self._print_try_8)
        func_list.append(self._print_try_9)
        func_list.append(self._print_try_10)
        func_list.append(self._print_try_11)

        return func_list

    def print_next(self):
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
