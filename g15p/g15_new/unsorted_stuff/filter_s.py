import numpy as np
from g15_new.unsorted_stuff.board import hole, get_xy
from g15_new.unsorted_stuff.g15_contstants import goals_tail
from g15_new.unsorted_stuff.g15_functions_0 import get_goal

s0 = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])


def filter_state(s=[], g=int):
    if goals_tail.__contains__(g): return s
    s = np.array(s)
    s = np.reshape(s, [16])
    h = hole

    # -----------
    g, g0 = get_g0(g)
    # -----------

    i0 = g - 1
    i1 = np.where(s == g)[0][0]
    i2 = np.where(s == h)[0][0]

    # -----------
    i3 = get_i3(g0, s)
    # -----------

    s = s[0:i0]
    s = np.append(s, s0)
    s = s[0:16]
    s[i1] = g
    s[i2] = h

    # -----------
    set_i3(i3, s)
    # -----------

    return np.reshape(s, [4, 4])


# ------special case----------------
def set_i3(i3, s):
    if i3 == None: return
    for x in i3:
        s[x[0]] = x[1]


def get_i3(g0, s):
    if g0 == None: return None
    return [(np.where(s == x)[0][0], x) for x in g0]


def get_g0(g):
    g0 = None
    if g == 13:
        g = 9
        g0 = [13]
    if g == 14 or g == 10:
        g = 10
        g0 = [13, 14]
    return g, g0


# ------------------------

# =========old f=============
def filter_state_old(state=np.ndarray, gm=int):
    g = get_goal(state, gm)

    l = list([10, 11, 12, 14, 15])
    # l = list([11, 12, 15])
    if (l.__contains__(g)): return state

    xy = list(map(lambda e: get_xy(state, e), range(0, g + 1)))
    a = list(map(lambda e: -1, range(0, 16)))
    a = np.reshape(a, [4, 4]).astype(int)

    for e in range(0, g + 1):
        if g == 13 and l.__contains__(e): continue
        a[xy[e][0], xy[e][1]] = e

    return a
# =========old f=============
