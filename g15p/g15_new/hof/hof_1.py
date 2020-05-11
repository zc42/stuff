from g15_new.lessons.objective_goto_base.base_objctv_func import if_is_need_go_2_base
from g15_new.lessons.objective_goto_base.reward_4_base_objctv import is_base_objctv_finished
from g15_new.hof.reward_5 import is_terminal_step, calc_reward, minus_rwrd
from g15_new.hof.encoder_0 import state_encoded
from g15_new.g15_context import Ctx
from g15_new.unsorted_stuff.g15_contstants import goals_tail
from g15_new.unsorted_stuff.g15_functions_1 import is_game_finished
from g15_new.unsorted_stuff.mask_tester import test_masks_g, test_masks_10_ok, test_masks_13_ok, test_masks_14_ok
import g15_new.unsorted_stuff.g15_functions_1 as fnc
import g15_new.unsorted_stuff.g15_functions_0 as fnc_0


def hof_4_encode_state(ctx=Ctx):
    return state_encoded(ctx)


def hof_4_check_action(ctx=Ctx):
    ctx.prev_goal = get_goal(ctx)
    # region ---------chechk available_actions-----------
    avlbl_actions = fnc.get_available_actions(ctx)
    f = not ctx.keyboard
    f = f and not avlbl_actions.__contains__(ctx.get_last_action())
    # endregion
    r = minus_rwrd if f else 0

    if f:  # 4 debug ..
        return f, r

    return f, r


def hof_4_rwrd(ctx=Ctx, f=bool, r=int):
    if f: return f, r
    # if ctx.max_goal == 13:
    #     ctx = ctx

    ctx.set_not_alowed_action()
    reset_state_hist_when_goal_changed(ctx)

    # todo: -> hof
    f = False
    # region ---------test if lesson done--------------
    b = not ctx.test_rndm
    b = b and not ctx.run_base_objective
    b = b and is_lesson_finished(ctx)
    if b: r, f = ctx.final_rwdr, True
    # r, f = if_lesson_finished(b)
    # endregion
    # region ----------test if base objective done--------------
    b = not f
    b = b and not ctx.test_rndm
    b = b and ctx.run_base_objective
    b = b and is_base_objctv_finished(ctx)
    if b: r, f = ctx.final_rwdr, True
    # endregion
    # region --------test if terminal & calc reward-----------------
    f = is_terminal_step(ctx, f)
    r = calc_reward(ctx, f)
    # endregion
    # region --------test if game done-----------------
    done = is_game_done(ctx, f)
    if done: r = ctx.final_rwdr
    f = f or done
    # endregion
    return f, r


def is_lesson_finished(ctx=Ctx):
    g = ctx.lessons.g
    f = g < 10 and test_masks_g(g, ctx.state)

    f = f or (g == 10 and test_masks_10_ok(ctx.state))
    f = f or (g == 13 and test_masks_13_ok(ctx.state))
    f = f or (g == 14 and test_masks_14_ok(ctx.state))
    f = f or (goals_tail.__contains__(g) and test_masks_g(15, ctx.state))
    return f


def is_game_done(ctx=Ctx, f=bool):
    if f: return False
    return is_game_finished(ctx)


# region reset_state_hist_when_goal_changed
def reset_state_hist_when_goal_changed(ctx=Ctx):
    if check_base_objctv_2(ctx): reset_vars_after_base_objctv_done(ctx)

    g = get_goal(ctx)
    if g != ctx.prev_goal: ctx.not_alowed_action = -1

    ctx.set_max_goal(g)

    if if_goal_achived(ctx, g):
        ctx.set_init_xy(g)
        ctx.action_history.clear()


def if_goal_achived(ctx=Ctx, g=int):
    b = test_goal_regular(ctx, g)
    b = b or test_goal_tail(ctx, g)
    return b


def test_goal_regular(ctx=Ctx, g=int):
    b = g != ctx.prev_goal
    b = b and not goals_tail.__contains__(g)
    return b


def test_goal_tail(ctx=Ctx, g1=int):
    g0 = ctx.prev_goal
    b = g0 != g1
    b = b and not goals_tail.__contains__(g0)
    b = b and goals_tail.__contains__(g1)
    return b


def get_goal(ctx=Ctx):
    if need_goto_base(ctx): return 0
    return fnc_0.get_goal(ctx.state, ctx.max_goal)


def need_goto_base(ctx=Ctx):
    b = ctx.run_base_objective
    b = b or if_is_need_go_2_base(ctx.lessons, ctx.goal, ctx.init_h_xy)
    return b


def is_finished(ctx=Ctx):
    if check_base_objctv_1(ctx): return is_base_objctv_finished(ctx)

    if check_base_objctv_2(ctx):
        reset_vars_after_base_objctv_done(ctx)
        return False

    return fnc.is_finished(ctx)


def reset_vars_after_base_objctv_done(ctx=Ctx):
    ctx.run_base_objective = False
    ctx.set_goals(ctx.init_goal)
    ctx.not_alowed_action = -1


def check_base_objctv_2(ctx=Ctx):
    b = ctx.test_rndm
    b = b and ctx.run_base_objective
    b = b and is_base_objctv_finished(ctx)
    return b


def check_base_objctv_1(ctx=Ctx):
    b = not ctx.test_rndm
    b = b and ctx.run_base_objective
    return b
# endregion
