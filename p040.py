# 01/07/19

i = 1
number = ''

while len(number)<=10**6+1:
	number+=str(i)
	i+=1

number = '0'+number

prod = 1

for i in range(7):
	prod *= int(number[10**i])

print(prod)