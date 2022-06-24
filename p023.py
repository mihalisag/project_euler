import time
from pprint import pprint
from primes import divisors
from itertools import combinations

start = time.time()

def abundant_check(n):
    if sum(divisors(n)[:-1]) > n: return True

flag = True
num = 1
abundant_list = []
sum_abun =  set()

while flag:

    if abundant_check(num):
        abundant_list.append(num)

        for abundant_num in abundant_list:
            sum_abun.add(abundant_num + num)

    if num > 28123: flag = False

    num += 1

s = 0

for num in range(1, 28123):
    if num not in sum_abun:
        s += num

# 39.84575080871582 s κακολύση
# abundant_list = [i for i in range(1, 28123) if abundant_check(i)]

# print(abundant_list)
# print(sum_abun)
print(s)
print(time.time() - start, 's')

# 1. Βρίσκω όλους τους abundant < 28123
# 2. Βρίσκω όλα τα δυνατά αθροίσματα abundant < 28123
# 3. for i in range(1, 28123)
#    Αν ο i δεν ανήκει στο 2 => προσθήκη σε λίστα
#    Απάντηση = άθροισμα λίστας
