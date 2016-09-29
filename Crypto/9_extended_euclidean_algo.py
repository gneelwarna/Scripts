"""
Extended Euclidean Algorithm
"""
def ex_euclid(A, B):
	if B[2] == 0:
		print(A[2])
		return 1
	elif B[2] == 1:
		print("1")
		return 1
	T = [1,1,1]
	Q = int(A[2]/B[2])
	for i in range(0,3):
		T[i] = A[i] - Q*B[i]
	ex_euclid(B, T)

l = int(input("Enter number1: "))
s = int(input("Enter number2: "))
if l < s:
	l,s=s,l
print("Large number: ",l,"\nSmall number: ",s)
A = [1, 0, l]
B = [0, 1, s]
print("gcd(",l,", ",s,") = ")
ex_euclid(A, B)
