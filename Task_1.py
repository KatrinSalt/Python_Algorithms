"""
Homework 5
Done by Saltykova Ekaterina

Task 1
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name, profit_per_quarter, average_profit')

amount = int(input('Введите количество предприятий: '))

company_list = []
for i in range(amount):
    name = input(f'Введите наименование {i+1} предприятия: ')
    profit = input(f'Введите прибыль {i+1} предприятия (млн. руб.) за каждый из четырех кварталов через пробел: ').split()
    average_profit = mean(map(int, profit))
    company = New_Company(name, profit, average_profit)
    company_list.append(company)

average = mean([i.average_profit for i in company_list])
print(f'Средняя прибыль предприятий за четыре квартала (Q1-Q4): {average}')

above_average = []
below_average = []

for i in company_list:
    if i.average_profit >= average:
        above_average.append(i.name)
    else:
        below_average.append(i.name)

print(f"Компании, чья прибыль ниже среднего: {', '.join(below_average)} \n"
      f"Компании, чья прибыль выше среднего: {', '.join(above_average)}")


