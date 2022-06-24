# 16/09/20

import sympy as sp
import numpy as np

import time

start = time.time()

# Ορίζει τη μεταβλητή
n = sp.symbols('n')

# Αριθμητική συνάρτηση
# u = sp.Poly(n ** 3)
u = sp.Poly(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10)

degree = u.degree()
alphabet = [chr(i) for i in range(97, 123)]

# Υπολογίζει τη γραμμή στον πίνακα για το σύστημα των συντελεστών
def coef(degree, n): return [n**i for i in range(degree)][::-1]

# Υπολογίζει τον πίνακα
def system(variables): return np.array([np.array(coef(variables, n)) for n in range(1, variables + 1)])

# Υπολογίζει το πολυώνυμο OP
def op(variables):

    A = system(variables)
    b = np.array([u(i) for i in range(1, variables + 1)]).astype('int64')  

    x = np.linalg.solve(A, b)
    monom = [n ** i for i in range(variables)][::-1]

    op = sp.Poly(np.dot(x, monom))
    
    return op

bop_list = [op(i)(i + 1) for i in range(2, degree + 1)]
bop_list.insert(0, 1)
print(sum((bop_list)))
print(time.time()- start, 's')
    
