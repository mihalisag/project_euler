# 28/09/19

def number_of_partitions(n):

	partitions = (n+1)*[0]
	partitions[0] = 1

	for i in list(range(1, n)):
		for j in range(i, n+1):

			print((i, j), partitions)
			partitions[j] += partitions[j-i]


	return partitions

if __name__ == '__main__':

	a = number_of_partitions(5)
	print(a)

	# key = True
	# k = 10

	# while key:
	# 	a = number_of_partitions(k)
	# 	if a%2 == 1:
	# 		if (a+1) % 10**6 == 0:
	# 			print(k)
	# 			key = False
	# 	k+=1

