money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while money_capital >= 1:
    money_capital = money_capital - spend + salary
    spend = spend * 1.05
    month += 1
    if money_capital < spend:
        break


print(month)
