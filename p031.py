# 28/09/19

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = (target+1) * [0]
ways[0] = 1

for coin in coins:
	for j in range(coin, target+1): # j = συνολικά λεπτά
		ways[j] += ways[j - coin]
	# print(ways)
print(ways[-1])

# for i in range(len(coins)):
# 	for j in range(coins[i], target+1):
# 		ways[j] += ways[j - coins[i]]


# coins = [100,50,20,10,5,2,1]
#
# list_max_times  = [2,4,10,20,40,100]
# list_max_times  = [2,4,10,20,40,100]
# ways = 0
#
# for a in range(0,3):
# 	for b in range(0,5):
# 		for c in range(0,11):
# 			for d in range(0, 21):
# 				for e in range(0, 41):
# 					for f in range(0, 101):
# 						ways += 200-(a*100+b*50+c*20+d*10+e*5+f*2)
#
# print(ways+1)
#
# # # [2,4,10,20,40,100]
# # list_of_coefficients = 7*[]
# # # [0,0,0,0,0,0,0]
# #
# # i=0
# # j=0
# #
# # while 200-inner_prod(list_of_coefficients,coins)>0:
# #     while j<=6:
# #         list_of_coefficients(j) += 1
# #         j+=1
# #     j = 0
