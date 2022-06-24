# 20/06/19

import time
start = time.time()

l = set()

for i in range(2,101):
     for j in range(2,101):
         l.add(i**j)

print(len(l),time.time()-start)
