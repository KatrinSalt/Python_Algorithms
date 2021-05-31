"""
Homework 2
Done by Saltykova Ekaterina

Task 8
Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел. Количество вводимых чисел и цифра,
которую необходимо посчитать, задаются вводом с клавиатуры..
"""

amount = int(input('Сколько чисел вы бы хотели ввести?: '))
digit = input('Введите ту цифру, для которой программа посчитает количество ее появлений'
              'в веденных вами числах: ')
num_str = ''
for i in range(0, amount):
    num_str += input('Введите число: ')

count = 0
# решение через цикл
for num in num_str:
    if num == digit:
        count += 1
print(f'В введенных вами числах цифра {digit} встречается {count} раз.')

# решение через метод str
count_2 = num_str.count(digit)
print(f'В введенных вами числах цифра {digit} встречается {count_2} раз.')
