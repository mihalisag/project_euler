from primes import eratosthenes_sieve

def prime_summations(n):

	primes = eratosthenes_sieve(n)
	permutations = (n + 1) * [0]
	permutations[0] = 1

	for prime in primes:
		for i in range(prime,n+1):
			permutations[i] += permutations[i-prime]

	return permutations[-1]

if __name__ == '__main__':

	k = 10

	while prime_summations(k) < 5000:
		if prime_summations(k) >= 5000:
			print(k)
		k+=1

