import math
import time

def Fibonacci1(n):

    start = time.time()
    n1 = 0
    n2 = 1
    i = 0

    while i<n:
        nth = n1+n2
        n1 = n2
        n2 = nth
        i+=1

    end = time.time()-start

    #return nth,end
    return n1,end

def Fibonacci2(n):

    start = time.time()
    phi = (1+math.sqrt(5))/2

    #return math.floor((phi**n)/math.sqrt(5)+1/2),time.time()-start
    a = math.floor((phi**n)/math.sqrt(5)+1/2)

    end = time.time()-start

    return a,end
