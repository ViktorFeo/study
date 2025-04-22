# Основные методы HTTP-запросов:

# GET - получение данных
# POST - отправка данных
# PUT - обновление данных
# DELETE - удаление данных
# PATCH - частичное обновление данных

# Структура HTTP-ответа включает:
# Статус код (200 OK, 404 Not Found и т.д.)
# Заголовки (мета-информация)
# Тело ответа (основные данные)

# Синхронные запросы
# Блокируют выполнение программы до завершения запроса.
# Код выполняется последовательно, шаг за шагом.
# Пока запрос выполняется, программа "висит" и ждёт ответа.
# Обычно используются стандартные библиотеки (requests, urllib).
# Пример синхронного запроса (с requests):

import requests

# Простой GET-запрос
response = requests.get("https://example.com")  # Блокирует выполнение
print(response.status_code)  # 200

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.text)  # Тело ответа

# GET с параметрами
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)  # https://httpbin.org/get?key1=value1&key2=value2

# Простой POST с данными формы
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

# POST с JSON
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())

# Отправка файла
files = {'file': open('notes.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
print(response.json())

# Заголовки и параметры:

# Пользовательские заголовки
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://api.github.com', headers=headers)

# Авторизация
from requests.auth import HTTPBasicAuth

response = requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', 'password')
)
# Или проще:
response = requests.get(
    'https://api.github.com/user',
    auth=('username', 'password')
)

# Обработка ответов
response = requests.get('https://api.github.com')

# Проверка статуса
if response.status_code == 200:
    print("Успешный запрос")
elif response.status_code == 404:
    print("Страница не найдена")

# Получение содержимого
content = response.text  # как строка
json_data = response.json()  # как JSON (если ответ в JSON)

# Заголовки ответа
print(response.headers)
print(response.headers['Content-Type'])

# Обработка ошибок
from requests.exceptions import RequestException

try:
    response = requests.get('https://invalid-url', timeout=5)
    response.raise_for_status()  # Вызовет исключение для 4XX/5XX ответов
except requests.exceptions.Timeout:
    print("Превышено время ожидания")
except requests.exceptions.TooManyRedirects:
    print("Слишком много перенаправлений")
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
