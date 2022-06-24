# 13/08/19

def product_list(list):
    p = 1
    for i in list:
        p *= i
    return p

file = open('p13_text.txt','r')
numbers = file.read()
# numbers = [int(i) for i in numbers if i != '\n']

# s1 = str(sum(numbers))
# print(s1[:10])
# print(numbers[:51])

s = int(numbers[:51])
a = 0

for i in range(99):
    a += 51
    s += int(numbers[a:51+a])

print(s)



