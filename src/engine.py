import os
from abc import ABC, abstractmethod

import requests

from src.connect import Connector


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        return Connector(file_name)


class HH(Engine):
    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page,
            "per_page": 100,
            "search_field": "name",
        }

    def get_request(self):
        return requests.get(self.url, params=self.params)


class Superjob(Engine):
    def __init__(self, keyword, page=0):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {
            "keywords[0][keys]": keyword,
            "keywords[0][srwc]": 4,
            "keywords[0][skwc]": "or",
            "page": page,
            "count": 100
        }

    def get_request(self):
        headers = {"X-Api-App-Id": os.environ["SUPERJOB_API_KEY"]}
        return requests.get(self.url, headers=headers, params=self.params)
