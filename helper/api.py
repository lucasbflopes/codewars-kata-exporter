import json
import requests


class CodeWarsApi:
    def __init__(self, token):
        self.token = token

    def get_kata_description(self, kata_id):
        endpoint = 'https://www.codewars.com/api/v1/code-challenges/{}'.format(kata_id)
        res = requests.get(endpoint, params={'Authorization': self.token})
        data = json.loads(res.text)
        return data['description']
