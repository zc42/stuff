from g15_new.model.mdl import build_Conv2D_model_x1, build_Conv2D_model_4x11, get_model
from model_selection.mdl_selection_fnctns import run_exprmt, Expermnt_ctx

ectx = Expermnt_ctx('lg2__2_lsns', 30)

# **************************************************
dqn = get_model()
run_exprmt(ectx, dqn, 'categorical_0')

# **************************************************
dqn = build_Conv2D_model_4x11()
run_exprmt(ectx, dqn, 'conv2d_x2', encode_4_conv_v2=True)


# **************************************************
dqn = build_Conv2D_model_x1()
run_exprmt(ectx, dqn, 'conv2d_x1', encode_4_conv=True)

# **************************************************

ectx.log_experiment_results()
