from keras import Input
from keras.layers import Dense, Activation, Flatten, Reshape,  LSTM,  Conv2D
from keras.models import Sequential
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy, Model
from keras import backend as K

from dnq_4_g15.dnq_g15 import DQNAgent_g15

K.set_image_dim_ordering('th')


def get_model_():
    d = 0.2

    model = Sequential()
    model.add(Flatten(input_shape=(1, 1, 264)))

    model.add(Dense(264))
    model.add(Activation('relu'))
    # model.add(Dropout(d))

    model.add(Dense(264))
    model.add(Activation('relu'))
    # model.add(Dropout(d))

    # model.add(Dense(316))
    # model.add(Activation('relu'))
    # model.add(Dropout(d))

    # model.add(Reshape(input_shape=(None,1,4),target_shape=(1, 4)))
    model.add(Dense(4))
    model.add(Activation('relu'))
    # model.add(Dropout(d))

    # print(model.summary())
    memory = SequentialMemory(limit=100000, window_length=1)
    # policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1.,
    #                               value_min=.1, value_test=.05,
    #                               nb_steps=10000)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent(model=model,
                   enable_dueling_network=True,
                   dueling_type='avg',
                   nb_actions=4,
                   memory=memory,
                   nb_steps_warmup=100,
                   target_model_update=1e-3,
                   policy=policy)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    return dqn


def get_model_256():
    d = 0.5

    model = Sequential()
    # model.add(Flatten(input_shape=(1, 1, 316)))

    model.add(Reshape(input_shape=(1, 1, 316), target_shape=(1, 316)))
    model.add(LSTM(24, input_shape=(1, 316), return_sequences=False))
    model.add(Activation('relu'))
    # model.add(Dropout(d))

    model.add(Dense(316))
    model.add(Activation('relu'))

    model.add(Dense(316))
    model.add(Activation('relu'))

    model.add(Dense(256))
    model.add(Activation('relu'))

    # print(model.summary())
    memory = SequentialMemory(limit=1000000, window_length=1)
    # policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1.,
    #                               value_min=.1, value_test=.05,
    #                               nb_steps=10000)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent(model=model,
                   enable_dueling_network=True,
                   dueling_type='avg',
                   nb_actions=256,
                   memory=memory,
                   nb_steps_warmup=100,
                   target_model_update=1e-3,
                   policy=policy)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    return dqn


def get_model_sq(model=Sequential):
    d = 0.5

    # model = Sequential()
    # model.add(Flatten(input_shape=(1, 1, 316)))

    a = Reshape(input_shape=(1, 1, 316), target_shape=(1, 316))
    a = LSTM(24, input_shape=(1, 316), return_sequences=False, inputs=a)
    a = Activation('relu', inputs=a)
    # model.add(Dropout(d))

    a = Dense(316, inputs=a)
    a = Activation('relu', inputs=a)

    a = Dense(316, inputs=a)
    a = Activation('relu', inputs=a)

    a = Dense(4, inputs=a)
    a = Activation('relu', inputs=a)

    return model


def build_Conv2D_model_4_a3c(smth):
    input = Input(shape=smth.state_size)
    conv = Conv2D(16, (8, 8), strides=(4, 4), activation='relu')(input)
    conv = Conv2D(32, (4, 4), strides=(2, 2), activation='relu')(conv)
    conv = Flatten()(conv)
    fc = Dense(256, activation='relu')(conv)
    policy = Dense(smth.action_size, activation='softmax')(fc)
    value = Dense(1, activation='linear')(fc)

    actor = Model(inputs=input, outputs=policy)
    critic = Model(inputs=input, outputs=value)

    actor._make_predict_function()
    critic._make_predict_function()

    actor.summary()
    critic.summary()

    return actor, critic


def build_Conv2D_model():

    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    # model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    # model.add(Conv2D(128, (3, 3), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    model.add(Dense(49, activation='relu'))

    for x in range(5):
        model.add(Dense(16, activation='relu'))

    model.add(Dense(4, activation='relu'))

    return get_dqn(model)

