import math

from keras.utils import to_categorical

import g15_new.g15_context as gctx
import g15_new.unsorted_stuff.board as brd
from g15_new.unsorted_stuff.mask_tester import mask_13, mask_8, mask_6, mask_5, mask_4, mask_2, mask_1, is_mask_ok, \
    mask_3, mask_7, test_masks_is_9_and_not_13, test_masks_is_10_and_not_14
from g15_new.unsorted_stuff.max_step_counts import get_max_step_count
import numpy as np

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


def get_goal(state=np.ndarray, gm=int):
    if test_masks_is_9_and_not_13(state): return 13
    if test_masks_is_10_and_not_14(state): return 14

    g1 = get_goal_0(state)

    if gm == 4 and g1 == 3: return 4
    if gm == 8 and g1 == 7: return 8
    if gm == 13 and g1 == 9: return 13
    if gm == 14 and g1 == 10: return 14

    return g1





def is_state_in_history(ctx=gctx.Ctx):
    l = ctx.state_hist
    s = ctx.state
    # try:
    for s0 in l:
        if np.array_equal(s0, s): return True
    return False

def max_step_count(ctx=gctx.Ctx, level=None):
    if ctx.test_rndm: return 10000
    # if ctx.keyboard: return 10000
    # if ctx.tail: return ctx.max_game_step_count

    # level = ctx.current_level if level is None else level
    return ctx.lessons.max_borad_steps()


def get_available_actions(ctx=gctx.Ctx):
    l = brd.get_available_actions(ctx.state)
    l = list(map(lambda e: ctx.actions.index(e), l))

    a = ctx.not_alowed_action
    if l.__contains__(a): l.remove(a)

    return l


def add_to_action_history(action_history, action, size):
    x = action_history
    x.append(action)
    if len(x) > size:
        list.pop(x, 0)
    return x


def get_level_goal_distances(state, g):
    a = list(range(1, g + 1))
    a = list(map(lambda e: brd.distance_from_origin(state, e), a))
    return a


def is_level_finished(ctx=gctx.Ctx):
    a = get_level_goal_distances(ctx.state, ctx.current_level + 1)
    a = list(filter(lambda x: x > 0, a))
    r = len(a) == 0
    return r


def level_up(ctx=gctx.Ctx):
    ctx.action_history = []
    ctx.not_alowed_action = -1
    g = get_goal(ctx.state, ctx.max_goal)
    ctx.current_level = g - 1
    ctx.step_count = 0
    ctx.max_steps = get_max_step_count(ctx.state, g)

    # self.update_goals_collected(self.current_level)
    # self.print_next_level_nb()


def get_borad_variations_count(ctx=gctx.Ctx):
    a = list(i for i in range(1, 16))
    a = list(brd.distance_from_origin(ctx.state, i) for i in a)
    a = len(list(filter(lambda x: x != 0, a)))
    a = math.factorial(a)
    return a


def is_finished(ctx=gctx.Ctx):
    return ctx.step_count > max_step_count(ctx) \
           or is_game_finished(ctx)


def is_game_finished(ctx=gctx.Ctx):
    r = np.array_equal(ctx.state, brd.f_state)
    if r: print("GAME is FINISHED!")
    return r





def get_level(ctx=gctx.Ctx):
    b = 0
    b = 13 if b == 0 and is_mask_ok(mask_13, ctx.state) else b
    b = 8 if b == 0 and is_mask_ok(mask_8, ctx.state) else b
    b = 7 if b == 0 and is_mask_ok(mask_7, ctx.state) else b
    b = 6 if b == 0 and is_mask_ok(mask_6, ctx.state) else b
    b = 5 if b == 0 and is_mask_ok(mask_5, ctx.state) else b
    b = 4 if b == 0 and is_mask_ok(mask_4, ctx.state) else b
    b = 3 if b == 0 and is_mask_ok(mask_3, ctx.state) else b
    b = 2 if b == 0 and is_mask_ok(mask_2, ctx.state) else b
    b = 1 if b == 0 and is_mask_ok(mask_1, ctx.state) else b
    return b


def get_max_steps_4_level(ctx=gctx.Ctx):
    lvl = get_level(ctx)
    r = 0
    r = 21 if lvl == 0 else r
    r = 21 if lvl == 1 else r
    r = 21 if lvl == 2 else r
    r = 32 if lvl == 3 else r
    r = 17 if lvl == 4 else r
    r = 17 if lvl == 5 else r
    r = 17 if lvl == 6 else r
    r = 28 if lvl == 7 else r
    r = 30 if lvl == 8 else r
    r = 30 if lvl == 13 else r
    return r
