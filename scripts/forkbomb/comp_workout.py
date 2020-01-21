import base64
import json

import requests


def to_int(num):
    return int.from_bytes(bytes.fromhex(num), byteorder='little', signed=True)


def parse_input(string):
    left, right = string.split('<')
    a, b = to_int(left), to_int(right)
    return a, b


s = requests.Session()
r = s.get("https://compworkout.forkbomb.ru/")

for i in range(37):
    response = s.get("https://compworkout.forkbomb.ru/gettask")
    task = base64.b64decode(json.loads(response.text)['task']).decode()
    print(i, task)

    a, b = parse_input(task)
    r = s.post("https://compworkout.forkbomb.ru/verify",
               data=json.dumps({"ans": int(a < b)}),
               headers={"Content-Type": "application/json"})

