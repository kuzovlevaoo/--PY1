# TODO написать функцию генерации случайных паролей
import random
def get_random_password() -> str:
    str_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password_ = random.sample(str_, 8, counts=None)
    return ''.join(password_)




print(get_random_password())
