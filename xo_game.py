field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_field():
    for i in range(len(field) - 1):
        print(" | ".join(field[i]))
        print("---------")
    print(" | ".join(field[len(field) - 1]))


def can_make_a_move(i, j):
    return 0 <= i - 1 < len(field) and 0 <= j - 1 < len(field[0]) and field[i - 1][j - 1] == '-'


def field_not_filled():
    return any([('-' in row) for row in field])


def get_coords_for_player(player, xo):
    coords = input(f"{player}, введите через пробел координаты клетки, куда хотите поставить \"{xo}\": ").split(" ")
    while len(coords) != 2 and not can_make_a_move(*[int(c) for c in coords]):
        if len(coords) != 2:
            coords = input("Количество координат должно быть равно двум. Пожалуйста, повторите ввод: ").split(" ")
        elif not can_make_a_move(*[int(c) for c in coords]):
            coords = input(
                "Вы ввели неверные координаты, данная клетка не существует или заполнена, попробуйте еще раз: ").split(
                " ")
    i, j = [int(c) for c in coords]
    return i - 1, j - 1


def winner_move(xo, player):
    i, j = get_coords_for_player(player, xo)
    field[i][j] = xo
    print_field()
    any_row = any([all([elem == xo for elem in row]) for row in field])
    any_column = any([all(elem == xo for elem in row) for row in [[field[i][j] for i in range(3)] for j in range(3)]])
    main_diag = all([field[i][i] == xo for i in range(len(field))])
    side_diag = all([field[i][len(field) - 1 - i] == xo for i in range(len(field))])
    return any_row or main_diag or side_diag or any_column



def main():
    have_a_winner = False
    player_1 = ""
    while player_1 not in ['x', 'o']:
        player_1 = input("Пожалуйста, выберите, чем будет ходить первый игрок (x или o на английской раскладке): ")
    player_2 = 'x' if player_1 == 'o' else 'o'
    print_field()
    while field_not_filled():
        if winner_move(player_1, "Игрок 1"):
            print("Игрок 1 победил!")
            have_a_winner = True
            break
        if winner_move(player_2, "Игрок 2"):
            print("Игрок 1 победил!")
            have_a_winner = True
            break
    if not field_not_filled() and not have_a_winner:
        print("Ничья!")


main()