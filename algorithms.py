from os.path import devnull


def linear_search(lst, target):  # Передаем список и искомое число
    for i in range(len(lst)):  # Перебор индексов списка
        if lst[i] == target:  # Если элемент под индексом i == искомому числу
            return f'Число {target} под индексом {i}.'  # Возвращаем индекс числа
    return f'Числа {target} нет в списке.'  # Если не нашли число в списке


print(linear_search([3, 7, 12, 5, 9, 1], 99))
print(linear_search([3, 7, 12, 5, 9, 1], 9))


# Реализуйте линейный поиск для поиска всех вхождений элемента в список
def line_search(lst, target):
    occurrences = []
    for i in range(len(lst)):
        if lst[i] == target:
            occurrences.append(i)
    return occurrences


lst = [1, 3, 7, 2, 4, 3, 5, 9, 4, 2, 9, 3]
print(line_search(lst, 3))


# Реализация бинарного поиска
def binary_search(lst, target):
    left = 0  # Первый индекс списка
    right = len(lst) - 1  # Последний индекс списка

    while left <= right:
        mid = (left + right) // 2  # Находим средний индекс
        if lst[mid] == target:  # Если средний индекс равен искомому числу
            return mid  # Возвращаем индекс
        elif lst[mid] < target:  # Если средний индекс меньше искомого числа
            left = mid + 1  # Середина + 1
        else:  # Иначе
            right = mid - 1  # Средний индекс - 1

    return f'Элемент {target} не найден'  # Возвращаем если число не найдено


print(binary_search([1, 2, 3, 4, 5], 5))


# Модифицируйте бинарный поиск для работы с убывающим отсортированным массивом
def binary_search(lst, target):
    left = 0  # Первый индекс списка
    right = len(lst) - 1  # Последний индекс списка

    while left <= right:
        mid = (left + right) // 2  # Находим средний индекс
        if lst[mid] == target:  # Если средний индекс равен искомому числу
            return mid  # Возвращаем индекс
        elif lst[mid] > target:  # Если средний индекс больше искомого числа
            left = mid + 1  # Середина + 1
        else:  # Иначе
            right = mid - 1  # Средний индекс - 1

    return f'Элемент {target} не найден'  # Возвращаем если число не найдено


print(binary_search([5, 4, 3, 2, 1], 1))


# Напишите функцию, которая определяет, нужно ли использовать линейный или бинарный поиск
def search_select(lst):
    temp = lst[0]
    for i in lst:
        if i < temp:
            return f'Необходим линейный поиск'
        else:
            temp = i
    return f'Необходим бинарный поиск'


print(search_select([1, 2, 3, 6, 5]))


# Реализуйте линейный поиск для поиска первого/последнего вхождения элемента в массиве с дубликатами
def first_last_occurrences(lst, target):
    first = None
    last = None
    for i, num in enumerate(lst):
        if num == target:
            if first is None:
                first = i
            last = i
    return (first, last) if first is not None else (None, None)


print(first_last_occurrences([1, 2, 3, 4, 4, 5, 6, 3, 7, 8, 3, 5, 9], 1))  # Вывод: (2, 10)


# Реализуйте бинарный поиск для поиска первого/последнего вхождения элемента в массиве с дубликатами
def binary_search(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)
    return (first, last) if first != -1 and last != -1 else (-1, -1)


def find_first(arr, target):
    left, right = 0, len(arr) - 1
    first = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  # Продолжаем искать в левой части
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first


def find_last(arr, target):
    left, right = 0, len(arr) - 1
    last = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1  # Продолжаем искать в правой части
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last


print(binary_search([1, 2, 3, 3, 3, 3, 3, 3, 4, 5], 3))  # (2, 7)


# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Меняем местами
                swapped = True
        n -= 1  # Уменьшаем длину, т.к. последний элемент уже на месте
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)


# Рекурсия
def countdown(x):
    if x == 0:  # Базовый случай, останавливает рекурсию
        print('Поехали')
    else:
        print(x)
        countdown(x - 1)  # Рекурсивный вызов


countdown(5)


def fact(n):
    if n == 1:  # Базовый случай
        return 1
    else:
        return n * fact(n - 1)  # Рекурсивный вызов


print(fact(5))


# Напиши рекурсивную функцию, которая выводит числа Фибоначчи.
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(6))


# Сумма чисел от 1 до N
def summ(n):
    if n <= 1:
        return 1
    else:
        return n + summ(n - 1)


print(summ(5))


