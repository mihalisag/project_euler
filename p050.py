from primes import eratosthenes_sieve
import math
import time

start = time.time()

max_num = 10**6

prime_list = eratosthenes_sieve(max_num)
n = len(prime_list)
print(n)

key = True

def myLoop():
    
    max_prime = 1
    max_sublist = [1]
    
    for i in range(n-1):
        # print(i)
        sublist = [1]
        m = 1
        k = 1
        while sum(sublist)<max_num:
            sublist = prime_list[i:m+i]
            while k <= len(sublist)-1:
                sub_sublist = sublist[:k]
                pos_prime = sum(sub_sublist)
                # if sum(sublist)>=max_num:
                #     break
                # print(sub_sublist,pos_prime)
                if pos_prime%2 != 0 and pos_prime < max_num and pos_prime in prime_list and len(sub_sublist)>len(max_sublist):
                    max_prime = pos_prime
                    max_sublist = sub_sublist
                k+=1  
            m += 1
    print(max_prime,max_sublist, len(max_sublist))
                    

myLoop()

print(time.time()-start,'s')

# def myLoop():
#     for l in range(n,1,-1):
#         print(l)
#         for k in range(n-l+1):
#             sublist = prime_list[k:k+l-1]
#             pos_prime = sum(sublist)
#             print(pos_prime)
#             if pos_prime%2 != 0 and pos_prime in prime_list:
#                 max_prime = pos_prime
#                 max_sublist = sublist
#                 print(max_prime,max_sublist, len(max_sublist))
#                 return 
#         n = round(10**6/min(sublist))

   

# myLoop()

# 382.6573996543884 s ΑΚΟΥ ΑΚΟΥ