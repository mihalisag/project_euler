# 20/07/20

from day import day as day

count =0

for month in range(1,13):
    for year in range(1901,2001):
        date = '1/'+str(month)+'/'+str(year)
        if day(date) == 0: count+=1

print(count)