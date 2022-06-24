# 18/10/19

import itertools
import math

P = [2,3,5,7,11,13,17]


cart_product = itertools.product(range(0,10),repeat=10)

def residue_class(a,n):
	rc = []
	min_t = math.ceil(-a/n)
	max_t = math.floor((9-a)/n)
	for t in range(min_t,max_t+1):
		rc.append(t*n+a)

	return rc


d4 = range(0,9,2)
# d5 = residue_class(2*(d3+d4),n)
d6 = [0,5]

def remaining_numbers(l_big,l_small): return [i for i in l_big if i not in l_small]

s = []

for d1 in range(1,10):
	for d2 in remaining_numbers(range(10),[d1]):
		for d3 in remaining_numbers(range(10),[d1,d2]):
			for d4 in remaining_numbers(range(0,9,2),[d1,d2,d3]):
				for d5 in remaining_numbers(residue_class(2*(d3+d4),3),[d1,d2,d3,d4]):
					for d6 in [0,5] :
						if d6 not in [d1, d2, d3, d4, d5]:
							for d7 in remaining_numbers(range(10),[d1,d2,d3,d4,d5,d6]):
								n567 = int(str(d5)+str(d6)+str(d7))
								if n567 % 7 == 0:
									class8 = (d7>d6)*residue_class(d7-d6,11)+(d6>d7)*residue_class(10*(d6-d7),11)# KOLO 10 ANTEEEEEEEEEEEEEE
									for d8 in remaining_numbers(class8,[d1,d2,d3,d4,d5,d6,d7]):
										for d9 in remaining_numbers(range(10),[d1,d2,d3,d4,d5,d6,d7,d8]):
											n789 = int(str(d7)+str(d8)+str(d9))
											if n789 % 13 == 0:
												for d10 in remaining_numbers(range(10),[d1,d2,d3,d4,d5,d6,d7,d8,d9]):
													n8910 = int(str(d8) + str(d9) + str(d10))
													if n8910 % 17 == 0:
														s.append([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10])

a = [int(''.join(list(map(str,i)))) for i in s]
print(a)





		


# from primes import *
#
# for number in range(647,10**5):
#     pf1 = list(prime_factorization(number).keys())
#     if len(pf1) == 4:
#         pf2 = list(prime_factorization(number+1).keys())
#         if len(pf2) == 4:
#             pf3 = list(prime_factorization(number+2).keys())
#             if len(pf3) == 4:
#                 pf4 = list(prime_factorization(number+3).keys())
#                 if len(pf4) == 4:
#                     print(number)
