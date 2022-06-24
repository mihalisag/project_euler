# 17/06/19

from fibo import Fibonacci1
import math

i = 100

number_of_digits = 1

while number_of_digits <= 1000:
    number_of_digits = math.floor(math.log10(Fibonacci1(i)[0]))+1
    i+=1

print(i)
