import numpy as np
from keras.utils import to_categorical

from g15_new.lessons.objective_goto_base.base_objctv_func import encode_4_base
from g15_new.g15_context import Ctx
from g15_new.unsorted_stuff.g15_functions_0 import local_reshape

from dropout_test.env.grid_context import GridCtx
from g15_new.unsorted_stuff.filter_s import filter_state


def int_to_list(v=int):
    v = 1000 + v
    s = str(v)
    s = s[1:]
    s = ",".join([s[i] for i in range(len(s))])
    s = s.split(",")
    return [int(i) for i in s]


def get_flattened_observation(encoded_state=[]):
    a = encoded_state
    a = local_reshape(a, [256])
    a.extend([1])
    a = np.reshape(a, [1, a.__len__()])

    return a


def hot_encoded(ctx=Ctx):
    r = to_categorical(ctx.state),
    r = np.reshape(r, [256]).tolist()
    return r


def encoded_from_0_to_1(ctx=Ctx):
    r = np.reshape(ctx.state, [4, 4])
    r = np.interp(r, (r.min(), r.max()), (0, 1))
    r = list(r)
    return r


def state_filtered(ctx=Ctx):
    b = ctx.test_rndm
    b = b and ctx.run_base_objective
    if b: return encode_4_base(ctx.state, ctx.init_goal)

    if ctx.run_base_objective: ctx.state

    fs = ctx.state
    fs = filter_state(fs, ctx.goal)
    return fs


def state_encoded(ctx=Ctx):
    # fs = ctx.state
    fs = state_filtered(ctx)

    if ctx.encode_4_conv: return state_encoded_4_conv(ctx, fs)
    if ctx.encode_4_conv_v2: return state_encoded_4_conv_v2(ctx, fs)

    # -------------    
    fs_cat = to_categorical(fs, num_classes=17)
    fs_e = __state_encoded(ctx, fs_cat)
    return fs_e


def get_last_states(h=[], nb=int):
    sz = len(h)
    if sz != 0 and sz >= nb:
        _nb = sz - nb
        return h[_nb:]

    _h = []
    if sz != 0:
        nb = nb - sz
        _h = np.copy(h).tolist()

    l = [[-2 for x in range(1, 17)] for x in range(nb)]

    _h.extend(l)
    return _h


def state_encoded_4_grid(ctx=GridCtx):
    s = ctx.state
    s0 = np.array(s)

    sh = get_last_states(ctx.state_hist, 2)

    # s0=[]
    for h in sh:
        h = np.reshape(h, [4, 4])
        s0 = np.append(s0, h, axis=1)

    # print(s0)

    return s0

    # fs = ctx.state
    # fs = state_filtered(ctx)

    # if ctx.encode_4_conv: return state_encoded_4_conv(ctx, fs)
    # if ctx.encode_4_conv_v2: return state_encoded_4_conv_v2(ctx, fs)
    #
    # # -------------
    # fs_cat = to_categorical(fs, num_classes=17)
    # fs_e = __state_encoded(ctx, fs_cat)
    # return fs_e


def state_encoded_4_conv(ctx, fs):
    length = 25 + 4
    _actns = encode_step_history(ctx.action_history, length)
    _fs = np.reshape(fs, [16]).tolist()

    _h_xy = ctx.init_h_xy
    _g_xy = ctx.init_g_xy

    l = []
    l.extend(_h_xy)
    l.extend(_g_xy)
    l.extend(_actns)
    l.extend(_fs)

    r = np.reshape(l, [7, 7]).astype(dtype=int).tolist()

    return r


def __state_encoded(ctx=Ctx, encoded_state=np.ndarray):
    r1 = encoded_state.tolist()
    r1 = local_reshape(r1, [272])

    length = 25

    r5 = encode_step_history(ctx.action_history, length)
    r5 = to_categorical(r5, 5)
    r5 = local_reshape(r5, [length * 5])

    r = r1
    r += r5
    r += ctx.init_h_x
    r += ctx.init_h_y
    r += ctx.init_g_x
    r += ctx.init_g_y
    r = np.reshape(r, [len(r)])

    return r


def encode_available_actions(available_actions):
    a1 = 1 if available_actions.__contains__(0) else 0
    a2 = 1 if available_actions.__contains__(1) else 0
    a3 = 1 if available_actions.__contains__(2) else 0
    a4 = 1 if available_actions.__contains__(3) else 0
    a1 = list(to_categorical(a1, 2))
    a2 = list(to_categorical(a2, 2))
    a3 = list(to_categorical(a3, 2))
    a4 = list(to_categorical(a4, 2))
    r = a1 + a2 + a3 + a4
    return r


def encode_int_2_binary_array(v, lenght):
    l = [int(x) for x in list('{0:0b}'.format(v))]
    l0 = [0 for x in range(lenght - len(l))]
    l0.extend(l)
    return l0


def encode_step_history(step_history=[], length=50):
    l = step_history
    l0 = [-1 for x in range(length - len(l))]
    l0.extend(l)
    l0 = l0 if len(l0) == length else l0[0:length]

    # if len(l0) > length:
    #     l0 = l0

    return l0


def encode_step_count_left(count=int, length=3):
    s = list(str(count))
    l0 = [0 for x in range(length - len(s))]
    l0.extend(s)
    return l0


def negative_reword(ctx=Ctx, available_actions=None, over_edge=False, foward_back_detected=False):
    ctx.reward = -0.25  # + (self.step_count * -1)
    ctx.total_reward = ctx.total_reward + ctx.reward

    # self.print_finishe_level()
    return state_encoded(ctx=ctx), \
           ctx.reward, \
           True, \
           ctx.state


def state_encoded_4_conv_v2(ctx, fs):
    _actns = encode_step_history(ctx.action_history, 24)
    _h_xy = ctx.init_h_xy
    _g_xy = ctx.init_g_xy
    r = encode_4_conv2d_v2(fs, _actns, _h_xy, _g_xy)
    return r


def encode_4_conv2d_v2(s=np.ndarray, h=[], xy_h=(), xy_g=()):
    s0 = np.array(s)

    xy = np.append(xy_h, xy_g)
    xy = np.reshape(xy, [4, 1])

    s2 = np.append(s0, xy, axis=1)

    _h = np.reshape(h, [4, 6])
    s3 = np.append(s2, _h, axis=1)

    return s3
