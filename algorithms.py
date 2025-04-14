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