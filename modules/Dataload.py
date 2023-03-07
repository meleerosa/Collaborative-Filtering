import json

import requests


class Dataload:
    def __init__(self,url):
        self.url = url

    def get_response(self):
        self.response = requests.get(self.url)
        return self.response
    
    def get_json(self):
        self.response = requests.get(self.url)
        self.contents = self.response.text
        self.data = json.loads(self.contents)
        return self.data