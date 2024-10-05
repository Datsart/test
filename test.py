import requests
import random

try:
    res = requests.post(url='http://127.0.0.1:8000/test', headers={'Content-type': 'application/json'},
                        json=random.randint(1, 100))
    print(res.status_code)
    print(res.text)
except BaseException as e:
    print('Ошибка нахуй -', e)
