import requests
from random import randint


def req():
    req = requests.post(
        "http://127.0.0.1:5000/test",
        headers={"Content-type": "application/json"},
        json=randint(1, 100),
    )

    print(req.text)
