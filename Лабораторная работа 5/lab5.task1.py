# TODO решить с помощью list comprehension и распечатать его

# определим функцию, возвращающую словарь нужного формата
def dicmaker( i:int ):
    out_ = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    return out_

# импортируем функцию pprint
from pprint import pprint

# сохраним границы для избегания магических чисел
minznach = 0
maxznach = 15

# создадим список из словарей с помощью list comprehension
out_ = [dicmaker(key) for key in range(minznach, maxznach + 1)]

# Распечатать этот список с помощью функции pprint из модуля pprint
pprint(out_)