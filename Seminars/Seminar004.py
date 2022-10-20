# Задача №1. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def negafib (n):
# result = [0, 1]
# resultn = [0, 1]
# for i in range(2,n+1):
# next = result[i-1] + result[i-2]
# if i%2 == 0:
# resultn.append(-next)
# else:
# resultn.append(next)
# result.append(next)
# print(result)
# print(resultn)
# print(resultn[1:][::-1] + result)


# # num = int(input("Введите число: "))
# # fib = negafib(num)

# def fibanachi(n):
#     if n in (1, 2):
#         return  1
#     else:
#         return fibanachi(n-1) + fibanachi (n-2)

# N = int(input('Enter n: '))
# = = []
# for i in range (1, N  +  1):
#     fib_arr.appendappend(fibanachi(i))
# fib_arr.insert(0, 0)
# for i in range(1, N + 1):
#     fib_arrfib_arr.insert(0, ((-1)**( ii + 1)) * fibanachi(i))
# print(fib_arr)




# Задача 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) 
# с помощью математических формул нахождения корней квадратного 
# уравнения

# import math

# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)

# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")




# Задача 3. Задайте два числа. Напишите программу, которая 
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

# НОД

# def check_nok (num1, num2):
#     if num1 > num2:
#         num1,num2 = num2,num1
#     for i in range(2,num1+1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             print(f'НОК = {i}')
#             break
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# check_nok(num1,num2)
# # НОК
# def lcm(a, b):
#     for i in range(max(a, b), a * b + 1):
#         if i % a == 0 and i % b == 0:
#             return i

# def main():
#     try:
#         a = int(input('Input number A: '))
#         b = int(input('Input number B: '))
#     except ValueError as ex:
#         print('Input natural number!')
#         exit(ex)

#     print(f'LCM({a}, {b}) = {lcm(a, b)}')


# if __name__ == '__main__':
#     main()