# Implementation of Monoalphabetic Cipher Algorithm.

alpha_dict1 = {'a':'b', 'b':'a', 'c':'d', 'd':'c', 'e':'f', 'f':'e',
 'g':'h', 'h':'g', 'i':'j', 'j':'i', 'k':'l', 'l':'k', 'm':'n', 'n':'m',
 'o':'p', 'p':'o', 'q':'r', 'r':'q', 's':'t', 't':'s', 'u':'v', 'v':'u',
 'w':'x', 'x':'w', 'y':'z', 'z':'y'}

alpha_dict2 = {}
alpha_dict2 = dict((v,k) for k,v  in alpha_dict1.items())
flag = choice = 0

while(choice<3):
	print("\n1. Plain Text to Cipher Text\n2. Cipher Text to Plain Text\n3. Exit\nEnter your choice: ")
	choice = int(input())
	if choice == 1:         #PLAIN TEXT TO CIPHER TEXT
		PT = input("Enter plain text:    ")
		CT = []
		for ch in PT:
			if ch.isalpha():
				CT.append(alpha_dict1[ch.lower()])
			else:
				CT.append(ch)
		CT = ''.join(CT)
		print("Cipher text: \t",CT)
		flag = 1
	elif choice == 2:       #CIPHER TEXT TO PLAIN TEXT
		if flag == 1:
			PT = []
			for ch in CT:
				if ch.isalpha():
					PT.append(alpha_dict2[ch.lower()])
				else:
					PT.append(ch)
			print("Plain Text:  \t", ''.join(PT))
	elif choice == 3:
		choice = 3
	else:
		print("Enter correct choice.")


