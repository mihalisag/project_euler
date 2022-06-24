# 05/09/20

import time
from math import sqrt
import sympy

start = time.time()

num = 1
square = 1
side = 2
count = 1
square_side = 1
flag = True
l = []
perc = 1


while perc > 0.1:

    square = num ** 2
    diag_elem = square
    count += 4
    square_side += 2

    for i in range(4):

        if sympy.isprime(diag_elem):
            l.append(diag_elem)

        diag_elem += side

        perc = len(l) / count

    square = num ** 2
    side += 2
    num += 2

# print('Number of primes = ', len(l))
# print('Last prime = ', l[-1])
# print(count)
print('Side =', square_side)
print(time.time() - start, 's')
# print(l)
# import numpy as np
# from primes import eratosthenes_sieve

# def coor_make(coor, sq, coordinates, num, A):

#     mat_dict = {'row' : 0, 'col' : 1}

#     if coor ==  'row':
#         end = sq
#     elif coor == 'col':
#         end = sq + 1

#     for i in range(1, end):

#         if sq % 2 == 0:
#             coordinates[mat_dict[coor]] -= 1
#         else:
#             coordinates[mat_dict[coor]] += 1

#         # print(tuple(coordinates - np.ones(2).astype('int64')), 'left')
#         num += 1
#         A[tuple(coordinates - np.ones(2).astype('int64'))] = num

#     return A, num

# def square_creator(n):

#     A = np.zeros((n + 1, n + 1))
#     start_coor = int((n+1) / 2)

#     num = 2

#     coordinates = np.array((start_coor, start_coor + 1))
#     A[coordinates - np.ones(2).astype('int64')] = num

#     for sq in range(2, n + 1):

#         A, num = coor_make('row', sq, coordinates, num, A)
#         A, num = coor_make('col', sq, coordinates, num, A)

#     A[(start_coor - 1, start_coor - 1)] = 1

#     return A[:-1, :-1]

# def diagonals(A):

#     left_diag = A.diagonal()
#     right_diag = np.fliplr(A).diagonal()

#     diag = list(left_diag)
#     diag.extend(list(right_diag))
#     diag.remove(1)

#     return diag

# flag = True
# num = 621
# sieve = eratosthenes_sieve(100000)

# while flag:

#     A = square_creator(num)
#     diagonals_list = diagonals(A)

#     perc = sum([1 for elem in diagonals_list if elem in sieve]) / len(diagonals_list)
#     print(perc)

#     if perc <= 0.1:
#         flag = False
#         size = np.shape(A)
#     else:
#         num += 2

# print(size)

# print(A)


# margin = start_coor - 1

# orig_odd = 3
# orig_even = 2

# # Odd squares on bottom-right diagonal
# for i in range(start_coor, n):
#     A[(i, i)] = orig_odd ** 2
#     orig_odd += 2

# # Even squares on upper-left diagonal
# for i in range(start_coor - 1, 0, -1):
#     A[(i - 1, i)] = orig_even ** 2
#     orig_even += 2
