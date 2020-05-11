import numpy as np
import g15_new.unsorted_stuff.board as brd
import g15_new.hof.encoder_0 as enc
import g15_new.unsorted_stuff.g15_functions_1 as fnc
from dropout_test.env.grid_context import GridCtx
from dropout_test.env.reward_5 import negative_reword, calc_reward_new, is_finished


class Game4x4:
    def __init__(self, ctx=GridCtx):
        self.ctx = ctx

    def init(self):
        self.ctx.init()

    def state_encoded(self):
        return enc.state_encoded_4_grid(ctx=self.ctx)

    # ----------*************---------
    # make a move
    def make_move(self, action):
        self.ctx.add_state_2_hist(self.ctx.state)
        a = self.ctx.actions[action]
        self.ctx.step_count += 1
        self.ctx.action_history = fnc.add_to_action_history(self.ctx.action_history, action, 50)
        avlbl_actions = fnc.get_available_actions(self.ctx)
        b = not avlbl_actions.__contains__(action)

        if b:
            s, r, f, s0 = negative_reword(ctx=self.ctx)
        else:
            self.ctx.prev_state = np.copy(self.ctx.state).tolist()
            self.ctx.state = brd.move(self.ctx.state, self.ctx.actions[action])

            self.ctx.reward, f = calc_reward_new(self.ctx)
            self.set_prev_action(action)
            s = self.state_encoded()
            r = self.ctx.reward
            s0 = self.ctx.state

        return s, r, f, s0

    def set_prev_action(self, action=None):
        if action == 0: self.ctx.not_alowed_action = 1
        if action == 1: self.ctx.not_alowed_action = 0
        if action == 2: self.ctx.not_alowed_action = 3
        if action == 3: self.ctx.not_alowed_action = 2

    def is_finished(self):
        return is_finished(self.ctx)
