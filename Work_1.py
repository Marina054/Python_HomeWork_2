# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
import re


print('Ввведите вещественное число:')
v = input()
print(v)
print(f'list1 = {list (v)}')
list2 = list(v)
del list2[1]
print(list2)
print(sum([sum(map(int, i)) for i in list2]))