# Напишите рекурсивную функцию power(a, b), которая возвращает a в степени b
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


print(power(2, 3))


# Напишите рекурсивную функцию, которая возвращает сумму цифр числа.
def summa(n):
    if len(str(n)) == 1:
        return n
    else:
        return summa(n % 10) + summa(n // 10)


print(summa(1234))


# Напишите рекурсивную функцию, которая проверяет, является ли строка палиндромом.
def pal(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return pal(word[1:-1])


print(pal('racecar'))


# Напишите рекурсивную функцию, которая разворачивает строку.
def invert(word):
    if len(word) <= 1:
        return word
    else:
        return invert(word[1:]) + word[0]


print(invert('hello'))


# Напишите рекурсивную функцию для нахождения наибольшего общего делителя (НОД) двух чисел
def divider(a, b):
    if b == 0:
        return a
    else:
        return divider(b, a % b)


print(f'НОД: {divider(48, 18)}')


# Написать рекурсивную функцию, которая считает количество элементов в списке.\
def count_elements(lst):
    if not lst:
        return 0
    else:
        print(lst)
        return 1 + count_elements(lst[1::])


print(count_elements([1, 2, 3, 4]))


# Написать рекурсивную функцию для нахождения минимального числа в списке.
def find_min(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min(lst[1:]))


print(find_min([3, 7, 2, 4, 1]))


# Написать рекурсивную функцию multiply(a, b), которая возвращает произведение чисел a и b, используя только сложение.
def multiply(a, b):
    if b == 0:
        return 0  # Правильный базовый случай!
    else:
        return a + multiply(a, b - 1)


print(multiply(3, 4))


# Написать рекурсивную функцию, которая проверяет, есть ли элемент в списке.
def contains(a, b):
    if b in a: return True
    if b not in a: return False
    if len(a) == 1:
        return a[0]
    else:
        return contains(a[1:], b)


print(contains([1, 2, 3, 4], 5))

print('------')


# Написать рекурсивную функцию, которая считает, сколько раз элемент встречается в списке.
def count_occurrences(a, b):
    if not a:
        return 0
    if a[0] == b:
        return 1 + count_occurrences(a[1:], b)
    else:
        return count_occurrences(a[1:], b)


# Быстрая сортировка (Quick sort)
def quick_sort(arr):
    # Базовый случай: массивы длиной 0 или 1 уже "отсортированы"
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент (здесь - средний)
    pivot = arr[len(arr) // 2]

    # Разделяем элементы на три списка
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортируем левую и правую части и объединяем
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([8, 6, 9, 7, 5, 4, 1, 3, 2]))


def quick_sort_inplace(arr, low=0,
                       high=None):  # arr - массив, low - начальный индекс, high = конечный индекс подмассива
    if high is None:
        high = len(arr) - 1  # Если high не передан (первый вызов), устанавливаем его в последний индекс массива.

    if low < high:  # если массив не пуст или содержит не 1 элемент
        pi = partition(arr, low, high)
        # partition — функция, которая переупорядочивает массив так, чтобы:
        # Все элементы меньше опорного оказались слева.
        # Все элементы больше опорного — справа.
        # pi — индекс опорного элемента после разделения.

        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low,
              high):  # Принимает массив arr и границы low и high. Возвращает индекс опорного элемента после разделения.
    pivot = arr[high]  # Опорный элемент (pivot) выбирается как последний элемент подмассива (arr[high]).
    i = low - 1  # i — индекс, который будет указывать на последний элемент, меньший pivot. Начинаем с low - 1,
    # потому что пока не нашли ни одного такого элемента.
    for j in range(low, high):  # j проходит от low до high - 1 (не включая high, так как pivot = arr[high]).
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # Если arr[j] <= pivot, значит, его нужно переместить в левую часть.
            # Увеличиваем i и меняем местами arr[i] и arr[j].
            # Теперь все элементы до i гарантированно ≤ pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # После цикла i указывает на последний элемент, меньший pivot.
    # Поэтому pivot (arr[high]) ставим на позицию i + 1.
    # Теперь:
    # Слева от pivot — элементы ≤ ему.
    # Справа — элементы > него.

    return i + 1


print(quick_sort_inplace([3, 6, 8, 2, 5, 4], 0, 5))
data = [3, 6, 8, 10, 1, 2, 1]
sorted_data = quick_sort(data)
print(quick_sort_inplace([3, 6, 8, 10, 1, 2, 1]))  # [1, 1, 2, 3, 6, 8, 10]
