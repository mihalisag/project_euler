# 19/08/19

# Βλέπε τετράδιο για προηγούμενα
from math import sqrt

n = 10**12

key = True

while key:

    d = 1+2*n*(n-1)

    if sqrt(d) % 1 == 0:
        key = False
        print([n, d])

    n += 1

b = (1+sqrt(d))/2

print(b)



# [4, 25]
# [21, 841]
# [120, 28561]
# [697, 970225]
# [4060, 32959081]
# [23661, 1119638521]
# [137904, 38034750625]
# [803761, 1292061882721]
# [4684660, 43892069261881]
# [27304197, 1491038293021225]
# [65918162, 8690408031080165]