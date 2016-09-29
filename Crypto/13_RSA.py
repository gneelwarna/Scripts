#RSA Algorithm
def euclid(l, s):
	r = l % s
	if r > 0:
		return euclid(s, r)
	else:
		return s


p = int(input("Enter Prime No #1 :  "))
q = int(input("Enter Prime No #2 :  "))
if(q < p):
        q,p=p,q
n = p * q
print("n = ",n)
phi_n = (p-1) * (q-1)
print("Phi_n = ",phi_n)

e = 2
while e<phi_n:
	ans = euclid(phi_n, e)
	if ans == 1:
		break
	e += 1
print("e = ",e)
d = 2
while d <= 9999:
	if ((d *e) % phi_n) == 1:
		break
	d += 1
print("d = ",d)

print("Public Key  (e,n) = (",e,", ",n,")")
print("Private Key (d,n) = (",d,", ",n,")")
m = 0
c = 0
ch = 0
print("\n1. Encrypt\n2. Decrypt\n3. Exit")
while ch != 3:
	#print("\n1. Encrypt\n2. Decrypt\n3. Exit")
	ch = int(input("Enter your choice: "))
	if ch == 1:
		m = int(input("Enter value of M = "))
		c = (m**d) % n
		print("Cipher Value [c] = ",c)
	elif ch == 2:
		c = int(input("Enter value of C = "))
		m = (c**e) % n
		print("Plain Value [m]  = ",m)
	elif ch == 3:
		print("Exiting...")
	else:
		print("Wrong choice")

