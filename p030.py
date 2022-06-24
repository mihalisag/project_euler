# 20/06/19

l = []

for n in range(1,1000000):
    digits = [(int(i))**5 for i in str(n)]
    if sum(digits)==n:
        l+=[n]

print(sum(l))
