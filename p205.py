import time,random

n = 10**7


def total(dice,sides): return sum([ random.randint(1,sides) for i in range(dice)])

colin_end = []
pete_end = []
p = 0

for i in range(n):

	colin = total(9,4)
	pete = total(6,6)

	if pete>colin:
		p+=1

print(p/n)




