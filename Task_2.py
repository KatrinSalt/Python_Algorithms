"""
Homework 2
Done by Saltykova Ekaterina

Task 2
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
"""

number = input('Введите любое натуральное число: ')

even_numbers_1 = 0
odd_numbers_1 = 0

for num in number:
    if int(num) % 2 == 0:
        even_numbers_1 += 1
    else:
        odd_numbers_1 += 1
print(f'Количество четных чисел в введенном числе: {even_numbers_1}\n'
      f'Количество нечетных чисел в введенном числе: {odd_numbers_1}')

# решение через список:
even_numbers_2 = [i for i in number if int(i) % 2 == 0]
odd_numbers_2 = [j for j in number if int(j) % 2 != 0]

print(f'Количество четных чисел в введенном числе: {len(even_numbers_2)}\n'
      f'Количество нечетных чисел в введенном числе: {len(odd_numbers_2)}')



