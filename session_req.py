import aiohttp
import pandas
import requests
import json
from pprint import pprint
import asyncio


class Api():
    def __init__(self, file):
        self.url = 'http://public-api.solscan.io/transaction/'

        with open(file, 'r') as file:
            data = file.readlines()
            list_of_ids = [element.strip() for element in data]

        self.id_list = list_of_ids

    def http_get(self):
        with requests.session() as session:
            for i in self.id_list:
                response = session.get(self.url + i)
                print(response)
                # self.write_all_logs()

    async def async_http_get(self):
        async with aiohttp.ClientSession() as session:
            content = []
            for i in self.id_list:
                response = await session.get(self.url + i)
                content.append(await response.text())
            return content

    def write_all_logs(self):
        pass

    def write_false_logs(self):
        pass