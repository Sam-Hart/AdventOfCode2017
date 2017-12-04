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
    sum_spiral = {}
    sum_spiral[pos[0]] = {}
    sum_spiral[pos[0]][pos[1]] = n
    yield n, pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                pos = move(*pos)
                current_adjacents_sum = 0
                current_adjacents_sum += sum_spiral.get(pos[0] - 1, 0).get(pos[1] - 1, 0) if sum_spiral.get(pos[0] - 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0] - 1, 0).get(pos[1], 0) if sum_spiral.get(pos[0] - 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0] - 1, 0).get(pos[1] + 1, 0) if sum_spiral.get(pos[0] - 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0] + 1, 0).get(pos[1] - 1, 0) if sum_spiral.get(pos[0] + 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0] + 1, 0).get(pos[1], 0) if sum_spiral.get(pos[0] + 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0] + 1, 0).get(pos[1] + 1, 0) if sum_spiral.get(pos[0] + 1) else 0
                current_adjacents_sum += sum_spiral.get(pos[0], 0).get(pos[1] - 1, 0) if sum_spiral.get(pos[0]) else 0
                current_adjacents_sum += sum_spiral.get(pos[0], 0).get(pos[1] + 1, 0) if sum_spiral.get(pos[0]) else 0
                n = current_adjacents_sum
                if not sum_spiral.get(pos[0]):
                    sum_spiral[pos[0]] = {}
                sum_spiral[pos[0]][pos[1]] = n
                yield n, pos
                if n > end:
                    return
        times_to_move += 1


challenge_input = 265149
# challenge_input = 12
print(list(gen_points(challenge_input))[-1])
