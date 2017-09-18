'''POLYALPHABETIC CIPHER ALGORITHM'''

key = str(input("ENTER KEY: "))


choice = 0
while(choice !=3):
	print("\n1. PLAIN TEXT TO CIPHER TEXT\n2. CIPHER TEXT TO PLAIN TEXT\n3. EXIT")
	choice = int(input("ENTER CHOICE:  "))
	if choice == 1:
		PT = input("ENTER PLAIN TEXT: ").lower()

		i = 0
		CT = []
		while (i < len(PT)):
			if PT[i].isalpha() :
				CT.append( chr( (((ord(PT[i])-97) + (ord(key[ (i%len(key)) ])-97 ))% 26 )+97 ) )
			else:
				CT.append('?')
			i = i + 1
		print("CIPHER TEXT: ",''.join(CT))
	elif choice == 2:
		CT = input("ENTER CIPHER TEXT: ").lower()
		i = 0
		PT = []
		while (i < len(CT)):
			if CT[i].isalpha() :
				PT.append( chr( (((ord(CT[i])-97) - (ord(key[ (i%len(key)) ])-97))% 26 )+97 )  )
			else:
				PT.append('?')
			i = i + 1 
		print("PLAIN TEXT: ",''.join(PT))
	elif choice == 3:
		break
	else:
		print("WRONG CHOICE.\n")





