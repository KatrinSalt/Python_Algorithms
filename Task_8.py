"""
Homework 3
Done by Saltykova Ekaterina

Task 8
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой
строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

matrix = [[int(input('Введите эл-т матрицы: ')) for _ in range(4)] for _ in range(4)]


for line in matrix:
    sum_row = 0
    for elem in line:
        sum_row += elem
    line.append(sum_row)

for line in matrix:
    for elem in line:
        print(f'{elem:>4}', end='')
    print()


