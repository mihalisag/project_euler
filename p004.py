# 03/03/19


i = 316

o = 0
l = ''
s = 0

while i<999:
    for j in range(317,1000):
        o = i*j
        t = str(i*j)
        k = list(t)
        a = k[3:]
        a.reverse()

        if k[:3] == a:
            if o > s:
                s = o
                l = str(i)+'x'+str(j) 


    i+=1

print(s,l)
