# 08/07/19


for number in range(1,10**6):
    l1 = set(list(str(number)))
    l2 = set(list(str(2*number)))
    if l2 == l1 :
        l3 = set(list(str(3 * number)))
        if l3 == l2:
            l4 = set(list(str(4 * number)))
            if l4 == l3:
                l5 = set(list(str(5 * number)))
                if l5 == l4:
                    l6 = set(list(str(6 * number)))
                    if l6 == l5: print(number)