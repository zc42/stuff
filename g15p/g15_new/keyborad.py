from pynput.keyboard import Key, Listener
import g15_new.unsorted_stuff.print_board as pb
from g15_new.ctx_hof import Ctx_hof
from g15_new.g15_context import Ctx
from g15_new.game15 import Game_15
from g15_new.lessons.lesson_groups import Lsn, get_lessons_one_case


def init():
    global g

    # (3, 1, (0, 3))
    lsn = get_lessons_one_case(Lsn(5, 10, (0, 3)))
    # -----------------
    ctx = Ctx(keyboard=True,
              # base_objective=True,
              test=True,
              lessons=lsn)
    # test_rndm_brd=True)
    ctx_hof = Ctx_hof(ctx, Ctx_hof.get_hof_v1())
    g = Game_15(ctx_hof)

    pb.pprint_test_info(g, 0)
    with Listener(on_press=on_press) as listener:
        listener.join()


def move(m):
    s, r, f, s0 = g.make_move(m)
    pb.pprint_test_info(g, r)


#     pb.pprint_test_info(self)

def on_press(key):
    key_press = key
    # print("PRESSED", key_press)
    m = -1
    m = 0 if key_press == Key.up else m
    m = 1 if key_press == Key.down else m
    m = 2 if key_press == Key.left else m
    m = 3 if key_press == Key.right else m
    if (m != -1):
        move(m)


# while True:

if __name__ == '__main__':
    init()
