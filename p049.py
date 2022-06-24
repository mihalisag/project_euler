# 17/06/19

from primes import eratosthenes_sieve
import time

start = time.time()

l = eratosthenes_sieve(10000)

l = l[l.index(1009)+1:] # 1009 first prime after 1000

for prime_1 in l:
    for prime_2 in l[l.index(prime_1)+1:]: #prime_2>prime_1
            p = 2*prime_2-prime_1 # p-prime_2 = prime_2-prime_1
            if p<10000:
                if set(str(prime_1)) == set(str(prime_2))== set(str(p)):
                    if p in l: # check if prime
                        triple = [prime_1,prime_2,p]

end = time.time()-start

print(triple,end)

# dl = [len(str)*set(str(i)) for i in l]
#
# print(dl)

#
# i = 0
#
# key = True
#
# while key:
#     k = l[i]
#     if k>=1000:
#         key = False
#     i+=1
