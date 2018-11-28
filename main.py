import configuration
import gamedata
import gamelogic
import requests
import json
import fileinput
import urllib


def main():
    token = requests.get("https://opentdb.com/api_token.php?command=request")
    print("lel")

    #r = requests.get('https://opentdb.com/api_token.php?command=reset&token=9a45ec413b44895929797b3d9d7f5adbe882c95651ef8da5a3bc48deb215bed4')
    #r = requests.get('https://opentdb.com/api.php?amount=50&category=9&difficulty=easy&encode=url3986&type=multiple&token=3c340d9bec3e1daf1aa3a9568f4f3ddf636a92fa3bbf26bdeb6557bc1583974c')
    #content = r.text
    filename = "/home/nrt/Downloads/db1"
    convert_url3986_to_text(filename)
    # json_data = json.loads(content)
    # with open(filename, "a") as my_file:
    #     json.dump(json_data, my_file)


    # option = 0
    # while option not in range(1, 3):
    #     print("Welcome to Hangman! What you wanna do?")
    #     option = int(input("Select a valid option (input number):\n1. Start a new game.\n2. Exit ta'fuck out.\n\nYour choice: "))
    #     if option == 1:
    #         config = configuration.Configuration(gamedata.GameData())
    #         config.setup()
    #         logic = gamelogic.GameLogic(config)
    #         logic.pretty_print(config.candidate)
    #         while not config.is_guessed and config.retries > 0:
    #             logic.guess(input("Enter your guess: \n"))
    #         option = 0
    #     if option == 2:
    #         print("Thanks for playing!")
    #         exit(0)


def convert_url3986_to_text(filename):
    for line in fileinput.input([filename], inplace=True):
    #with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        #for line in file:
            for word in line.split():
                try:
                    decoded = urllib.parse.unquote(word)
                    if word is not decoded:
                        print(line.replace(word, decoded), end='')
                except:
                    pass



if __name__ == "__main__":
    main()
