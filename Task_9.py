"""
Homework 3
Done by Saltykova Ekaterina

Task 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random
matrix = [[random.randint(1,10) for _ in range(5)] for _ in range(4)]
print(matrix)

min_arr = []
for i in range(len(matrix[0])):
    min_elem = matrix[0][i]
    for line in matrix:
        if line[i] < min_elem:
            min_elem = line[i]
    min_arr.append(min_elem)

max_elem = min_arr[0]
for elem in min_arr:
    if elem > max_elem:
        max_elem = elem
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_elem}')
