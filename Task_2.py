"""
Homework 4
Done by Saltykova Ekaterina

Task 2:
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
а) Алгоритм: 'Решето Эратосфена'
б) Алгоритм: 'Без решета Эратосфена'
"""
import cProfile

# поиск всех простых чисел до числа N
def sieve_er(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


# поиск n-ого просто числа
def eratosthenes_sieve(n):

    if n == 1:
        return 2

    count = 1
    start = 3
    end = n * 4

    sieve = [i for i in range(start, end) if i % 2 != 0]  # all even numbers (except 2) are not prime numbers
    prime = [2]

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i != 0]

        for i in range(len(sieve)):
            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

# "Task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 10.4 usec per loop

# "Task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 165 usec per loop

# "Task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 12.9 msec per loop

# Алгоритм может быть сложности O(n^2). Увеличивая входящее значение в 10 раз,
# скорость выполнения алгоритма увеличивается примерно в 100 раз


# cProfile.run('eratosthenes_sieve(10)')
# 1    0.000    0.000    0.000    0.000 Task_2.py:33(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Task_2.py:42(<listcomp>)

# cProfile.run('eratosthenes_sieve(100)')
# 1    0.000    0.000    0.000    0.000 Task_2.py:33(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Task_2.py:42(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Task_2.py:61(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Task_2.py:64(<listcomp>)

# cProfile.run('eratosthenes_sieve(1000)')
# 1    0.016    0.016    0.016    0.016 Task_2.py:33(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Task_2.py:42(<listcomp>)
# 2    0.000    0.000    0.000    0.000 Task_2.py:61(<listcomp>)
# 2    0.000    0.000    0.000    0.000 Task_2.py:64(<listcomp>)


