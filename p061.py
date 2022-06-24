# 09/10/21

from itertools import permutations
from functools import reduce

triangle = lambda n: (n*(n+1)) / 2
square = lambda n: n**2
pentagonal = lambda n: (n*(3*n-1))/2
hexagonal = lambda n:  n*(2*n-1)
heptagonal = lambda n: (n*(5*n-3))/2
octagonal = lambda n: n*(3*n-2)

n_ranges = {
    3: list(range(45, 141)),
    4: list(range(32, 100)),
    5: list(range(26, 82)),
    6: list(range(23, 71)),
    7: list(range(21, 64)),
    8: list(range(19, 59))
}

functions = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
figurate_dict = { functions.index(func) + 3: list(map(int, map(func, n_ranges[functions.index(func) + 3]))) for func in functions}

cyclical_check = lambda x, y: str(x)[2:] == str(y)[:2]
initial_digits = lambda num: str(num)[:2]
last_digits = lambda num: str(num)[2:]

def figurate_class(num, figurate_dict):

    for key in figurate_dict:
        if num in figurate_dict[key]:
            return key

def initial_digits_list(first_num, l, figurate_dict):
    
    limited_list = []
    existing_class = figurate_class(first_num, figurate_dict)

    for num in l:
        num_class = figurate_class(num, figurate_dict)
        if num_class != existing_class and initial_digits(num) == last_digits(first_num):
            limited_list.append(num)

    return limited_list

figurate_dict