from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_context import Ctx
from g15_new.model.mdl import build_Conv2D_model_4x11
from model_test.check_points_dict import G15_models_by_goal
from model_test.test_fnctns import test_mdl


def run_test(root_dir=None):
    dqn_f = build_Conv2D_model_4x11
    checks = G15_models_by_goal(root_dir)

    ctx = Ctx(test_rndm_brd=True, encode_4_conv_v2=True, render=True)
    ctx_hof=Ctx_hof(ctx, Ctx_hof.get_hof_v1())

    # lsn = get_lessons_one_case(Lsn(5, 1, (0, 3)))
    # ctx = Ctx(test=True, encode_4_conv_v2=True, lessons=lsn)
    test_mdl(dqn_f, ctx_hof, checks)


if __name__ == '__main__':
    run_test()
