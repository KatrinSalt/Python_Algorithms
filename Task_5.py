"""
Homework 3
Done by Saltykova Ekaterina

Task 5
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
import random
import math
random_list = [random.randint(-50, 50) for _ in range(10)]
print(random_list)

max_neg = -math.inf
for val in random_list:
    if 0 > val > max_neg:
        max_neg = val
print(f'Максимальный отрицательный элемент в массиве: {max_neg}')