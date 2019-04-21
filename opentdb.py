import trivia_item
import requests
import json
import base64


# Based on https://opentdb.com/
class Opentdb:

    def __init__(self):
        self._token = self._generate_new_token()

    def _generate_new_token(self):
        req = requests.get("https://opentdb.com/api_token.php?command=request")
        content = req.text
        json_data = dict(json.loads(content))
        return json_data.get("token")

    def get_trivia_item(self, category, difficulty):
        item = trivia_item.TriviaItem()
        try:
            req = requests.get('https://opentdb.com/api.php?amount=1&category={0}&difficulty={1}&encode=base64&type=multiple&token={2}'.format(category, difficulty, self._token))
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
