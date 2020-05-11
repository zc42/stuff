import math

import numpy as np

from g15_new.unsorted_stuff.board import get_xy, distance_from_origin, hole
from g15_new.unsorted_stuff.max_step_counts import get_h_distance_2_g
from g15_new.unsorted_stuff.mask_tester import test_masks_3, test_masks_7, test_masks_9_for_13


class GameSteps:
    def __init__(self, state=[], cell_steps=[], g=int):
        self.m = np.copy(cell_steps)
        self.pass_init_check = False
        self.pass_check = None
        self.steps_c0 = 0
        self.steps_c1 = 0
        self.g_distance_0 = None
        self.g_distance_1 = None
        self.exit = False
        self.loop_stpes = 0

        a = 5 if [4, 8, 13].__contains__(g) else 1
        self.inti_hole_distance = get_h_distance_2_g(state, g) + a

        self.last_g_xy = get_xy(state, g)
        self.init_g_xy = self.last_g_xy[0], self.last_g_xy[1]

    def get_loop_steps(self, state=[], g=int):
        xy_g = get_xy(state, g)
        return self.m[xy_g[0], xy_g[1]]

    def check_init_distance(self, state=[], g=int):
        self.steps_c0 += 1

        if (self.pass_init_check): return True

        g_xy = get_xy(state, g)
        if self.last_g_xy != None and g_xy != self.last_g_xy:
            self.pass_init_check = True
            self.last_g_xy = None
            return True

        if (self.steps_c0 < self.inti_hole_distance): return True

        if (self.steps_c0 >= self.inti_hole_distance):
            d = get_h_distance_2_g(state, g)
            if d > 1: return False
            self.pass_init_check = True
            self.just_pass_init_check = True
            self.last_g_xy = None

        return True

    def test_h_from_g_max_distance(self, state=[], g=int, max_d=int):
        xy_g = get_xy(state, g)
        xy_h = get_xy(state, hole)
        x = math.fabs(xy_h[0] - xy_g[0])
        y = math.fabs(xy_h[1] - xy_g[1])
        return x > max_d or y > max_d

    def check_1__9_13(self, state=[], g=int):
        if self.pass_init_check == False: return True
        if g == 4 and test_masks_3(state) == False: return False
        if g == 8 and test_masks_7(state) == False: return False
        if g == 13 and not test_masks_9_for_13(state): return False

        lx = [4, 8, 13]
        # s = 1 if lx.__contains__(g) else 1
        s = 2 if lx.__contains__(g) else 1
        if self.test_h_from_g_max_distance(state, g, s): return False

        if (self.last_g_xy is None
                or self.last_g_xy != get_xy(state, g)):
            self.steps_c1 = 0
            self.g_distance_0 = distance_from_origin(state, g)
            self.loop_stpes = self.get_loop_steps(state, g)
            self.last_g_xy = get_xy(state, g)

        if (self.steps_c1 >= self.loop_stpes):
            self.g_distance_1 = distance_from_origin(state, g)
            if self.g_distance_1 == 0:
                self.pass_check = True
                return True
            if self.g_distance_1 >= self.g_distance_0:
                self.pass_check = False
                return False

            self.g_distance_0 = self.g_distance_1
            self.steps_c1 = 0

        self.steps_c1 += 1

        return True

    def check(self, state=[], g=int):
        # ==============================
        lx = [10, 11, 12, 14, 15]
        if lx.__contains__(g): return True
        # ==============================
        if self.check_init_distance(state, g) == False:
            self.exit = True
            return False
        # ==============================
        b = self.check_1__9_13(state, g)
        self.exit = not b
        if not b:
            b = b

        return b

    def print_info(self):
        return self.inti_hole_distance, \
               self.steps_c0, \
               self.pass_init_check, \
               self.g_distance_0, \
               self.g_distance_1, \
               self.steps_c1, \
               self.pass_check, \
               self.loop_stpes, \
               self.exit
