# 23/06/19

file = open('p22_names.txt','r')
names = file.read()
names = names.split(',')

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# letter_number = [ord(i)-64 for i in alphabet]

names = [i.replace('"','') for i in names]
names.sort()

value = 0

for string in names:
    sum = 0
    for j in string:
        sum+=ord(j)-64

    value += (sum*(names.index(string)+1))


print(value)

#print(letter_number)
