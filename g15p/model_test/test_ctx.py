import datetime
import types

from rl.agents import DQNAgent


class Lsn_ctx():
    def __init__(self,
                 lsn_f=types.FunctionType,
                 name=str,
                 check_from=str,
                 check_to=str):
        # -----------------
        self.lsn_f = lsn_f
        self.name = name
        self.check_point_f_from = check_from
        self.check_point_dir_to = check_to
        # -----------------

    def get_check_point_dir_from(self, base_dir=str):
        if self.check_point_f_from == None: return None
        return base_dir + self.get_base_dir() + self.check_point_f_from

    def get_check_point_dir_to(self, base_dir=str):
        if self.check_point_dir_to == None: return None
        return base_dir + self.get_base_dir() + self.check_point_dir_to + '/'

    def get_base_dir(self):
        return self.name + '/'


class Train_ctx():

    def __init__(self, dqna_f=types.FunctionType, name=str, lsns=[Lsn_ctx], max_run_time=int):
        self.dqna_f = dqna_f
        self.name = name
        self.max_run_time = max_run_time
        self.lsns = lsns

        self.t1 = datetime.datetime.now()
        self.t1_str = self.t1.strftime('%Y.%m.%d_%H:%M:%S')
        self.log_dir_base = './' + self.name + '/logs/log_' + self.t1_str + '/'
        self.check_dir_base = './' + self.name + '/checks/'
        self.log_dict = dict()

    # ---dir struct--------
    # conv2d_4x11
    #   lsn_15
    #       check_0
    #       check_1
    #       check_n
    #   logs
    #       log_2020.04...
    # ----------------------

    def get_log_dirs(self, l_ctx=Lsn_ctx):
        lsn_chk_from = l_ctx.get_check_point_dir_from(self.check_dir_base)
        lsn_chk_to = l_ctx.get_check_point_dir_to(self.check_dir_base)
        return lsn_chk_from, lsn_chk_to, self.log_dir_base
