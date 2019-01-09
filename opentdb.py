import trivia_item
import os
import requests
import json
import base64


class Opentdb:

    def __init__(self):
        self._token_file = "{0}/token".format(os.getcwd())
        self.token = self._get_token(self._token_file)
        if not self._is_token_valid(self.token):
            self.token = self._generate_new_token()
            self._update_token_file(self._token_file, self.token)

    def _get_token(self, token_file):
        with open(token_file) as file:
            return file.read()

    def _is_token_valid(self, token):
        response = requests.get("https://opentdb.com/api.php?amount=1&token={0}".format(token))
        if "\"response_code\":0" not in response.text:
            return False
        return True

    def _generate_new_token(self):
        req = requests.get("https://opentdb.com/api_token.php?command=request")
        content = req.text
        json_data = dict(json.loads(content))
        return json_data.get("token")

    def _update_token_file(self, file, token):
        with open(file, "r+") as my_file:
            my_file.seek(0)
            my_file.write(token)
            my_file.truncate()

    def get_trivia_item(self, category, difficulty):
        #category - 9, difficulty, easy, medium, hard
        query = trivia_item.TriviaItem()
        req = requests.get('https://opentdb.com/api.php?amount=1&category={0}&difficulty={1}&encode=base64&type=multiple&token={2}'.format(category, difficulty, self.token))
        content = req.text
        json_data = dict(json.loads(content))
        results = json_data.get('results')
        for key, value in dict(results[0]).items():
            if key == 'question':
                question = str(base64.b64decode(value))
                query.question = question[2:-1]
            if key == 'correct_answer':
                answer = str(base64.b64decode(value))
                query.answer = answer[2:-1].lower()
        return query
