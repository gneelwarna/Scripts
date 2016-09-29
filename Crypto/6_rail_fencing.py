'''RAIL FENCING'''

slice_no = int(input("Enter Slicing number: "))
choice = 0
while(choice != 3) :
	print("\n1.PLAIN TEXT TO CIPHER TEXT\n2. CIPHER TEXT TO PLAIN TEXT\n3. EXIT")
	choice = int(input("ENTER CHOICE:  "))
	if choice == 1 :
		PT = input("ENTER PLAIN TEXT:  ")
		CT = []
		i = j = k = 0
		while(i < slice_no):
			j = 0
			while( (i+j) < len(PT) ):
				CT.append(PT[i+j])
				print(i," ",j," ",PT[i+j])
				j = j + slice_no
				k = k + 1
			i = i + 1
		print("CIPHER TEXT: ",''.join(CT))
	elif choice == 2:
		CT = input("ENTER CIPHER TEXT:  ")
		PT = []
		i = j = k = 0
		while(i < (len(CT)/slice_no) ):
			j = 0
			mod = int(len(CT) % slice_no)
			while( (i+j) < ( len(CT) ) ):
				print(i+j)
				PT.append(CT[i+j])
				print(i," ",j," ",CT[i+j])
				j = j + int(len(CT)/slice_no)
				if mod > 0:
					j = j + 1
					mod = mod - 1
				k = k + 1
			i = i + 1
		print("PLAIN TEXT: ",''.join(PT))
	elif choice == 3:
		break
	else:
		print("Wrong input.\n")
