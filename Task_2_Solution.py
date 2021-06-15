"""
Homework 4
Solution by Tutor

Task 2:
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
а) Алгоритм: 'Решето Эратосфена'
б) Алгоритм: 'Без решета Эратосфена'
"""
import cProfile
import math


# функция для теста
def test_prime(func_search, n=2000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    real_prime = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(real_prime)}')

    for i, item in enumerate(real_prime, start=1):
        assert func_search(i) == item, f'Test{i} fail\t func({i}) = {func_search(i)}'
        print(f'Test {i} OK')


def prime_search(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        #for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime


test_prime(prime_search)


def eratosthenes_sieve(num):
    # pi_f = x / math.log(x) - функция распределения простых чисел
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func.keys():
        if num <= key:
            size = pi_func[key]
            break
    else:
        raise Exception('Слишком большой аргумент.')

    array = [i for i in range(size)]
    array[1] = 0
    for m in range(2, size):
        if array[m] != 0:
            j = m ** 2
            while j < size:
                array[j] = 0
                j += m
    res = [i for i in array if i != 0]
    return res[num - 1]


def eratosthenes_sieve_improved(num):
    # pi_f = x / math.log(x) - функция распределения простых чисел
    assert num <= 5761455, f'Слишком большой аргумент {num}'
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func.keys():
        if num <= key:
            size = pi_func[key]
            break

    array = [True for _ in range(size)]  # мы экономим память на хранении данных
    array[:2] = [False, False]

    count = 0

    for m in range(2, size):
        if array[m]:

            count += 1
            if count == num:
                return count

            for j in range(m ** 2, size, m):
                array[j] = False
    return None



