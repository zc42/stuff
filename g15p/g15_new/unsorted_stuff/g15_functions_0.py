import numpy as np
from keras.utils import to_categorical

from g15_new.unsorted_stuff.mask_tester import test_masks_is_9_and_not_13, test_masks_is_10_and_not_14


def local_reshape(l=[], newshape=[]):
    return np.reshape(l, newshape).astype(dtype=int).tolist()


def local_reshape_n(l=[], newshape=[]):
    l = np.reshape(l, newshape)
    l = np.reshape(l, [1, -1])
    return l

def xy_2_categorical(xy=()):
    x = to_categorical(xy[0], 4)
    y = to_categorical(xy[1], 4)
    x = local_reshape(x, [4])
    y = local_reshape(y, [4])
    return x, y

def get_goal(state=np.ndarray, gm=int):
    if test_masks_is_9_and_not_13(state): return 13
    if test_masks_is_10_and_not_14(state): return 14

    g1 = get_goal_0(state)

    if gm == 4 and g1 == 3: return 4
    if gm == 8 and g1 == 7: return 8
    if gm == 13 and g1 == 9: return 13
    if gm == 14 and g1 == 10: return 14

    return g1


def get_goal_0(state=[]):
    # state = ctx.state if len(state) == 0 else state
    a = np.reshape(state, [16]).tolist()
    r = 1
    for x in a:
        if x == a.index(x) + 1:
            r = x + 1
        else:
            break

    r = 0 if r == 15 and a[15] == 0 else r
    r = 0 if r == 16 else r
    return r

