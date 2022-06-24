from primes import eratosthenes_sieve
from itertools import combinations

primes_list = eratosthenes_sieve(1000000)

a = list(combinations(primes_list[:100], 5))