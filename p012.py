# 19/06/19

from primes import *

i = 1
triagonal = 1
number = 0

def prime_factorization(n):

    k = n
    exp = [] #list of exponents
    factor_dict = {}
    e = eratosthenes_sieve(75000)  #έχω ακροφοβία

    while k>1:

        for i in e:
            if k%i == 0:
                a = 0
                while k%i == 0:
                    k = k/i
                    a+=1
                factor_dict.update({i:a})

    return(factor_dict)

def number_of_divisors(n):

    exponents = list(prime_factorization(n).values())
    l = [i+1 for i in exponents]
    return product_list(l)


while number_of_divisors(triagonal)<500:

    triagonal = int(i*(i+1)/2)
    i+=1
    print(triagonal)

print(triagonal)
