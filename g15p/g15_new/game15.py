import numpy as np
import g15_new.unsorted_stuff.board as brd
from g15_new.ctx_hof import Ctx_hof
from g15_new.lessons.log_lsn.log_2_file import log_lsn_progress
from g15_new.lessons.log_lsn.log_game_state import log_failed_game


class Game_15:
    def __init__(self, ctx=Ctx_hof):
        self.ctx = ctx.ctx

        self.hof_4_encode_state=ctx.hof['hof_4_encode_state']
        self.hof_4_check_action = ctx.hof['hof_4_check_action']
        self.hof_4_rwrd = ctx.hof['hof_4_rwrd']

    def init(self):
        self.ctx.init_by_need()

    def get_encoded_state(self):
        return self.hof_4_encode_state(self.ctx)

    def make_move(self, a):
        a_txt = self.ctx.actions[a]
        self.ctx.accum_action(a)
        f, r = self.hof_4_check_action(self.ctx)
        self.move(a, f)
        f, r = self.hof_4_rwrd(self.ctx, f, r)

        # region ..encode save state / sum rwrds..
        s_e = self.get_encoded_state()
        self.ctx.save_state()
        self.ctx.sum_rewards(r)
        # endregion

        # region --------4 debug-----------------
        # todo: -> hof
        log_lsn_progress(self.ctx, r, f)
        # todo: -> hof -> debug functions
        # -------------
        if f and r < 0:
            log_failed_game(self.ctx)
            f = f

        if f and r == 10:
            f = f
        # endregion

        return s_e, r, f, self.ctx.state

    def move(self, a, f):
        if f: return
        self.ctx.prev_state = np.copy(self.ctx.state).tolist()
        self.ctx.state = brd.move(self.ctx.state, self.ctx.actions[a])
