# 26/06/19

def frac(number,frac): # frac = [NUMERATOR,DENOMINATOR]

    numerator_new = number*frac[1]+frac[0]
    return [numerator_new,frac[1]]

def inv(l): # 1/(a/b) = b/a

    return [l[1],l[0]]


if __name__ == '__main__':

    k_n = [3, 2]
    count = 0

    for i in range(1, 1000):
        k_n = frac(1, inv(frac(1,k_n)))

        if len(str(k_n[0]))>len(str(k_n[1])):
            count+=1

    print(count)



