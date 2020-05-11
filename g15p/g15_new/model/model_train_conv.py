import pathlib

import numpy as np
from keras.callbacks import TensorBoard, ModelCheckpoint
from rl.agents import DQNAgent

from g15_new.g15_env import G15_env
from g15_new.g15_context import Ctx
from g15_new.model import mdl

# ENV_NAME = 'MyEnv-v0'

check_dir = "./checkpoint_conv/"
log_dir = './logs/back_2_black_v3'
f_name_templt = 'weights.{epoch:04d}.hdf5'
lsns_log = './logs/lessons_progress_log_1/'


def train_mdl(dqn=DQNAgent,
              ctx=Ctx,
              check_f_from=str,
              check_dir=str,
              tensorBoard=False):
    env = G15_env(ctx)
    np.random.seed(123)

    load_weigths(dqn, check_f_from)

    pathlib.Path(check_dir).mkdir(parents=True, exist_ok=True)
    f_name = check_dir + f_name_templt
    callbacks, checkpoint = get_callbacks(f_name, tensorBoard)

    env.check_point(checkpoint)
    try:
        dqn.fit(env,
                nb_steps=10000000000000,
                visualize=False,
                verbose=2,
                callbacks=callbacks)
    except Exception as e:
        print(e)
        # raise e


def load_weigths(dqn, check_f_from=str):
    if check_f_from == None: return
    try:
        dqn.load_weights(check_f_from)
    except Exception as e:
        print(e)


def get_callbacks(f_name, tensorBoard):
    checkpoint = ModelCheckpoint(f_name, save_weights_only=True, verbose=1, period=5000)
    callbacks = [checkpoint]
    if tensorBoard:
        tb = TensorBoard(log_dir=log_dir, write_grads=True, write_images=True)
        callbacks.append(tb)
    return callbacks, checkpoint


if __name__ == '__main__':
    dqn = mdl.build_Conv2D_model()
    ctx = Ctx(encode_4_conv=True, lsns_log_dir=lsns_log)
    train_mdl(check_dir, dqn, ctx)
