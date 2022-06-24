# 01/07/19

i = 0
max_set= set()

for n in range(1,10**6):
    m = n
    seq = set()

    if n in max_set:
        max_set = max_set.union(seq)

    while n > 1:

        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1

        seq.add(n)

        if len(seq)>len(max_set):
            max_set = seq
            max_number = m


print('max = ',max_number)
