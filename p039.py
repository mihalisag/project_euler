# 24/07/20

import math
from functools import reduce
import time

def gcd_of(l):
	return reduce(math.gcd, l)


def pyth_triples_perim(s):

	solutions = []
	# d = 0

	upper_limit = math.floor(math.sqrt(s/2))

	for n in range(1,upper_limit):

		for m in range(n+1,upper_limit):

			a = m**2-n**2
			b = 2*n*m
			c = m**2+n**2

			l = {a, b, c}
			# print(l)
			
			g = s/sum(l)

			if g%1 == 0: l = {g*a, g*b, g*c}

			if sum(l) == s and l not in solutions:
				solutions.append(l)
				# print(d)


	return solutions


if __name__ == '__main__':

	m = 1
	start = time.time()

	for perim in range(1,1001):
		solutions = pyth_triples_perim(perim)
		if len(solutions) > m:
			m = len(solutions)
			max_solutions = solutions
			max_perim = perim
	
	print(max_perim, max_solutions, time.time()-start ,sep='\n')





# def pyth_triples_perim(s):
# 	d = 0
#
# 	upper_limit = math.floor(math.sqrt(s/2))
# 	solutions = set()
#
# 	for n in range(1,upper_limit):
#
# 		for m in range(n+1,upper_limit):
# 			a = m**2-n**2
# 			b = 2*n*m
# 			c = m**2+n**2
#
# 			if a+b+c == s:
# 				d = solutions.union(set([a,b,c]))
# 				print(d)
# 			elif s%a == 0 and s%b == 0 and s%c == 0:
# 				p = s/a
# 				if p*(a + b + c) == s:
# 					d = solutions.union(set([p*a,p*b,p*c]))
#
#
#
# 	return solutions