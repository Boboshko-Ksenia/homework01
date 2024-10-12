import requests
# імпортуємо модуль requests для роботи з ним
from .read_json import read_json
# з модуля read_json імпортуємо функцію read_json
import json
# імпортуємо модуль json
data_api = read_json(name_file= 'config_api.json')
# створюємо змінну та задаємо параметр з типом данних str
API_KEY = data_api['api_key']
# створюємо константу зі спеціальним ключем для користувача
CITY_NAME = data_api['city_name']
# створюємо константу для запису міста
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# константа з адрессою в якій записано місто та ключ
response = requests.get(URL)
# відправляємо запрос на отримання адресси
if response.status_code == 200:
    # якщо відповідь була отримана з адресси, то
    data_dict = json.loads(response.content)
    # перетворює відповідь з формата json в об'єкт python
    print(json.dumps(data_dict, indent= 4))