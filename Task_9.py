"""
Homework 2
Done by Saltykova Ekaterina

Task 9
Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
# overkill

numbers = input('Введите любое количество чисел через пробел: ')


def sum_digits(number):
    s = 0
    for i in number:
        s += int(i)
    return s


def next_number(nums):
    current_num = ''
    rest_num = ''
    is_space_found = False
    for i in nums:
        if is_space_found:
            rest_num += i
        elif i != ' ':
            current_num += i
        else:
            is_space_found = True
    return current_num, rest_num


def largest_number(nums, current_max, current_sum):
    if nums == '':
        return f'Максимальное число: {current_max}, сумма его цифр: {current_sum}'
    num, remaining_nums = next_number(nums)
    if current_sum < sum_digits(num):
        current_sum = sum_digits(num)
        current_max = num
    return largest_number(remaining_nums, current_max, current_sum)


def find_largest_number(nums):
    return largest_number(nums, 0, 0)


print(find_largest_number(numbers))
