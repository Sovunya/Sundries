# КХе ну ничего не обычного просто кодик который записывает все возможные комбинации символов в файлик(кто поймет тот поймет)
# Вообще это просто как показать вам насколько быстро можно подобрать ваш пароль если вы используете только символы из этого алфавита.
#Осторожнее, файлик содержащий числа до символов 7 будет весить гигов 30.

from itertools import product
import hashlib

alphabet = '0123456789.-'
#alphabet = '0123456789.-aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

password_length = 1

counter = 0
with open("example.txt", "w") as f:
    while password_length != 10:
        combinations = product(alphabet, repeat=password_length)

        for combination in combinations:
            possible_password = ''.join(combination)
            counter += 1
            f.write(f'{possible_password}\n')
            # Открывать нижнюю строчку на свой страх и риск! Сам код очень нагружает пк, так эта строчка просто заставит его страдать.
            # По сути комп записывает каждую вариацию, и если он не выводит ему легко, но вот выводить постоянно каждый символ затормаживает его.
            #(Это прикольно когда охото посмотреть насколько быстро он перебирает числа, но в ином случае лучше этого не выводить)
            #print(possible_password)

        password_length += 1