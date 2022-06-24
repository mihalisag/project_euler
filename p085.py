import math

rec_num = lambda n, m: n*(n+1)*m*(m+1) / 4 # Returns number of rectangles that an n x m grid contains

l = math.inf

for i in range(1, 100):
    for j in range(i, 100):
        d = abs(2_000_000 - rec_num(i, j))
        print(d)
        if d < l:
            l = d
            n, m = [i, j]

print(n, m)
