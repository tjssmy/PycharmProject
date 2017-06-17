import cmath

r = 1
phi = 1.2

z1 = r*cmath.exp(1j*phi)
z2 = 1 + 5j

z3 = z1*z2

print(z1, z2, z3)
