# 07/07/21

def repetend_calc(n):

    if len(str(1/n)) < 19:
        print('skata')
        return str(1/n)[2:]


    else:
        rem = 1
        repetend = str(10//n)
        key = True
        index = 0

        while key:

            rem = (10*rem) % n
            div = (10*rem) // n

            if str(div) in repetend:

                a = str(1/n)[index + 3:index + 3 + len(repetend)]

                if a == repetend:
                    print(a)
                    key = False

                else:
                    return 'irrational'

            else:
                repetend += str(div)
                index += 1

        if repetend[-1] == '0':
            repetend = repetend[:-1]

    return repetend




# eps = 4.440892098500626e-16








#  import math
# l = []


# for d in range(1,10):
#     c = 0
#     r = 1/d
#     a = r
#     key = True
#     while key :
#         a = 10*a
#         c+=1
#         rel = a-r
#         if math.ceil(rel)-rel < 0.1:
#             key = False
#             l.append([d,c])


# print(l)