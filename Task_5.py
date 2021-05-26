"""
Homework 1
Done by Saltykova Ekaterina

Task 5:
 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

ch_number = int(input('Введите номер буквы алфавита (от 0 до 26): '))
char = chr(ch_number + 96)
print(f'Буква под номером {ch_number}: {char}')
