import datetime
import pathlib

from rl.agents import DQNAgent
from lazy_streams import stream

from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_context import Ctx
from g15_new.model.model_train_conv import train_mdl


class Expermnt_ctx():
    def __init__(self, name=str, max_run_time=int):
        self.name = name
        self.max_run_time = max_run_time

        self.check_dir_base = './checks/'
        self.log_dir_base = './logs/log_'
        self.t1 = datetime.datetime.now()
        self.t1_str = self.t1.strftime('%Y.%m.%d_%H:%M:%S')
        self.log_dict = dict()

    def get_log_dirs(self, log=str):
        check_dir = self.check_dir_base + log
        t1 = self.t1.strftime('%Y.%m.%d_%H:%M:%S')
        lsns_log = self.log_dir_base + t1 + '/' + log
        return check_dir, lsns_log

    def log_experiment_results(self):
        dir = self.get_log_dirs('')[1]
        pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
        fn = dir + self.name + '.txt'
        # t1_str = t1.strftime('%Y.%m.%d_%H:%M:%S')
        # fn += '_' + t1_str + '.txt'

        f = open(fn, 'w')
        write_start_and_duration(f, self.t1)
        l = [x for x in self.log_dict.values()]
        r = stream(l).reduce(lambda x, y: x + '\n' + y)
        f.writelines(r)


def run_exprmt(ectx=Expermnt_ctx, dqn=DQNAgent, name=str, encode_4_conv=False, encode_4_conv_v2=False):
    t1 = datetime.datetime.now()
    # -----------------
    check_dir, lsns_log = ectx.get_log_dirs(name + '/')
    ctx = Ctx(encode_4_conv=encode_4_conv,
              encode_4_conv_v2=encode_4_conv_v2,
              lsns_log_dir=lsns_log,
              max_run_time=ectx.max_run_time)

    train_mdl(dqn=dqn,
              ctx=ctx,
              check_f_from=None,
              check_dir=check_dir)
    # -----------------
    t2 = datetime.datetime.now()
    d = '{0}'.format(t2 - t1)
    # -----------------
    ectx.log_dict[name] = str(d) + ' | ' + name


def write_start_and_duration(f=None, t1=datetime):
    t1_str = t1.strftime('%Y.%m.%d %H:%M:%S')
    t2 = datetime.datetime.now()
    d = '{0}'.format(t2 - t1)
    f.writelines('started: ' + t1_str + '\n')
    f.writelines('duration: ' + d + '\n')
    f.writelines('------------\n')
