# Создаем хоста для мессенджера. Этот хост использует локальный айпишник получаемый через ipconfig.
# Когда пользователь запускает код клиента он регистрируется через хост этого пк(при этом все что необходимо иметь пользователю это код клиента и находиться в одной сети с хостом).
# Честно говоря я очень пытался продумать как создать потоки под каждого пользователя и чтобы они все сначала проходили авторизацию и потом только шли в общий чат,
# но я очень намучался с этим и оставлю этот код просто как рабочий вариант с помаркой на точ то сначала надо всем зарегаться и только потом общаться.
# Впринципе я еще попробую доработать его, но пока выложу хотя бы так (иначе блин и так в гитхабе мышь повесилась от скуки).

import socket
import client_database
from threading import Thread

# hostname = socket.gethostname()
# localip = socket.gethostbyname(hostname)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.82.72.185', 55001))  # Привязываем сервер к локальному айпишнику. Важно проверять его через ipconfig перед запуском хоста.
sock.listen(10)
print('Сервер запущен')

users = []  # Создаем список пользователей.

client_sockets = set() # Переменная в которой мы храним сокеты пользователей.


def reciver(
        cs):  # Регистрация и авторизация пользователя происсходит здесь. Пользователь выходит из цикла только когда авторизуется.
    while True:
        start = cs.recv(1024).decode()
        if 'зар' in start.lower():
            name, password = cs.recv(1024).decode().split()
            print(name, password)
            if not client_database.create(name, password):
                continue
        elif 'авт' in start.lower():
            name, password = cs.recv(1024).decode().split()
            if client_database.authenticate(name, password):
                if name not in users:
                    users.append(name)
                else:
                    cs.send((str('Bad').encode()))
                    cs.send((str('Bad').encode()))
                    continue
                cs.send('Good'.encode())
                cs.send(str(users).encode())

                break
            else:
                cs.send((str('Bad').encode()))
                cs.send((str('Bad').encode()))

    while True:  # Через этот цикл мы посылаем всем пользователям сообщения.
        try:
            msg = cs.recv(1024).decode()  # <-Вот тут принимает.
            if msg == 'exit' or msg == 'выход':
                if name in users:
                    users.remove(name)
                client_sockets.remove(cs)
                cs.close()
                break
        except:  # Здесь мы проверяем не отключился ли какой-нибудь пользователь. Если кто-нибудь отключился мы закрываем с ним соединение. Так же удаляем пользователя из списка.
            client_sockets.remove(cs)
            if name in users:
                users.remove(name)
            cs.close()
            break
        else:
            for i in client_sockets:  # Вот тут с рассылкаем всем подключенным пользователям.
                i.send(msg.encode())


while True:  # Множество в котором храним список пользователей.
    conn, addr = sock.accept()
    print('connected: ', addr)
    # data = conn.recv(1024)
    # print(str(data))
    client_sockets.add(conn)  # Функцией добавляем в список нового пользователя.

    thread = Thread(target=reciver, args=(conn, addr), daemon=True)
    thread.start()
