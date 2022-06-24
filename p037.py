# 27/06/19

from primes import eratosthenes_sieve
import time

start = time.time()

prime_list = eratosthenes_sieve(10**6)
prime_list = [str(i) for i in prime_list]
composite_list = ['4','6','8','9','0'] # δεν είναι όλα


def left(n): #σβήνει τα αριστερά
	l = []
	for i in range(len(n)):
		l.append(n[i:])
	return l

def right(n): #σβήνει τα δεξιά
	l = []
	for i in range(len(n)):
		l.append(n[:len(n)-i])
	return l

trunctable_list = []

for prime in prime_list[prime_list.index('11'):]:

	if prime[0] not in composite_list and prime[len(prime)-1] not in composite_list:

		key_l = True
		key_r = True

		for k in left(prime):
			if k not in prime_list and key_l:
				key_l = False

		if key_l:
			for k in right(prime):
				if k not in prime_list and key_r:
					key_r = False


		if key_l and key_r:
			trunctable_list.append(prime)

trunctable_list = [int(i) for i in trunctable_list]

print(trunctable_list,str(time.time()-start)+'s')


# def right(n):
# 	k = []
# 	l = left(n[::-1])
# 	for i in l:
# 		k.append(i[::-1])
# 	return k