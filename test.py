# Задача 1: Напиши программу, которая находит наибольшее число в списке без использования max().
numbers = [1, 7, 3, 2, 5]
temp = 0
for i in numbers:
    if i > temp:
        temp = i
print(temp)

# Задача 2: Сумма всех чётных чисел от 1 до N.
n = 10
summ = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        summ += i
print(summ)

# Напиши функцию calculate, которая:
# Принимает два числа и операцию (+, -, *, /)
# Возвращает результат или None, если операция не поддерживается
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else None
    else:
        return None

print(calculate(22, 15, "-"))

# Валидатор пароля
# Функция validate_password, которая проверяет:
# Длина >= 8 символов
# Есть хотя бы одна цифра
# Есть хотя бы одна заглавная буква

def validate_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    return len(password) >= 8 and has_digit and has_upper

print(validate_password("Pass123"))