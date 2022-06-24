# 24/02/19


def fibo(n):
#n = ο n-ιοστος όρος
    n1 = 0
    n2 = 1
    i = 0

    while i<n-2:
        nth = n1+n2
        n1 = n2
        n2 = nth
        i+=1

    return nth


def sumFibo(n):

    i = 3
    s = 0

    while fibo(i)<n:

        if fibo(i)%2==0:
            s+=fibo(i)

        i+=1

    return s

#n = 4000000
