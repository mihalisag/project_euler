# 14/10/19

import math

def pentagon_test(n):
	if (1+math.sqrt(1+24*n))/6 % 1 == 0:
		return True
	return False

def p(n): return (n*(3*n-1))/2 # pentagon number

for i in range(1,10000):
	for j in range(i,10000):
		D = p(j)-p(i)
		S = p(j)+p(i)
		if pentagon_test(D) and pentagon_test(S):
			print(D,i,j)