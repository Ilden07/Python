# Задача №1. Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# from distutils.log import error


# def sum_list (list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return sum

# def create_list (n):
#     list = []
#     for i in range(1,n+1):
#         list.append(round((1+1/i)**i, 3))
#     return list

# try:
#     num = int(input('Введите целое число: '))
#     new_list = create_list(num)
#     print(new_list)
#     print(f'Сумма элементов последовательности: {round(sum_list(new_list),3)}')
# except ValueError as error:
#     print(f'Введите целое число! - {error}')



# Задача №2. Задайте список из N элементов, заполненных числами
#  из промежутка [-N, N]. Найдите произведение элементов
#   на указанных позициях. Позиции хранятся в файле file.txt
#    в одной строке одно число.

# from random import randint

# def create_file(n):
#     with open('file2.txt', 'w') as data:
#         for i in range(3):
#             value = str(randint(0,n-1))
#             data.write(value)
#             data.write('\n')

# def create_list (n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n,n))
#     return list

# def multiply (list):
#     data = open('file2.txt', 'r')
#     res = 1
#     for line in data:
#         print(f'Элемент на позиции {line}равен: {list[int(line)]}')
#         res *=list[int(line)]
#     data.close()
#     return res

# try:
#     num = int(input('Введите целое число: '))
#     create_file(num)
#     new_list = create_list(num)
#     print(new_list)
#     print(f'Произведение элементов равно: {multiply(new_list)}')
 
# except ValueError as error:
#     print(f'Введите целое число! - {error}')



# Задача №3. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# def create_list():
#     list = []
#     value = 0
#     print('Чтобы закончить ввод, отправьте пустое значение!')
#     while value != '':
#         value = input('Введите значение: ')
#         list.append(value)
#     list.pop()
#     return list



# try:
#     new_list = create_list()
#     print(new_list)
#     num = int(input('Введите число, которое будем искать: '))
#     if str(num) in new_list:
#         print(f'Число {num} найдено в этом списке!')
#     else:
#         print(f'Число {num} не найдено в этом списке!')
# except ValueError as error:
#     print(f'Введите целое число! - {error}')



# Задача №4. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# def create_list():
#     list = []
#     value = 0
#     print('Чтобы закончить ввод, отправьте пустое значение!')
#     while value != '':
#         value = input('Введите значение: ')
#         list.append(value)
#     list.pop()
#     return list


# new_list = create_list()
# print(new_list)
# str = input('Введите то, что будем искать: ')
# index = None
# count = 0
# for i in range(len(new_list)):
#     if count == 2:
#         break
#     if str == new_list[i]:
#             index = i
#             count +=1
# if count < 2:
#     print(f'Второе вхождение не найдено!')
# elif count == 2:
#     print(f'Второе вхождение найдено на {index} элементе')


# Решение из зала

# # 20. Задайте список. Напишите программу, которая определит, присутствует ли в
# # заданном списке строк некое число.

# def get_list_from_input(n):
# str_list = [''] * n
# for i in range(n):
# str_list[i] = input(f'Input row {i + 1}: ')

# return str_list


# def get_list_from_file(path):
# with open(path, 'r') as f:
# return f.read().split('\n')


# def check_num_in_list(lst, num):
# if str(num) in lst:
# print(f'Number {num} is found in list')
# else:
# print(f'Number {num} is not found in list')


# try:
# n = int(input('Input number of rows: '))
# except ValueError as ex:
# print('Input natural number!')
# exit(ex)

# list1 = get_list_from_input(n)

# try:
# num = int(input('Input natural number: '))
# except ValueError as ex:
# print('Input natural number!')
# exit(ex)

# print()
# print('List from input: ')
# print(list1)
# check_num_in_list(list1, num)

# path = 'str.txt'
# list2 = get_list_from_file(path)

# print()
# print('List from file: ')
# print(list2)
# check_num_in_list(list2, num)