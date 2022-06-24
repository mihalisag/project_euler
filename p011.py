# 04/08/20

import numpy as np
from functools import reduce

matrix_file = open('p11_matrix.txt', 'r')
orig_matrix = matrix_file.readlines()

matrix = np.array([list(map(int, row[:-1].split(' '))) for row in orig_matrix])

def possible_arrays(i, j):

    pos_dict = {
        1: [(i, j + 1), (i, j + 2), (i, j + 3)], # E
        2: [(i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)], # NE
        3: [(i - 1, j), (i - 2, j), (i - 3, j)], # N
        4: [(i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)], # NW
        5: [(i, j - 1), (i, j - 2), (i, j - 3)], # W
        6: [(i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)], # SW
        7: [(i + 1, j), (i + 2, j), (i + 3, j)], # S
        8: [(i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)], # SE
    }

    return pos_dict

A = np.ones((26, 26))
A[3:23, 3:23] = matrix

max_prod = 1

for i in range(3, 23):
    for j in range(3, 23):

        pos_dict = possible_arrays(i, j)
        max_array = []

        for key in pos_dict:
            triple = A[list(zip(*pos_dict[key]))]
            quat = np.append(A[i, j], triple)
            max_array.append(np.prod(quat))

        m = np.max(max_array)

        if m > max_prod:
            max_prod = m

print(max_prod)


# b = np.array(range(1, 10)).reshape((3, 3))
