# посчитаем расходы как сумму геом. прогрессии, без циклов
# разница с доходами и будет искомое значение

def func_need_money(salary, spend, months, increase):

    return_value = (spend * ((1 + increase) ** months - 1)) \
                   / increase - salary * months
    return (return_value)

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = func_need_money(salary, spend, months, increase)  # количество денег, чтобы прожить 10 месяцев

print(round(need_money))
