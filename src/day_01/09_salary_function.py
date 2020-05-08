"""
Пример программы для работы с функциями (аналог файла 01_hours_salary.py)

Аргументы
- стоимость часа в руб
- количество дней в руб

Сделать
- функцию, которая вернет размер зарплаты в руб
"""


def salary(hour_cost, day_quantity):
    total = (hour_cost * 8) * day_quantity
    tax = 0.13 * total
    final = total - tax
    return total, tax, final


a = salary(hour_cost=600, day_quantity=21)
b = salary(hour_cost=1200, day_quantity=22)

salaries = [a, b]
for worker_salary in salaries:
    print("Зарплата: ", worker_salary[0],
          "Налог:", worker_salary[1],
          "Получаете на руки:", worker_salary[2], sep="\n", end="\n\n")
