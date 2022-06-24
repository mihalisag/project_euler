# 01/07/19

# Monopoly

import random

pos = 0
draw = 0
double_count = 0

n = 10**6

cc = [0,10]+14*['else']
ch = [0,10,11,24,39,5,'railway','railway','utility','back']+6*['else']

squares = {}
for i in range(40): squares[str(i)] = 0

for i in range(1,n):

	dice_1 = random.randint(1,6)
	dice_2 = random.randint(1,6)

	if dice_1 == dice_2:
		double_count += 1
	else:
		double_count = 0

	if double_count == 3:
		pos = 10

	dice = dice_1 + dice_2
	pos = (pos + dice) % 40

	# CC
	if pos in [2,17,33]:
		draw = random.randint(0,len(cc)-1)
		if cc[draw] != 'else':
			pos = cc[draw]

	# CH
	if pos in [7,22,36]:
		draw = random.randint(0,len(ch)-1)

		if ch[draw] == 'railway':
			if pos == 7 :
				pos = 15
			elif pos == 22 :
				pos = 25
			elif pos == 36 :
				pos = 5

		elif ch[draw] == 'utility':
			if pos == 7 or pos == 36 : pos = 12
			else: pos = 28

		elif ch[draw] == 'back':
			pos = pos - 3

		elif ch[draw] != 'else' :
			pos = ch[draw]

	# JAIL
	if pos == 30: pos = 10

	squares[str(pos)]+=1

values = list(squares.values())
values.sort(reverse=True)

for i in values:
	a = list(squares.keys())[list(squares.values()).index(i)]
	b = str((i/n)*100)+'%'
	print(a,b)





# m_key = (list(squares.keys())[list(squares.values()).index(max(squares.values()))])





