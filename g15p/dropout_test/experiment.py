# [[1,  2,  3,  4],
#  [5,  6,  7,  8],
#  [9,  10, 11, 12],
#  [13, 14, 15, 0]]
# -----train--------------------------
# [[1,  2,  3,  4],
#  [x,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [h,   ,   ,   ]]
#
# [[1,  2,  3,  4],
#  [5,   ,   ,  x],
#  [ ,   ,   ,   ],
#  [ ,   ,  h,   ]]
# -----test--------------------------
# [[1,  2,  3,  4],
#  [ ,  x,   ,   ],
#  [ ,   ,   ,   ],
#  [h,   ,   ,   ]]
#
# [[1,  2,  3,  4],
#  [h,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [ ,   ,   ,  x]]
#
# ======================
# todo:
# generate - train/test data
from rl.agents import DQNAgent

from dropout_test.agent import get_agent_4x12
from dropout_test.env.grid_context import GridCtx
from dropout_test.env.grid_env import GridEnv
from dropout_test.sate_data import data
from dropout_test.train_model import train_mdl


def train(a=DQNAgent, states=[], check_from=None, checks_to=None, max_run_time=10):
    ctx = GridCtx(states, max_run_time=max_run_time)
    env = GridEnv(ctx)

    train_mdl(dqn=a,
              env=env,
              check_f_from=check_from,
              check_dir=checks_to)

    a.save_weights(checks_to + '/last.hdf5', overwrite=True)


def test(a=DQNAgent, states=[], fpath=str):
    if not load_weights(a, fpath): return False

    states_nb = len(states)
    ctx = GridCtx(states)
    env = GridEnv(ctx)

    a.test(env=env, nb_episodes=states_nb, visualize=False)
    b = save_test_results(ctx, states_nb)

    return b


def save_test_results(ctx, states_nb):
    passed_states = ctx.get_passed_states_nb()
    b = states_nb == passed_states
    txt = 'total:' + str(states_nb) + ', passed:' + str(passed_states)
    print(txt)
    f = open('./results.txt', 'a')
    f.write(txt + '\n')
    f.close()
    return b


def load_weights(a=DQNAgent, fpath=str):
    try:
        a.load_weights(fpath)
        return True
    except Exception as e:
        print(e)
        return False


def run_experiment():
    size = len(data) / 2
    size = int(size)
    train_data, test_data = data[:size], data[size:]

    a = get_agent_4x12()

    c_from = './checks/last.hdf5'
    c_to = './checks/'

    while test(a, data, c_from) != True:
        train(a, train_data, c_from, c_to, max_run_time=5)

    print('done!!!')


# drop out ? ..
run_experiment()
