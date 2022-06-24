import numpy as np
from itertools import permutations
from functools import reduce
from pprint import pprint

def possible_numbers(iter):

    perm_list = list(permutations(iter))

    return set([int(''.join(map(str, perm))) for perm in perm_list])

def num_to_list(n): return list(map(int, list(str(n))))

flag = True
i = 345
perm_dict = {}
kako_l = set()

while flag:

    digits = num_to_list(i**3)
    digits.sort()
    perm_dict[i] = digits

    for key_1 in perm_dict:
        l = [k for k,v in perm_dict.items() if v == perm_dict[i]]
        print(l)
        if len(l) == 5:
            print(l)
            flag = False
    # if len(perm_dict[i]) == 2: flag = False

    i += 1
# print(kako_l)
# pprint(perm_dict)















# if __name__ == '__main__':

#     b = [4, 1, 0, 6, 5]
#     a = possible_numbers(b)
#     # print(a)

#     a = 345**3
#     possible_set = possible_numbers(num_to_list(a))

#     # possible_set = [i**3 for i in range(1, 31)]

#     cube_root_list = list(map(lambda x: x**(1/3), possible_set))
#     print(len(list(cube_root_list)))
#     v = [float(format(i, '0.1f')).is_integer() for i in cube_root_list]
#     print(len(v))
#     print(len(possible_set))
#     print(np.array(possible_set)[True, False])
