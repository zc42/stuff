import numpy as np
from g15_new.unsorted_stuff.board import get_xy, hole
from g15_new.g15_context import Ctx
from g15_new.unsorted_stuff.g15_functions_0 import get_goal


def get_state_4_zen(ctx=Ctx):
    g = get_goal(ctx.state, ctx.max_goal)
    g_xy = get_xy(ctx.state, g)
    h_xy = get_xy(ctx.state, hole)

    s = np.copy(ctx.state)
    s = np.reshape(s, [16]).tolist()
    s = list(map(lambda e: -1 if e != s.index(e) + 1 else e, s))
    s = np.reshape(s, [4, 4])
    s[g_xy[0], g_xy[1]] = g
    s[h_xy[0], h_xy[1]] = hole
    return s
