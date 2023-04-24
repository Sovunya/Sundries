# Хитрая упрощенная версия в которой не нужна бд и вы просто сами вводите себе логин.
# (блин, по сути в ней нет проблемы с потоками потому что в них нет сильной необходимости).

import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.82.79.188", 55001))     #Вписываем айпишник пк-сервера.
print('Подключение прошло успешно')
name = input('Введите свое имя: ')

def get_messages(): #Получаем сообщения с хоста от других пользователей и декодируем их.
    while True:
        message = sock.recv(1024).decode()
        print(message)

thread1 = Thread(target = get_messages, daemon=True)
thread1.start()

while True: # Сюда вводим свои сообщения которые принимают вид дата\время\ник\сообщение и текст кодируется.
    send_message = input()
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    to_send = f'{date} {name}:{send_message}'
    sock.send(to_send.encode())