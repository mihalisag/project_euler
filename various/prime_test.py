from sympy import sieve
from primes import eratosthenes_sieve
import time

start = time.time()

# sym = list(sieve.primerange(1, 10000000))
own = eratosthenes_sieve(10000000)

print(time.time() - start, 's')

# Γρηγορότερο το own