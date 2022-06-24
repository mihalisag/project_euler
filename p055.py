# 25/08/20

import time

start = time.time()

def reverse(n): return int(str(n)[::-1])

def isLychrel(n):

    for i in range(50):
        n += reverse(n)
        if n == reverse(n): return 0
    return 1


lychrel_count = sum(isLychrel(n) for n in range(1, 100001))

print(lychrel_count)
print(time.time() - start, 's' )



# import time

# start= time.time()

# def is_palindrome(n):

#     n = str(n)

#     if n[:int(len(n)/2)] == n[int(len(n)/2)+(len(n)%2):][::-1]: return True

#     return False

# def iter_algor(n): return n + int(str(n)[::-1])

# lychrel_list = []

# for num in range(1, 100001):

#     iterations = 0
#     orig = num

#     while iterations <= 50:

#         num = iter_algor(num)
#         iterations += 1

#         if is_palindrome(num):
#             # print(orig, num)
#             iterations = 100

#     if iterations == 51: lychrel_list.append((orig, iterations))


# print(len(lychrel_list))
# print(time.time() - start, 's' )

# Μέχρι 100001
# Πρώτη έκδοση
# 6208
# 2.2476751804351807 s
# Δεύτερη έκδοση
# 6208
# 1.468015193939209 s