"""
Пример программы для расчета почасовой зарплаты

Данные
- пользователь вводит стоимость часа (число)
- пользователь вводит количество дней (число)

Сделать
- найти размер оплаты в руб (по кол-во дней)
- найти размер налога 13% в руб (по кол-во дней)
"""

while True:
    try:
        hour_cost = int(input("Введите стоимость часа >>"))
        break
    except ValueError:
        print("Введите число!")

while True:
    try:
        day_quantity = int(input("Введите количество дней >>"))
        break
    except ValueError:
        print("Введите число!")

total = (hour_cost * 8) * day_quantity
tax = 0.13 * total
final = total - tax

print("\nЗарплата: ", total, "Налог:", tax, "Получаете на руки:", final, sep="\n")
