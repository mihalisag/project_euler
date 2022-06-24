# 04/07/19

import math

def eucl_norm(n): return math.sqrt(n[0]**2+n[1]**2)

def quadrant(n):

	[x,y] = [n[0],n[1]]

	if x>0 and y>0: return 1
	elif x<0 and y>0: return 2
	elif x<0 and y<0: return 3
	elif x>0 and y<0: return 4

def area_of_triangle(l): # l =[A,B,C]
	[a,b,c] = [l[0],l[1],l[2]]
	[[xa,ya],[xb,yb],[xc,yc]] = [[a[0],a[1]],[b[0],b[1]],[c[0],c[1]]]

	return 0.5*abs((xa*yb-xa*yc+xb*yc-xb*ya+xc*ya-xc*yb))

def dot_product(a,b): return a[0]*b[0]+a[1]*b[1]

def angle_of_vectors(a,b): return math.acos((dot_product(a,b))/(eucl_norm(a)*eucl_norm(b)))

def check_triangle(l): # l = [v1,v2,v3]

	l.sort()
	[v1,v2,v3] = [l[0],l[1],l[2]]

	if quadrant(v1) == quadrant(v2) == quadrant(v3): return False
	else:
		angle_1 = angle_of_vectors(v1,v2)
		angle_2 = angle_of_vectors(v1,v3)
		angle_3 = angle_of_vectors(v2,v3)
		print(angle_1+angle_2+angle_3)

		if angle_1+angle_2+angle_3==2*math.pi:
			return True
		else: return False

file = open('p102_triangles.txt','r')
coordinates = file.read()

coordinates = coordinates.split('\n')
triades = []

for i in coordinates:
	i = i.split(',')
	triades.append(i)

triades = triades[:len(triades)-1]

o = [0,0]
count = 0

for triada in triades:
	l = [[int(triada[0]),int(triada[1])],[int(triada[2]),int(triada[3])],[int(triada[4]),int(triada[5])]]
	[a,b,c] = [l[0],l[1],l[2]]
	area_big = area_of_triangle(l)
	area_1 = area_of_triangle([o,b,c])
	area_2 =  area_of_triangle([o,a,c])
	area_3 = area_of_triangle([o,a,b])

	if area_1+area_2+area_3 == area_big:
		count+=1

print(count)


