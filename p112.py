
# def num_type(n):
#     n = str(n)
#     if n[0]<n[1]:
#         return 'inc'
#     elif n[0]>n[1]:
#         return 'dec'
#     else:
#         return num_type(str(n)[1:])

inc_count = 0

for i in range(1, 10):
    for j in range(i, 10):
        # for k in range(j, 10):
            # print(''.join([str(i),str(j),str(k)]))
        inc_count += 1

dec_count = 0

for i in range(9, 1, -1):
    for j in range(i, 1, -1):
        # for k in range(j, 1, -1):
        dec_count += 1

print(1000-(inc_count + dec_count))