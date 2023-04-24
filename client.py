# Эта часть кода находится у пользователя. С ее помощью происходит регистрация, авторизация и отправка сообщений.
# Этот код относится к первой версии(если последующие вообще будут) хоста в котором рекомендуется сначала всех зарегать.

import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.82.72.185', 55001))     # Вписываем айпишник пк-сервера.
print('Подключение прошло успешно')
while True: # Проходим регистрацию.
    print('Зарегистрироваться или авторизоваться?')
    start = input() # Сюда вводится первое сообщение которое определяет хочет пользователь зарегестрироваться или авторизоваться.
    sock.send(start.encode())   # Сообщение кодируется и отправляетсся на хост где его принимают и декодируют.
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
        else:   # Ошибка в случае если пользователь неыерно ввел данные или пользователь уже в сети.
            print('Дырка')
            continue

def get_messages(): #Получаем сообщения из чата.
    while True:
        message = sock.recv(1024).decode()
        print(message)

thread1 = Thread(target = get_messages, daemon=True)    # Создаем поток, который будет выполняться в фоновом режиме.
thread1.start()

while True: #Отправляем в чат сообщения.
    send_message = input()
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    to_send = f'{date} {name}:{send_message}'
    sock.send(to_send.encode())