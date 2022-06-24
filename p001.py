# 24/02/19


def sum_multiples(n):

    s = 0

    for i in range(n):
        if i%3==0 or i%5==0:
            s = s + i

    print(s)
