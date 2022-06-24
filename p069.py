# 19/06/19

from my_primes import *

prime_list = eratosthenes_sieve(10**6)
max = 1
p = 1

for i in prime_list:
    if p*i<10**6:
        p = p*i

print('n = ' ,p)

# composite_list = [i for i in list(range(1,(10**5+1))) if i not in prime_list]
#
# # all_list = set(range(1,(10**2+1)))
# # composite_list = list(all_list-prime_list)
#
# max = 0
# # numerator = 0
# # denominator = 0
#
# for i in composite_list:
#
#     factor_list_n = list(prime_factorization(i).keys())
#     # factor_list_d = [i-1 for i in factor_list_n]
#     factor_list_d = [1,2]
#
#     numerator = product_list(factor_list_n)
#     # denominator = product_list(factor_list_d)
#     denominator = 2
#
#     fraction = numerator/denominator
#
#     if fraction>max:
#         max = fraction
#         n = i
