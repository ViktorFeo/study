# Основные методы HTTP-запросов:

# CRUD - это основные действия с данными:
# Create (Создать) - POST
# Read (Прочитать) - GET
# Update (Обновить) - PUT/PATCH
# Delete (Удалить) - DELETE

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
import pprint # Для удобного отображения словарей в терминале
response = requests.get('https://google.com')
print(response.status_code)
print(response.ok)  # Возвращает True если статус-код меньше 400 иначе False

if response.ok:
    print('OK')

# print(response.text)  # Ответ сервера в unicode в виде строки

response = requests.get('https://api.github.com')
print(response.status_code)
response_json = response.json() # Распарсит ответ и введет в виде пайтон словаря
pprint.pprint(response_json)
print(response_json['repository_search_url'])
print(response.headers)
print(response.request.headers)

params = {'q': 'python'}
response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
pprint.pprint(response_json)
print(response_json['total_count'])
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

# Асинхронные запросы
# Не блокируют выполнение программы. Пока один запрос ждёт ответа, программа может выполнять другие задачи.
# Используются в асинхронном программировании (asyncio, aiohttp).
# Требуют async/await синтаксиса.
# Эффективны при множестве I/O операций (например, много HTTP-запросов).

import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com') as response:
            print(await response.text())


# Запуск асинхронной функции
asyncio.run(main())


# GET-запросы
async def fetch_data():
    async with aiohttp.ClientSession() as session:
        # Простой GET
        async with session.get('https://api.github.com/events') as resp:
            print(resp.status)
            print(await resp.text())

        # GET с параметрами
        params = {'key1': 'value1', 'key2': 'value2'}
        async with session.get('https://httpbin.org/get', params=params) as resp:
            print(await resp.json())


asyncio.run(fetch_data())


# POST-запросы
async def post_data():
    async with aiohttp.ClientSession() as session:
        # POST с данными формы
        data = {'key': 'value'}
        async with session.post('https://httpbin.org/post', data=data) as resp:
            print(await resp.json())

        # POST с JSON
        json_data = {'key': 'value'}
        async with session.post('https://httpbin.org/post', json=json_data) as resp:
            print(await resp.json())


asyncio.run(post_data())


# Клиентские сессии
async def use_session():
    # Сессия сохраняет куки и заголовки между запросами
    async with aiohttp.ClientSession(
            headers={'User-Agent': 'my-app/0.0.1'},
            timeout=aiohttp.ClientTimeout(total=10)
    ) as session:
        async with session.get('https://api.github.com') as resp:
            print(await resp.json())

        async with session.get('https://api.github.com/user') as resp:
            print(await resp.json())


asyncio.run(use_session())


# Обработка ошибок
async def handle_errors():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://invalid-url') as resp:
                resp.raise_for_status()  # Аналогично requests
                print(await resp.text())
    except aiohttp.ClientError as e:
        print(f"Ошибка клиента: {e}")
    except asyncio.TimeoutError:
        print("Превышено время ожидания")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


asyncio.run(handle_errors())
