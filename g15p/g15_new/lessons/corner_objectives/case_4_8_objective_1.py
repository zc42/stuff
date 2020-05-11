from g15_new.unsorted_stuff.mask_tester import is_mask_ok

# region 'masks'
#  3 and 4
mask_3 = [[1, 2, 0, 3],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_4 = [[1, 2, 3, 4],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_4_1 = [[1, 2, 3, 0],
            [0, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

mask_4_x_1 = [[1, 2, 0, 0],
              [0, 0, 3, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

mask_4_x_2 = [[1, 2, 0, 0],
              [0, 0, 0, 3],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
# ----------------------------
#  7 and 8
mask_7 = [[1, 2, 3, 4],
          [5, 6, 0, 7],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_8 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_8_1 = [[1, 2, 3, 4],
            [5, 6, 7, 0],
            [0, 0, 0, 8],
            [0, 0, 0, 0]]

mask_8_x_1 = [[1, 2, 3, 4],
              [5, 6, 0, 0],
              [0, 0, 7, 0],
              [0, 0, 0, 0]]

mask_8_x_2 = [[1, 2, 3, 4],
              [5, 6, 0, 0],
              [0, 0, 0, 7],
              [0, 0, 0, 0]]

# ----------.....----------------------

masks_4 = [mask_4_x_1, mask_4_x_2, mask_3, mask_4_1, mask_4]
masks_8 = [mask_8_x_1, mask_8_x_2, mask_7, mask_8_1, mask_8]


# ----------masks----------------------
# endregion

def objective_for_goals_4_and_8(state=[], lesson=(), steps_done=int):
    gls = [4, 8]
    g = lesson[0]
    if not gls.__contains__(g): return True

    masks = masks_4 if g == 4 else masks_8

    r = is_mask_ok(masks[0], state) \
        or is_mask_ok(masks[1], state)

    if r: return False

    steps_done += 1
    max_steps = get_max_steps(lesson)
    if steps_done < max_steps: return True

    r = is_mask_ok(masks[2], state) \
        or is_mask_ok(masks[3], state) \
        or is_mask_ok(masks[4], state)

    return r


def get_max_steps(v):
    x = v[2][1]
    if v[1] == 0 and v[2][0] == 1: return 7 - x
    if v[1] == 2 and v[2][0] == 1: return 7 - x
    if v[1] == 6 and v[2][0] == 1: return 12 - x
    if v[1] == 7 and v[2][0] == 1: return 7 - x
    if v[1] == 9 and v[2][0] == 1: return 11 - x
    if v[1] == 10 and v[2][0] == 1: return 7 - x
    if v[1] == 12 and v[2][0] == 1: return 7 - x
    if v[1] == 14 and v[2][0] == 1: return 20 - x

    if v[1] == 4 and v[2][0] == 1: return 5 - x
    if v[1] == 8 and v[2][0] == 1: return 5 - x
    if v[1] == 11 and v[2][0] == 1: return 11 - x
    if v[1] == 15 and v[2][0] == 1: return 20 - x

    # if v[1] == 0 and v[2] == (2, 0): return 6
    # if v[1] == 0: return 5
    if v[1] == 5: return 7
    if v[2] == (1, 2): return 3
    return 1
