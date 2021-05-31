"""
Homework 2
Done by Saltykova Ekaterina

Task 7
Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

n = int(input('Введите любое натуральное число: '))


def prove_statement(n):
    sum1 = calculate_sum(n)
    sum2 = (n * (n + 1)) / 2
    if sum1 == sum2:
        return f'Вы доказали утверждение: {sum1} = {int(sum2)}'
    else:
        return f'Утверждение не доказано.'


def calculate_sum(n):
    if n == 0:
        return 0
    return n + calculate_sum(n-1)


print(prove_statement(n))




