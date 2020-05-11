import datetime
from g15_new.model.mdl import build_Conv2D_model, get_model, build_Conv2D_model_o, build_Conv2D_model_x0, \
    build_Conv2D_model_x1, \
    build_Conv2D_model_x2, build_Conv2D_model_x3
from model_selection.mdl_selection_fnctns import run_exprmt, Expermnt_ctx

log_dict = dict()
t1 = datetime.datetime.now()
ectx = Expermnt_ctx('lg2__2_lsns', 0.1)

# ***********1***02:21***390**********************15
dqn = build_Conv2D_model_x1()
run_exprmt(ectx, dqn, 'conv2d_x1', encode_4_conv=True)

# ************************************************15
dqn = build_Conv2D_model_x2()
run_exprmt(ectx, dqn, 'conv2d_x2', encode_4_conv=True)

# ************************************************15
dqn = build_Conv2D_model_x3()
run_exprmt(ectx, dqn, 'conv2d_x3', encode_4_conv=True)

# ******2*****0:02:49.***470**********************15
dqn = get_model()
run_exprmt(ectx, dqn, 'categorical_0')

# ********3****0:03:04.****666********************15
dqn = build_Conv2D_model()
run_exprmt(ectx, dqn, 'conv2d_0', encode_4_conv=True)

# **********4**** 0:04:20.***436******************15
dqn = build_Conv2D_model_o()
run_exprmt(ectx, dqn, 'conv2d_1', encode_4_conv=True)

# ***********5****13****2465**********************15
dqn = build_Conv2D_model_x0()
run_exprmt(ectx, dqn, 'conv2d_x0', encode_4_conv=True)
# -----------------

ectx.log_experiment_results()
