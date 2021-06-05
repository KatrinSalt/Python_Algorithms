"""
Homework 3
Done by Saltykova Ekaterina

Task 4
Определить, какое число в массиве встречается чаще всего.
"""
import random
random_list = [random.randint(1, 15) for _ in range(30)]

max_fr = 1
num = random_list[0]
for i in range(len(random_list) - 1):
    count = 1
    for j in range(i+1, len(random_list)):
        if random_list[i] == random_list[j]:
            count += 1
    if count > max_fr:
        max_fr = count
        num = random_list[i]

print(f'Дан массив: {random_list}')
if max_fr > 1:
    print(f'Чаще всего встречается число {num} в данном массиве. Кол-во повторений: {max_fr}')
else:
    print('Все числа встречаются по одному разу.')



