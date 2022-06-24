import math

def erat(n):

    l = list(range(2,n+1))

    for i in l:

        k=2

        while k*i <= l[len(l)-1]:
            if k*i in l:
                l.remove(k*i)
            k+=1

    return l

def number_of_primes(n):

    p = len(erat(n))
    return p
