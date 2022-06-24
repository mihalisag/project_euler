import math
import primes as p

def frac(n):

    # a = math.floor(math.log10(n))+1 αριθμός ψηφίων
    o = list(str(n))
    a = len(o)-2
    s = 10**a
    n = s*n
    print(n,a)
    q = []

    for i in [2,5]:
        l = 0
        while n%i == 0 and l <= a:
                n = n/i
                l+=1
        print(l)
        q = q + [l]
        # s = s/q[len(q)-1]

    d = (2**(q[0]))*(5**q[1])
    s = s/d

    return n,q,s
