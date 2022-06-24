# 29/07/19

import math,time

start = time.time()

l = []
m = 2/7

for d in range(1,9):
    max = math.floor((3/7) * d)
    min = math.ceil((2/7)*d)
    for n in range(min,max+1):
        if n/d > m:
          g = math.gcd(n,d)
          l = [n/g,d/g]

print(l)