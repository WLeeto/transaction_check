import pandas
import requests
import json


def get_transactions(signature: str):
    URL = ' http://public-api.solscan.io/transaction/'
    FULL_REQUEST = URL + signature
    request = requests.get(FULL_REQUEST)
    templates = request.json()
    return templates


def read_xlsx(file_path: str):
    excel_data = pandas.read_excel(file_path)
    data = pandas.DataFrame(excel_data, columns=['ID', ])
    return data.ID


def write_logs(file_path: str, name: str, status: str):
    with open(file_path, 'a') as file:
        file.write(f'{name} : {status}\n')


def write_false_logs(file_path: str, name: str, status: str):
    with open(file_path, 'a') as file:
        file.write(f'{name} : {status}\n')


if __name__ == '__main__':

    incorrect_post = 'Program log: Instruction: Sell'  # Всегда в ['logMessage'][1]

    list = read_xlsx('transactions.xlsx')

    for i in list:
        current_transaction = get_transactions(i)
        if current_transaction['logMessage'][1] == 'Program log: Instruction: Sell':
            write_logs('logs.txt', name=i, status='False')
            write_false_logs('logs_false.txt', name=i, status='False')
            print('False')
        else:
            write_logs('logs.txt', name=i, status='True')
            print('True')
