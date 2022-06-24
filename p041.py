# 06/07/19

from primes import prime_check
from itertools import permutations

r = ['1234','1234567']
count = 0
max = 0

for number in r:

	s = list(number)
	l = list(permutations(s))

	for tuple in l:
		t = ''
		for i in tuple:
			t+=i
		t = int(t)

		if t>max and prime_check(t):
			max = t

print(max)

