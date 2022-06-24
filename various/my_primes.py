import math,time

def eratosthenes_sieve(n):

    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.

    prime = (n+1)*[True]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    sieve = []

    for p in range(2, n):
        if prime[p]:
            sieve += [p]

    return sieve


def number_of_primes_below(n):

    p = len(eratosthenes_sieve(n))
    return p

def prime_check(n):

    if n % 2 == 0: return False
    # s = math.floor(math.sqrt(n))
    #
    # for i in eratosthenes_sieve(s):
    #     if n%i == 0:
    #         return False
    #
    # return True

    if n in eratosthenes_sieve(n+5): return True

    return False

def prime_factorization(n):

    start = time.time()
    k = n
    factor_dict = {}
    sieve = eratosthenes_sieve(n+2)  #έχω ακροφοβία


    while k>1:
        for prime in sieve:

            if k%prime == 0:
                exp = 0
                while k%prime == 0:
                    k = k/prime
                    exp+=1
                factor_dict.update({prime:exp})

    # end = time.time()-start
    #return(factor_dict,end)
    return factor_dict

# {2: 2, 3: 2, 3423367: 1}

def primeFactorsOnly(n):

    l = []

    while n % 2 == 0:
        l.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            l.append(i)
            n = n/i

    if n>2:
        l.append(int(n))

    return l

def product_list(l):

    p = 1
    for i in l:
        p *= i
    return p

def divisors(n):

    s = []

    for i in range(1,n+1):
        if n%i == 0:
            s+=[i]

    return s



def number_of_divisors(n):

    exponents = list(prime_factorization(n).values())
    # l = [a + b for a, b in zip(exponents, len(exponents)*[1])]
    l = [i+1 for i in exponents]

    return product_list(l)

def twin_prime(a,b):
    if b == a+2:
        if prime_check(a)==prime_check(b)==1:
            return True

    return False

def prime_count(x): return math.floor(x/math.log(x))

def nth_prime(n):

    x = 2
    key = True

    while key:

        if prime_count(x) > n:
            key = False
            return eratosthenes_sieve(x)[n-1]

        x+=1


def phi(n):
    '''
        Totient function
    '''
    factor_dict = prime_factorization(n) # n = 12: f = {2: 2, 3: 1} 
    totient = 1

    for prime in factor_dict:
        totient *= (prime**(factor_dict[prime]-1)) * (prime - 1)
    
    return totient



# 1.0 def eratosthenes_sieve(n):  #all primes below n
#
#     start = time.time()
#
#     l = list(range(2,n+1))
#
#     for i in l:
#
#         k = 2
#
#         while k*i <= l[len(l)-1]:
#             if k*i in l:
#                 l.remove(k*i)
#             k += 1
#
#     end = time.time()
#     s = end - start
#
#     return l,s





# def eratosthenes_sieve(n): #primes under n
#
#     start = time.time()
#
#     l = [2]
#     i = 3
#
#     while i<=n:
#         m = True
#         for k in l:
#             if i%k==0:
#                 m = False
#         if m == True:
#             l.append(i)
#         i+=1
#
#     end = time.time()
#     s = end - start
#
#     # return l,s
# #     return l
#
# def prime_factorization(n):
#
#     start = time.time()
#     k = n
#     factor_dict = {}
#     sieve = eratosthenes_sieve(n+2)  #έχω ακροφοβία
#     count = 0
#
#     while k>1 and count>=0:
#         prime = sieve[count]
#         if k%prime == 0:
#             exp = 0
#             while k%prime == 0:
#                 k = k/prime
#                 exp+=1
#             factor_dict.update({prime:exp})
#         print(k)
#         if k == 1:
#             count = -2
#         count+=1
#
#     end = time.time()-start
#     return(factor_dict,end)