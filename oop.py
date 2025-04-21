# Класс определяет, какие атрибуты и методы будут у объектов.
from multiprocessing.context import set_spawning_popen


# Атрибуты - переменные, принадлежащие объекту или классу. Бывают:
# Атрибуты экземпляра - уникальны для каждого объекта
# Атрибуты класса - общие для всех объектов класса
# self - это ссылка на сам объект (как местоимение "я" для объекта)

# Магические методы (dunder methods) cпециальные методы,
# которые начинаются и заканчиваются двойным подчёркиванием (__).
# Они позволяют определять поведение объектов в различных ситуациях.

# Методы - это функции, принадлежащие объекту или классу.

# Инкапсуляция - это сокрытие внутренней реализации и предоставление интерфейса для работы с объектом.

# Наследование - позволяет создавать новый класс на основе существующего.

# Полиморфизм - возможность использовать объекты разных классов одинаковым образом.

# Абстрактные классы не предназначены для создания экземпляров, а только для наследования.

class Animal:
    species = 'Canis familiaris'  # Атрибут класса

    def __init__(self, name, color):  # __init__ конструктор - вызывается при создании объекта.
        self.name = name  # Атрибут экземпляра
        self.__color = color  # Приватный атрибут

    def __str__(self):  # Возвращает строковое представление объекта (для пользователя).
        return f'dog named {self.name}'

    def greed(self):
        return f'Hello {self.name}'

    def get_color(self):  # Публичный метод для доступа к приватному атрибуту
        return self.__color

    def speak(self):
        return 'Some sound'


class Dog(Animal):  # Наследуем от Animal
    def speak(self):  # Переопределяем метод
        return 'Woof!'


class Cat(Animal):  # Наследуем от Animal
    def speak(self):  # Переопределяем метод
        return 'Meow!'


def animal_sound(animal):  # Полиморфизм
    print(animal.speak())


cat = Cat('Keks', 'black')
animal_sound(cat)

my_dog = Animal('Rex', 'black')  # создаём объект (экземпляр) класса Dog
print(my_dog.name)  # Rex
print(my_dog.species)  # Canis familiaris
print(str(my_dog))  # dog named Rex
print(my_dog.greed())  # Hello Rex
print(my_dog.get_color())
dog = Dog('Rex', 'white')
print(dog.speak())


# Абстрактные классы.
class Parser:
    def parse(self):
        raise NotImplementedError("Метод parse() должен быть реализован!")


class JSONParser(Parser):
    def parse(self):
        print("Парсинг JSON")


parser = JSONParser()
parser.parse()

from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self, text):
        pass


class ConsoleWriter(Writer):
    def write(self, text):
        print(text)


writer = ConsoleWriter()
writer.write("Hello!")  # Hello!


# главный принцип абстракции - скрытие реализации за простым интерфейсом

# Мини-проект: "Банковский счет" (ООП)
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance
        self.__password = '1234'

    def check_password(self, input_password):
        return self.__password == input_password

    def deposit(self, amount, password):  # Пополнение счета
        if not self.check_password(password):
            return "Ошибка: Неверный пароль!"
        if amount <= 0:
            return "Ошибка: Сумма должна быть положительной!"
        self.__balance += amount
        return f"Счет пополнен на {amount}. Новый баланс: {self.__balance}"

    def withdraw(self, amount, password):  # Снятие денег
        if not self.check_password(password):
            return "Ошибка: Неверный пароль!"
        if amount <= 0:
            return "Ошибка: Сумма должна быть положительной!"
        if amount > self.__balance:
            return "Ошибка: Недостаточно средств!"
        self.__balance -= amount
        return f"Со счета снято {amount}. Новый баланс: {self.__balance}"

    def get_balance(self, password):  # Возвращает текущий баланс
        if not self.check_password(password):
            return "Ошибка: Неверный пароль!"
        return f"Баланс: {self.__balance}"

    def display_info(self) -> str:
            return f"Владелец: {self.owner_name}\nНомер счета: {self.account_number}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, interest_rate):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self, password):
        if not self.check_password(password):
            return "Ошибка: Неверный пароль!"
        interest = self._BankAccount__balance * (self.interest_rate / 100)
        self._BankAccount__balance += interest
        return f"Начислено {interest} по ставке {self.interest_rate}%."

class LimitedAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, withdraw_limit):
        super().__init__(account_number, owner_name, balance)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount, password):  # Снятие денег
        if not self.check_password(password):
            return "Ошибка: Неверный пароль!"
        if amount <= 0:
            return "Ошибка: Сумма должна быть положительной!"
        if amount > self._BankAccount__balance:
            return "Ошибка: Недостаточно средств!"
        if amount > self.withdraw_limit:
            return f"Ошибка: Превышен лимит снятия ({self.withdraw_limit})!"
        self._BankAccount__balance -= amount
        return f"Со счета снято {amount}. Новый баланс: {self._BankAccount__balance}"

if __name__ == "__main__":
    # Обычный счет
    acc1 = BankAccount("123456", "Иван Иванов", 1000)
    print(acc1.deposit(500, "1234"))  # OK
    print(acc1.withdraw(200, "1234"))  # OK
    print(acc1.get_balance("1234"))    # Баланс: 1300

    # Сберегательный счет
    savings = SavingsAccount("654321", "Анна Петрова", 5000, 5)  # 5% годовых
    print(savings.add_interest("1234"))  # Начислено 250.0
    print(savings.get_balance("1234"))   # Баланс: 5250

    # Лимитированный счет
    limited_acc = LimitedAccount("999999", "Петр Сидоров", 3000, 1000)
    print(limited_acc.withdraw(1500, "1234"))  # Ошибка: Превышен лимит снятия (1000)!
    print(limited_acc.withdraw(500, "1234"))   # OK