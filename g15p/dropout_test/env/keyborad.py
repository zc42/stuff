from pynput.keyboard import Key, Listener
import g15_new.unsorted_stuff.print_board as pb
from dropout_test.env.grid_4x4 import Game4x4
from dropout_test.env.grid_context import GridCtx
from dropout_test.sate_data import data


def init():
    global g

    # -----------------
    ctx = GridCtx(data=data)
    ctx.init()
    # test_rndm_brd=True)
    g = Game4x4(ctx)

    pb.pprint_grid_4x4(g, 0)
    with Listener(on_press=on_press) as listener:
        listener.join()


def move(m):
    s, r, f, s0 = g.make_move(m)
    pb.pprint_grid_4x4(g, r)


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
