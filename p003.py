# 02/03/19

import math
import primes

def max_prime_factor_of(n): # n = number to factorize

    l = [] # list of prime factors of n

    for i in primes.eratosthenis_sieve(n):
        if n%i == 0:
            l.append(i)

    m = max(l)

    return m
