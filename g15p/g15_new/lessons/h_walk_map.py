import math

import numpy as np

h = 0
d = 1
o = 1
x = 3
z = -1
H = -2


def get_h(v=np.ndarray):
    return np.where(v == H)


# def aaa(v=None):
#     v = np.array(v)
#
#     # x1 = get_h(v)
#     # print(x1)
#
#     x_xy = np.where(v == x)
#     h_xy = np.where(v == h)
#     H_xy = np.where(v == H)
#
#     x_xy = get_xy(x_xy, 0)
#     h_xy = get_xy(h_xy, 0)
#
#     H_xy_a = [get_xy(H_xy, i) for i in range(len(H_xy))]
#
#     # H_xy0 = get_xy(H_xy, 0)
#     # H_xy1 = get_xy(H_xy, 1)
#     # H_xy2 = get_xy(H_xy, 2)
#
#     print('x: ', x_xy)
#     print('h: ', h_xy)
#     for i in range(len(H_xy_a)):
#         print('H_xy[' + str(i) + ']: ', H_xy_a[i])
#     # print(h_xy, 0)
#     # print(H_xy, 0)
#     # print(H_xy, 1)
#     # print(H_xy, 2)
#
#     d0 = dist(H_xy_a[0], x_xy)
#     d1 = dist(H_xy_a[1], x_xy)
#
#     # print(H_xy_a)
#     print(d0)
#     print(d1)
#
#     print(v)


def dist(H_xy0, x_xy):
    return math.fabs(x_xy[0] - H_xy0[0]) + math.fabs(x_xy[1] - H_xy0[1])


def get_xy(a, i):
    x = a[0][i]
    y = a[1][i]
    return (x, y)


def get_primary_maps(m=np.ndarray):
    if not isinstance(m, np.ndarray): raise Exception('not isinstance(m, np.ndarray)')

    x_xy = np.where(m == x)
    x_xy = get_xy(x_xy, 0)
    h_xy_a = get_xy_a_for(m, h)
    r = []
    for h_xy in h_xy_a:
        v = (m, x_xy, h_xy)
        r.append(v)

    return r


def in_a_middle(xy0=(), xy1=(), xy2=()):
    b = middle_v(xy0[0], xy1[0], xy2[0])
    b = b or middle_v(xy0[1], xy1[1], xy2[1])
    return b


def replace_other_H(m=np.ndarray,
                    x_xy=(),
                    H_xy_a=[],
                    i=int):
    h_xy0 = H_xy_a[i]
    d0 = dist(h_xy0, x_xy)

    m = np.copy(m)
    m[h_xy0[0]][h_xy0[1]] = 4

    if len(H_xy_a) == 1: return m

    for j in range(len(H_xy_a)):
        if j == i: continue
        h_xy1 = H_xy_a[j]
        d1 = dist(h_xy1, x_xy)
        b = not in_a_middle(h_xy0, x_xy, h_xy1)
        if b and d1 < d0: m[h_xy1[0]][h_xy1[1]] = 4
    return m


def get_secondary_maps(m=np.ndarray):
    H_xy_a = get_xy_a_for(m, H)
    if len(H_xy_a) == 0: return None

    x_xy = get_xy_a_for(m, x)[0]

    r0 = []
    for i in range(len(H_xy_a)):
        r1 = replace_other_H(m, x_xy, H_xy_a, i)
        r2 = (r1, x_xy, H_xy_a[i])
        r0.append(r2)

    return r0


def get_all_maps(m=[]):
    m = np.array(m)

    a1 = get_primary_maps(m)
    a2 = get_secondary_maps(m)

    if a2 != None: a1.extend(a2)
    return a1


def get_h_choices(m=[]):
    m = np.array(m)
    a1 = get_xy_a_for(m, h)
    a2 = get_xy_a_for(m, H)
    a1.extend(a2)
    return a1


def get_g_xy(m=[]):
    m = np.array(m)
    x_xy = np.where(m == x)
    x_xy = get_xy(x_xy, 0)

    return x_xy


def get_map_for_h_xy(maps=[], h_xy=()):
    l = list(filter(lambda x: x[2] == h_xy, maps))
    if len(l) == 0 or len(l) > 1: raise Exception('len(l) == 0 or len(l) > 1')
    return l[0][0]


def get_xy_a_for(m, v=int):
    xy = np.where(m == v)
    xy_a = [get_xy(xy, i) for i in range(len(xy[0]))]
    return xy_a


def need_walk_around(g=(), x=(), h=()):
    b = middle_v(g[0], x[0], h[0])
    b = b or middle_v(g[1], x[1], h[1])
    return b


def middle_v(g=int, x=int, h=int):
    return (g < x < h) or (g > x > h)


def is_in_line(g=int, x=int, h=int):
    return g == x == h

# v = [[d, h, h, H],
#      [H, o, o, z],
#      [z, x, o, z],
#      [z, z, z, z]]
#
# print(get_h_choices(v))
#
# r = get_all_maps(v)
#
# for e in r:
#     print(e)
#
# print(get_map_for_h_xy(r, (0, 3)))
