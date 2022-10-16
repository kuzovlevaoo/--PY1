salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
y = 0
while y != 10:
    x = (salary - spend)* -1
    spend = spend * 1.03
    need_money += x
    y += 1

print(round(need_money))
