money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
a = 6000
month = 0  # количество месяцев, которое можно прожить

while money_capital + (salary * month) >= a :
    month += 1
    a += spend * ((1+ increase)**month)

    # TODO Оформить решение

print(month)
