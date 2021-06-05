"""
Homework 3
Done by Saltykova Ekaterina

Task 6
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
random_list = [random.randint(1, 100) for _ in range(15)]
print(f'Массив: {random_list}')

min_num = max_num = random_list[0]
index_min = index_max = 0
for index in range(len(random_list)):
    if random_list[index] > max_num:
        max_num = random_list[index]
        index_max = index
    if random_list[index] < min_num:
        min_num = random_list[index]
        index_min = index

print(f'Минимальный элемент: {min_num}, индекс: {index_min}\n'
      f'Максимальный элемент: {max_num}, индекс: {index_max}')

sum_arr = 0
if index_min < index_max:
    for index in range(index_min + 1, index_max):
        sum_arr += random_list[index]
else:
    for index in range(index_max + 1, index_min):
        sum_arr += random_list[index]

print(f'Сумма элементов между минимальным и максимальным элементом: {sum_arr}')
