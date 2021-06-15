"""
Homework 5
Done by Saltykova Ekaterina

Task 2
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

symbol_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_to_dec(string):
    number = deque(string)
    number.reverse()
    decimal = 0

    for i in range(len(number)):
        decimal += symbol_table[number[i]] * 16 ** i

    return decimal


def dec_to_hex(integer):
    hexadecimal = deque()

    while integer > 0:
        remainder_dec = integer % 16
        for key, value in symbol_table.items():
            if value == remainder_dec:
                hexadecimal.appendleft(key)
        integer //= 16

    return hexadecimal


num_1 = hex_to_dec(input('Введите первое шестнадцатиричное число: ').upper())
num_2 = hex_to_dec(input('Введите второе шестнадцатиричное число: ').upper())

print(f'Результат сложения двух чисел: {list(dec_to_hex(num_1 + num_2))}')
print(f'Результат умножения двух чисел: {list(dec_to_hex(num_1 * num_2))}')

