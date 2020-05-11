import datetime

from keras.callbacks import ModelCheckpoint
import g15_new.unsorted_stuff.board as brd
import numpy as np

from g15_new.lessons.lesson_groups_2_test import get_lessons_3
from g15_new.lessons.log_lsn.log_entry import Log
from g15_new.lessons.objective_goto_base.base_objctv_func import if_is_need_go_2_base, encode_4_base
from g15_new.lessons.objective_goto_base.base_objective_ctx import BaseObjctvCtx
from g15_new.lessons.random_borad import get_random_board
from g15_new.lessons.steps_left import GameSteps
from g15_new.unsorted_stuff.g15_functions_0 import xy_2_categorical, get_goal
from g15_new.unsorted_stuff.max_step_counts import get_max_step_count
from g15_new.lessons.lessons_v2 import Lessons_v2

circle1 = [1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2]
circle2 = [1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0, 3]

brd_nbr = 0


class Ctx:

    def __init__(self,
                 test=False,
                 test_rndm_brd=False,
                 keyboard=False,
                 tail=False,
                 encode_4_conv=False,
                 encode_4_conv_v2=False,
                 lsns_log_dir=str,
                 test_name=str,
                 max_run_time=-1,
                 lesson_f=None,
                 lessons=None,
                 render=True,
                 base_objective=False):
        self.render = render
        self.start_t = datetime.datetime.now()
        # ---------------
        self.max_run_time = max_run_time
        self.runs_count = 0
        self.action_history_size = 50

        self.set_lesson(lesson_f, lessons)

        self.log = Log(log_dir=lsns_log_dir, test_name=test_name)
        self.log_write_count = 100
        # ---------------
        self.save_chk_point = False
        self.done = False
        self.test = test
        self.test_rndm = test_rndm_brd
        self.tail = tail
        self.keyboard = keyboard
        self.encode_4_conv = encode_4_conv
        self.encode_4_conv_v2 = encode_4_conv_v2

        self.base_objective__ = base_objective
        self.run_base_objective = base_objective
        self.baseObjCtx = BaseObjctvCtx()
        # if not base_objective: self.baseObjCtx = None

        # ------------
        self.init_by_need()

    def init_by_need(self):
        if self.test_rndm:
            self.init_test_rndm()
        elif self.base_objective__:
            self.init_base_obj_4_train()
        else:
            self.init_with_lessons()

    def set_lesson(self, lesson_f, lessons):
        if lessons != None:
            self.lessons = Lessons_v2(lessons)
            return
        f = lesson_f if lesson_f != None else get_lessons_3
        self.lessons = Lessons_v2(f())

    def init_with_lessons(self):
        self.test_run_time()
        if self.save_chk_point: self.save_check_point()
        if self.done: raise Exception('all done')
        # if self.runs_count > 20: raise Exception('all done')

        self.runs_count = self.runs_count + 1
        self.init_vars()

        self.lessons.next_lesson()
        # level_steps[self.lessons.g - 1] = self.lessons.max_borad_steps()

        self.state = np.copy(self.lessons.board())

        self.state_4_rwrds = []
        self.current_level = self.lessons.g - 1

        self.prev_state = np.copy(self.state)

        # ------------
        g = self.lessons.g
        self.max_steps = get_max_step_count(self.state, g)
        self.save_state()
        self.g_steps = GameSteps(self.state, self.lessons.possible_cell_steps(), g)
        self.set_goals(g)

    def init_base_obj_4_train(self):
        self.test_run_time()
        if self.save_chk_point: self.save_check_point()
        if self.done: raise Exception('all done')

        self.runs_count = self.runs_count + 1
        self.init_vars()

        self.baseObjCtx.init()
        self.state = np.copy(self.baseObjCtx.state)

        self.state_4_rwrds = []

        self.prev_state = np.copy(self.state)

        # ------------
        self.max_steps = self.baseObjCtx.max_step_count
        self.save_state()
        self.set_goals(brd.hole)
        # self.init_goal = (self.baseObjCtx.xy_g[1] + 1) \
        #                  + (self.baseObjCtx.xy_g[0] * 4)
        # print(self.init_goal)

    def init_test_rndm(self):
        self.test_rndm = True
        if self.done:
            self.done = False
            # raise Exception('all done')
        # ----------
        self.init_vars()
        # ----------

        # ++++++++++++++++++++++
        self.state = get_random_board()
        # self.state = np.array([[7, 11, 3, 0], [2, 14, 12, 10], [9, 8, 5, 15], [6, 4, 13, 1]])
        # ++++++++++++++++++++++

        self.prev_state = np.copy(self.state)

        # ------------
        self.max_steps = 100
        self.save_state()

        g = get_goal(self.state, self.max_goal)
        self.set_goals(g)

        b = if_is_need_go_2_base(self.lessons, g, self.init_h_xy)
        if b: self.prepare_4_base_obj()

    def prepare_4_base_obj(self):
        self.init_goal = self.goal
        self.clear_init_xy()
        self.baseObjCtx.state = encode_4_base(self.state, self.goal)
        self.baseObjCtx.set_max_steps()
        self.max_steps = self.baseObjCtx.max_step_count
        self.run_base_objective = True
        self.goal = 0

    def set_goals(self, g):
        if self.base_objective__: self.clear_init_xy()
        if not self.base_objective__: self.set_init_xy(g)
        self.set_max_goal(g)

    def init_vars(self):
        # ----------
        self.exit_rsn = ""
        self.state_hist = []
        self.rewards_for_distance = []
        self.reward = 0
        self.total_reward = 0
        self.action_history = []
        self.actions = brd.actions
        self.prev_goal = 0
        self.max_goal = 0
        self.final_rwdr = 10  # [5, 50][brd_nbr]
        self.step_count = 0
        self.total_step_count = 0
        self.not_alowed_action = -1
        # ----------

    def set_init_xy(self, g):
        self.init_g_xy = brd.get_xy(self.state, g)
        self.init_h_xy = brd.get_xy(self.state, brd.hole)
        self.g_h_xy_to_categorical()

    def clear_init_xy(self):
        self.init_g_xy = (0, 0)
        self.init_h_xy = (0, 0)
        self.g_h_xy_to_categorical()

    def g_h_xy_to_categorical(self):
        self.init_g_x, self.init_g_y = xy_2_categorical(self.init_g_xy)
        self.init_h_x, self.init_h_y = xy_2_categorical(self.init_h_xy)

    def save_state(self):
        a = np.copy(self.state)
        self.state_hist.append(a)

    def check_point(self, checkpoint=ModelCheckpoint):
        self.checkpoint = checkpoint

    def save_check_point(self):
        if self.test: return
        dir = self.checkpoint.filepath
        log_name = self.lesns_log_name
        f_name = dir + "__" + log_name + "__.hdf5"
        self.checkpoint.model.model.save_weights(f_name, overwrite=True)
        return f_name

    def save_weights(self, fn):
        f_name = fn + ".hdf5"
        self.checkpoint.model.model.save_weights(f_name, overwrite=True)

    def set_max_goal(self, g):
        gm = self.max_goal
        gm = g if gm < g else gm
        self.goal = g
        self.max_goal = gm

    def test_run_time(self):
        if self.max_run_time == -1: return

        t1 = self.start_t
        t2 = datetime.datetime.now()

        d = t2 - t1
        minutes = d.total_seconds() / 60
        b = self.max_run_time < minutes

        if b: raise Exception('run_time > max_run_time\n'
                              'max_run_time: '
                              + str(self.max_run_time))

    def set_not_alowed_action(self):
        a = self.get_last_action()
        if a == 0: self.not_alowed_action = 1
        if a == 1: self.not_alowed_action = 0
        if a == 2: self.not_alowed_action = 3
        if a == 3: self.not_alowed_action = 2

    def sum_rewards(self, v=int):
        self.reward = v
        self.total_reward += v

    def accum_action(self, a=int):
        s = self.action_history_size
        l = self.action_history
        l.append(a)
        if len(l) > s: list.pop(l, 0)
        # ------
        self.step_count += 1

    def get_last_action(self):
        l = self.action_history
        s = len(l)
        if s == 0: return None
        return l[s - 1]
