# 25/06/19

from primes import eratosthenes_sieve
import time

start = time.time()

prime_list = eratosthenes_sieve(10**6)
prime_list = [str(i) for i in prime_list]

count = 0
circular_primes = set()
prime_set = set(prime_list)


for prime in prime_list:
    l = set()
    if len(prime)>1 and len(set(prime)) == 1:
        circular_primes.add(prime)
    for i in range(len(prime)):
        prime = prime[1:]+prime[0]
        l.add(prime)
    if l.intersection(prime_set) == l:
        circular_primes.update(l)

count = len(circular_primes)
circular_primes = [int(i) for i in circular_primes]
circular_primes.sort()

end = time.time()-start
print(circular_primes,count,str(end)+'s')

['2', '3', '5', '7', '11', '13', '17', '31', '37', '71', '73', '79', '97',
 '113', '131', '197', '199', '311', '313', '331', '337', '373', '733',
 '773', '919', '991', '997', '1117', '1171', '1979', '1993', '3137',
  '3313', '3319', '3331', '3779', '9397', '11113', '11117', '11131',
   '11171', '11311', '13313', '13331', '13339', '17333', '19391',
    '19997', '31139', '31193', '31319', '31333', '31391', '33113',
    '33119', '33191', '33311', '33331', '37993', '39317', '73771',
    '77377', '77713', '77731', '77773', '77933', '91997', '93979',
    '99371', '99991', '111337', '111733',
 '111919', '113131', '119191', '131113', '131311', '131317', '133117',
 '133319', '133391', '139393', '191119', '191911', '193393', '311137',
 '313133', '313331', '313333', '331319', '331333', '331391', '331999',
 '333131', '333331', '333337', '333719', '373777', '377393', '377717',
  '377737', '379397', '379777', '399793', '713939', '719393', '733333',
  '737773', '739397', '777173', '777373', '779173', '793999', '799991',
  '919111', '993779', '993977', '997991']
