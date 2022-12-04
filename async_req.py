import aiohttp
import pandas
import requests
import json
from pprint import pprint
import asyncio


file = 'transactions.txt'
with open(file, 'r') as file:
    data = file.readlines()
    list_of_ids = [element.strip() for element in data]


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'http://public-api.solscan.io/transaction/'
        for i in list_of_ids:
            async with session.get(url + i) as resp:
                result = await resp.json()
                print(result['logMessage'][1])


if __name__ == '__main__':
    # api = Api('transactions.txt')
    # api.http_get()
    # api.async_http_get()

    asyncio.Queue(main())

