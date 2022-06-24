# 26/01/2021

import time

start = time.time()

import sympy as sp
import numpy as np

rad = lambda n: np.prod(list(sp.factorint(n).keys()))

N = 100000
n_to_rad = {i:rad(i) for i in range(1, N+1)}

rad_to_n = {}

for key, value in n_to_rad.items():
    rad_to_n.setdefault(value, []).append(key)

index = 0
k_under = 0
k = 10000
rads = sorted(rad_to_n.keys())
              
while k_under < k:
    k_under += len(rad_to_n[rads[index]])
    index += 1

index -= 1
list_index = k - (k_under-len(rad_to_n[rads[index]])) - 1 

e_k = rad_to_n[rads[index]][list_index]

print(e_k)
print(time.time() - start, 's')
