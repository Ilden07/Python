# задача 1. Создайте программу для игры с конфетами человек против человека.Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшемупоследний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

import random


def input_selection(invite_text, selection_type):
    for _ in range(3):
        try:
            input_choice = int(input(invite_text))
            if 1 <= input_choice <= 2:
                return input_choice - 1
            else:
                print(f'Неверно {selection_type}. Попробуйте снова.')
        except ValueError:
            print(f'Неверно {selection_type}. Попробуйте снова.')
    return


def candy_game(candies, max_per_turn):

    two_players = input_selection('Выберете режим игры (1 player - 1, 2 players - 2): ',
                                  selection_type='Режим игры')
    if two_players is None:
        print('Неправильный режим игры. Игра окончена.')
        return

    if not two_players:
        hard_level = input_selection('Выберете уровень сложности (easy - 1, hard - 2): ',
                                    selection_type='Уровень сложности')
        if hard_level is None:
            print('Неправильный уровень сложности. Игра окончена.')
            return

    player_turn = random.choice([True, False])

    if two_players:
        player = '2' if player_turn else '1'
        print(f'Поздравляю! Игрок {player} выиграл жеребъевку и делаент свой первый ход!')
    else:
        if player_turn:
            print('Поздравляю! Вы выиграли жеребъевку, делайте свой первый ход!')
        else:
            print('В результате жеребъевки первый ход за мной.')

    while candies:
        print('Конфеты остались:', candies)
        max_turn = min(max_per_turn, candies)
        if player_turn or two_players:
            for _ in range(3):
                try:
                    if two_players:
                        player = '2' if player_turn else '1'
                        invite_text = f'Игрок {player} переход (возьмите от 1 до {max_turn} конфет): '
                    else:
                        invite_text = f'Ваш ход (возьмите от 1 до {max_turn} конфет): '
                    turn = int(input(invite_text))
                    if 1 <= turn <= max_turn:
                        break
                    print('Пробовать снова!')
                except ValueError:
                    turn = 0
                    print('Пробовать снова!')

            if 1 <= turn <= max_turn:
                candies -= turn
            else:
                turn = 0
                break
        else:
            if hard_level:
                if candies <= max_turn:
                    turn = max_turn
                elif candies == max_turn + 1:
                    turn = 1
                else:
                    turn = candies % (max_per_turn + 1)
            else:
                turn = random.randint(1, max_turn)
            candies -= turn
            print('Моя очередь:', turn)

        player_turn = not player_turn

    if turn:
        print('Конфеты остались:', candies)
        if two_players:
            print(f'Игрок {"1" if player_turn else "2"} выиграл!')
        else:
            print('Ты проиграл!' if player_turn else 'Ты выиграл!')
        print('Игра окончена')
    else:
        print('Неправильное количество конфет. Игра окончена.')


def main():
    print('Добро пожаловать в игру с конфетами')
    try:
        candies = int(input('Введите общее количество конфет: '))
        max_per_turn = int(input('Введите максимальное количество конфет за ход: '))
    except ValueError as ex:
        print('Ошиблись номером! Игра окончена.')
        exit(ex)

    candy_game(candies, max_per_turn)


if __name__ == '__main__':
    main()