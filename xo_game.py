field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def can_make_a_move(i, j):
    return 0 <= i - 1 < len(field) and 0 <= j - 1 < len(field[0]) and field[i - 1][j - 1] == '-'


def field_not_filled():
    return any([('-' in row) for row in field])