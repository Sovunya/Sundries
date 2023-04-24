# Впринципе то же самое что и первый клиент, сделан для проверки работы двух пользователей в одном чате.

import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.82.72.185', 55001))     #Вписываем айпишник пк-сервера
print('Подключение прошло успешно')
while True:
    print('Зарегистрироваться или авторизоваться?')
    start = input()
    sock.send(start.encode())
    if 'зар' in start.lower():
        name = input('Введите ваше имя: \n')
        password = input('Введите пароль: \n')
        string_to_send = f'{name} {password}'.encode()
        sock.send(string_to_send)
        continue
    elif 'авт' in start.lower():
        name = input('Введите ваше имя: \n')
        password = input('Введите пароль: \n')
        string_to_send = f'{name} {password}'.encode()
        sock.send(string_to_send)
        message = sock.recv(1024).decode()
        users = sock.recv(1024).decode()
        if message == 'Good':
            print(users)
            break
        else:
            print('Дырка')
            continue

def get_messages():
    while True:
        message = sock.recv(1024).decode()
        print(message)

thread1 = Thread(target = get_messages, daemon=True)
thread1.start()

while True:
    send_message = input()
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    to_send = f'{date} {name}:{send_message}'
    sock.send(to_send.encode())