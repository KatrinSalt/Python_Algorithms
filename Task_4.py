"""
Homework 1
Done by Saltykova Ekaterina

Task 4:
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

print('Введите две строчные буквы: ')
ch1 = input('Первая буква: ')
ch2 = input('Вторая буква: ')

ch1_p = ord(ch1)-96
ch2_p = ord(ch2)-96
distance = ch2_p - ch1_p - 1
print(f'Буква {ch1}, место в алфавите: {ch1_p}\n'
      f'Буква {ch2}, место в алфавите: {ch2_p}\n'
      f'Между ними находится {distance} букв(ы).')




