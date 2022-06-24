from math import sqrt
import time

start = time.time()
x = 1
a_minus = 1
l_plus = []
l_minus = []
# for a in range(1,10**7):

while 3*a_minus + 1 < (10**9):


	# t = ((a+1)/4)*sqrt(((3*a + 1)*(a-1)))

	a_plus = (1+sqrt(3*(x**2)+4))/3

	if a_plus % 1 == 0 :

		t_plus = ((a_plus + 1) / 4) * sqrt(((3 * a_plus + 1) * (a_plus - 1)))

		if t_plus % 1 == 0:

			l_plus.append(a_plus)

	a_minus = (-1 + sqrt(3 * (x ** 2) + 4)) / 3

	if a_minus % 1 == 0:

		t_minus = ((a_minus - 1) / 4) * sqrt(((3 * a_minus - 1) * (a_minus + 1)))

		if t_minus % 1 == 0:

			l_minus.append(a_minus)

	# if t%1 == 0 :
	# 	l.append(a)

	x+=1
	# a+=1

def p_plus(n): return 3*n + 1
def p_minus(n): return 3*n - 1


p_plus_list = list(map(p_plus,l_plus))
p_minus_list = list(map(p_minus,l_minus))
total_sum = sum(p_plus_list)+sum(p_minus_list)

end = time.time() - start

print('+: ',l_plus,p_plus_list)
print('-: ',l_minus,p_minus_list)
print(end,'s')
print('Total sum of perimeters =',total_sum)

# 5.0
# 65.0
# 901.0
# 12545.0
# 174725.0
# 2433601.0
# 33895685.0
# 63250209.0
# 92604733.0
# 121.49500703811646 s

# +:  [5.0, 65.0, 901.0, 12545.0, 174725.0, 2433601.0, 33895685.0, 92604733.0, 114093736.0, 143448260.0, 172802784.0, 180668305.0, 194291787.0, 202157308.0, 223646311.0, 231511832.0, 253000835.0, 260866356.0, 274489838.0, 282355359.0, 290220880.0, 303844362.0, 311709883.0, 333198886.0] [16.0, 196.0, 2704.0, 37636.0, 524176.0, 7300804.0, 101687056.0, 277814200.0, 342281209.0, 430344781.0, 518408353.0, 542004916.0, 582875362.0, 606471925.0, 670938934.0, 694535497.0, 759002506.0, 782599069.0, 823469515.0, 847066078.0, 870662641.0, 911533087.0, 935129650.0, 999596659.0]
# -:  [1.0, 17.0, 241.0, 3361.0, 46817.0, 652081.0, 9082321.0, 97145893.0, 126500417.0, 155854941.0, 185209465.0, 206698468.0, 214563989.0, 228187471.0, 236052992.0, 265407516.0, 286896519.0, 316251043.0] [2.0, 50.0, 722.0, 10082.0, 140450.0, 1956242.0, 27246962.0, 291437678.0, 379501250.0, 467564822.0, 555628394.0, 620095403.0, 643691966.0, 684562412.0, 708158975.0, 796222547.0, 860689556.0, 948753128.0]
# 837.8356318473816 s
# Total sum of perimeters = 18689947611.0