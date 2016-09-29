"""
Miller Rabin Algorithm
"""
N = int(input("Enter value of N:  "))
if (N < 3 or (N % 2) == 0) :
	print(N," is composite.")
	exit()
q = N - 1
k = 0
while q % 2 == 0 :
	k += 1
	q = int(q / 2)
	print(k," ",q)
a = 2
print("N = ",N,",k = ",k,",q = ",q,",a = ",a,".")

if pow(a,q) % N == 1 :
	print("In conclusive.")
	exit()
for j in range(k) :
	if (pow(a, pow(2,j)*q) % N) == (N-1) :
		print("In conclusive.")
		exit()
print("Composite.")
