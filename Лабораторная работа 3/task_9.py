salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
a= 6000
for i in range(months):

    if i > 1:
        a += spend * ((1 + increase)**i)
    else:
        a += spend
salary *= 10
need_money = a - salary# TODO Оформить решение

print(round(need_money))
