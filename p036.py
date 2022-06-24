# 26/06/19

import math, time

start = time.time()

def is_palindrome(n):

    n = str(n)
    if n[:int(len(n)/2)] == n[int(len(n)/2)+(len(n)%2):][::-1]: return True

    return False

def dec_to_binary(n): return '{0:b}'.format(n)

l = []

for i in range(1,10**6+1):
    if is_palindrome(i) and is_palindrome(dec_to_binary(i)):
        print([i,dec_to_binary(i)])
        l.append(i)

end = time.time()-start

print(sum(l),str(end)+'s')


# import math,time
#
# start = time.time()
#
# def is_palindrome(n):
#
#     n = str(n)
#
#     if len(n)%2==0:
#         if n[:int(len(n)/2)] == n[int(len(n)/2):][::-1]: return True
#     else:
#         if n[:int(len(n)/2)] == n[int(len(n)/2)+1:][::-1]: return True
#     return False
#
# def dec_to_binary(n): return '{0:b}'.format(n)
#
# l = []
#
# for i in range(1,10**6+1):
#     if is_palindrome(i) and is_palindrome(dec_to_binary(i)):
#         print([i,dec_to_binary(i)])
#         l.append(i)
#
# end = time.time()-start
#
# print(sum(l),str(end)+'s')
