"""
Homework 3
Done by Saltykova Ekaterina

Task 3
В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.
"""
import random
# создаем массив случайных целых чисел
random_list = [random.randint(1, 100) for _ in range(10)]
print(f'Изначальный массив: {random_list}')

min_num = max_num = random_list[0]
for num in random_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

index_min = random_list.index(min_num)
index_max = random_list.index(max_num)
print(f'Минимальное значение в массиве и его индекс: {min_num}, {index_min}\n'
      f'Максимальное значение в массиве и его индекс: {max_num}, {index_max}')

random_list[index_min] = max_num
random_list[index_max] = min_num

print(f'Обновленный массив: {random_list}')

