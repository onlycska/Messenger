"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


def user_hello(user):
    print(f"Hello, {user}!")


clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    user_hello(user=user)

new_user = "Arthur"
clients.append(new_user)
user_hello(clients[-1])
