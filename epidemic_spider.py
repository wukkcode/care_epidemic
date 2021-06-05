import requests
import json


class EpidemicSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.39"}

    def request(self, url):
        resonse = requests.get(url, headers=self.headers).text
        return resonse

    def get_rumors(self, url):
        return json.loads(self.request(url))

    def get_news(self, url):
        return json.loads(self.request(url))

    def get_data(self, url):
        return json.loads(self.request(url))

    def get_overall(self, url):
        return json.loads(self.request(url))
