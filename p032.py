# 07/08/20

from itertools import permutations
import time

start = time.time()

# Επιστρέφει λίστα με τους δυνατούς n-ψήφιους αριθμούς
def n_digit_numbers(digits_list, n):

    pos_tuples = list(permutations(digits_list, n))
    pos_num_list = [int(''.join(list(map(str, tup)))) for tup in pos_tuples]

    return pos_num_list

all_digits = set(range(1,10))

# Επιστρέφει τα ψηφία ενός αριθμού
def digits_set(num): return set(map(int, list(str(num))))

# Επιστρέφει το συμπλήρωμα των ψηφίων ενός αριθμού
def rem_digits(num): return set(range(1, 10)).difference(digits_set(num))

# Επιστρέφει αν ένας αριθμός έχει μη επαναλαμβανόμενα ψηφία
def unique_test(num):
    if len(str(num)) == len(digits_set(num)): return True
    return False

prod_set_1 = set()

for cand in range(10, 100):

    if unique_test(cand):

        for plier in range(100, 1000):

            if unique_test(plier):

                if digits_set(plier).intersection(digits_set(cand)) == set():
                    prod = cand * plier

                    if 0 not in digits_set(prod) and unique_test(prod) and prod not in prod_set_1:
                        joined_set = digits_set(cand).union(digits_set(plier))

                        if rem_digits(prod) == joined_set:
                            prod_set_1.add(prod)
                            print([(cand, plier), prod])


print('---------------------------------')

prod_set_2 = set()

for cand in range(1, 10):

    if unique_test(cand):

        for plier in range(1000, 10000):

            if unique_test(plier):

                if digits_set(plier).intersection(digits_set(cand)) == set():
                    prod = cand * plier

                    if 0 not in digits_set(prod) and unique_test(prod) and prod not in prod_set_2:
                        joined_set = digits_set(cand).union(digits_set(plier))

                        if rem_digits(prod) == joined_set:
                            prod_set_2.add(prod)
                            print([(cand, plier), prod])

print(sum(prod_set_1)+sum(prod_set_2))
print(time.time()-start,'s')