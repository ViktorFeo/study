"""
1.Базовый синтаксис (3-4 дня)

1.1 Переменные, типы данных, операторы
1.2 Условные операторы (if-elif-else)
1.3 Циклы (for, while)
1.4 Функции (def, return, args/kwargs)
1.5 Работа с файлами (open, read, write)
"""

# 1.1 Переменные, типы данных, операторы
# Создайте переменные разных типов (int, float, str, bool) и выведите их типы с помощью type()
num1 = 10
num2 = 2.5
text = 'random text'
not_true = False
print(type(num1), type(num2), type(text), type(not_true))
# Напишите программу, которая принимает два числа и выводит их сумму, разность, произведение и частное
print(
    f'Даны два числа: 10, 2\nСумма: {num1 + num2}, Разность: {num1 - num2}, '
    f'Произведение: {num1 * num2}, Частное: {num1 / num2}, остаток от деления: {num2 % num1}')
# Создайте строку "Hello, World!" и:
# Выведите ее длину
hello = 'Hello, World!'
print(f'Длина строки - {hello}: {len(hello)} символов')
# Переведите в верхний регистр
print(F'В верхнем регистре: {hello.upper()}')
# Замените "World" на ваше имя
hello = 'Hello, Viktor!'
print(hello)
# Напишите программу, которая вычисляет площадь круга по заданному радиусу (используйте math.pi)
import math

radius = 5
print(f'Площадь круга: {math.pi * radius ** 2}')
# Создайте список чисел от 1 до 10, затем:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Удалите все четные числа
print(f'Убираем четные числа из списка: {lst[::2]}')
# Добавьте число 11 в конец
lst.append(11)
# Отсортируйте список в обратном порядке
lst.reverse()
print(f'Сортировка списка в обратном порядке: {lst[::2]}')

# 1.2 Условные операторы (if-elif-else)
# Напишите программу, которая проверяет, является ли число четным или нечетным
num = 12
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
# Напишите программу, которая определяет, является ли год високосным
year = 1700
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Год високосный.')
else:
    print('Год не високосный.')
# Создайте калькулятор ИМТ (индекс массы тела):
# Запросите вес (кг) и рост (м)
# Рассчитайте ИМТ (вес/рост²)
# Выведите категорию (недостаточный вес, норма, избыточный вес, ожирение)
weight = 60
height = 1.76
bmi = weight / height ** 2
print(f"Ваш ИМТ: {bmi:.2f}")

if bmi < 18.5:
    print('Дефицит массы тела')
elif 18.5 <= bmi < 25:
    print('Масса в норме')
elif 25 <= bmi < 30:
    print('Избыточная масса тела')
else:
    print('Ожирение')
# Напишите программу, которая определяет, является ли введенная строка палиндромом
text = 'rever'
cleaned_text = text.lower().replace(" ", "")  # Приводим к нижнему регистру и удаляем пробелы
if cleaned_text == cleaned_text[::-1]:
    print(f'Строка "{text}" является палиндромом')
else:
    print(f'Строка "{text}" не является палиндромом')
# Реализуйте простую систему аутентификации:
# Запросите логин и пароль
# Проверьте их (заранее заданные значения)
# Выведите сообщение об успехе/неудаче
ACCESS_DATA = {'login': 'admin', 'password': '1111'}
# user_login = input('Введите логин: ')
# user_password = input('Введите пароль: ')
# if user_login == ACCESS_DATA['login'] and user_password == ACCESS_DATA['password']:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# 1.3 Циклы (for, while)
# Напишите программу, которая выводит все числа от 1 до 100, кратные 3
for num in range(1, 100 + 1):
    if num % 3 == 0:
        print(num)
# Вычислите факториал числа N (используйте for и while)
num = 5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(f'Факториал числа {num}: {fact}')

num = 5
fact = 1
count = 1
while count < num + 1:
    fact = fact * count
    count += 1
