"""
2. Структуры данных (3-4 дня)
2.1 Списки, кортежи, множества, словари
2.2 Методы работы с ними (sort, map, filter, lambda)
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
from collections import defaultdict
words = ["xthtp", "ckjdfhb", "xthtp", "word", "ckjdfhb", "xthtp"]
frequency = defaultdict(int)
for word in words:
    frequency[word] += 1

for word, count in frequency.items():
    print(f"Слово '{word}' встречается {count} раз(а)")
# Объедините два словаря в один (если ключи совпадают, берётся значение из второго).
d1 = {'a': 1, 'b': 3}
d2 = {'b': 2}
merged = {**d1, **d2}
print(merged)
