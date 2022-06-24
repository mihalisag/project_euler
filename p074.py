# 12/09/20

import math
import time
from functools import reduce

start = time.time()

def sum_fact_digits(n):

    digits = list(map(int, list(str(n))))
    return sum(map(math.factorial, digits))

    # return reduce(lambda x, y: math.factorial(x) + math.factorial(y), digits)

def chain_maker(n):

    chain = [n]
    flag = True

    while flag:

        n = sum_fact_digits(n)

        if n in chain:
            flag = False
        else:
            chain.append(n)

    return chain

count = 0
num_chain_length = {i:0 for i in range(1, 10**6 + 1)}

for num in range(1, 10**6 + 1):

    if num_chain_length[num] == 0:

        chain = chain_maker(num)

        for elem in chain:
            num_chain_length[elem] = len(chain)

        if len(chain) == 60:

            count += 1

print(count, time.time() - start, 's')







