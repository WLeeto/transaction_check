import pandas
import requests
import json
from pprint import pprint

from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing


def get_transactions(signature: str):
    URL = 'http://public-api.solscan.io/transaction/'
    FULL_REQUEST = URL + signature
    request = requests.get(FULL_REQUEST)
    templates = request.json()
    return templates


def file_to_list(file_path: str):
    with open(file_path, 'r') as file:
        data = file.readlines()
        list = [element.strip() for element in data]

    return list


def __read_xlsx(file_path: str):
    excel_data = pandas.read_excel(file_path)
    data = pandas.DataFrame(excel_data, columns=['ID', ])
    return data.ID


def write_logs(file_path: str, name: str, status: str):
    with open(file_path, 'a') as file:
        file.write(f'{name} : {status}\n')


def write_false_logs(file_path: str, name: str):
    with open(file_path, 'a') as file:
        file.write(f'{name}\n')


def req_cycle(list_of_id):
    for i in list_of_id:
        current_id = get_transactions(i)
        if current_id['logMessage'][1] == 'Program log: Instruction: Sell':
            write_logs('logs.txt', name=i, status='False')
            write_false_logs('logs_false.txt', name=i)
            print('False')
        else:
            write_logs('logs.txt', name=i, status='True')
            print('True')


def req_one(id):
    current_id = get_transactions(id)
    if current_id['logMessage'][1] == 'Program log: Instruction: Sell':
        write_logs('logs.txt', name=id, status='False')
        write_false_logs('logs_false.txt', name=id)
        print('False')
    else:
        write_logs('logs.txt', name=id, status='True')
        print('True')


if __name__ == '__main__':

    file_path = 'transactions.txt'  # Сюда пишем имя фаила на проверку. Только txt, разделитель \n

    incorrect_post = 'Program log: Instruction: Sell'  # Всегда в ['logMessage'][1]

    list = file_to_list('transactions.txt')

    pool = Pool(processes=3)
    pool.map(req_one, list)