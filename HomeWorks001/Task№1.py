# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def check_weekend (num):
    if num > 5:
        return True
try:
    day_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    print('Проверим, является ли этот день выходным!')
    num_day = 0
    while num_day < 1 or num_day > 7:
        num_day = int(input('Введите цифру дня недели (от 1 до 7): '))
    
    if check_weekend(num_day) == True:
        print(f'Да, {day_week[num_day-1]} - выходной день!')
    else:
        print(f'Нет, {day_week[num_day-1]} - будний день!')

except:
    print('Введите целое число')
    
