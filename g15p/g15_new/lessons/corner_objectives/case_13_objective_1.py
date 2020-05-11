from g15_new.unsorted_stuff.mask_tester import is_mask_ok

# region 'masks'
mask_9_1 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [0, 0, 0, 0],
            [9, 0, 0, 0]]

mask_9_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 0, 0],
            [0, 13, 0, 0]]

mask_9_3 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 0, 0],
            [13, 0, 0, 0]]
# -------------
mask_9_x_1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [0, 9, 0, 0],
              [0, 0, 0, 0]]


# endregion

def objective_for_goal_13(state=[], lesson=(), steps_done=int):
    g = lesson[0]
    if g != 13: return True

    r = is_mask_ok(mask_9_x_1, state)
    if r: return False

    steps_done += 1
    max_steps = get_max_steps(lesson)
    if steps_done < max_steps: return True

    r = is_mask_ok(mask_9_1, state) \
        or is_mask_ok(mask_9_2, state) \
        or is_mask_ok(mask_9_3, state)
    return r


def get_max_steps(v):
    x = v[2][1]

    b = [2, 4].__contains__(v[1])
    if b and v[2][0] == 2: return 2 + x
    if v[1] == 5 and v[2][0] == 2: return 7 + x

    if v[2] == (2, 3): return 5
    # if v[1] == 2: return 4
    if [6, 7, 8].__contains__(v[1]): return 9
    if v[1] == 0: return 7
    if v[1] == 3: return 5
    if v[2] == (2, 1): return 3
    return 1
