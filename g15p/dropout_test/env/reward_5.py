import math
import g15_new.unsorted_stuff.board as brd
import g15_new.hof.encoder_0 as enc

from dropout_test.env.grid_context import GridCtx, hole

minus_rwrd = -10


# def need_exit(ctx=GridCtx):
#     ctx.exit = None
#     if is_state_in_history(ctx): ctx.exit = "is_state_in_history == True"
#     if ctx.step_count > ctx.max_step_count: ctx.exit = "ctx.step_count >= fnc.max_step_count(ctx)"
#     if ctx.exit != None: return True
#     return False

def need_exit(ctx=GridCtx):
    return ctx.step_count > 10
    # ctx.exit = None
    # if is_state_in_history(ctx): ctx.exit = "is_state_in_history == True"
    # if ctx.step_count > ctx.max_step_count: ctx.exit = "ctx.step_count >= fnc.max_step_count(ctx)"
    # if ctx.exit != None: return True
    # return False


# def calc_reward_new(ctx=GridCtx):
#     if need_exit(ctx): return minus_rwrd, True
#     if is_finished(ctx):  return ctx.final_rwdr, True
#     r = calc_reward_4_distance_from_goal(ctx)
#     r = r * 1e-02
#     return r, False

def calc_reward_new(ctx=GridCtx):
    if need_exit(ctx): return minus_rwrd, True
    if is_finished(ctx):  return ctx.final_rwdr, True
    return -1, False
    # r = calc_reward_4_distance_from_goal(ctx)
    # r = r * 1e-02
    # return r, False


def is_finished(ctx=GridCtx):
    xy_h = brd.get_xy(ctx.state, hole)
    b = xy_h == ctx.xy_g
    if b: ctx.register_as_passed()
    return b


def calc_reward_4_distance_from_goal(ctx=GridCtx):
    xy_g = ctx.xy_g
    xy_h = brd.get_xy(ctx.state, hole)
    d = math.fabs(xy_g[0] - xy_h[0]) + math.fabs(xy_g[1] - xy_h[1])
    v = 15 - d
    return v


def add_total_reward(ctx=GridCtx, v=None):
    ctx.total_reward = ctx.total_reward + v


def negative_reword(ctx=GridCtx):
    ctx.reward = minus_rwrd  # + (self.step_count * -1)
    add_total_reward(ctx, ctx.reward)
    # self.print_finishe_level()
    return enc.state_encoded_4_grid(ctx=ctx), \
           ctx.reward, \
           True, \
           ctx.state
