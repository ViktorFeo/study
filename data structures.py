"""
2. Структуры данных (3-4 дня)
2.1 Списки, кортежи, множества, словари
2.2 Методы работы с ними (sort, map, filter, lambda)
# sort() – сортирует список на месте (изменяет исходный список).
# sorted() – возвращает новый отсортированный список, не изменяя исходный.
# map() – Применяет функцию ко всем элементам коллекции.
# filter() - Оставляет только те элементы, которые удовлетворяют условию.
2.3 List/Dict comprehensions
2.4 Итераторы и генераторы

Практика:
Проект: Парсинг CSV/JSON (например, анализ данных о погоде)
"""


# 2.1 Списки, кортежи, множества, словари
# Напишите функцию, которая удаляет дубликаты из списка.
def remove_duplicate(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


print(remove_duplicate([1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 7, 8]))


# Напишите функцию, которая находит второй максимальный элемент в списке.
def second_max_item(lst):
    if len(lst) < 2:
        return None
    max1 = max(lst)
    lst_copy = lst.copy()
    while max1 in lst_copy:
        lst_copy.remove(max1)

    if not lst_copy:
        return None
    return max(lst_copy)


print(second_max_item([1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 7, 8, 8]))  # 7
# Дан список чисел. Разделите его на два списка: чётных и нечётных чисел.
lst = [1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 7, 8, 8]
even_lst = [x for x in lst if x % 2 == 0]  # Чётные числа
odd_lst = [x for x in lst if x % 2 != 0]  # Нечётные числа


# Напишите функцию, которая принимает два кортежа и возвращает кортеж из их общих элементов.
def tuples(tuple1, tuple2):
    new_tuple = []
    for i in tuple1:
        if i in tuple2:
            new_tuple.append(i)
    return tuple(new_tuple)


print(tuples((1, 2, 3, 4, 5), (1, 3, 7, 9, 5)))
# Дан кортеж чисел. Посчитайте сумму всех элементов.
number_tuple = (1, 2, 3, 4, 5)
print(sum(number_tuple))
# Создайте кортеж из 5 разных типов данных (int, str, float, bool, list).
bad_tuple = (1, '2', 3.0, True, [1, 2, 3])
print(bad_tuple)
# Удалите все дубликаты из списка, используя множество.
lst = [1, 2, 3, 2, 4, 5, 6, 5, 5, 7, 7, 8, 8]
print(set(lst))


def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_s = set(s.lower())
    return alphabet.issubset(letters_in_s)


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello, world!"))

# Напишите функцию, которая инвертирует словарь (ключи ↔ значения).
d = {'a': 1, 'b': 2}
d2 = dict()
for key, value in d.items():
    d2.update({value: key})
print(d2)
# Дан список слов. Посчитайте частоту каждого слова.
words = ["xthtp", "ckjdfhb", "xthtp", "word", "ckjdfhb", "xthtp"]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"Слово '{word}' встречается {count} раз(а)")
# Объедините два словаря в один (если ключи совпадают, берётся значение из второго).
d1 = {'a': 1, 'b': 3}
d2 = {'b': 2}
merged = {**d1, **d2}
print(merged)
# Отсортируйте список строк по длине.
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)
print(words)
# Дан список кортежей (имя, возраст). Отсортируйте его по возрасту в порядке убывания.
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people_sorted = sorted(people, key=lambda x: x[1], reverse=True)
print(people_sorted)
print(people[1][1])
# Преобразуйте список чисел в список строк.
numbers = [1, 2, 3, 4]
str_numbers = list(map(str, numbers))
print(str_numbers)
# Дан список имён. Создайте список приветствий: "Hello, {name}!".
names = ["Alice", "Bob", "Charlie"]
greet = list(map(lambda x: f'Hello, {x}', names))
print(greet)
# Отфильтруйте список чисел, оставив только положительные.
numbers = [-2, -1, 0, 1, 2]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)
# Дан список слов. Оставьте только те, которые начинаются на букву 'a'.
words = ["apple", "banana", "avocado", "cherry"]
new_words = list(filter(lambda x: x.startswith('a'), words))
print(new_words)
# Возведите все числа в квадрат и оставьте только чётные результаты.
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(new_numbers)
# Из списка строк выберите те, длина которых >3, и преобразуйте их в верхний регистр.
words = ["cat", "dog", "elephant", "fox"]
new_words = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, words)))
print(new_words)

pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Создайте список первых 10 кубов чисел
print([x ** 3 for x in range(1, 11)])
# Создайте словарь, где ключи - числа от 1 до 5, а значения - их факториалы
s = [s for s in range(1, 6)]
print({s: s * s * s for s in s})
# Отфильтруйте список слов, оставив только те, что начинаются с буквы 'a'
words = ["apple", "banana", "avocado", "cherry"]
new_words = [s for s in words if s.startswith('a')]
print(new_words)
# Создайте словарь из списка строк, где ключ - строка, а значение - ее длина, но только для строк длиннее 3 символов
words = ["cat", "dog", "elephant", "fox"]
new_words = {s: len(s) for s in words if len(s) > 3}
print(new_words)

numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))


def count_up_to(max_num):
    current = 1
    while current <= max_num:
        yield current
        current += 1


counter = count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))

squares = (x ** 2 for x in range(5))  # генераторное выражение

print(next(squares))
print(next(squares))
print(next(squares))


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2

# Напишите код, который создаёт итератор из списка строк и выводит каждый элемент по очереди с помощью next().
fruits = ["apple", "banana", "cherry"]
iter_fruits = iter(fruits)
print(next(iter_fruits))
print(next(iter_fruits))


# Создайте генератор even_numbers(n), который возвращает чётные числа от 0 до n (включительно).
def even_numbers(n):
    for num in range(0, n + 1, 2):
        yield num


for num in even_numbers(5):
    print(num)

print()

# Напишите генератор random_numbers(count, max_num), который генерирует count случайных чисел от 0 до max_num.
import random


def random_numbers(count, max_num):
    for _ in range(count):
        yield random.randint(0, max_num)


for num in random_numbers(3, 10):
    print(num)

print()
# Создайте итератор из списка чисел, который останавливается, когда встречает число -1.
numbers = [2, 4, 6, -1, 8, 10]
iterator = iter(lambda i=iter(numbers): next(i), -1)
for num in iterator:
    print(num)


# Напишите генератор read_lines(filename), который построчно читает файл и возвращает строки без символа \n.
def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


for line in read_lines("notes.txt"):
    print(line)
