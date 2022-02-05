player_pass = True
while player_pass:
    player1 = input('Выберите символ Х или О').lower()

    if player1 == '0' or player1 == 'o' or player1 == 'о':
        player_pass = False
        P1 = 'O'
        P2 = 'X'

    elif player1 == 'x' or player1 == 'х':
        player_pass = False
        P2 = 'O'
        P1 = 'X'

    else:
        print('Играть можно только за О или Х')
x = ['s',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player_win = True
player_turn = 0

while player_win:
    position = int(input(f'Введите число от 1 до 9'))

    if position > 9 or position < 1:
        print('Неверное число, введите от 1 до 9')
    elif x[position] != ' ':
        print('Поле занято, введите другое число')
    else:
        player_turn += 1
        number_right = False

        if player_turn % 2 == 0:
            x[position] = P2
            if x[1:4] == [P2, P2, P2]:
                player_win = False
                break
            elif x[4:7] == [P2, P2, P2]:
                player_win = False
                break
            elif x[7:10] == [P2, P2, P2]:
                player_win = False
                break
            elif x[1:8:3] == [P2, P2, P2]:
                player_win = False
                break
            elif x[2:9:3] == [P2, P2, P2]:
                player_win = False
                break
            elif x[3:10:3] == [P2, P2, P2]:
                player_win = False
                break
            elif x[1:10:4] == [P2, P2, P2]:
                player_win = False
                break
            elif x[3:9:2] == [P2, P2, P2]:
                player_win = False
                break

        else:
            x[position] = P1
            if x[1:4] == [P1, P1, P1]:
                player_win = False
                break
            elif x[4:7] == [P1, P1, P1]:
                player_win = False
                break
            elif x[7:10] == [P1, P1, P1]:
                player_win = False
                break
            elif x[1:8:3] == [P1, P1, P1]:
                player_win = False
                break
            elif x[2:9:3] == [P1, P1, P1]:
                player_win = False
                break
            elif x[3:10:3] == [P1, P1, P1]:
                player_win = False
                break
            elif x[1:10:4] == [P1, P1, P1]:
                player_win = False
                break
            elif x[3:9:2] == [P1, P1, P1]:
                player_win = False
                break

    print(f'{x[7]}|{x[8]}|{x[9]}\n-----\n{x[4]}|{x[5]}|{x[6]}\n-----\n{x[1]}|{x[2]}|{x[3]}')
    i_count = 0
    if player_turn == 9:
        print('Ничья')
        exit()

print(f'{x[7]}|{x[8]}|{x[9]}\n-----\n{x[4]}|{x[5]}|{x[6]}\n-----\n{x[1]}|{x[2]}|{x[3]}')
if player_turn%2 == 0:
    print(f'Игрок {P2} Победил! Ура! ')
else:
    print(f'Игрок {P1} Победил! Ура!')

