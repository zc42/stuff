from keras import Sequential
from keras.constraints import maxnorm
from keras.layers import Reshape, Conv2D, Flatten, Dense, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy


def get_agent_4x12():
    return get_agent(get_model_4x12())


def get_model_4x12():
    m = Sequential()
    m.add(Reshape(input_shape=(1, 4, 12), target_shape=(12, 4, 1)))

    m.add(Conv2D(4, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    # m.add(Conv2D(4, (1, 1), strides=(1, 1), padding='same', data_format='channels_first'))
    # m.add(BatchNormalization())
    # m.add(Activation("relu"))
    m.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    # m.add(Conv2D(32, (2, 2), strides=(1, 1), padding='same', data_format='channels_first'))
    # m.add(BatchNormalization())
    # m.add(Activation("relu"))

    m.add(Flatten())

    for x in range(10):
        # m.add(Dense(44, activation='relu'))
        m.add(Dense(44, activation='relu', kernel_constraint=maxnorm(3)))
        m.add(Dropout(0.5))

    m.add(Dense(4, activation='relu'))
    return m


def get_agent(model):
    memory = SequentialMemory(limit=100000, window_length=1)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent(model=model,
                   gamma=.99,
                   enable_dueling_network=True,
                   dueling_type='avg',
                   nb_actions=4,
                   memory=memory,
                   nb_steps_warmup=100,
                   target_model_update=1e-3,
                   policy=policy)
    # buvo .0001
    # veike .001
    dqn.compile(Adam(lr=.01), metrics=['mae'])
    return dqn
