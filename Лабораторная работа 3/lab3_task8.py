# Решение оформите в виде функции

# определим функцию расчёта расходов
def func_spend (spend_, month_, increase_):
    return_value = spend_*(month_ + 1) * (1 + increase_)
    return return_value


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

# сравниваем расходы на конец месяца с доходами
while money_capital + salary * month > func_spend(spend, month, increase):
    month += 1

print(month)

