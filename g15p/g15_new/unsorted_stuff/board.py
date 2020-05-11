import math
import numpy as np
from random import shuffle

from g15_new.lessons.test_if_solvable import is_solvable

hole = 0
actions = ['U', 'D', 'L', 'R']
f_state = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, hole]]
# brd_nbr = 0
hardest_level_ever = [[hole, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 1]]

test_level_0 = (2, [[1, 2, 3, hole],
                    [5, 6, 7, 4],
                    [14, 11, 9, 15],
                    [8, 13, 12, 10]])

test_level_1 = (10, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 11, 15, 4],
                     [8, 13, 12, 10]])

test_level_2 = (16, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 11, 10, 15],
                     [8, 13, 12, 4]])

test_level_3 = (15, [[1, 2, 3, hole],
                     [5, 6, 4, 9],
                     [14, 11, 7, 15],
                     [8, 13, 12, 10]])

test_level_4 = (10, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 11, 4, 15],
                     [8, 13, 12, 10]])

test_level_5 = (20, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 11, 12, 15],
                     [8, 13, 4, 10]])

test_level_6 = (15, [[1, 2, 3, hole],
                     [5, 4, 7, 9],
                     [14, 11, 6, 15],
                     [8, 13, 12, 10]])

test_level_7 = (20, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 4, 11, 15],
                     [8, 13, 12, 10]])

test_level_8 = (25, [[1, 2, 3, hole],
                     [5, 6, 7, 9],
                     [14, 8, 11, 15],
                     [13, 4, 12, 10]])

test_level_9 = (30, [[1, 2, 3, hole],
                     [4, 6, 7, 9],
                     [14, 8, 11, 15],
                     [13, 5, 12, 10]])

test_level_10 = (30, [[1, 2, 3, hole],
                      [5, 6, 7, 9],
                      [4, 8, 11, 15],
                      [13, 14, 12, 10]])

test_level_11 = (30, [[1, 2, 3, hole],
                      [5, 6, 7, 9],
                      [14, 8, 11, 15],
                      [4, 13, 12, 10]])

test_levels = [test_level_2,
               test_level_3,
               test_level_4]


# test_levels = [test_level_0, test_level_1,
#                test_level_2, test_level_3,
#                test_level_4, test_level_5,
#                test_level_6, test_level_7,
#                test_level_8, test_level_9,
#                test_level_10, test_level_11]

# def get_xy(state=[], v=None):
#     if v is not None and (v < 0 or v > 15):
#         return -1, -1
#
#     v = hole if v is None else v
#
#     # try:
#     for e in state:
#         if v in e:
#             return state.index(e), e.index(v)
#     # except:
#     #     return -1, -1
#
#     return -1, -1


def distance_from_origin(s, v=int):
    x1, y1 = get_xy(s, v)
    x0, y0 = get_origin_xy(v)
    r = math.fabs(x0 - x1) + math.fabs(y0 - y1)
    return r


def distance_from_xy(s, xy=(), v=int):
    x1, y1 = get_xy(s, v)
    r = math.fabs(xy[0] - x1) + math.fabs(xy[1] - y1)
    return r


def get_origin_xy(v):
    v -= 1
    y = v % 4
    x = v // 4
    return x, y


def distance_from_v1_to_v2(s, v1=int, v2=int):
    x1, y1 = get_xy(s, v1)
    x2, y2 = get_xy(s, v2)

    r = math.fabs(x1 - x2) + math.fabs(y1 - y2)
    return r


def distance_from_v1_to_v2_2(s, v1=int, v2=int):
    x1, y1 = get_xy(s, v1)
    x2, y2 = get_xy(s, v2)

    r = math.fabs(x1 - x2) + math.fabs(y1 - y2)
    return r, x1, x2, y1, y2


def distance_from_hole_to_goal_number(s, goal=int, hole=int):
    x1, y1 = get_xy(s, goal)
    x2, y2 = get_xy(s, hole)
    x = math.fabs(x1 - x2)
    y = math.fabs(y1 - y2)
    return x if x > y else y


def get_actions_4_line(v, a):
    r = []
    if v == 3:
        r.append(a[0])
    elif v == 0:
        r.append(a[1])
    else:
        r.append(a[0])
        r.append(a[1])
    return r


def get_available_actions(state):
    if state is None:
        state = state

    x, y = get_xy(state)
    return get_available_actions_xy(x, y)


def get_available_actions_xy(x, y):
    r = get_actions_4_line(x, actions[:2])
    return r.__add__(get_actions_4_line(y, actions[2:]))


def swap_v(s, x0, y0, x1, y1):
    try:
        v0 = s[x0][y0]
        v1 = s[x1][y1]
        s[x0][y0] = v1
        s[x1][y1] = v0
    except Exception:
        pass
    return s


def move(state, action):
    x, y = get_xy(state)
    if action == 'U':
        return swap_v(state, x, y, x - 1, y)
    elif action == 'D':
        return swap_v(state, x, y, x + 1, y)
    elif action == 'L':
        return swap_v(state, x, y, x, y - 1)
    elif action == 'R':
        return swap_v(state, x, y, x, y + 1)


def position_of_hole(state):
    x, y = get_xy(state, hole)
    p = (x * 4) + y
    return p


# def get_random_board():
#     s = np.copy(f_state).tolist()
#     s = np.reshape(s, [16]).tolist()
#     shuffle(s)
#     s = np.reshape(s, [4, 4]).tolist()
#
#     if is_solvable(s): return s
#     return get_random_board()


def get_random_board_tail_4():
    head = [1, 2, 3, hole]
    tail = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    shuffle(tail)

    s = np.copy(head).tolist()
    s = np.append(s, list(tail)).tolist()
    s = np.reshape(s, [4, 4]).tolist()
    if is_solvable(s): return s
    return get_random_board_tail_4()


def get_random_board_tail():
    tail = [10, 11, 12, 14, 15, hole]
    shuffle(tail)

    s = np.copy(f_state).tolist()
    s = np.reshape(s, [16]).tolist()
    s[9:12] = tail[0:3]
    s[13:16] = tail[3:6]

    s = np.reshape(s, [4, 4]).tolist()
    if is_solvable(s): return s
    return get_random_board_tail()


def get_xy(state=np.ndarray, v=None):
    if v is not None and (v < 0 or v > 15):
        raise Exception('v is not None and (v < 0 or v > 15)')

    v = hole if v is None else v
    x, y = np.where(state == v)
    return x[0], y[0]


def get_random_board_np(state=np.ndarray):
    s = np.copy(state)
    s = np.reshape(s, [16])
    shuffle(s)
    s = np.reshape(s, [4, 4])

    if is_solvable(s.tolist()): return s
    return get_random_board_np(state)

#
# state = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15, 0]]
#
# state = np.array(state).astype(int)
#
# print(get_xy(state, 2))
# print(get_random_board_np(state))
