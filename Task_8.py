"""
Homework 1
Done by Saltykova Ekaterina

Task 8:
Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if (b > a > c) or (c > a > b):
    print(f'Среднее число - {a}')
elif (a > b > c) or (c > b > a):
    print(f'Среднее число - {b}')
elif (a > c > b) or (b > c > a):
    print(f'Среднее число - {c}')
else:
    print('Здесь нет среднего числа.')
