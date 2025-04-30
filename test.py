import my_module

my_module.hello()


# Задание 1.1: Калькулятор
# Напиши функцию calculator(a, b, operation), которая:
# Принимает два числа (a, b) и строку operation (+, -, *, /).
# Возвращает результат операции или None, если операция не поддерживается.

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b if b != 0 else 'На ноль делить нельзя!'
    elif operation == '*':
        return a * b
    else:
        return 'Команда не может быть выполнена.'


print(calculator(1, 3, "+"))  # 8
print(calculator(2, 0, "/"))  # 5.0
print(calculator(7, 4, "*"))  # None


# Задание 1.2: Чётные числа
# Напиши функцию even_numbers(numbers), которая:
# Принимает список чисел.
# Возвращает новый список только с чётными числами (или пустой список, если чётных нет).

def even_numbers(list_of_numbers):
    new_list = [i for i in list_of_numbers if i % 2 != 1]
    return new_list


print(even_numbers([1, 2, 3, 4, 5]))  # [2, 4]
print(even_numbers([1, 3, 5]))  # []


# Задание 1.3: Поиск максимального числа
# Напиши функцию find_max(numbers), которая:
# Принимает список чисел
# Возвращает наибольшее число в списке
# Если список пустой, возвращает None

def find_max(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    # return max(numbers) if numbers else None


print(find_max([1, 5, 3, 9, 2]))  # 9
print(find_max([]))  # None


# Задание 1.4: Подсчет слов
# Напиши функцию count_words(text), которая:
# Принимает строку
# Возвращает количество слов в строке
# Словом считается любая последовательность символов, разделенная пробелами

def count_words(text):
    return len(text.split())


print(count_words("Hello world"))  # 2
print(count_words(""))  # 0
print(count_words("   "))  # 0


# Задание 1.5: Обработка списка
# Напиши функцию process_list(numbers), которая:
# Принимает список чисел
# Возвращает новый список, где:
# Четные числа умножены на 2
# Нечетные числа уменьшены на 1
# Числа меньше 0 остаются без изменений
# Если список пустой, возвращает пустой список

def process_list(numbers):
    if not numbers:
        return numbers

    new_list = []
    for i in numbers:
        if i % 2 != 1 and i > 0:
            new_list.append(i * 2)
        elif i % 2 == 1 and i > 0:
            new_list.append(i - 1)
        elif i <= 0:
            new_list.append(i)
    return new_list
    # return [
    #     num * 2 if num > 0 and num % 2 == 0 else num
    #     - 1 if num > 0 and num % 2 != 0 else num
    #     for num in numbers
    # ]


print(process_list([1, 2, 3, 4, 5]))  # [0, 4, 2, 8, 4]
print(process_list([-1, -2, 0, 6]))  # [-1, -2, 0, 12]
print(process_list([]))  # []


# Задание 1.6: Поиск уникальных элементов
# Напиши функцию find_unique(numbers), которая:
# Принимает список чисел
# Возвращает новый список, содержащий только уникальные элементы (в порядке первого вхождения)
# Если список пустой, возвращает пустой список

def count_duplicates(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts


print(count_duplicates([1, 2, 2, 3]))  # {1: 1, 2: 2, 3: 1}
print(count_duplicates([]))  # {}


# Задание 1.8: Фильтр строк
# Напиши функцию filter_strings(strings, min_len), которая:
# Принимает список строк и минимальную длину
# Возвращает новый список со строками, длина которых >= min_len
# Сохраняет исходный порядок
# Для пустого списка возвращает пустой список
def filter_strings(strings, min_len):
    return [i for i in strings if len(i) >= min_len]


print(filter_strings(["cat", "dog", "elephant"], 4))  # ["elephant"]
print(filter_strings([], 5))  # []


# Усложнённое задание 1.9:
# Напиши функцию count_vowels(string), которая:
# Принимает строку
# Возвращает количество гласных букв (a,e,i,o,u, без учёта регистра)
# Для пустой строки возвращает 0
def count_vowels(string):
    pass


print(count_vowels("Hello World"))  # 3 (e,o,o)
print(count_vowels("Python"))  # 1 (o)
