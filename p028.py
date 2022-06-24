# 17/07/19

end = 1
s = 1

for i in range(3,1003,2):
    start = end+(i-1)
    end = start+3*(i-1)
    s+=2*(start+end)

print(s)
