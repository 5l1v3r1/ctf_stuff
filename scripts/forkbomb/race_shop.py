from multiprocessing import Pool
import requests
import string
import random

alphabet = string.printable
session = requests.Session()

url_shop = 'http://shop2.race.sinketsu.ru/'
users = []
users_count = 20

def generate_string():
    len = random.randint(30, 40)
    string = ''
    for i in range(len):
        string += alphabet[random.randint(0, len-1)]
    return string


def reg(user):
    r = session.post(url_shop + 'signup', data=user)
    print('Reg new user:', user, 'Status: ', r)
    users.append({'login': user['login'], 'password': user['password'], 'cookie': session.cookies.get_dict()})


def share_money(x):
    data = users[x]
    r = requests.post(url_shop + 'share', data={
        'login': users[0]['login'],
        'money': 100
        }, cookies=data['cookie'])


for i in range(users_count):
    reg({'login': generate_string(), 'password': generate_string()})

p = Pool(users_count)
p.map(share_money, range(users_count))
print("Login as ", users[0])