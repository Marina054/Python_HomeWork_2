# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)




print('введите значение N:')
N = int(input())
n = N
print('введите число начала диапозона:')
a = int(input())
print ('введите число конца диапозона:')
b = int(input())

import random
arr = []
for i in range(n):
    arr.append(random.randint(a,b))
print(arr)


factorial = 1
for i in arr:
    factorial *= i
    print(factorial, end=' ')