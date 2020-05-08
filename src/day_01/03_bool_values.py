"""
Пример программы для определения истинности данных

Данные
- пользователь вводит два числа A и B

Сделать
- вывести истинность, что число A больше B
"""

while True:
    try:
        number_1 = int(input("Введите число 1 >>"))
        break
    except ValueError:
        print("Введите число!")


while True:
    try:
        number_2 = int(input("Введите число 2 >>"))
        break
    except ValueError:
        print("Введите число!")


result = number_1 > number_2

print(result)
