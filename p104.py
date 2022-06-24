from fibo import Fibonacci1

key = True
i = 1

while key:

    f = Fibonacci1(i)[0]

    digits = list(map(int, str(f)))
    number_of_digits = len(digits)

    # if set(digits[number_of_digits-9:]) == (set([1,2,3,4,5,6,7,8,9])):
    if set(digits[:3]) == (set([1,2,3])):
        if set(digits[number_of_digits-2:]) == (set([1,2,3])):

            print(f,i)
            key = False

    i+=1



# #problem 104
# import time
# import fibo as f
#
# start = time.time()
#
# i = 1
# d = ['1','2','3','4','5','6','7','8','9']
# key = True
#
# while key:
#
#     t = str(f.Fibonacci1(i))
#     print(i)
#
#     if sorted(list(t[:9])) == d and sorted(list(t[len(t)-9:])) == d :
#         key = False
#
#     i+=1
#
#
# print('The '+str(i)+'th Fibonacci number is the requested number.')
# print(t)
# print('Time = '+str(time.time()-start)+'s.')
