from lazy_streams import stream
import numpy as np

from g15_new.lessons.objective_goto_base.training_data import base
from g15_new.unsorted_stuff.board import hole
from g15_new.lessons.lessons_v2 import Lessons_v2



def if_is_need_go_2_base(lsns=Lessons_v2, g=int, h_xy=()):
    x = lsns.shift_ma_x(g)
    xy = (h_xy[0] + x, h_xy[1])
    l = lsns.all_lessons_holder
    return not has_lesson(l, g, xy)


def has_lesson(all_lessons=[], g=int, h_xy=()):
    r = stream(all_lessons) \
        .filter(lambda x: x[0] == g) \
        .filter(lambda x: x[2] == h_xy) \
        .first_or_else(None)

    return r != None


def spec_cases_encode_4_base(s=np.ndarray, g=int, h=int):
    if not [13, 10, 14].__contains__(g): return s

    s13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, base, -1, -1, -1]
    s10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, base, -1, -1, 13, -1, -1, -1]
    s14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1, 13, base, -1, -1]

    if g == 13: s1 = s13
    if g == 10: s1 = s10
    if g == 14: s1 = s14

    s1 = np.copy(s1)
    s1[h] = hole

    return s1


def encode_4_base(s=np.ndarray, g=int):
    if [11, 12, 15].__contains__(g): raise Exception('[11, 12, 15].__contains__(g), g == ' + str(g))

    s0 = np.reshape(s, [16])
    i = np.where(s0 == hole)[0][0]

    if g > i + 1:
        raise Exception('g_i > h_i')

    s1 = [x if x < g else -1 for x in range(1, 17)]
    # s1 = [-1 for x in range(1, 17)]
    s1[g - 1] = base
    s1[i] = hole

    s1 = spec_cases_encode_4_base(s1, g, i)

    s1 = np.reshape(s1, [4, 4])
    return s1


# s = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 0]]
#
# print(encode_4_base(s, 2))
