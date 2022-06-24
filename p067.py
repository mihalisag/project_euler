# 29/09/19

# Βλέπε p18 (copy-paste)

file = open('p067_triangle.txt', 'r')
numbers = file.readlines()

numbers = [i.split() for i in numbers]
rows = len(numbers)

# numbers = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# rows = len(numbers)


a = 1
d = {}

for list in numbers:
	for number in list:
		d[a] = number
		a += 1

for key in d.keys():
	d[key] = int(d[key])

# print(d)
# print(numbers)

row = rows - 2


def key_finder(index, row, list):
	s = 0
	for k in range(row):
		s += len(list[k])
	s += index + 1

	return s


while row >= 0:
	row_length = len(numbers[row])
	temp_list = []
	for index in range(row_length):
		key = key_finder(index, row, numbers)
		# print(key)
		m = max(d[key] + d[key + row_length], d[key] + d[key + row_length + 1])
		d[key] = m  # αυτό είχα ξεχάσει
		temp_list.append(m)
	numbers[row] = temp_list
	# print(numbers)
	row -= 1

print(numbers)