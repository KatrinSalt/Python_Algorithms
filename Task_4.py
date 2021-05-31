"""
Homework 2
Done by Saltykova Ekaterina

Task 4
Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите натуральное число: '))

# решение 1:
s = 0
for i in range(0, n+1):
    s += 1/(-2) ** i
print(s)


# решение 2: есть недостаток: maximum recursion depth is exceeded
def cal(a):
    if a < 0:
        return 0
    return 1/(-2) ** a + cal(a-1)


print(cal(n))





