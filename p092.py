# 17/08/19

import time

start = time.time()

def sum_sq_digits(n):

    n = str(n)
    r = list(map(int,n))
    p = [i**2 for i in r]

    return sum(p)

n = 1
count = 0
previous = set()

while n <= 10**7:

    a = []
    o = n
    key = True

    while key:

        o = sum_sq_digits(o)

        if o in previous or o == 89:

            previous =  previous.union(set(a))
            count += 1
            key = False

        elif o == 1:

            key = False

        a.append(o)

    n += 1

end = time.time()-start

print(count,end)