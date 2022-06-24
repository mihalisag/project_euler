# 09/08/20

import time

start = time.time()

def digit_sum(n): return sum(list(map(int, list(str(n)))))

m = 1

for a in range(1, 100):
    for b in range(1, 100):
        if digit_sum(a**b) > m:
            m = digit_sum(a**b)
            l = (a, b)


print(m)
print(l)
print(time.time()-start,'s')

