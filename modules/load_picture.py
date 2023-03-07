import json

import requests


class LoadPicture:
    def __init__(self, url):
        self.url = url

    
    def get_response(self):
        self.response = requests.get(self.url)
        return self.response
    
    def get_picture(self):
        self.response = requests.get(self.url)
        self.contents = self.response.text
        self.data = json.loads(self.contents)
        self.list = []
        for i in range(int(5)):
            self.list.append(self.data['response']['body']['items']['item'][i]['firstimage'])
        return self.list