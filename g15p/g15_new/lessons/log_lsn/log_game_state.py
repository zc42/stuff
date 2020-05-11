from g15_new.g15_context import Ctx
import numpy as np

log_name = './failed_game_states.txt'


def need_2_write(ctx=Ctx):
    b = ctx.test_rndm
    b = b and not ctx.keyboard
    return b


def log_failed_game(ctx=Ctx):
    if not need_2_write(ctx): return
    h = ctx.state_hist
    if len(h) == 0: return

    s0 = h[0]
    s1 = get_state1(h, ctx.goal)
    write(s0, s1, ctx.goal, ctx.max_goal)


# ... neveiks visad .. bet ir nereik..
def is_g_in_place(s=np.ndarray, g=int):
    s = np.reshape(s, [16])
    v = s[g - 1]
    return v == g


def get_state1(h=[], g=int):
    g = g - 1
    if g < 1: return None

    h = reversed(h)
    for s in h:
        if is_g_in_place(s, g): return s

    return None


def write(s0=np.ndarray, s1=np.ndarray,
          g=int, gmax=int):
    f = open(log_name, 'a')
    f.writelines(str(s0.tolist()) + '\n')
    if isinstance(s1, np.ndarray):
        f.writelines(str(s1.tolist()) + '\n')
    f.writelines('g: ' + str(g) + '\n')
    f.writelines('gmax: ' + str(gmax) + '\n')
    f.writelines('-----------------\n')
    f.close()
