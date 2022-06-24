# 25/06/19


for i in range(1,16):
    digits = [int(i) for i in str(2**i)]
    print('2^'+str(i)+'  '+str(2**i)+'  '+str(sum(digits)))

digits = [int(i) for i in str(2**1000)]
print(sum(digits))
