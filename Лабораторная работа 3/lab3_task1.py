src = not False and True or False and not True

# TODO расписать упрощение выражения

result =  True and True or False and False  # Упростить оператор not
result =  True or False  # Упростить оператор and
result =  True  # Упростить оператор or
print(src == result)
# Результат проверки: Congratulations!
