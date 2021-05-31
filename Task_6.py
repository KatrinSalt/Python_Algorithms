"""
Homework 2
Done by Saltykova Ekaterina

Task 6
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""
import random

number = random.randint(0, 100)
guess = int(input('Угадайте, какое число загадал компьютер (от 0 до 100): '))

num_guesses = 9
while num_guesses >= 0:
    if num_guesses == 0:
        print(f'Вы не угадали число. Загаданное число: {number}')
        break
    elif guess == number:
        print(f'Поздравляю, вы угадали число {number}!')
        break
    elif guess > number:
        print(f'Введенное вами число {guess} больше загаданного. Повторите попытку.\n'
              f'У вас осталось {num_guesses} попыток.')
        guess = int(input('Угадайте, какое число загадал компьютер (от 0 до 100): '))
    else:
        print(f'Введенное вами число {guess} меньше загаданного. Повторите попытку.\n'
              f'У вас осталось {num_guesses} попыток.')
        guess = int(input('Угадайте, какое число загадал компьютер (от 0 до 100): '))
    num_guesses -= 1





