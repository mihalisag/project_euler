# 11/07/19


for n in range(10,100):
    for d in range(n,100):
        fraction = n/d
        n_list = [int(i) for i in str(n)]
        d_list = [int(i) for i in str(d)]
        nd_list = [n_list,d_list]
        common = set(n_list).intersection(set(d_list))

        if 0 not in common and common != set() :
            common = common.pop()
            n_index = n_list.index(common)
            d_index = d_list.index(common)
            del n_list[n_index]
            del d_list[d_index]
            n_new = n_list[0]
            d_new = d_list[0]
            
            if  n != d and d_new != 0 and fraction == n_new/d_new:
                print([n,d])

# [n,d] = list(map(int(str()),fraction))
# [16, 64]
# [19, 95]
# [26, 65]
# [49, 98]
# [64, 16]
# [65, 26]
# [95, 19]
# [98, 49]