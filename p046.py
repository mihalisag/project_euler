# 16/06/19

from primes import eratosthenes_sieve
from math import sqrt
import time

start = time.time()

n = 33
key = [1,2]

while len(key)>=2:
    n+=2
    key = [0]
    for p in eratosthenes_sieve(n+2):
        if sqrt((n-p)/2)%1==0:
            key += [1]

end = time.time() - start

print(n,end)
