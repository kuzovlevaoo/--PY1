# TODO написать функцию для получения списка уникальных целых чисел
import random
from random import randint
def get_unique_list_numbers() -> list[int]:
    list_ = set([randint(-10, 10) for _ in range(16)])
    list_ = set(list_)
    while len(list_) < 15:
        if randint(-10, 10) not in list_:
            list_.add(randint(-10, 10))
    return set(list_)


list_unique_numbers = get_unique_list_numbers()

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
