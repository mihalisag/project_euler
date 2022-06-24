# 17/08/19

from primes import eratosthenes_sieve,prime_check

primes_list = eratosthenes_sieve(1000)
b_list = [-i for i in primes_list]
b_list.extend(primes_list)


# b_list = eratosthenes_sieve(998)
m = 0
a = -999
coefficient_list = []

def quadratic_function(n,a,b):

    return n**2 + a*n + b

while a <= 999:

    for b in b_list:

        n = 0
        key = True

        while key:

            p = quadratic_function(n, a, b)

            if p > 0 and prime_check(p):
                n += 1
            else:
               key = False

        size = n + 1

        if  size > m:

            m  = size
            # coefficient_list.append([a,b,n])
            coefficient_list = [a, b, n]

    a += 2

print(coefficient_list)


#
# for b in b_list:
#     for a in range(1,1000,2):
#         if




# b_list = [-i for i in primes_list]
# b_list.extend(primes_list)
# primes_list = eratosthenes_sieve(998)

