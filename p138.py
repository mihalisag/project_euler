# 21/07/19

import math,time

start = time.time()

# while len(l)<8:
#
#     for i in range(math.ceil(17.5*L),18*L):
#
#         D = 5*(i**2)-1
#         ds = math.sqrt(D)
#
#         if ds%1==0:
#             b_minus = (2*ds+4)/5
#             if b_minus>0 and b_minus%1==0:
#                 l.append(i)
#             else:
#                 b_plus = (2*ds-4)/5
#                 if b_plus > 0 and b_plus % 1 == 0:
#                     l.append(i)
#
#     L = i
#

l = [17,305]

while len(l)<12:

    a = math.ceil(((l[-1])**2)/l[-2])
    l.append(a)


end = time.time()-start
print(sum(l),end)
# [17, 305, 5473, 98209, 1762289, 31622993, 567451585]