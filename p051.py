import numpy as np
from my_primes import eratosthenes_sieve
from itertools import permutations

MAX = 10 ** 8
sieve = eratosthenes_sieve(MAX)
sieve.remove(2)
sieve.remove(5)

first_digit = lambda num: int(str(num)[0])
first_digit_family = lambda num: 'f_' + str(int(str(num)[0]))
last_digit_family = lambda num: 'e_' + str(int(str(num)[-1]))
digits_number_family  = lambda num: 'I_' + str(len(str(num)))
digits_number = lambda num: len(str(num))

def max_next(num, one_number):
    '''
        Finds next possible number
    '''
    num = str(num)
    one_number_digits = digits_number(one_number)

    if one_number_digits >= digits_number(num):
        return (first_digit(num)+1) * 10**(one_number_digits-1)
    else:
        return digit_replacer(num, -one_number_digits, 9) 

def ones(n):
    '''
        n = 4: [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
    '''
    
    zeros = n * [0]
    pos_list = []

    for i in range(n):
        a = len(zeros[i:])
        b = n - len(zeros[i:])
        pos =  a*[1] + b*[0]
        pos_list.append(pos)

    return pos_list

def possible_digits_replacements(n):
    '''
        n = 4: [10, 100, 110, 1000, 1010, 1100, 1110]
    '''
    
    pos_list = ones(n - 1)
    per_list = []

    for pos in pos_list:
        one_per = list(permutations(pos, n - 1))
        
        for per in one_per:
            new_per = list(per) + [0]
            if new_per not in per_list:
                per_list.append(new_per) 

    diff_list = []
    for per in per_list:
        per = [str(i) for i in per]
        diff_list.append(int(''.join(per)))

    diff_list.sort()

    return diff_list

max_digits = len(str(MAX))

# Intervals with specific number of digits
interval_dict = {}
for j in range(1, max_digits):
    interval_dict['I_' + str(j)] = range(10 ** (j-1), (10 ** j) - 1)

# Dictionary with primes which are ordered 
digit_num_dict = {}
for i in range(1, max_digits):
    digit_num_dict['I_' + str(i)] = set()

for prime in sieve:
    digit_num_dict['I_' + str(digits_number(prime))].add(prime)

for digit_family_name in digit_num_dict:
    prime_interval = digit_num_dict[digit_family_name]
    end_dict = {('e_' + str(num)) : [] for num in [1, 3, 7, 9]}

    for prime in prime_interval:
        end_dict[last_digit_family(prime)].append(prime)
        end_dict[last_digit_family(prime)].sort()

    digit_num_dict[digits_number_family(prime)] = end_dict

def max_next_prime():
    '''
        Finds max possible prime greater than input
    '''
    for interval in list(digit_num_dict.values())[1:]:
        for ending in interval.values():
            ending = np.array(ending)
            for prime in ending:
                max_pos_prime = max_next(prime)
                max_prime_index = sum(ending < max_pos_prime) - 1
                max_prime = ending[max_prime_index]

    return max_prime

def digit_replacer(num, pos, new_digit):
    '''
        Replaces digits in given number
    '''
    num = [str(i) for i in list(str(num))]
    num[pos] = str(new_digit)
    num = int(''.join(num))

    return num

    # def number_representation(num):

#     digits = list(map(int, list(str(num))))
#     representation = dict(enumerate(digits[::-1], 0))
    
#     return representation