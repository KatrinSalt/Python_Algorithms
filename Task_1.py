"""
Homework 3
Done by Saltykova Ekaterina

Task 1
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

# решение 1
multiples = [0] * 8
for i in range(2, 10):
    for j in range(2, 100):
        if j % i == 0:
            multiples[i-2] += 1


for i in range(0, 8):
    print(f'Кол-во чисел кратных {i+2} : {multiples[i]}')

print('-'*20)

# решение 2: просто меньше строк
for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    print(f'Кол-во чисел кратных {i}: {count}')

