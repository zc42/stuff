from random import shuffle
import numpy as np
from g15_new.unsorted_stuff.board import hole, get_xy
from g15_new.lessons.test_if_solvable import is_solvable

array0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])


def get_random_board(g=None):
    g = 1 if g == None else g

    s = np.copy(array0)
    i = g - 1

    s1 = s[:i]
    s2 = s[i:]
    # s2 = np.append(s2, 0)
    shuffle(s2)

    s = np.append(s1, s2)
    s = np.reshape(s, [4, 4])

    if is_solvable(s): return s
    s = switch_v(s, 14, 15)

    if not is_solvable(s):
        txt = str(s.tolist()) + '\n'
        txt += 'not solvable '
        raise Exception(txt)

    return s


def t(o=()):
    b = 0 <= o[0] <= 3
    b = b and 0 <= o[1] <= 3
    return b


def get_random_board_aa(g=int, xy_g=(3, 0), xy_h=()):
    if not (t(xy_g) or t(xy_h)): return None
    if xy_g == xy_h: return None
    s = get_random_board(g)

    s = switch(s, hole, xy_h)
    s = switch(s, g, xy_g)

    if is_solvable(s): return s
    s = switch_v(s, 12, 15)
    # b = is_solvable(s)
    return s
    #
    #
    # return get_random_board_aa(g, xy_g, xy_h)


def get_random_board_13(xy_g=(), xy_h=()):
    if not (t(xy_g) or t(xy_h)): return None
    if xy_g == xy_h: return None

    s = get_random_board(10)

    s = switch(s, hole, xy_h)
    s = switch(s, 13, xy_g)

    if is_solvable(s): return s
    s = switch_v(s, 14, 15)
    return s


def get_random_board_10__14(g=int, xy_g=(), xy_h=()):
    if not (t(xy_g) or t(xy_h)): return None
    if xy_g == xy_h: return None
    s = get_random_board(g)
    s = switch(s, hole, xy_h)
    s = switch(s, 13, (3, 0))

    if is_solvable(s): return s
    s = switch_v(s, 14, 15)
    # b = is_solvable(s)
    return s


def get_random_board_10__14(g=int, xy=()):
    s = get_random_board(g)
    s = switch(s, hole, xy)
    s = switch(s, 13, (3, 0))

    if is_solvable(s): return s
    s = switch_v(s, 14, 15)
    # b = is_solvable(s)
    return s

    # return get_random_board_10__15(g, xy)


def switch(s=np.ndarray, v0=int, xy0=()):
    xy1 = get_xy(s, v0)
    v1 = s[xy0[0]][xy0[1]]
    if v1 == v0: return s

    s = np.copy(s)
    s[xy0[0]][xy0[1]] = v0
    s[xy1[0]][xy1[1]] = v1
    return s


def switch_v(s=np.ndarray, v1=int, v2=int):
    xy1 = get_xy(s, v1)
    xy2 = get_xy(s, v2)

    s = np.copy(s)

    s[xy1[0]][xy1[1]] = v2
    s[xy2[0]][xy2[1]] = v1
    return s


def get_random_board_10(xy_g=(), xy_h=()):
    g = 10
    if xy_h == xy_g: return None
    s = get_random_board_10__14(10, xy_h)

    s = switch(s, hole, xy_h)
    s = switch(s, g, xy_g)

    if is_solvable(s): return s
    s = switch_v(s, 14, 15)

    return s


def get_random_board_14(xy_g=(), xy_h=()):
    g = 14
    if xy_h == xy_g: return None
    s = get_random_board_10__14(10, xy_h)

    s = switch(s, 10, (2, 1))
    s = switch(s, hole, xy_h)
    s = switch(s, g, xy_g)

    if is_solvable(s): return s
    return get_random_board_14(xy_g, xy_h)


def get_random_board_15(xy_g=(), xy_h=()):
    g = 15
    if xy_h == xy_g: return None
    s = get_random_board_10__14(10, xy_h)

    s = switch(s, 10, (2, 1))
    s = switch(s, 14, (3, 1))
    s = switch(s, hole, xy_h)
    s = switch(s, g, xy_g)

    if is_solvable(s): return s
    return get_random_board_15(xy_g, xy_h)


# print(get_random_board_15((2, 2), (2, 3)))
# print(get_random_board_13((2, 1), (3, 0)))