print(f'Факториал числа {num}: {fact}')
# Напишите программу, которая выводит таблицу умножения для числа N
n = 6
for i in range(1, 10 + 1):
    print(f'{n} * {i} = {i * n}')
# Создайте программу "Угадай число":
# Компьютер загадывает число от 1 до 100
# Пользователь вводит предположения
# Программа подсказывает "больше" или "меньше"
# При угадывании выводит количество попыток
from random import randint

hidden_number = randint(1, 100)


# enter_number = int(input('Введите число: '))
# count = 1
# while enter_number != hidden_number:
#     if enter_number > hidden_number:
#         print('Ваше число больше чем загаданное компьютером ')
#         enter_number = int(input('Введите число: '))
#         count += 1
#     elif enter_number < hidden_number:
#         print('Ваше число меньше чем загаданное компьютером ')
#         enter_number = int(input('Введите число: '))
#         count += 1
# print(f'Вы угадали число. Кол-во попыток: {count}')

# 1.4 Функции (def, return, args/kwargs)
# Напишите функцию is_even, которая возвращает True, если число чётное.
def is_even(number):
    return number % 2 == 0


print(is_even(8))


# Создайте функцию max_of_three(a, b, c), возвращающую максимальное из трёх чисел.
def max_of_three(a, b, c):
    return max(a, b, c)


print(f'Максимальное из трех чисел: {max_of_three(2, 7, 5)}')


# Напишите функцию multiply_all, которая умножает все переданные числа (*args).
def multiply_all(*args):
    if not args:
        return 0  # или 1, в зависимости от логики
    prod = 1
    for number in args:
        prod *= number
    return prod


print(f'Произведение переданных чисел: {multiply_all(1, 2, 3)}')

# 1.5 Работа с файлами (open, read, write)
# Создайте файл notes.txt и запишите в него строку "Мои заметки".
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write('Мои заметки')
# Напишите программу, которая добавляет новые строки в файл без удаления старых.
with open('notes.txt', 'a', encoding='utf-8') as file:
    file.write('\n1. Начало')
# Прочитайте файл и выведите его содержимое.
with open('notes.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)


# Дополнительные задания
# Калькулятор: пользователь вводит два числа и операцию (+, -, *, /), программа выводит результат.
# def calc(a, b, operation):
#     if operation == '+':
#         return f'{a} + {b} = {a + b}'
#     elif operation == '-':
#         return f'{a} - {b} = {a - b}'
#     elif operation == '*':
#         return f'{a} * {b} = {a * b}'
#     elif operation == '/':
#         if b == 0:
#             return 'Ошибка: деление на ноль!'
#         return f'{a} / {b} = {a / b}'
#     else:
#         return 'Неизвестная операция!'
#
#
# operation = input('Введите операцию(+,-,*,/): ')
# print(calc(8, 2, operation))

# Задача: Простой парсер текста на Python
text = 'Привет, мир! Это тестовый текст. Текст содержит несколько предложений. Привет еще раз.'
words = []
current_word = ''
for char in text:
    if char.isalpha():
        current_word += char.lower()
    else:
        if current_word:
            words.append(current_word)
            current_word = ''
if current_word:
    words.append(current_word)

count_word = len(words)
unic_word = len(set(words))

count_symbol = len(text)
excluding_spaces = sum(1 for char in text if not char.isspace())

sentences = 0
for char in text:
    if char in '.!?':
        sentences += 1

word_counts = []
unique_words = list(set(words))

for word in unique_words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    word_counts.append((count, word))

word_counts.sort(reverse=True)

top_words = word_counts[:3]

print(f'Статистика текста:')
print(f'- Количество слов: {count_word}')
print(f'- Количество символов (с пробелами): {count_symbol}')
print(f'- Количество символов (без пробелов): {excluding_spaces}')
print(f'- Количество предложений: {sentences}')
print(f'- Количество уникальных слов: {unic_word}')
print('- Топ-3 слов:')
for i, (count, word) in enumerate(top_words, 1):
    print(f'  {i}. {word} - {count} раз' + ('а' if count > 1 else ''))