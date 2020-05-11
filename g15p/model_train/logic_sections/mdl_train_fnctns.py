import datetime
import pathlib

from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_context import Ctx
from model_train.logic_sections.training_ctx import Train_ctx, Lsn_ctx
from g15_new.model.model_train_conv import train_mdl
from lazy_streams import stream


# ---dir struct--------
# conv2d_4x11
#   lsn_15
#       check_0
#       check_1
#       check_n
#   logs
#       log_2020.04...
# ----------------------

def create_dirs(t_ctx, l_ctx):
    check_f_from, check_dir, lsns_log = t_ctx.get_log_dirs(l_ctx)
    pathlib.Path(lsns_log).mkdir(parents=True, exist_ok=True)
    pathlib.Path(check_dir).mkdir(parents=True, exist_ok=True)
    return check_f_from, check_dir, lsns_log


def train(t_ctx=Train_ctx, l_ctx=Lsn_ctx):
    check_f_from, check_dir_to, lsns_log = create_dirs(t_ctx, l_ctx)
    ctx = Ctx(encode_4_conv_v2=True,
              lsns_log_dir=lsns_log,
              max_run_time=t_ctx.max_run_time,
              lesson_f=l_ctx.lsn_f)

    # ctx_hof = Ctx_hof(ctx, Ctx_hof.get_hof_v1())

    t1 = datetime.datetime.now()
    train_mdl(t_ctx.dqna_f(), ctx, check_f_from, check_dir_to)
    ctx.save_weights(t_ctx.get_log_dirs(l_ctx)[1] + '/last')
    add_lsn_progress_info_2_dict(ctx, l_ctx, t1, t_ctx)


def add_lsn_progress_info_2_dict(ctx, l_ctx, t1, t_ctx):
    # -----------------
    t2 = datetime.datetime.now()
    d = '{0}'.format(t2 - t1)
    # -----------------
    t_ctx.log_dict[l_ctx.name] = str(d) + ' | ' + l_ctx.name + ' | done: ' + str(ctx.done)


def write_start_and_duration(f=None, t1=datetime):
    t1_str = t1.strftime('%Y.%m.%d %H:%M:%S')
    t2 = datetime.datetime.now()
    d = '{0}'.format(t2 - t1)
    f.writelines('started: ' + t1_str + '\n')
    f.writelines('duration: ' + d + '\n')
    f.writelines('------------\n')


def write_lessons_info(f=None, t_ctx=Train_ctx):
    f.writelines('---lessons info:---\n')
    for lsn in t_ctx.lsns:
        s = 'lsn: ' + lsn.name
        s += '| chk from: ' + str(t_ctx.get_log_dirs(lsn)[0])
        s += '| chk to: ' + str(t_ctx.get_log_dirs(lsn)[1])
        f.writelines(s + '\n')
    f.writelines('-------------------\n')


def log_train_results(t_ctx=Train_ctx):
    dir = t_ctx.log_dir_base
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
    fn = dir + t_ctx.name + '.txt'
    # t1_str = t1.strftime('%Y.%m.%d_%H:%M:%S')
    # fn += '_' + t1_str + '.txt'

    f = open(fn, 'w')

    write_start_and_duration(f, t_ctx.t1)
    write_lessons_info(f, t_ctx)

    l = [x for x in t_ctx.log_dict.values()]
    if (len(l) > 0):
        r = stream(l).reduce(lambda x, y: x + '\n' + y)
        f.writelines(r)
    f.close()
