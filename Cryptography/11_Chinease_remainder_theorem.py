"""
Chinease Remainder Thoerem
"""
print("For 3 Equations of the form: x = A mod B")
print("Enter values of A1, A2, A3:  ")
A = []
m = []
M = 1
Z = []
Y = []
x = 0
for i in range(3):
	A.append(int(input()))
print("Enter values of m1, m2, m3:  ")
m = []
for i in range(3):
	m.append(int(input()))
	M = M * m[i]

print("\nEquations : ");
for i in range(3):
	print("x = ",A[i]," mod ",m[i])
	Z.append(int(M/m[i]))
	y = 1
	while( (Z[i] * y ) % m[i] != 1):
		y += 1
		if y >= 99999:
			print("Unable to compute y for this equation. Exiting...")
			exit()
	Y.append(y)
	x = x + (A[i] * Z[i] * Y[i] )
x = x % M
print("X = ",x)	

