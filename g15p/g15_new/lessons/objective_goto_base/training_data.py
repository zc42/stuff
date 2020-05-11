# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 0]]

# -----train--------------------------
# [[b ,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [h,   ,   ,   ]]
#
# [[ 1,  2 , b  ,   ],
#  [ ,   ,   ,  ],
#  [ ,   ,   ,   ],
#  [ ,   ,  h,   ]]


# base_i = 0
# hole_i=[x for x in range(0, 16)]
# state = [x for x in range(1, 17)]
# print(hole_i)
# print(state)

import numpy as np

base = 18
hole = 0


def get_base_dict():
    base_dict = dict()
    for i in range(1, 16, 4):
        x = i
        if x == 1: base_dict[x] = x - 1
        if x > 1: base_dict[x] = x - 1 + 3
        x += 1
        base_dict[x] = x - 1
        x += 1
        base_dict[x] = x - 1
        x += 1
        if x == 16: break
        base_dict[x] = x - 1

    # base_dict[10]=12
    base_dict[10] = 12
    base_dict[11] = 13
    # base_dict[12] =
    # base_dict[13] =
    # base_dict[14] =
    # base_dict[15] =
    return base_dict


def get_data_1():
    r = []
    base_dict = get_base_dict()
    # pass_x = [11, 12, 15]
    for x in range(1, 17):
        state_0 = [v for v in range(1, x)]
        state_1 = [-1 for v in range(x, 17)]
        state_0.extend(state_1)

        if not x in base_dict.keys(): continue
        base_i = base_dict[x]
        # base_i = x - 1
        state_0[base_i] = base

        if x > 10: continue
        for v in range(x - 1, 16):
            hole_i = v
            if hole_i == base_i: continue
            state_1 = np.copy(state_0)
            state_1[hole_i] = hole
            r.append(state_1.tolist())
            # if x > 10: state_1[12] = 13

            # state_1 = np.reshape(state_1, [4, 4])  # .astype(dtype=int)

    #         print(base_dict)
    #         print(state_1)
    #         print('----------')
    # print('----------')
    # print('----------')
    return r


def get_data_x(base_i, a):
    r = []
    s = [x for x in range(1, 17)]
    for i in a:
        s[i] = -1

    a.remove(base_i)
    # a = [10, 11, 13, 14, 15]

    s[base_i] = base
    for i in a:
        s1 = np.copy(s)
        s1[i] = hole
        r.append(s1.tolist())
        # s1 = np.reshape(s1, [4, 4])
        # print(s1)
        # print('----------')
    return r


def get_data_2():
    global base_i, a
    base_i = 9
    a = [9, 10, 11, 13, 14, 15]
    r0 = get_data_x(base_i, a)
    # print('----------')
    # print('----------')
    base_i = 13
    a = [10, 11, 13, 14, 15]
    r1 = get_data_x(base_i, a)
    r0.extend(r1)
    return r0


def get_train_data_4_base_objctv():
    r0 = get_data_1()
    r1 = get_data_2()
    r0.extend(r1)
    return r0
    # i = 1
    # for a in r0:
    #     print(i, a)
    #     i += 1


# print(get_train_data_4_base_objctv())
