import math, random, time
from functools import reduce

start = time.time()

# def squares(n):
#
#     triple_list = []
#     i = 1
#
#     while i**2 <= n:
#         s.append(i**2)
#         i += 1
#
#     return s


def triangle_inequality(a, b, c):

    if a + c > b > abs(a - c):
        if b + c > a > abs(b - c):
            if a + b > c > abs(a - b):
                return True
    return False


def gcd_of(l):
    x = reduce(math.gcd, l)
    return x


def ntl(multiplier, l): return [multiplier*i for i in l]

def list_of_multiples(times,zlist):

    return_list = [zlist]

    for mul in range(2, times+1):
        return_list.append(ntl(mul, zlist))

    return return_list

triple_list = []
i = 2
perimeter = 0
perimeter_max = 10**5


while perimeter <= perimeter_max:

    b_squared = i**2
    b = i
    multiplier = 1
    # print(b)


    for a in range(b, 1, -1):

        # print(a)
        if b_squared % a == 0:

            c = int(b_squared/a)

            if c > a:

                triple = [a, b, c]

                if triple not in triple_list and gcd_of(triple) == 1:

                    if b < c and triangle_inequality(a, b, c):

                        lf = triple
                        number = perimeter_max//sum(lf)
                        # print([a,b,c])
                        perimeter = sum(triple)
                        key = True

                        while key:

                            triple = ntl(multiplier, lf)
                            perimeter_loop = sum(triple)

                            if perimeter_loop > perimeter_max:

                                key = False

                            else:

                                # print(triple)
                                triple_list.append(triple)
                                multiplier += 1

                        # lf = triple
                        # number = perimeter_max//sum(lf)
                        # # print([a,b,c])
                        # perimeter = sum(triple)
                        # multiples_list = list_of_multiples(number,triple)
                        #
                        # triple_list.append(multiples_list)



    i += 1


dif_len = len(triple_list)
end_len = dif_len + perimeter_max//3
end = time.time()

print(end_len,  end-start)


# while perimeter <= perimeter_max:
#
#     b_squared = i**2
#     b = i
#
#     for a in range(b_squared,1,-1):
#         if b_squared%a == 0:
#             c = int(b_squared/a)
#             triple = set([a,b,c])
#             if triple not in triple_list:
#                 if a!=c and a!= b and b!=c and triangle_inequality(a,b,c):
#
#                     perimeter = sum(triple)
#                     print(triple)
#                     triple_list.append(triple)
#     i += 1


# while key:
#
#     triple = ntl(multiplier, lf)
#     perimeter_loop = sum(triple)
#
#     if perimeter_loop > perimeter_max:
#
#         key = False
#
#     else:
#
#         # print(triple)
#         triple_list.append(triple)
#         multiplier += 1