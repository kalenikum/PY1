import random
def get_unique_list_numbers() -> list[int]:
# зададим значения (чтобы не было магических чисел)
    min_ = -10
    max_ = 10
    len_ = 15
    out_ = []
# в цикле с постусловием бросаем кости, пока не выпадут уникальные значения
    while True:
        out_ = [random.randint(-10,10) for _ in range(15)]
        if len(out_) == len(set(out_)):
            break
   return out_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
