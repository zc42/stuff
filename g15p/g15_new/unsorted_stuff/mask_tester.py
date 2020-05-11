import numpy as np

mask_1 = [[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_2 = [[1, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_3 = [[1, 2, 3, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_4 = [[1, 2, 3, 4],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_5 = [[1, 2, 3, 4],
          [5, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_6 = [[1, 2, 3, 4],
          [5, 6, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_7 = [[1, 2, 3, 4],
          [5, 6, 7, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_8 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

mask_9 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 0, 0, 0],
          [0, 0, 0, 0]]

mask_13 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 0, 0, 0],
           [13, 0, 0, 0]]

mask_10 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 0, 0],
           [13, 0, 0, 0]]

mask_14 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 0, 0],
           [13, 14, 0, 0]]


def is_mask_ok(mask=np.ndarray, state=np.ndarray):
    l0 = np.reshape(mask, [16])
    l1 = np.reshape(state, [16])
    l2 = list(map(lambda x: (l0[x], l1[x]), range(0, len(l0))))
    l3 = list(filter(lambda x: x[0] != 0, l2))
    l4 = list(filter(lambda x: x[0] != x[1], l3))
    # l3 = list(filter(lambda x: True, l2))

    # print(l0)
    # print(l1)
    # print(l2)
    # print(l3)
    # print(l4)
    # print(len(l4) == 0)
    return len(l4) == 0


def test_if_level_degraded(state, prev_state, mask=[]):
    b0 = is_mask_ok(mask, prev_state)
    b1 = is_mask_ok(mask, state)
    return b0 and not b1


def is_all_masks_ok(state, prev_state):
    b = True
    b = b and test_if_level_degraded(state, prev_state, mask_1)
    b = b and test_if_level_degraded(state, prev_state, mask_2)
    b = b and test_if_level_degraded(state, prev_state, mask_4)
    b = b and test_if_level_degraded(state, prev_state, mask_5)
    b = b and test_if_level_degraded(state, prev_state, mask_6)
    b = b and test_if_level_degraded(state, prev_state, mask_8)
    b = b and test_if_level_degraded(state, prev_state, mask_13)
    b = b and test_if_level_degraded(state, prev_state, mask_14)
    return not b


def test_masks_is_9_and_not_13(state):
    b = is_mask_ok(mask_9, state)
    b = b and not is_mask_ok(mask_13, state)
    return b


def test_masks_is_10_and_not_14(state):
    b = is_mask_ok(mask_10, state)
    b = b and not is_mask_ok(mask_14, state)
    return b

def test_masks_14_ok(state):
    return is_mask_ok(mask_14, state)


def test_masks_13_ok(state):
    return is_mask_ok(mask_13, state)


def test_masks_10_ok(state):
    return is_mask_ok(mask_10, state)


def test_masks_3(state):
    mask_1 = [[1, 2, 3, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    mask_2 = [[1, 2, 0, 3],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    return is_mask_ok(mask_1, state) or is_mask_ok(mask_2, state)


def test_masks_9_for_13(state):
    mask_1 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 0, 0, 0],
              [0, 0, 0, 0]]
    mask_2 = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [0, 0, 0, 0],
              [9, 0, 0, 0]]
    # mask_3 = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [0, 0, 0, 0],
    #           [0, 9, 0, 0]]
    # mask_4 = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [0, 9, 0, 0],
    #           [0, 0, 0, 0]]
    return is_mask_ok(mask_1, state) \
           or is_mask_ok(mask_2, state)
    # or is_mask_ok(mask_3, state) \
    # or is_mask_ok(mask_4, state)


def test_masks_g(g=int, state=[]):
    l1 = list(range(1, g + 1))
    l2 = list(map(lambda x: 0, range(g + 1, 17)))
    mask = np.copy(l1).tolist()
    mask = np.append(mask, list(l2)).astype(int).tolist()
    mask = np.reshape(mask, [4, 4]).tolist()
    return is_mask_ok(mask, state)


def test_masks_7(state):
    mask_1 = [[1, 2, 3, 4],
              [5, 6, 7, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    mask_2 = [[1, 2, 3, 4],
              [5, 6, 0, 7],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    return is_mask_ok(mask_1, state) or is_mask_ok(mask_2, state)


def manhattan_heuristic(state):
    """
    this sums up the manhattan distances between the board's state and the solution's state.
    excludes the 0 tile
    """
    state = np.array(state)
    indices = np.array([np.argwhere(state == i)[0] for i in range(1, 16)])
    correct_indices = np.array([[i, j] for i in range(4) for j in range(4)])[:-1]

    return 50 - np.abs(indices - correct_indices).sum()

# ctx = Ctx()

# ctx.prev_state = [[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12],
#                   [0, 14, 15, 0]]

# state = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 12, 0, 11],
#          [13, 15, 14, 10]]

# masks_9_13_ok = test_masks_9_13(ctx)
# print(masks_9_13_ok)
# print(test_masks_g(15, state))

# ---------------------------
