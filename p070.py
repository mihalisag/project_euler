# 15/07/21

from my_primes import prime_factorization
from itertools import permutations
from tqdm import tqdm

def phi(num):
    '''
        Totient function
    '''
    factor_dict = prime_factorization(num) # n = 12: f = {2: 2, 3: 1} 
    totient = 1

    for prime in factor_dict:
        totient *= (prime**(factor_dict[prime]-1)) * (prime - 1)
    
    return totient


int_joiner = lambda str_list: int(''.join(str_list))

def ananumber(num):

    digit_permutations = permutations(str(num))
    
    return list(map(int_joiner, digit_permutations))[1:]


MAX = 10**5 + 1
min_ratio = MAX
totient_list = []

for num in tqdm(range(1, MAX)):

    totient = phi(num)
    totient_list.append(totient)
    if totient in ananumber(num):
        ratio = num / totient
        if ratio < min_ratio:
            min_ratio = ratio