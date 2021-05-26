"""
Homework 1
Done by Saltykova Ekaterina

Task 7:
Определить, является ли год,
который ввел пользователь, високосным или не високосным.
"""
year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Этот год - високосный.')
        else:
            print('Этот год - обычный.')
    else:
        print('Этот год - високосный.')
else:
    print('Этот год - обычный.')
