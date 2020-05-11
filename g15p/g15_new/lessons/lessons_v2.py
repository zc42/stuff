from random import shuffle
from lazy_streams import stream
import numpy as np

from g15_new.lessons.bord_possibilities.case_10 import ma_10
from g15_new.lessons.bord_possibilities.case_13 import ma_13
from g15_new.lessons.bord_possibilities.case_1_5_9 import ma_1_5_9
from g15_new.lessons.bord_possibilities.case_2_6 import ma_2_6
from g15_new.lessons.bord_possibilities.case_3_7 import ma_3_7
from g15_new.lessons.bord_possibilities.case_4_8 import ma_4_8
from g15_new.lessons.h_walk_map import get_all_maps, get_map_for_h_xy, get_h_choices, get_g_xy, need_walk_around
from g15_new.unsorted_stuff.board import get_origin_xy, get_xy, hole
from g15_new.unsorted_stuff.max_step_counts import get_h_distance_2_g
from g15_new.lessons.lesson_groups import Lesson_group, Lesson_groups, Lsn
from g15_new.lessons.bord_possibilities.case_14 import ma_14
from g15_new.lessons.bord_possibilities.case_15 import ma_15
from g15_new.lessons.random_borad import get_random_board_aa, \
    get_random_board_13, get_random_board_10, get_random_board_14, get_random_board_15


