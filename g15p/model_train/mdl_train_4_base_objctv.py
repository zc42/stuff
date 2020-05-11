from rl.agents import DQNAgent

from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_env import G15_env
from g15_new.g15_context import Ctx
from g15_new.model.mdl import build_Conv2D_model_4x11
from g15_new.model.model_train_conv import train_mdl

check_f_from = './check_4_base_objctv_v3/last.hdf5'
check_dir_to = './check_4_base_objctv_v3/'
max_run_time = 0.1


def save_test_results(ctx):
    states_nb = ctx.baseObjCtx.data_size
    passed_states = ctx.baseObjCtx.get_passed_states_nb()
    b = states_nb == passed_states
    txt = 'total:' + str(states_nb) + ', passed:' + str(passed_states)
    print(txt)
    f = open('./results.txt', 'a')
    f.write(txt + '\n')
    f.close()
    return b


def train_v2(a=DQNAgent):
    ctx = Ctx(encode_4_conv_v2=True,
              max_run_time=1,
              base_objective=True)
    ctx_hof = Ctx_hof(ctx, Ctx_hof.get_hof_v1())

    train_mdl(a, ctx_hof, check_f_from, check_dir_to)
    a.save_weights(check_f_from, overwrite=True)


def test(a=DQNAgent):
    if not load_weights(a, check_f_from): return False

    ctx = Ctx(encode_4_conv_v2=True,
              max_run_time=max_run_time,
              base_objective=True)
    ctx_hof = Ctx_hof(ctx, Ctx_hof.get_hof_v1())

    env = G15_env(ctx_hof)
    states_nb = ctx.baseObjCtx.data_size

    a.test(env=env, nb_episodes=states_nb, visualize=False)
    b = save_test_results(ctx)

    return b


def load_weights(a=DQNAgent, fpath=str):
    try:
        a.load_weights(fpath)
        return True
    except Exception as e:
        print(e)
        return False


def run_experiment():
    a = build_Conv2D_model_4x11()

    while test(a) != True:
        train_v2(a)

    print('done!!!')


run_experiment()
