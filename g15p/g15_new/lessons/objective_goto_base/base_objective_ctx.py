import math

import numpy as np

from g15_new.lessons.objective_goto_base.training_data import base, get_train_data_4_base_objctv, hole


class BaseObjctvCtx:
    def __init__(self):
        self.base = base
        data = get_train_data_4_base_objctv()
        # data.reverse()
        self.init_data(data)
        self.states_passed = dict()

    def init_data(self, data):
        self.data = data
        self.data_size = len(data)
        self.data_i = -1

    def init(self):
        self.state = self.get_next_state()
        self.set_max_steps()

    def set_max_steps(self):
        xy_g = self.get_xy(self.state, base)
        xy_h = self.get_xy(self.state, hole)
        d = math.fabs(xy_g[0] - xy_h[0]) + math.fabs(xy_g[1] - xy_h[1])
        self.max_step_count = d
        self.xy_g = xy_g

    def get_next_state(self):
        self.data_i += 1
        if self.data_i >= self.data_size: self.data_i = 0
        s = self.data[self.data_i]
        s = np.reshape(s, [4, 4]).astype(dtype=int)
        return s

    def register_as_passed(self):
        self.states_passed[self.data_i] = True

    def get_passed_states_nb(self):
        return len(self.states_passed)

    def get_xy(self, state=np.ndarray, v=None):
        # if v is not None and (v < 0 or v > 15):
        #     raise Exception('v is not None and (v < 0 or v > 15)')

        v = hole if v is None else v
        x, y = np.where(state == v)
        return x[0], y[0]
