# 18/07/19

import math

number = 3
key = True
i = 2
l = []


while len(l)<2:

    th = math.sqrt(1+8*number)
    p = math.sqrt(1+24*number)

    np = (1+p)/6
    nt = (th-1)/2
    nh = (1+th)/4


    if p%1 == 0 and nt%1==0 and np%1==0 and nh%1==0:
        l.append(number)

    i += 1
    number += i

print(l)