""" Matrix Method """
from numpy import matrix
import numpy
N = int(input("Enter Square Matrix (NxN) Size:  "))

key = []
print("Enter key values:  ")
i = 0
while i < N:
	ip = int(input())
	if ip <= N and ip > 0 and ip not in key:
		key.append(ip)
		i = i + 1
	else:
		print("Wrong key value. Enter again.")
print("KEY = ",key)
Transpose = int(input("Enter no. of transpositions :  "))

choice = 0
while choice !=3 :
	choice = int(input("\n1. Plain Text to Cipher Text.\n2. Cipher Text to Plain Text\n3. Exit\n   Enter your choice:  "))
	if choice == 1:
		PT = input("Enter plain text: ")
		if len(PT) % N == 0:
			row_num = int(len(PT)/N)
		else:
			row_num = int(len(PT)/N + 1)

		T = 1
		while T <= Transpose :
			print("\nStage ",T," Transposition  :")
			i = j = 0
			row = []
			m = []
			while i < len(PT):
				row.append(PT[i])
				j = j + 1
				if j == N:
					j = 0
					m.append(row)
					row = []
				i = i + 1
			if j > 0:
				while j < N:
					row.append('x')
					j = j + 1
				m.append(row)
				print("ROW = ",row)
			print("\nMatrix :  ",numpy.matrix(m))

			""" Transpose """
			i = 0
			CT = []
			while i < N:
				j = 0
				while j < row_num:
					CT.append(  m[j] [key.index(i+1)]  )
					j = j + 1
				i = i + 1
			PT = ''.join(CT)
			print("\nOutput Text :  ",PT)
			T = T + 1
		print("\nCipher Text :  ",''.join(CT))
	elif choice == 2:
		""" Cipher To Plain Text """
		CT = input("Enter Cipher Text :  ")
		if len(CT) % N == 0:
			row_num = int(len(CT)/N)
		else:
			row_num = int(len(CT)/N + 1)

		T = 1
		while T <= Transpose :
			print("\nStage ",T," Reverse Transposition  :")
			i = j = 0
			col = []
			m = []
			while i < len(CT):
				col.append(CT[i])
				j = j + 1
				if j == row_num:
					j = 0
					m.append(col)
					col = []
				i = i + 1
			if j > 0:
				while j < N:
					col.append('x')
					j = j + 1
				m.append(col)
			print("\nMatrix :  ",numpy.matrix(m).T)

			""" Transpose """
			i = 0
			PT = []
			while i < row_num:
				j = 0
				while j < N:
					PT.append(  m[key[j] - 1] [i]  )
					j = j + 1
				i = i + 1
			CT = ''.join(PT)
			print("Output Text :  ",CT)
			T = T + 1
		print("\nPlain Text :  ",''.join(PT))
	elif choice == 3:
		break
	else:
		print("\nWrong choice.")

