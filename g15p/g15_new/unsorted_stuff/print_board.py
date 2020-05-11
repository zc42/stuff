import os
import time

import g15_new.unsorted_stuff.board as brd
import g15_new.unsorted_stuff.g15_functions_1 as fnc
from g15_new.hof.hof_1 import get_goal, is_finished
from g15_new.g15_context import Ctx
from g15_new.unsorted_stuff.render_rewards import  get_state_4_zen

from dropout_test.env.grid_4x4 import Game4x4
from dropout_test.env.grid_context import goal

CRED = '\033[91m'
CEND = '\033[0m'


def print_t(ctx=Ctx):
    if ctx.test_rndm: return

    inti_hole_distance, \
    steps_c0, \
    pass_init_check, \
    g_distance_0, \
    g_distance_1, \
    steps_c1, \
    pass_check, \
    loop_stpes, \
    exit = ctx.g_steps.print_info()

    print("----")
    print("inti_hole_distance: " + str(inti_hole_distance))
    print("steps_c0: " + str(steps_c0))
    print("pass_init_check: " + str(pass_init_check))
    print("g_distance_0: " + str(g_distance_0))
    print("g_distance_1: " + str(g_distance_1))
    print("steps_c1: " + str(steps_c1))
    print("pass_check: " + str(pass_check))
    print("loop_stpes: " + str(loop_stpes))
    print("exit: " + str(exit))


def pprint_test_info(game, r):
    os.system('clear')
    # print_stone_garden(game)
    # print()
    goal = get_goal(game.ctx)
    print_board(game, goal)
    print("----")
    print("lesson: " + str(game.ctx.lessons.lesson_nb))
    print("goal: " + str(goal))
    print("level: " + str(fnc.get_level(game.ctx)))
    print("step: " + str(game.ctx.step_count))
    print("max step: " + str(game.ctx.lessons.max_borad_steps()))
    print("exit rsn: " + str(game.ctx.exit_rsn))
    print("reward: " + str(r))
    print("total_reward: " + str(game.ctx.total_reward))
    print_t(game.ctx)
    # print("board variations: " + str(fnc.get_borad_variations_count(game.ctx)))

    time.sleep(0.5)
    if is_finished(game.ctx):
        print('done')
        time.sleep(3)
    return True


def pprint_grid_4x4(g=Game4x4, r=int):
    os.system('clear')
    # print_stone_garden(game)
    # print()
    # goal = game.get_goal()
    print_normal(g, goal)
    print("----")
    # print("lesson: " + str(game.ctx.lessons.lesson_nb))
    # print("goal: " + str(goal))
    # print("level: " + str(fnc.get_level(game.ctx)))
    print("step: " + str(g.ctx.step_count))
    # print("max step: " + str(game.ctx.lessons.max_borad_steps()))
    print("exit rsn: " + str(g.ctx.exit))
    print("reward: " + str(r))
    print("total_reward: " + str(g.ctx.total_reward))
    # print_t(game.ctx)
    # print("board variations: " + str(fnc.get_borad_variations_count(game.ctx)))

    time.sleep(0.5)
    if g.is_finished():
        print('done')
        time.sleep(3)
    return True


def print_board(game, goal=int):
    print_stone_garden(game)
    print_normal(game, goal)
    # print_rwrds(game, goal)


def print_normal(game, goal):
    print("-------------------------")
    for v in game.ctx.state:
        line = ''
        for e in v:
            if e == brd.hole:
                e = CRED + 'x' + CEND
            elif e == goal:
                e = CRED + str(e) + CEND
            line += str(e) + '\t'
        print(line)
    print("-------------------------")


def print_stone_garden(game):
    print("-------------------------")
    for v in get_state_4_zen(game.ctx):
        line = ''
        for e in v:
            if e == -1:
                e = ''
            elif e == 0:
                e = 'x'
            else:
                e = 'o'
            line += CRED + e + CEND + '\t'
        print(line)
    print("-------------------------")


# def print_rwrds(game, goal):
#     # blogai veikia
#     # veike kai paduodavau ctx.state, bet luzdavo kai ivarydavau 13 .. tai px gal kol kas
#     print("-------------------------")
#     game.ctx.state_4_rwrds = np.copy(game.ctx.state).tolist()
#     for v in add_rewads_2_state(game.ctx):
#         line = ''
#         for e in v:
#             if e == -1:
#                 e = CRED + 'x' + CEND
#             elif e == goal:
#                 e = CRED + str(e) + CEND
#             else:
#                 e = str(round(e, 2))
#                 # e = str(e)
#
#             line += e + '\t'
#         print(line)
#     print("-------------------------")
