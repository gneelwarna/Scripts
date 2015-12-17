"""
Euclidean Algorithm
"""
def euclid(l, s):
	r = l % s
	if r > 0:
		return euclid(s, r)
	else:
		return s

l = int(input("Enter num1: "))
s = int(input("Enter num2: "))
if(l < s):
	l,s=s,l
print("Large number: ",l,"\nSmall number: ",s)
gcd = euclid(l, s)
print("gcd(",l,", ",s,") = ",gcd)
