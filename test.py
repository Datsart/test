import requests
from random import randint

res = requests.post('http://127.0.0.1:8000/test', headers={'Contant-type': 'application/json'}, json=randint(1, 100))
print(res.text)
