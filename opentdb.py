import trivia_item
import requests
import json
import base64
import os


# Based on https://opentdb.com/
class Opentdb:

    def __init__(self):
        self._token_file = "{0}\\token".format(os.getcwd())
        self.token = self.get_token(self._token_file)
        if not self.is_token_valid(self.token):
            self.token = self.generate_new_token()
            self.update_token_file(self._token_file, self.token)

    def get_token(self, token_file):
        with open(token_file) as file:
            return file.read()

    def is_token_valid(self, token):
        if not token:
            return False
        response = requests.get("https://opentdb.com/api.php?amount=1&token={0}".format(token))
        if "\"response_code\":0" not in response.text:
            return False
        return True

    def generate_new_token(self):
        req = requests.get("https://opentdb.com/api_token.php?command=request")
        content = req.text
        json_data = dict(json.loads(content))
        return json_data.get("token")

    def update_token_file(self, file, token):
        with open(file, "r+") as my_file:
            my_file.seek(0)
            my_file.write(token)
            my_file.truncate()

    def get_trivia_item(self, category, difficulty):
        item = trivia_item.TriviaItem()
        try:
            req = requests.get('https://opentdb.com/api.php?amount=1&category={0}&difficulty={1}&encode=base64&type=multiple&token={2}'.format(category, difficulty, self.token))
        except requests.exceptions.RequestException as exception:
            print("Error while trying to access open-trivia DB.\nError: {0}".format(exception.strerror))
            exit(0)
        content = req.text
        json_data = dict(json.loads(content))
        results = json_data.get('results')
        for key, value in dict(results[0]).items():
            if key == 'question':
                question = str(base64.b64decode(value))
                item.question = question[2:-1]
            if key == 'correct_answer':
                answer = str(base64.b64decode(value))
                item.answer = answer[2:-1].lower()
        return item
