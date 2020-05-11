from g15_new.hof.hof_1 import hof_4_encode_state, hof_4_check_action, hof_4_rwrd
from g15_new.g15_context import Ctx


class Ctx_hof:

    def __init__(self, ctx=Ctx, hof=dict):
        self.ctx = ctx
        self.hof = hof

    @classmethod
    def get_hof_v1(cls):
        return {
            'hof_4_encode_state': hof_4_encode_state,
            'hof_4_check_action': hof_4_check_action,
            'hof_4_rwrd': hof_4_rwrd
        }
