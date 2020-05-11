from g15_new.unsorted_stuff.mask_tester import is_mask_ok

# region 'masks'
mask_10_1 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 0, 0],
             [13, 10, 0, 0]]

mask_10_2 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 0, 0],
             [13, 0, 14, 0]]

mask_10_3 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 0, 0],
             [13, 14, 0, 0]]
# -------------
mask_10_x_1 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 0, 10, 0],
               [10, 0, 0, 0]]


# endregion

def objective_for_goal_14(state=[], lesson=(), steps_done=int):
    g = lesson[0]
    if g != 14: return True

    r = is_mask_ok(mask_10_x_1, state)
    if r: return False

    steps_done += 1
    max_steps = get_max_steps(lesson)
    if steps_done < max_steps: return True

    r = is_mask_ok(mask_10_1, state) \
        or is_mask_ok(mask_10_2, state) \
        or is_mask_ok(mask_10_3, state)
    return r


def get_max_steps(lesson):
    # if lesson[2] == (2, 3):
    if lesson[1] == 0:
        return 7
    if lesson[1] == 1 and lesson[2] == (2, 2):
        return 3
    if lesson[1] == 2:  # and lesson[2] == (2, 2):
        return 3
    elif lesson[1] == 3:
        return 5
    elif lesson[2] == (2, 1):
        return 3
    return 1
