import time
import types

from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_env import G15_env
from model_test.check_points_dict import G15_models_by_goal

ENV_NAME = 'MyEnv-v0'


def test_mdl(dqn_f=types.FunctionType, ctx=Ctx_hof, checks=G15_models_by_goal):
    env = G15_env(ctx)
    dqn = dqn_f(env)
    dqn.g15_mdls = checks
    load_weights(dqn, checks.get_default_check())

    while True:
        test(dqn, env)


def test(dqn, env):
    dqn.test(env, nb_episodes=10, visualize=True)


def load_weights(dqn, fname):
    try:
        dqn.load_weights(fname)
        print(fname)
        time.sleep(3)
        return
    except OSError as e:
        raise e
