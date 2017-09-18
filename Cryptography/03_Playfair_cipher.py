'''Implementation of Playfair Cipher Algorithm'''

''' INPUT KEY STRING;  REPLACE 'J' BY 'I' IN PLAIN TEXT.'''
key = ((str(input("ENTER KEY FOR PLAYFAIR CIPHER:  "))).lower()).replace('i','j')
if not key.isalpha():
	print("Wrong key input.")
	exit()

'''REMOVE DUPLICATES FROM KEY'''
clear_key = []
for ch in key:
	if ch not in clear_key:
		clear_key.append(ch)
#print(clear_key)

'''APPEND REMAINING ALPHABETS IN KEYMATRIX'''
i = 97
while i < 123:
	if i == 106:
		i = i + 1
	if chr(i) not in clear_key:
		clear_key.append(chr(i))
	i = i + 1

'''BUILD KEYMATRIX'''
print("KEYMATRIX IS = ")
j = row = 0
keymatrix = []
sam = [0,0,0,0,0]
for ch in clear_key:
	sam[j] = ch
	j = j + 1
	if j == 5:
		j = 0
		print("\t\t",sam)	#PRINT
		keymatrix.append(sam)
		sam = [0,0,0,0,0]
		row = row + 1

choice = flag = 0
while(choice < 3):
	print("1. PLAIN TEXT TO CIPHER TEXT.\n2. CIPHER TEXT TO PLAIN TEXT.\n3. EXIT.")
	choice = int(input("   ENTER YOUR CHOICE: "))
	
	if choice == 1:
		'''ACCEPT PLAIN TEXT; REPLACE 'J' BY 'I' IN PLAIN TEXT.'''
		PT = ((str(input("Enter Plain Text:  "))).lower()).replace('j','i')
		if PT.isalpha():
			CT = []
			'''REPEATING LETTERS THAT FALL IN THE SAME PAIR ARE SEPARATED WITH A FILLER LETTER x'''
			i = 0
			while(i < (len(PT)-1)):
				if PT[i] == PT[i+1] == 'x':
					PT = PT[:i+1] + 'y' + PT[i+1:]
				elif PT[i] == PT[i+1]:
					PT = PT[:i+1] + 'x' + PT[i+1:]
				else: pass
				print(PT[i])
				i = i + 2
			
			'''IF REQUIRED ADD RANDOM VARIABLE TO FORM PAIR'''
			if len(PT) % 2 == 1:
				PT = PT + 'x'
			print("PLAIN TEXT AFTER PROCESSING: ",PT)		
	
			'''GENERATE CIPHER TEXT'''
			i = 0	
			while (i < (len(PT))):
				'''CALCULATE ROW AND COL OF LETTERS IN THE SAME PAIR'''
				ROW1 = COL1 = ROW2 = COL2 = j = flag = 0
				while (j < 5) and (flag <2):
					if PT[i] in keymatrix[j]:
						ind = keymatrix[j].index(PT[i])
						ROW1 = j
						COL1 = ind
						flag = flag + 1
						#print(PT[i],"=(",ROW1,COL1,"); ")
					if PT[i+1] in keymatrix[j]:
						ind = keymatrix[j].index(PT[i+1])
						ROW2 = j
						COL2 = ind
						flag = flag + 1
						#print(PT[i+1],"=(",ROW2,COL2,"); ")
					j = j + 1
				'''GENERATE CIPHER TEXT'''
				if ROW1 == ROW2:
					CT.append(keymatrix[ROW1][(COL1 + 1) % 5])
					CT.append(keymatrix[ROW2][(COL2 + 1) % 5])
				elif COL1 == COL2:
					CT.append(keymatrix[(ROW1 + 1) % 5][COL1])
					CT.append(keymatrix[(ROW2 + 1) % 5][COL2])
				else:
					CT.append(keymatrix[ROW1][COL2])
					CT.append(keymatrix[ROW2][COL1])
				i = i + 2
			
			print("CIPHER TEXT  (ECRYPTION) :  ",''.join(CT))
		else:
			print("Wrong Plain input.")
			exit()

	elif choice == 2:
		if flag > 0:
			i = 0
			PT = []
			while (i < (len(CT))):
				'''CALCULATE ROW AND COL OF LETTERS IN THE SAME PAIR'''
				ROW1 = COL1 = ROW2 = COL2 = j = flag = 0
				while (j < 5) and (flag <2):
					if CT[i] in keymatrix[j]:
						ind = keymatrix[j].index(CT[i])
						ROW1 = j
						COL1 = ind
						flag = flag + 1
						#print(CT[i],"=(",ROW1,COL1,"); ")
					if CT[i+1] in keymatrix[j]:
						ind = keymatrix[j].index(CT[i+1])
						ROW2 = j
						COL2 = ind
						flag = flag + 1
						#print(CT[i+1],"=(",ROW2,COL2,"); ")
					j = j + 1
				'''GENERATE CIPHER TEXT'''
				if ROW1 == ROW2:
					PT.append(keymatrix[ROW1][(COL1 - 1) % 5])
					PT.append(keymatrix[ROW2][(COL2 - 1) % 5])
				elif COL1 == COL2:
					PT.append(keymatrix[(ROW1 - 1) % 5][COL1])
					PT.append(keymatrix[(ROW2 - 1) % 5][COL2])
				else:
					PT.append(keymatrix[ROW1][COL2])
					PT.append(keymatrix[ROW2][COL1])
				i = i + 2
			PT = ''.join(PT)
			print("PLAIN TEXT (DECRYPTION) :  ",PT)
		else:
			print("\nPLAIN TEXT NOT GIVEN. SELECT CHOICE 1.\n")		
	elif choice == 3:		
		break;
	else:
		print("Wrong choice.")

