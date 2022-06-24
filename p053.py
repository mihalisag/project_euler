# 18/07/20

import math

def binomial_coefficient(n,k): return math.factorial(n)/((math.factorial(k))*(math.factorial(n-k)))

count = 0
l = []

for n in range(23,101):
	for k in range(1,n+1):
		value = binomial_coefficient(n,k)
		if value>=10**6:
			l.append(value)
			count+=1


print(count)


# s = 0
#
#
# for n in range(1,101):
#     key = True
#
#     while key:
#         for r in range(n,1,-1):
#             denominator = factorial(r)
#             numerator = 1
#             for k in range(r):
#                 numerator *= n-k
#             fraction = numerator/denominator
#             if fraction>=10**6:
#                 key = False
#                 s+=n-r
#                 print(s)
#
