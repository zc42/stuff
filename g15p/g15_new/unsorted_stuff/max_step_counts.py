import math
import numpy as np
from g15_new.unsorted_stuff.board import get_xy, hole
# from game_15.g15_contstants import  max_steps_11___15, goals_11___15

a = [[0, 1, 6, 11],
     [1, 4, 7, 12],
     [6, 7, 10, 13],
     [11, 12, 13, 16]]


b = [[0, 0, 1, 6],
     [8, 1, 4, 7],
     [11, 6, 7, 10],
     [12, 13, 12, 13]]


c = [[0, 0, 0, 1],
     [13, 8, 1, 4],
     [14, 11, 6, 7],
     [15, 12, 11, 12]]


d = [[0, 0, 0, 0],
     [24, 19, 14, 11],
     [23, 18, 13, 10],
     [24, 19, 16, 15]]

le_0 = [[0, 0, 0, hole],
        [30, 15, 20, 2],
        [30, 20, 15, 10],
        [30, 25, 20, 20]]


def get_min_steps(g=(), m=[]):
    # m = np.array(m)
    x, y = reverse(g)
    return m[x, y]


def reverse(g):
    return g[1], g[0]


def get_array_and_x_shift(g):
    if g == 1: return a, 0
    if g == 5: return a, -1
    if g == 9: return a, -2

    if g == 2: return b, 0
    if g == 6: return b, -1

    if g == 3: return c, 0
    if g == 7: return c, -1

    if g == 4: return d, 0
    if g == 8: return d, -1


test_level = [[1, 11, 3, 4],
              [2, 6, 7, 8],
              [9, 10, 12, 0],
              [13, 14, 5, 15]]


def get_h_distance_2_g(state=np.ndarray, g=int):
    xy_g = get_xy(state, g)
    return get_hole_distance_goal(state, xy_g)

def get_hole_distance_goal(state=np.ndarray, xy_g=()):
    # global d
    xy_0 = get_xy(state, hole)
    d = math.fabs(xy_0[0] - xy_g[0]) + math.fabs(xy_0[1] - xy_g[1])
    # --------
    # d = (d - 1) + 4
    # (d - 1) kad butu salia o ne vietoj
    # 4 - ejimu sk. skirtas prieiti is kitos puses
    # d = d + 3
    return d


def get_max_step_count(state=np.ndarray, g=5):
    return get_max_step_count_n(state, g, False)


def get_max_step_count_n(state=np.ndarray, g=4, fixed=bool):
    # if g == 13: return 22
    # if goals_10___14.__contains__(g) : return max_steps_10___14
    # if goals_11___15.__contains__(g) : return max_steps_11___15

    xy_g = get_xy(state, g)
    p = (le_0, 0) if fixed else get_array_and_x_shift(g)
    if (p is None or p[0] is None): return 0
    m = np.array(p[0])
    # x_shift = p[1]
    xy = (xy_g[0] + p[1], xy_g[1])
    min_steps = get_min_steps(xy, m)
    min_steps = min_steps + get_hole_distance_goal(state, xy_g)
    return min_steps


def get_steps_left(state=np.ndarray, g=4, steps_max=int, steps_done=int):
    steps_left = steps_max - steps_done
    xy_g = get_xy(state, g)
    distnc = get_hole_distance_goal(state, xy_g) - 3

    v0 = get_max_step_count_n(state, g, fixed=False)
    v1 = get_max_step_count_n(state, g, fixed=True)
    b0 = steps_left < v0
    b1 = steps_left < v1
    return steps_left, v0, v1, b0, b1

# print(get(5))

# state, g, steps_gone,
# get_goal_xy
# get_steps_count 4 xy
# get_hole_distance_goal

# steps_gone 20
# max 30

# [[ ,  ,  , o],
#  [ , x,  ,  ],
#  [ ,  ,  ,  ],
#  [4,  ,  ,  ]]
#


