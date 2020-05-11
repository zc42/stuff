from pynput.keyboard import Key, Listener
import g15_new.unsorted_stuff.print_board as pb
from g15_new.g15_context import Ctx
from game_15.game15 import Game_15


def init():
    global g

    # -----------------
    ctx = Ctx(keyboard=True,
              base_objective=True,
              encode_4_conv_v2=True)
    # ctx.init()
    # test_rndm_brd=True)
    g = Game_15(ctx)

    pb.pprint_grid_4x4(g, 0)
    with Listener(on_press=on_press) as listener:
        listener.join()


def move(m):
    s, r, f, s0 = g.make_move(m)
    pb.pprint_grid_4x4(g, r)
    if f:
        g.init()
        pb.pprint_grid_4x4(g, 0)


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
