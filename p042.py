# 06/07/19

import math

file = open('p042_words.txt','r')
words = file.read()
words = words.split(',')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_number = [ord(i)-64 for i in alphabet]

def triangle_test(n):
	if 0.5*((math.sqrt(1+8*n))-1) % 1 == 0:
		return True

triangle_words = 0

for word in words:
	s = 0
	l = list(word)[1:len(word)-1]
	for letter in l:
		s+=ord(letter)-64
	if triangle_test(s):
		triangle_words += 1

print(triangle_words)

# print(max(words))
#
# words[1] = "YOUTH"
#
# print(list(words[1])[:8])
# s = 0
#
# l = list(words[1])[:8]
#
# for letter in l:
# 	s+=ord(letter)-64
#
# 	if s in triangle_numbers:
# 		triangle_words+=1
#
# print(triangle_words)