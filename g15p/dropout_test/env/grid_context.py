import datetime
import math

import g15_new.unsorted_stuff.board as brd
import numpy as np

goal = 8
hole = 0


class GridCtx:
    def __init__(self,
                 data=[],
                 max_run_time=-1):

        self.init_data(data)
        self.start_t = datetime.datetime.now()
        # ---------------
        self.max_run_time = max_run_time
        self.runs_count = 0
        self.states_passed = dict()

    def init_data(self, data):
        self.data = data
        self.data_size = len(data)
        self.data_i = -1

    def init(self):
        self.test_run_time()
        self.state = self.get_state()
        self.init_vars()
        self.set_max_steps()
        # self.add_state_2_hist(self.state)

    def set_max_steps(self):
        xy_g = brd.get_xy(self.state, goal)
        xy_h = brd.get_xy(self.state, hole)
        d = math.fabs(xy_g[0] - xy_h[0]) + math.fabs(xy_g[1] - xy_h[1])
        self.max_step_count = d
        self.xy_g = xy_g

    def init_vars(self):
        # ----------

        self.exit = ""
        self.state_hist = []
        self.not_alowed_action = []
        self.reward = 0
        self.action_history = []
        self.actions = brd.actions
        self.final_rwdr = 10
        self.total_reward = 0
        self.step_count = 0
        # ----------

    def add_state_2_hist(self, state):
        a = np.copy(state)
        self.state_hist.append(a)

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

    def get_state(self):
        self.data_i += 1
        if self.data_i >= self.data_size: self.data_i = 0
        s = self.data[self.data_i]
        s = np.reshape(s, [4, 4]).astype(dtype=int)
        return s

    def register_as_passed(self):
        self.states_passed[self.data_i] = True

    def get_passed_states_nb(self):
        return len(self.states_passed)
