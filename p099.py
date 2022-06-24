# 02/07/19

import math

file = open('p099_base_exp.txt','r')
numbers = file.read()
numbers = str(numbers)

numbers =numbers.split('\n')
l = []

def merge(l):
	s =''
	for i in l:
		s+=i

	return s

m = 1
k = 1

for i in numbers:
	i = list(i)
	base = int(merge(i[:i.index(',')]))
	exp = int(merge(i[i.index(',')+1:]))
	if exp*math.log10(base)>m:
		m = exp*math.log10(base)
		b = base
		e = exp
		l = k
	k+=1

print(b,e,l)
