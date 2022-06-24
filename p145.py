import time

start = time.time()
#na do auto pou to kanei lista me 1 kai 0

def odd_check(n):

    for i in n:
        if int(i)%2==0:
            return False

    return True

count = 0
b = 1000


for i in range(1,b):

    key = True
    index = 0
    number = str(i)


    middle = len(number)//2


    while index<=middle:
        if (int(number[index])+int(number[-1-index]))%2 == 0:
            index = middle+2

        index+=1

    if index == middle+1:
        count+=1


    # percentage = 100*i/b
    # print(percentage)

end = time.time()-start
print(count,end)








# even = [0,2,4,6,8]
# odd = [1,3,5,7,9]
# l = [even,odd]

# for i in range(1,101):
#     first = str(i)
#
#     if i%2==1:
#         for last in even:
#             number = first+str(last)
#             print(number)
#     else:
#         for last in odd:
#             number = first + str(last)
#             print(number)


# reverse = int(number)+int(number[::-1])
# g = list(map(int,(str(reverse))))

#
# if number[-1] != '0' and (int(number[0]) + int(number[-1])) % 2 == 1:
#     reverse = int(number) + int(number[::-1])
#     if odd_check(str(reverse)):
#         count += 1