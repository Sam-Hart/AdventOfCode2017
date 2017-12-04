from itertools import cycle


def move_right(x, y):
    return x + 1, y


def move_up(x, y):
    return x, y + 1


def move_left(x, y):
    return x - 1, y


def move_down(x, y):
    return x, y - 1


def gen_points(end):
    moves = [move_right, move_up, move_left, move_down]
    _moves = cycle(moves)
    n = 1
    pos = 0, 0
    times_to_move = 1
    yield n, pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos
        times_to_move += 1


challenge_input = 265149
# challenge_input = 12
print(list(gen_points(challenge_input))[-1][-1])
