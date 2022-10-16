list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
x = max(list_numbers) #90
y = list_numbers[19]  #25
u = list_numbers.index(x)
list_numbers[19] = x
list_numbers[u] = y
# TODO Оформить решение

print(list_numbers)