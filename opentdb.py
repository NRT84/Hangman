import trivia_query
import os
import requests
import json
import base64


class Opentdb:

    def __init__(self):
        self.__token_file = "{0}/token".format(os.getcwd())
        self.token = self.__get_token(self.__token_file)
        if not self.__is_token_valid(self.token):
            self.token = self.__generate_new_token()
            self.__update_token_file(self.__token_file, self.token)


    def __get_token(self, token_file):
        with open(token_file) as file:
            return file.read()


    def __is_token_valid(self, token):
        response = requests.get("https://opentdb.com/api.php?amount=1&token={0}".format(token))
        if "\"response_code\":0" not in response.text:
            return False
        return True


    def __generate_new_token(self):
        req = requests.get("https://opentdb.com/api_token.php?command=request")
        content = req.text
        json_data = dict(json.loads(content))
        return json_data.get("token")


    def __update_token_file(self, file, token):
        with open(file, "r+") as my_file:
            old_token = my_file.read()
            my_file.seek(0)
            my_file.write(token)
            my_file.truncate()
            my_file.close()


    def get_question(self, category, difficulty):
        #category - 9, difficulty, easy, medium, hard
        query = trivia_query.TriviaQuery()
        query.difficulty = difficulty
        req = requests.get('https://opentdb.com/api.php?amount=1&category={0}&difficulty={1}&encode=base64&type=multiple&token={2}'.format(category, difficulty, self.token))
        content = req.text
        json_data = dict(json.loads(content))
        results = json_data.get('results')
        for key, value in dict(results[0]).items():
            if key == 'question':
                query.description = base64.decode(value)
            if key == 'correct_answer':
                query.answer = base64.decode(value)
        return query
