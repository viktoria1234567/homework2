#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# a = input('Введите вещественное число: ')
# sum = 0
# for i in a:
#     if i != '.':
#         sum += int(i)
# print(sum)

#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число: '))
# i = 1
# result=1
# while (i <= N):
#     result *= i
#     i=i+1
#     print(result)

# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число: '))
# i = 1
# result=0
# sum = 0
# while (i <= n):
#     result = round((1+1/i)**i,2)
#     print(result)
#     sum = sum + result
#     i=i+1
# print(round(sum))

# 4.Реализуйте алгоритм перемешивания списка
# import random
# list = [1, 2, 3, 4, 5, 6]
# random.shuffle(list)
# print(list)
