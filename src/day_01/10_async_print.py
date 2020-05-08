"""
Пример программы для работы с асинхронностью

Данные
- пользователь вводит число X

Сделать
- асинхронную функцию, которая запустится X раз
- функция должна считать от 0 до числа X
- между выводом чисел должны быть паузы по 0,5 сек
"""
import asyncio


async def print_counter(x):
    for number in range(x):
        print(number)
        await asyncio.sleep(0.5)


async def start(x):
    coroutines = []

    for number in range(x):
        coroutines.append(
            asyncio.create_task(print_counter(x=x))
        )

    await asyncio.wait(coroutines)


while True:
    try:
        user_count = int(input("Количество повторов функции >>"))
        break
    except ValueError:
        print("Введите число!")

asyncio.run(start(user_count))
