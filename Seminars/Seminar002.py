# #Задача №1 
# sp = []
# for i in range(3):
#     sp1=[]
#     for j in range(3):
#         sp1.append(i + j)
#     sp.append(sp1)

# for i in range(len(sp)):
#     print(sp[i])

# sp.insert(0,[8,9])
# print("------")

# sp.remove([8,9])
# a=sp.pop(-1)

# print(a)
# print("одномерный список")
# print(a[::-1])
# a=a + [15,11,99]
# print(a)
# print(a[2:5])

# book={}

# book['Миша'] = 69505906
# book['Саша'] = [56576857, 856748578]

# print(book)

# if 'Саша' in book:
#     print("Yes")
# else:
#     print("No")

# for x,y in book.items():
#     print(x,y)

# for x in book.values():
#     print(x)
# for y in book.keys():
#     print(y)





# Задача 2
# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в 
# этой четверти (x и y).

# def how_points (num):
#     if num == 1:
#         print(' x > 0; y > 0')
#     elif num == 2:
#         print(' x < 0; y > 0')
#     elif num == 3:
#         print(' x < 0; y < 0')
#     elif num == 4:
#         print(' x > 0; y < 0')
#     else:
#         print('Введите целое число от 1 до 4')

# try:
#     num = int(input('Введите число от 1 до 4: '))
#     how_points(num)
# except:
#     print('Введите целое число')

# num = int(input("Введите номер четверти: "))

# match num:
#     case 1:
#         print(" x > 0; y > 0")
#     case 2:
#         print(" x < 0; y > 0")
#     case 3:
#         print(" x < 0; y < 0")
#     case 4:
#         print(" x > 0; y < 0")
#     case _:
#         print("Что то не так")






# Задача №3 

# 5. Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.   
#     *Пример:*   
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

# from math import sqrt


# def length (point1, point2, size):
#     for i in range(size):
#         result = sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
#     return result

# try:

#     point1 = [0]*2
#     point2 = []
#     point1[0] = float(input('Введите значение Х 1 точки: '))
#     point1[1] = float(input('Введите значение Y 1 точки: '))
#     point2.append(float(input('Введите значение Х 2 точки: ')))
#     point2.append(float(input('Введите значение Y 2 точки: ')))
#     res = length(point1, point2)
#     print(f'Расстояние между точками {point1} и {point2} равно: {round(res, 3)}')
# except:
#     print('Введите число')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# import math
# try:
#     coordA = []
#     for i in range(2):
#         coordA.append(int(input("введите координату точки А: ")))
#     coordB = []
#     for i in range(2):
#         coordB.append(int(input('введите координату точки В: ')))
#     print(coordA, coordB)
    
#     distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
#     print(round(distan, 3))
# except:
#     print('Введите числа')





# Задача № 4

# 1. Напишите программу, которая принимает на вход число 
# N и выдаёт последовательность из N членов.
# *Пример:*   
#     - Для N = 5: 1, -3, 9, -27, 81

# def print_value(num):
#     for j in range(num):
#         print((-3)**j, end = " ")


# try:
#     num = int(input("Введите число: "))
#     print_value(num)
# except:
#     print('Введите число')





# Задача №5

# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def create_book (num):
#     book = {}
#     for i in range(1, num + 1):
#         book[i] = i*3 +1
#     return book

# try:
#     num = int(input("Введите число: "))
#     print(create_book(num))
# except:
#     print('Введите число')




# задача №6
# 3. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять количество 
# вхождений одной строки в другой.


# str1 = input('Где искать: ')
# str2 = input('Что искать')
# count = 0

# for i in str1:
#     for str2 in str1:
#         count +=1

# print(count)
