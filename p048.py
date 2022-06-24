# 17/06/19

i = 1
sum = 0

while i<=1000:
    sum += (i**i)%(10**10)
    i+=1

print(sum%(10**10))
