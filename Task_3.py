"""
Homework 2
Done by Saltykova Ekaterina

Task 3
Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

number = input('Введите любое натуральное число: ')

# решение 1:
reversed_number_1 = ''.join(reversed(number))
print(reversed_number_1)

# решение 2:
print(number[::-1])

# решение 3:
number = int(number)
reversed_number_2 = 0

while number > 0:
    reversed_number_2 = reversed_number_2 * 10 + number % 10
    number //= 10
print(reversed_number_2)








