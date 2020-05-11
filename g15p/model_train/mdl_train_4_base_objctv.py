from rl.agents import DQNAgent

from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_env import G15_env
from g15_new.g15_context import Ctx
from g15_new.model.mdl import build_Conv2D_model_4x11
from g15_new.model.model_train_conv import train_mdl

max_run_time = 0.1


def save_test_results(ctx, dir_to):
    states_nb = ctx.baseObjCtx.data_size
    passed_states = ctx.baseObjCtx.get_passed_states_nb()
    b = states_nb == passed_states
    txt = 'total:' + str(states_nb) + ', passed:' + str(passed_states)
    print(txt)
    f = open(dir_to + '/results.txt', 'a')
    f.write(txt + '\n')
    f.close()
    return b


def train_v2(a=DQNAgent, f_from=str, dir_to=str):
    ctx = Ctx(encode_4_conv_v2=True,
              max_run_time=1,
              base_objective=True)

    train_mdl(a, ctx, f_from, dir_to)
    a.save_weights(f_from, overwrite=True)


def test(a=DQNAgent, f_from=str, dir_to=str):
    if not load_weights(a, f_from): return False

    ctx = Ctx(encode_4_conv_v2=True,
              max_run_time=max_run_time,
              base_objective=True)
    ctx_hof = Ctx_hof(ctx, Ctx_hof.get_hof_v1())

    env = G15_env(ctx_hof)
    states_nb = ctx.baseObjCtx.data_size

    a.test(env=env, nb_episodes=states_nb, visualize=False)
    b = save_test_results(ctx, dir_to)

    return b


def load_weights(a=DQNAgent, fpath=str):
    try:
        a.load_weights(fpath)
        return True
    except Exception as e:
        print(e)
        return False


def train_model_4_base_objective(root_dir=None):
    exp = 'check_4_base_objctv_v4'
    f_from = exp + '/last.hdf5'
    dir_to = exp + '/'

    f_from = concat_dir(f_from, root_dir)
    dir_to = concat_dir(dir_to, root_dir)

    a = build_Conv2D_model_4x11()

    while test(a, f_from, dir_to) != True:
        train_v2(a, f_from, dir_to)

    print('done!!!')


def concat_dir(v1, v2):
    return './' + v1 if v2 == None else v2 + '/' + v1


if __name__ == '__main__':
    train_model_4_base_objective()
