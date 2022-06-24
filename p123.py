# 09/09/19

from primes import nth_prime

key = True
n = 3

while key:

	nth = nth_prime(n)

	if n % 2 == 1:

		r = (2*n*nth) % nth**2
		print(n, r, nth)

		if r > 10**10:

			print(2*n*nth,nth**2,r,nth,n)
			key = False

	n+=1