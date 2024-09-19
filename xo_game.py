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