def build_Conv2D_model_o():
    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    model.add(Dense(49, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    model.add(Dense(4, activation='relu'))

    return get_dqn(model)


def build_Conv2D_model_x0():

    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    model.add(Dense(49, activation='relu'))

    for x in range(25):
        model.add(Dense(16, activation='relu'))

    model.add(Dense(4, activation='relu'))

    return get_dqn(model)

def build_Conv2D_model_x1():

    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    for x in range(25):
        model.add(Dense(49, activation='relu'))

    model.add(Dense(4, activation='relu'))

    return get_dqn(model)


def build_Conv2D_model_x2():

    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    for x in range(50):
        model.add(Dense(49, activation='relu'))

    model.add(Dense(4, activation='relu'))

    return get_dqn(model)

def build_Conv2D_model_4x11(env=None):

    model = Sequential()
    model.add(Reshape(input_shape=(1, 4, 11), target_shape=(11, 4, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))
    model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    for x in range(10):
        model.add(Dense(44, activation='relu'))

    model.add(Dense(4, activation='relu'))

    if env == None:
        return get_dqn(model)
    else:
        return get_dqn_4_g15(model, env)

    # return get_dqn(model)




def build_Conv2D_model_x3():

    model = Sequential()
    model.add(Reshape(input_shape=(1, 7, 7), target_shape=(7, 7, 1)))

    model.add(Conv2D(17, (1, 1), strides=(1, 1), activation='relu', padding='same', data_format='channels_first'))

    model.add(Flatten())
    for x in range(25):
        model.add(Dense(49, activation='relu'))

    for x in range(25):
        model.add(Dense(24, activation='relu'))

    model.add(Dense(4, activation='relu'))

    return get_dqn(model)


def get_model(env=None):
    d = 0.5
    # x_n = 2560
    x_n = 413
    # x_n = 347

    model = Sequential()
    model.add(Flatten(input_shape=(1, x_n)))
    # model.add(Reshape(input_shape=(1, x_n), target_shape=(1, x_n)))
    # model.add(Flatten(input_shape=(1, 1, 316)))

    # model.add(Reshape(input_shape=(1, x_n)))
    # model.add(Reshape(input_shape=(1, 1, 1, x_n), target_shape=(1, x_n)))
    # model.add(LSTM(24, input_shape=(1, x_n), return_sequences=False))
    # model.add(Activation('relu'))
    # -------------
    # model.add(Dropout(d))
    model.add(Dense(x_n))
    model.add(Activation('relu'))

    # for x in range(20):
    for x in range(25):
        # model.add(Dense((16 + 15 + 3)))  # veikia su 3 case'ais
        # model.add(Dense((16 + 15 + 8)))  # veikia
        model.add(Dense((16 + 25)))
        # model.add(Dense(16 + 12))
        model.add(Activation('relu'))

    model.add(Dense(4))
    model.add(Activation('relu'))

    # print(model.summary())
    if env == None:
        return get_dqn(model)
    else:
        return get_dqn_4_g15(model, env)


def get_model_256():
    x_n = 256
    model = Sequential()
    model.add(Flatten(input_shape=(1, x_n)))

    # model.add(LSTM(24, input_shape=(1, x_n), return_sequences=False))
    # model.add(Activation('relu'))

    model.add(Dense(x_n))
    model.add(Activation('relu'))

    model.add(Dense(x_n))
    model.add(Activation('relu'))

    model.add(Dense(4))
    model.add(Activation('relu'))

    # print(model.summary())
    return get_dqn(model)


def get_model_16():
    x_n = 16
    model = Sequential(model_dir='train/game_15')
    model.add(Flatten(input_shape=(1, x_n)))

    # model.add(LSTM(24, input_shape=(1, x_n), return_sequences=False))
    # model.add(Activation('relu'))

    model.add(Dense(x_n))
    model.add(Activation('relu'))

    model.add(Dense(x_n))
    model.add(Activation('relu'))

    model.add(Dense(4))
    model.add(Activation('relu'))

    # print(model.summary())
    return get_dqn(model)


def get_dqn_0(model):
    memory = SequentialMemory(limit=1000000, window_length=1)
    # policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1.,
    #                               value_min=.1, value_test=.05,
    #                               nb_steps=10000)
    policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model,
                   enable_dueling_network=True,
                   dueling_type='avg',
                   nb_actions=4,
                   memory=memory,
                   nb_steps_warmup=100,
                   target_model_update=.001,  # cia ryskiai nesamone ..
                   policy=policy)
    dqn.compile(Adam(lr=.0001), metrics=['mae'])
    return dqn


def get_dqn(model):
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
    dqn.compile(Adam(lr=1e-4), metrics=['mae'])
    return dqn


def get_dqn_4_g15(model, env):
    memory = SequentialMemory(limit=100000, window_length=1)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent_g15(model=model,
                       env=env,
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
    dqn.compile(Adam(lr=1e-4), metrics=['mae'])
    return dqn


def get_model_n():
    d = 0.5

    model = Sequential()
    # model.add(Flatten(input_shape=(1, 1, 316)))

    model.add(Reshape(input_shape=(1, 1, 316), target_shape=(1, 316)))
    model.add(LSTM(24, input_shape=(1, 316), return_sequences=True))
    model.add(Activation('relu'))
    # model.add(Dropout(d))

    model.add(Dense(316 * 24))
    model.add(Activation('relu'))

    model.add(Dense(316))
    model.add(Activation('relu'))

    model.add(Dense(4))
    model.add(Activation('relu'))

    # print(model.summary())
    memory = SequentialMemory(limit=1000000, window_length=1)
    # policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1.,
    #                               value_min=.1, value_test=.05,
    #                               nb_steps=10000)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent(model=model,
                   enable_dueling_network=True,
                   dueling_type='avg',
                   nb_actions=4,
                   memory=memory,
                   nb_steps_warmup=100,
                   target_model_update=1e-3,
                   policy=policy)
    # dqn.compile(Adam(lr=1e-3), metrics=['mae'])
    dqn.compile(Adam(lr=1e-3), loss='categorical_crossentropy', metrics=['accuracy', 'mae'])
    return dqn
