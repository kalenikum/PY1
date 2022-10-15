list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# находим индекс максимального элемента

max_idx = 0
max_val = list_numbers[0]
for i in range(len(list_numbers)):
    if list_numbers[i] > max_val:
        max_val = list_numbers[i]
        max_idx = i

# меняем элементы местами

list_numbers[max_idx], list_numbers[-1] = list_numbers[-1], list_numbers[max_idx]
print(list_numbers)
