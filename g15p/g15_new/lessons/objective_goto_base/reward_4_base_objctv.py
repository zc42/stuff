import math
import g15_new.unsorted_stuff.board as brd
import g15_new.hof.encoder_0 as enc
from g15_new.lessons.objective_goto_base.training_data import hole
from g15_new.g15_context import Ctx
from g15_new.unsorted_stuff.g15_functions_1 import is_state_in_history

minus_rwrd = -1


def need_exit_4_base(ctx=Ctx):
    ctx.exit = None
    if is_state_in_history(ctx): ctx.exit = "is_state_in_history == True"
    if ctx.step_count > ctx.baseObjCtx.max_step_count: ctx.exit = "step_count > max_step_count"
    if ctx.exit != None: return True
    return False


def calc_reward_4_base(ctx=Ctx):
    # if need_exit(ctx): return minus_rwrd, True
    # if is_base_objctv_finished(ctx):  return ctx.final_rwdr, True

    r = calc_reward_4_distance_from_goal(ctx)
    r = r * 1e-02
    return r


def is_base_objctv_finished(ctx=Ctx):
    xy_h = brd.get_xy(ctx.state, hole)
    b = xy_h == ctx.baseObjCtx.xy_g
    if b: ctx.baseObjCtx.register_as_passed()
    return b


def calc_reward_4_distance_from_goal(ctx=Ctx):
    xy_g = ctx.baseObjCtx.xy_g
    xy_h = brd.get_xy(ctx.state, hole)
    d = math.fabs(xy_g[0] - xy_h[0]) + math.fabs(xy_g[1] - xy_h[1])
    v = 15 - d
    return v


def add_total_reward(ctx=Ctx, v=None):
    ctx.total_reward = ctx.total_reward + v


def negative_reword(ctx=Ctx):
    ctx.reward = minus_rwrd  # + (self.step_count * -1)
    add_total_reward(ctx, ctx.reward)
    # self.print_finishe_level()
    return enc.state_encoded_4_grid(ctx=ctx), \
           ctx.reward, \
           True, \
           ctx.state
