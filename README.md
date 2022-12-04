## Проверка транзакций

Скрипт проводит проверку транзакций из фаила ***transactions.xlsx***

---------------

Логи проверки пишутся в logs.txt в формате:
* 'Имя транзакции' : 'True/False'

В логах:

logs.txt:
- True - не содержит 'Program log: Instruction: Sell'
- False - содержит 'Program log: Instruction: Sell'

logs_false.txt:
- Только id транзакций не прошедших проверку

---------------

Установка зависимостей:
* pip install requirements.txt

Запуск с разложением по процессам (самый бустрый):
* multiprocessing_req.py

---------------

Бета версии:
* main.py (функционально)
* session_req (ООП - сессионый запуск)
* async_req (асинхронная функция, по идее должно было быть быстрее, но нет)

---------------

Перед запуском удалите фаилы logs.txt и logs_false.txt если они присутствуют