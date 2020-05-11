# -----train--------------------------
# [[ ,   ,   ,   ],
#  [x,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [h,   ,   ,   ]]
#
# [[ ,   ,   ,   ],
#  [ ,   ,   ,  x],
#  [ ,   ,   ,   ],
#  [ ,   ,  h,   ]]
# -----test--------------------------
# [[ ,   ,   ,   ],
#  [ ,  x,   ,   ],
#  [ ,   ,   ,   ],
#  [h,   ,   ,   ]]
#
# [[ ,   ,   ,   ],
#  [h,   ,   ,   ],
#  [ ,   ,   ,   ],
#  [ ,   ,   ,  x]]
#
# ======================
from random import shuffle

from dropout_test.env.grid_context import hole, goal


def get_rndm_state():
    l = [-1 for v in range(1, 17)]
    l[0] = hole
    l[1] = goal
    shuffle(l)
    return tuple(l)


def generate():
    global data
    s = set()
    while len(s) != 200:
        l = get_rndm_state()
        s.add(l)
    l = list(s)
    # ---------------------
    data = 'data = ['
    for s in l:
        data += str(list(s)) + ',\n'
    data = data[:-2]
    data += ']'
    # ---------------
    f = open('./sate_data.py', 'w')
    f.write(data)
    f.close()

# generate()
