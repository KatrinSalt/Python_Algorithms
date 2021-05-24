"""
Homework 1
Done by Saltykova Ekaterina

Task 1:
Выполнить логические побитовые операции “И”, “ИЛИ” и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

num_1 = 5
print(f'Десятичная система измерения: {num_1}, Двоичная система исчесления: {bin(num_1)}')

num_2 = 6
print(f'Десятичная система измерения: {num_2}, Двоичная система исчесления: {bin(num_2)}')

print(f'Выполним логические побитовые операции над числами {num_1} и {num_2}:')
bit_or = num_1 | num_2
bit_and = num_1 & num_2
bit_xor = num_1 ^ num_2

print(f'Побитовое \'ИЛИ\' чисел {num_1} и {num_2}: {bit_or} = {bin(bit_or)}')
print(f'Побитовое \'И\' чисел {num_1} и {num_2}: {bit_and} = {bin(bit_and)}')
print(f'Побитовое \'Исключающее ИЛИ\' чисел {num_1} и {num_2}: {bit_xor} = {bin(bit_xor)}')

shift_right = num_1 >> 2
shift_left = num_1 << 2

print(f'Логический \'сдвиг вправо\' на два бита числа {num_1}: {shift_right} = {bin(shift_right)}')
print(f'Логический \'сдвиг влево\' на два бита числа {num_1}: {shift_left} = {bin(shift_left)}')
