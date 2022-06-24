
def leap_check(year): return (year%400==0) or ((year%4==0) and (year%100!=0))
	

def day(p):
	p = p.split('/')
	date = [int(i) for i in p]

	# week = {0:'Κυριακή',1:'Δευτέρα',2:'Τρίτη',3:'Τετάρτη',4:'Πέμπτη',5:'Παρασκευή',6:'Σάββατο',7:'Κυριακή'}

	month = {1:6 , 2:2 , 3:2 ,4:5 ,5:0 ,6:3 ,7:5, 8:1, 9:4, 10:6 , 11:2, 12:4}

	d,m,y = date	
	
	y1 = y%100
	y_code = (y1//4 + y1)%7

	if leap_check(y):
		month[1] = 5
		month[2] = 1

	if 1900 <= y <= 1999:
		y_code += 1
	elif 1800 <= y <= 1899:
		y_code += 3
	elif 2100 <= y <= 2199:
		y_code += 5

	code = (month[m] + d + y_code)%7

	# print('Η μέρα που πέφτει ειναι '+ week[code])
	return code