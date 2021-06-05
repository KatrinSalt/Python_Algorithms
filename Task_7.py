"""
Homework 3
Done by Saltykova Ekaterina

Task 7
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random
random_list = [random.randint(1, 15) for _ in range(20)]
print(random_list)

if random_list[0] < random_list[1]:
    min_num1, min_num2 = random_list[0], random_list[1]
else:
    min_num1, min_num2 = random_list[1], random_list[0]


for index in range(2, len(random_list)):
    if min_num2 >= random_list[index] >= min_num1:
        min_num2 = random_list[index]
    elif min_num2 >= min_num1 >= random_list[index]:
        min_num2 = min_num1
        min_num1 = random_list[index]
print(f'Два минимальных значения в массиве: {min_num1}, {min_num2}')
