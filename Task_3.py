"""
Homework 1
Done by Saltykova Ekaterina

Task 3:
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random
import string

print('Введите диапазон (два числа) для генерации:\nа) случайного целого числа')
n1 = int(input('Первое число: '))
n2 = int(input('Второе число: '))
random_number = random.randint(n1, n2)
print(f'Случайное число: {random_number}')

print('б) случайного вещественного числа')
n1 = float(input('Первое число: '))
n2 = float(input('Второе число: '))
random_number = round(random.uniform(n1, n2), 2)
print(f'Случайное число: {random_number}')

print('в) случайного символа')
letters = string.ascii_letters
n1 = ord(input('Первый символ: '))
n2 = ord(input('Второй символ: '))
random_number = chr(random.randint(n1, n2))
print(f'Случайный символ: {random_number}')







