# 23/06/19

import math

# print('i   !   log10(factorial)')
# for i in range(1,10):
#     print(i,'  ',math.factorial(i),'    ',math.floor(math.log10(math.factorial(i)))+1)

# def digits(n): return math.floor(math.log10(math.factorial(n)))+1

n = 3
f = 1
l = []

while n>=3 and n<=10**8:
    digits = [int(i) for i in str(n)]
    f = len(str(math.factorial(max(digits))))
    if len(str(n)) >= f:
        s = 0
        for i in digits:
            s+=math.factorial(i)
        if n==s:
            l.append(n)
    n+=1

print(l)
