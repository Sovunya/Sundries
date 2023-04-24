# Пробиваем хэши и находим ключи от них
# А вот эта штука уже побрутальнее. У нас имеются хэши и мы декодируем их выискивая закодированное слово. Не до конца кстати понимаю как что происходит...

from itertools import product
import hashlib

alphabet = 'abcdefghijklmnopqrstuvwxyz'
hashes = {"d64cced9ecdc8fc643844b8f7083bdc3", "c43c73b27f50673486f948dc49ee010a", "ec9403fedd76a10c9ccc215a6f174b15"}

password_length = 1
found = False

passwd = {}
counter = 0

while len(hashes) != 0:
    combinations = product(alphabet, repeat=password_length)

    for combination in combinations:
        possible_password = ''.join(combination)
        pass_hash = hashlib.md5(possible_password.encode('utf-8')).hexdigest()

        counter += 1

        if counter % 100000 == 0:
            print(f'possible_password = {possible_password}, hash = {pass_hash}')

        if pass_hash in hashes:
            passwd[pass_hash] = possible_password
            hashes.remove(pass_hash)

    password_length += 1

print(passwd)