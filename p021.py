# 26/06/19

def divisors(n):

	l = []

	for i in range(1,n):
		if n%i==0:
			l.append(i)

	return l

def sum_of_divisors(n): return sum(divisors(n))


if __name__ == '__main__':

	l = set()

	for a in range(1,10000):
		b = sum_of_divisors(a)
		if  a!=b and sum_of_divisors(b) == a:
			l.update({a,b})

	print(sum(list(l)))
