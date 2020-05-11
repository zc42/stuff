# req..
# lsn group
# max_run_time
# load_weights from dir or file
# separate check_point_dir
# log file dir with timestamp
# log file contains check_point dirs from/to

# ---dir struct--------
# conv2d_4x11
#   lsn_15
#       check_0
#       check_1
#       check_n
#   logs
#       log_2020.04...
# ----------------------

from g15_new.model.mdl import build_Conv2D_model_4x11
from model_train.logic_sections.training_ctx import Lsn_ctx
from model_train.logic_sections.lesson_functions import lsn_15_f, lsn_14_f, lsn_10_f, lsn_13_f, lsn_09_f, lsn_08_f, \
    lsn_07_f, lsn_06_f, \
    lsn_05_f, lsn_04_f, lsn_03_f, lsn_02_f, lsn_01_f
from model_train.logic_sections.mdl_train_fnctns import Train_ctx, train, log_train_results

check_from = None  # 'check_24/last.hdf5'
check_to = 'check_01'

# region lessons
l_ctx_15 = Lsn_ctx(lsn_15_f, 'lsn_15', check_from=check_from, check_to=check_to)

l_ctx_14 = Lsn_ctx(lsn_14_f, 'lsn_14', check_from=check_from, check_to=check_to)
l_ctx_10 = Lsn_ctx(lsn_10_f, 'lsn_10', check_from=check_from, check_to=check_to)

l_ctx_13 = Lsn_ctx(lsn_13_f, 'lsn_13', check_from=check_from, check_to=check_to)
l_ctx_09 = Lsn_ctx(lsn_09_f, 'lsn_09', check_from=check_from, check_to=check_to)

l_ctx_08 = Lsn_ctx(lsn_08_f, 'lsn_08', check_from=check_from, check_to=check_to)
l_ctx_07 = Lsn_ctx(lsn_07_f, 'lsn_07', check_from=check_from, check_to=check_to)
l_ctx_06 = Lsn_ctx(lsn_06_f, 'lsn_06', check_from=check_from, check_to=check_to)
l_ctx_05 = Lsn_ctx(lsn_05_f, 'lsn_05', check_from=check_from, check_to=check_to)

l_ctx_04 = Lsn_ctx(lsn_04_f, 'lsn_04', check_from=check_from, check_to=check_to)
l_ctx_03 = Lsn_ctx(lsn_03_f, 'lsn_03', check_from=check_from, check_to=check_to)
l_ctx_02 = Lsn_ctx(lsn_02_f, 'lsn_02', check_from=check_from, check_to=check_to)
l_ctx_01 = Lsn_ctx(lsn_01_f, 'lsn_01', check_from=check_from, check_to=check_to)

l_ctx_a = [l_ctx_15, l_ctx_14, l_ctx_10, l_ctx_13,
           l_ctx_09, l_ctx_08, l_ctx_07, l_ctx_06,
           l_ctx_05, l_ctx_04, l_ctx_03, l_ctx_02,
           l_ctx_01]
# endregion

max_run_time = 0.5
t_ctx = Train_ctx(build_Conv2D_model_4x11, 'test_after_refactoring', l_ctx_a, max_run_time)
# **************************************************
for l_ctx in t_ctx.lsns: train(t_ctx, l_ctx)

log_train_results(t_ctx)
