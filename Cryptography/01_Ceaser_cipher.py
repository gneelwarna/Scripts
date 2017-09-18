#Implementation of Ceaser Cipher Algorithm.
alpha_dict1 = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,
 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21,
 'w':22, 'x':23, 'y':24, 'z':25}
alpha_dict2 = {}
alpha_dict2 = dict((v,k) for k,v  in alpha_dict1.items())
flag = choice = 0

while(choice<3):
	print("\n1. Plain Text to Cipher Text\n2. Cipher Text to Plain Text\n3. Exit\nEnter your choice: ")
	choice = int(input())
	if choice == 1:		#PLAIN TEXT TO CIPHER TEXT
		#Input key from user
		key = int(input("Enter KEY for Ceaser Cipher: "))
		if key >25:
			key = key % 26
		PT = input("Enter plain text:   \t")
		CT = []	
		for ch in PT:
			if ch.isalpha():
				CT.append(alpha_dict2[(alpha_dict1[ch.lower()] +key) % 26])
			else:
				CT.append(ch)
		CT = ''.join(CT)
		print("Ceaser Cipher text: \t",CT)
		flag = 1
	elif choice == 2:	#CIPHER TEXT TO PLAIN TEXT
		if flag == 1:
			PT = []
			for ch in CT:
				if ch.isalpha():
					PT.append(alpha_dict2[(alpha_dict1[ch.lower()] - key) % 26])
				else:
					PT.append(ch)
			print("Plain Text:  ", ''.join(PT))
	elif choice == 3:
		choice = 3
	else:
		print("Enter correct choice.")
