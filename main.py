from sys import exit
from core import configuration, gamedata, gamelogic, events, opentdb
import ctypes
import os


def main():
    is_first_game = True
    maximize()
    print("Welcome to Hangman!")
    option = 0
    while option not in range(1, 3):
        try:
            option = int(input("Select a valid option (input number):\n1. Start a new game\n2. Exit\n\nYour choice: "))
            if option not in range(1, 3):
                raise ValueError
        except ValueError:
            print("Not a valid input\n")
            option = 0
        if option == 1:
            if not is_first_game:
                clear_screen()
            config = configuration.Configuration(gamedata.GameData(), opentdb.Opentdb())
            logic = gamelogic.GameLogic(config)
            event = events.Events(config)
            print_instructions(config.question)
            logic.print_info()
            while not config.is_guessed and config.retries > 0:
                logic.guess(input("Enter your guess: "))
                print("\n")
            option = 0
            is_first_game = False
            event.stop_listener()
        if option == 2:
            exit(0)


def print_instructions(question):
    print("For simplicity reasons all your guesses should be lowercase as the answers will be as well.")
    print("Remember, at any point in time you can hit 'f1' to see the current question.\n")
    print(f"{question}\n")


def maximize():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    sw_maximize = 3
    hwnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hwnd, sw_maximize)


def clear_screen():
    os.system('cls')


if __name__ == "__main__":
    main()
