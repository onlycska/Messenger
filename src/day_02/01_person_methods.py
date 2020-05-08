"""
Пример программы для работы с ООП

Сделать
- добавить метод для вывода сообщений с префиксом имени
- добавить метод для вывода информации об объекте
- добавить конструктор класса для формирования полей
"""


class Person:
    name: str
    surname: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.name = first_name
        self.surname = last_name
        self.age = age

    def info(self):
        print(f"Объект класса Person: {self.name} {self.surname}, age: {self.age}")

    def say_as(self, message):
        return f"<{self.name}> {message}"


person1 = Person('John', 'Doe', 43)

print(person1.name)


person2 = Person('John', 'Doe', 43)

person2.info()
