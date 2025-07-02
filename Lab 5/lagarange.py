# to find the lagarange interpolation polynomial for the given data

import numpy as np
import sympy as sp

n = int(input("Enter the no. of data: "))

X = np.array(list(map(float, input("Enter all x-data: ").split())))
y = np.array(list(map(float, input("Enter all y-data: ").split())))

xp = float(input("Enter point to interpolate: "))

x = sp.symbols('x')

poly = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if(j!=i):
            lf *= (x - X[j])/(X[i]-X[j])    
    poly += lf * y[i]

poly = sp.simplify(poly)

print("\nThe Lagarange polynomial is:\n", poly)

int_val = poly.subs(x, xp)
print(f"The interpolated value at x = {xp} is {int_val}")