class Lessons_v2():
    # region init
    def __init__(self, lessons=Lesson_groups):
        self.goals = list(range(1, 16))
        self.lessons_done = dict()
        self.lessons_grps = lessons
        self.lessons_grps_indx = 0
        self.all_lessons_holder = self.get_all_lessons()
        self.init_0()

    def init_0(self):
        self.lessons_grp = self.lessons_grps.a[self.lessons_grps_indx]
        self.all_lessons = list(self.all_lessons_holder)
        self.all_lessons = self.filter_lessons(self.lessons_grp, self.all_lessons)
        shuffle(self.all_lessons)
        self.init_1(0)

    # endregion

    def init_1(self, l_indx=int):
        # self.test_one_case()
        self.init_2(l_indx)

    def test_one_case(self):
        self.all_lessons = list(self.all_lessons_holder)
        self.set_lesson(14, 1, (2, 2))

        # (15, 1, (2, 2))
        # (15, 3, (2, 2))

    # region unsorted_stuff
    def init_2(self, l_indx=int):
        self.l_indx = l_indx
        self.current_lesson = self.all_lessons[self.l_indx]
        self.g = self.current_lesson[0]
        self.lesson_nb = self.current_lesson[1]
        # ------------
        self.ma = self.get_ma(self.g)

        c = self.current_lesson[2]
        self.__board = self.get_board(self.g, self.lesson_nb, c)
        self.__possible_cell_steps = self.get_possible_cell_steps(self.g, self.lesson_nb)
        self.__max_board_steps = self.get_max_borad_steps()

        self.h_walk_map = self.get_walk_map()
        # print(self.h_walk_map)

    def get_walk_map(self):
        a = self.ma[self.lesson_nb][0]
        c = self.current_lesson[2]
        walk_maps = get_all_maps(a)

        # if self.g == 1: return walk_maps[0][0]
        return get_map_for_h_xy(walk_maps, c)

    def get_all_lessons(self):
        l = []
        for g in self.goals:
            self.ma = self.get_ma(g)
            self.generate_lessons_v2(g, l)
        return l

    def generate_lessons_v2(self, g, l):
        for nb in range(len(self.ma)):
            v = self.get_ma(g)[nb][0]
            choices_xy_h = get_h_choices(v)
            for c in choices_xy_h:
                self.append_lesson(l, c, g, nb)

    def generate_lessons_v1(self, _ma, g, l):
        choices_xy_h = _ma[1]
        for c in choices_xy_h:
            for nb in range(len(self.ma)):
                self.append_lesson(l, c, g, nb)

    def append_lesson(self, l, c, g, nb):
        x = self.get_board(g, nb, c)
        if isinstance(x, np.ndarray):
            l.append((g, nb, c))

    def get_ma(self, g=int):
        if [1].__contains__(g): return ma_1_5_9
        if [5, 9].__contains__(g): return ma_1_5_9
        if [2, 6].__contains__(g): return ma_2_6
        if [3, 7].__contains__(g): return ma_3_7
        if [4, 8].__contains__(g): return ma_4_8
        if [13].__contains__(g): return ma_13
        if [14].__contains__(g): return ma_14
        if [10].__contains__(g): return ma_10
        if [11, 12, 15].__contains__(g): return ma_15
        return None

    # def get_board_4_tail(self, g=int, c=()):
    #     if [10, 14].__contains__(g): return get_random_board_10__14(g, c)
    #     if goals_11___15.__contains__(g): return get_random_board_10__14(g, c)
    #     return None

    def get_board_13(self, g=int, lesson_nb=int, c=()):
        if g != 13: return None
        xy = self.g_start_xy(g, lesson_nb, True)
        if xy is None: return None
        # --------------
        if g == 13: return get_random_board_13(xy, c)
        return None

    def get_board_1__9(self, g=int, lesson_nb=int, xy_h=()):
        # if g == 9 and lesson_nb == 10:
        #     g = g

        xy_g = self.g_start_xy(g, lesson_nb, True)
        if xy_g is None: return None
        xy_h = self.shift_xy(g, xy_h, False)
        if xy_g == xy_h: return None
        # --------------
        return get_random_board_aa(g, xy_g, xy_h)

    def get_board_10_14_15(self, g=int, lesson_nb=int, xy_h=()):
        if not [10, 14, 11, 12, 15].__contains__(g): return None
        xy_g = self.g_start_xy(g, lesson_nb, True)
        if xy_g is None: return None
        if g == 10: return get_random_board_10(xy_g, xy_h)
        if g == 14: return get_random_board_14(xy_g, xy_h)
        return get_random_board_15(xy_g, xy_h)

    def get_board(self, g=int, lesson_nb=int, c=()):
        if g == 14:
            g = g

        # # -----------
        # r = self.get_board_4_tail(g, c)
        # if isinstance(r, np.ndarray): return r
        # --------------
        r = self.get_board_13(g, lesson_nb, c)
        if isinstance(r, np.ndarray): return r
        # --------------
        r = self.get_board_10_14_15(g, lesson_nb, c)
        if isinstance(r, np.ndarray): return r
        # --------------
        r = self.get_board_1__9(g, lesson_nb, c)
        return r

    def board(self):
        return self.__board

    def get_possible_cell_steps(self, g=int, lesson_nb=int):
        # lx = goals_11___15
        # if lx.__contains__(g): return None
        xy = self.g_start_xy(g, lesson_nb, True)
        if xy is None: return None

        a = np.copy(self.ma[lesson_nb][1])
        # b = np.copy(self.ma[lesson_nb][1])
        steps = self.shift_step_g(g)
        a = np.roll(a, steps, axis=0).tolist()
        # b = np.roll(b, steps, axis=0).tolist()
        return a

    def possible_cell_steps(self):
        return self.__possible_cell_steps

    def check_h(self, s=[]):
        xy_h = get_xy(s, hole)

        m = self.h_walk_map
        x = xy_h[0] + self.shift_ma_x(self.g)
        v = m[x][xy_h[1]]

        r = v > -1
        return r

    def shift_ma_x(self, g=int):
        if [5, 6, 7, 8].__contains__(g): return -1
        if g == 9: return -2
        return 0

    def check_g(self, s=[]):
        # lx = goals_11___15
        # if lx.__contains__(self.g): return True
        xy_h = get_xy(s, self.g)
        m = self.ma[self.lesson_nb][1]
        x = xy_h[0] + self.shift_ma_x(self.g)
        v = m[x][xy_h[1]]
        r = v != 0
        if not r:
            r = r
        return r

    def __g_start_xy(self, g, lesson_nb, ma, shift_g):
        if len(ma) < lesson_nb + 1: return None

        a = ma[lesson_nb][0]
        # try:
        xy = get_g_xy(a)
        # except Exception as e:
        #     xy = get_g_xy(a)

        # xy = ma[lesson_nb][3]
        xy = self.shift_xy(g, xy, shift_g)
        b = xy[0] > 3 or xy[1] > 3
        return None if b else xy

    def g_start_xy(self, g, lesson_nb, shift_g):
        return self.__g_start_xy(g, lesson_nb, self.ma, shift_g)

    def shift_xy(self, g, xy, shift_g):
        a = self.shift_step_g(g) \
            if shift_g \
            else self.shift_step_h(g)

        return xy[0] + a, xy[1]

    def shift_step_h(self, g=int):
        return self.shift_step_gh(g, [5, 6, 7, 8])

    def shift_step_g(self, g=int):
        return self.shift_step_gh(g, [5, 6, 7, 8])

    def shift_step_gh(self, g=int, lx=[]):
        if lx.__contains__(g): return 1
        if g == 9: return 2
        return 0

    def get_max_borad_steps(self):
        b = self.board()
        if b is None: return None
        # --------------
        d1 = get_h_distance_2_g(b, self.g)
        d2 = np.array(self.possible_cell_steps()).sum();
        d3 = 3 if self.need_walk_around() else 0

        d = d1 + d2 + d3

        return d

    def max_borad_steps(self):
        a = 1 if self.g == 1 else 0
        return self.__max_board_steps + a

    def next(self, i=int, l=[]):
        return 0 if i >= len(l) - 1 else i + 1

    def next_lesson(self):
        # =========
        i = self.l_indx
        i = self.next(i, self.all_lessons)
        self.l_indx = i
        # =========
        # g = self.all_lessons[i][0]
        # n = self.all_lessons[i][1]
        # =========
        self.init_1(i)
        # =========
        if not isinstance(self.board(), np.ndarray):
            self.next_lesson()

    def need_walk_around(self):
        s = self.board()
        g = get_origin_xy(self.g)
        x = get_xy(s, self.g)
        h = get_xy(s, 0)
        return need_walk_around(g, x, h)

    def set_lesson(self, g=int, l_nb=int, xy_h=()):
        # self.all_lessons
        l = list(filter(lambda x: \
                            x[0] == g and \
                            x[1] == l_nb and \
                            x[2] == xy_h,
                        self.all_lessons))

        if len(l) == 0: raise RuntimeError("lesson not found: " + str((g, l_nb, xy_h)))
        if len(l) > 1: raise RuntimeError("found more than one lesson: " + str((g, l_nb, xy_h)))
        indx = self.all_lessons.index(l[0])
        self.init_2(indx)

    def contains(self, l=[Lsn], lsn=()):
        r = stream(l) \
            .filter(lambda e: e.g == lsn[0]) \
            .filter(lambda e: e.lesson_nb == None or e.lesson_nb == lsn[1]) \
            .filter(lambda e: e.h_xy == () or e.h_xy == lsn[2]) \
            .first_or_else(None)

        return r != None

    def filter_lessons(self, lg=Lesson_group, all_lessons=[]):
        l = stream(all_lessons) \
            .filter(lambda x: self.contains(lg.a, x)) \
            .to_list()
        return l

    def get_log_name(self):
        return self.lessons_grp.name

    def next_lsn_grp(self):
        if self.all_groups_done(): return
        a = self.lessons_grps.a[self.lessons_grps_indx]
        size = len(self.lessons_grps.a)
        if not a.done: return
        a.done = True
        self.lessons_grps_indx += 1
        if self.lessons_grps_indx >= size: return
        self.init_0()

    def current_lesson_done(self, done=bool):
        key = self.all_lessons[self.l_indx]
        self.lessons_done[key] = done

    def group_lessons_done(self):
        if self.all_groups_done(): return True
        r = next(filter(lambda x: x == False, self.lessons_done.values()), True)
        a = self.lessons_grps.a[self.lessons_grps_indx]
        a.done = r
        return r

    def all_groups_done(self):
        r = next(filter(lambda x1: x1 == False, map(lambda x: x.done, self.lessons_grps.a)), True)
        return r
    # endregion
