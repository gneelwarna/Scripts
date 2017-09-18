from numpy import matrix
from numpy import linalg
import numpy

print("#### HILL CIPHER ####")
N = int(input("Enter value for N for [Matrix[NxN] =  "))

m = numpy.zeros(shape=(N,N))
#print(m)
i = j = 0;
while i < N:
	j = 0
	while j < N:
		m[i][j]=int(input())
		j = j + 1
	i = i + 1
m = matrix( m )

"""Validation for Determinent is ZERO """
if  numpy.linalg.det(m) == 0:
	print("Matrix determinent is ZERO.\nExiting...")
	exit()

inv = m.I
print("Matrix is =  \n",m,"\n ","\nInverse matrix =  \n",inv,"\n\n")

choice = 0
while choice != 3:
	choice = int(input("\n\n1. Plain Text to Cipher Text \n2.Cipher Text to Plain Text \n3. Exit \n   Enter your choice:   "))
	if choice == 1:
		""" Get Plain Text """
		PT_num = []
		PT = str(input("Enter Plain Text:  ")).lower().replace(" ","")
		""" Plain Text validations """
		if not PT.isalpha():
			print("Wrong input! Please enter alphabets only.\nExiting...")
			exit()

		"""Convert PT into equivalent integers. """
		for ch in PT:
			PT_num.append(ord(ch)-97)
		org_len = len(PT_num)
		while len(PT_num) % N != 0:
			PT_num.append(120)

		""" Convert PT into CT """
		i = 0
		CT = []
		while i < len(PT_num)/N:
			j = 0
			P = []
			while j < N:
				P.append([PT_num[(i * N) + j]])
				j = j + 1
			P = matrix(P)
			C = m * P
			C = numpy.array(C).tolist()
			k = 0
			#print("\nC = ",C)
			while k < N:
				C[k] = chr( int(int(C[k][0]) % 26) + 97 )
				#print(k," = ",C[k])
				k = k + 1

			CT.extend(C)
			i = i + 1
		i = 0
		print("\nCipher Text :  ",''.join(CT))
	elif choice == 2:
		CT_num = []
		CT = str(input("Enter Cipher Text:  ")).lower().replace(" ","")
		if not CT.isalpha():
			print("Wrong input! Please enter alphabets only.\nExiting...")
			exit()
		"""Convert CT into equivalent intgers. """
		for ch in CT:
			CT_num.append(ord(ch)-97)
		org_len = len(CT_num)
		while len(CT_num) % N != 0:
			CT_num.append(120)
		print(CT_num)

		""" Convert CT into PT """
		i = 0
		PT = []
		while i < len(CT_num)/N:
			j = 0
			C = []
			while j < N:
				C.append([CT_num[(i * N) + j]])
				j = j + 1
			C = matrix(C)
			P = inv * C
			P = numpy.array(P).tolist()
			k = 0
			#print("\nP = ",P)
			while k < N:
				P[k] = chr( int(int(P[k][0]) % 26) + 97 )
				#print(k," = ",P[k])
				k = k + 1
			PT.extend(P)
			i = i + 1
		i = 0
		print("\nPlain Text :  ",''.join(PT))
	elif choice == 3:
		break;
	else:
		print("Wrong choice.")

