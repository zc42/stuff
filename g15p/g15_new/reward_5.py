from g15_new.g15_context import Ctx, circle1, circle2
from g15_new.lessons.objective_goto_base.reward_4_base_objctv import need_exit_4_base, calc_reward_4_base
from g15_new.lessons.corner_objectives.case_13_objective_1 import objective_for_goal_13
from g15_new.lessons.corner_objectives.case_14_objective_1 import objective_for_goal_14
from g15_new.lessons.corner_objectives.case_4_8_objective_1 import objective_for_goals_4_and_8
from g15_new.unsorted_stuff.board import distance_from_hole_to_goal_number, distance_from_origin, hole, \
    distance_from_v1_to_v2
from g15_new.unsorted_stuff.g15_functions_1 import is_state_in_history, max_step_count
from g15_new.unsorted_stuff.mask_tester import is_all_masks_ok, test_masks_14_ok, manhattan_heuristic

minus_rwrd = -1


def circle_detected(ctx=Ctx):
    if len(ctx.action_history) < 12:
        return False

    l = ctx.action_history
    if not l.__contains__(1): return False
    i = l.index(1)
    if i == -1: return False

    l0 = l[i:] + l[:i]
    b = l0 == circle1 or l0 == circle2
    return b


def need_exit(ctx=Ctx):
    rsn = None

    if rsn == None and is_all_masks_ok(ctx.state, ctx.prev_state) == False: rsn = "is_all_masks_ok == False"
    if rsn == None and is_state_in_history(ctx): rsn = "state_in_history"
    if rsn == None and circle_detected(ctx): rsn = "circle_detected"

    ctx.exit_rsn = rsn
    return rsn != None


def is_terminal_step(ctx=Ctx, f=bool):
    if f: return f
    # ----------------------------
    if ctx.test_rndm: return False
    # ----------base ..-----------
    if ctx.run_base_objective:
        b = need_exit_4_base(ctx)
        ctx.exit_rsn = '[base obj] need_exit .. '
        return b
    # ---------------------

    rsn = None
    # ---------------------
    s, cl, c0 = ctx.state, ctx.lessons.current_lesson, ctx.g_steps.steps_c0
    if rsn == None and not objective_for_goals_4_and_8(s, cl, c0): ctx.exit_rsn = "objective_for_goals_4_and_8"
    if rsn == None and not objective_for_goal_13(s, cl, c0): rsn = "objective_for_goal_13"
    if rsn == None and not objective_for_goal_14(s, cl, c0): rsn = "objective_for_goal_14"
    if rsn == None and not ctx.lessons.check_h(s): rsn = "ctx.lessons.check_h"
    if rsn == None and not ctx.lessons.check_g(s): rsn = "ctx.lessons.check_g"
    if rsn == None and not ctx.g_steps.check(s, ctx.lessons.g): rsn = "g_steps.check"
    if rsn == None and need_exit(ctx): rsn = ctx.exit_rsn
    if rsn == None and ctx.step_count >= max_step_count(ctx): rsn = "ctx.step_count >= fnc.max_step_count(ctx)"
    # ---------------------
    ctx.exit_rsn = rsn
    return rsn != None


def calc_reward(ctx=Ctx, f=bool):
    if f: return minus_rwrd
    # ----------------------------
    if ctx.run_base_objective: return calc_reward_4_base(ctx)

    s = ctx.state
    g = ctx.goal

    if test_masks_14_ok(s):
        r = manhattan_heuristic(s) / 2 * 1e-02
        return r

    r1 = (6 - distance_from_hole_to_goal_number(s, g, hole)) * 1e-02
    r2 = (15 - distance_from_origin(s, g)) * 1e-02
    r = (r1 + r2) * 1.61803398875  # * 5e-01 .. 1.61803398875 <- magic..

    return r


def calc_reward_4_distance_from_goal(ctx=Ctx, goal=None):
    v = distance_from_v1_to_v2(ctx.state, goal, hole)
    v = 0 if v < 2 else v
    v = 6 - v
    return v
