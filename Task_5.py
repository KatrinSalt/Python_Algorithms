"""
Homework 2
Done by Saltykova Ekaterina

Task 5
Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме:
по десять пар «код-символ» в каждой строке.
"""

for i in range(32, 127, 10):
    res = ' '.join(chr(val) for val in range(i, i+11) if val < 128)
    print(res)
