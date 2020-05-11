from math import sqrt
import numpy as np


# source from https://github.com/gliderkite/puzzle15 .. done some fixies to empty tile row
# logic is here https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
def __is_solvable(a=np.array):
    """Check if the puzzle is solvable."""
    # count the number of inversions
    inversions = 0
    for i, v in [(i, v) for i, v in enumerate(a) if v != len(a)]:
        j = i + 1
        while j < len(a):
            if a[j] < v:
                inversions += 1
            j += 1
    # check if the puzzle is solvable
    size = int(sqrt(len(a)))
    # grid width is odd and number of inversion even -> solvable
    if size % 2 != 0 and inversions % 2 == 0:
        return True
    # grid width is even


    if size % 2 == 0:
        x = np.where(a == 16)[0][0]
        emptyrow = size - x // size
        b = (emptyrow % 2 != 0) == (inversions % 2 == 0)
        return b
    return False


def is_solvable(state=np.array):
    a = state
    a = np.reshape(a, [16]).astype(int)
    i = np.where(a == 0)[0][0]
    a[i] = 16
    # a = list(map(lambda x: 16 if x == 0 else x, a))
    return __is_solvable(a)


# state = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 0, 11, 10],
#                   [13, 12, 15, 14]])

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11, 10, 13, 16, 15, 14]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 15, 14]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# state = np.array([[5, 11, 8, 6], [14, 10, 15, 13], [7, 4, 9, 2], [12, 3, 0, 1]])

# print(is_solvable(state))
