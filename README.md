## Проверка транзакций

Скрипт проводит проверку транзакций из фаила ***transactions.xlsx***

---------------

Логи проверки пишутся в logs.txt в формате:
* 'Имя транзакции' : 'True/False'

В логах:
- True - не содержит 'Program log: Instruction: Sell'
- False - содержит 'Program log: Instruction: Sell'

---------------

Установка зависимостей:
* pip install requirements.txt

Запуск из:
* main.py