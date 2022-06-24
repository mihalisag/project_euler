# 11/07/19

from primes import primeFactorsOnly as pf

i = 200
key = True
l = []

while key:

    l = [len(set(pf(k))) for k in range(i,i+4)]

    if set(l) == set([4]):
        key = False
        print([i,i+1,i+2,i+3])

    i+=1



















# key = True
# n = 129000
#
# while key:
#
#     list_i = []
#     i = n
#
#     while i<=n+3:
#
#         if len(list(prime_factorization(i).keys())) == 4:
#             list_i += [len(list(prime_factorization(i).keys()))]
#             i+=1
#         if sum(list_i)==16:
#             check = [True]
#             for i in list_i:
#                 if i!=4:
#                     check += [False]
#             if False not in check:
#                 key = False
#                 print(n)
#
#         n+=1
