# 27/06/19

m = 1

for a in range(1,10000):

	k = 1
	n = ''

	while len(n)<=9:
		n+=str(k*a)
		k+=1

	n = n[:9]

	if set(list(n)) == set(list('123456789')):
		n = int(n)
		if n<987654321:
			if n>m:
				m = n
				l = a
print(m,l,k)
