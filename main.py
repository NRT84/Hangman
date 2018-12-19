import configuration
import gamedata
import gamelogic


def main():
    option = 0
    while option not in range(1, 3):
        print("Welcome to Hangman! What you wanna do?")
        option = int(input("Select a valid option (input number):\n1. Start a new game.\n2. Exit ta'fuck out.\n\nYour choice: "))
        if option == 1:
            config = configuration.Configuration(gamedata.GameData())
            config.setup()
            logic = gamelogic.GameLogic(config)
            logic.pretty_print(config.candidate)
            while not config.is_guessed and config.retries > 0:
                logic.guess(input("Enter your guess: \n"))
            option = 0
        if option == 2:
            print("Thanks for playing!")
            exit(0)


if __name__ == "__main__":
    main()
