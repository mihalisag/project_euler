# 22/06/19

def product_list(list):
    p = 1
    for i in list:
        p *= i
    return p

file = open('p8_text.txt','r')
numbers = file.read()
numbers = [int(i) for i in numbers if i != '\n']

max_product = 1
i = 0

while i<=len(numbers)-13-1:
    product = product_list(numbers[i:i+13])
    if product>max_product:
        max_product = product
    i+=1

print(max_product)
