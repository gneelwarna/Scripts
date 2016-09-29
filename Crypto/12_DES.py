"""Simple DES Program"""

DATA = []
KEY = []

class key:
	def __init__(self, k):
		self.key = k
	def permutation_P10(self):
		#print("\nIn Key::Class P10::Function -->")
		P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
		val = []
		for i in P10:
			#print("\ni = ",i," key[i-1] = ",self.key[i-1])
			val.append(self.key[i-1])
		self.key = val
		#print("key = ",self.key)
	def LS1(self):
		val = []
		for i in self.key:
			val.append(i)
		for i in range(0,4):
			val[i] = self.key[i+1]
		val[4] = self.key[0]
		#print("Val = ",val)
		for i in range(5,9):
			val[i] = self.key[i+1]
		val[9] = self.key[5]
		#print("\nIn Key::Class LS1::Function -->")
		self.key = val
		#print("\nKey = ",self.key)
	def permutation_P8(self):
		P8 = [6, 3, 7, 4, 8, 5, 10, 9]
		val = []
		for i in P8:
			val.append(self.key[i-1])
		self.key = val
		#print("\nIn Key::Class P8::Function -->")
		#print("\nKey = ",self.key)
	def LS2(self):
		val = []
		for i in self.key:
			val.append(i)
		for i in range(0,3):
			val[i] = self.key[i+2]
		val[3] = self.key[0]
		val[4] = self.key[1]
		#print("val = ",val)
		for i in range(5,8):
			val[i] = self.key[i+2]
		val[8] = self.key[5]
		val[9] = self.key[6]
		self.key = val
		#print("\nIn Key::Class LS2::Function -->")
		#print("\nKey = ",self.key)
	def show(self):
		print("Key is =  ",self.key)

def F_func(data, key): #data= 4 bits, key= 8 bits
	EP = [4, 1, 2, 3, 2, 3, 4, 1]
	S0 = [ [1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 3] ]
	S1 = [ [0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3] ]
	P4 = [2, 4, 3, 1]

	"""E/P"""
	val = []
	for i in EP:
		val.append(data[i-1])
	data = val
	#print("\nIn F_func::Function E/P -->")
	#print("\nData = ",data)
	"""Data XOR with 8-bit key"""
	val = []
	#print("\nIn F_func:Function -->")
	#print("\ndata = ",data)
	#print("\nkey  = ",key)
	for d,k in zip(data,key):
		val.append(d ^ k)
	data = val
	#print("\nIn F_func::Function After Data XOR -->")
	#print("Data = ",data)
	"""Pass left 4 bits through S0 and right 4 bits through S1"""
	val = []
	temp = bin(  S0[int(str(data[0]) + str(data[3]), 2)] [int(str(data[1]) + str(data[2]), 2)] )
	#print("\nResult of S0 -> ",temp)
	temp = temp[2:]
	temp = '0'+temp
	#print("\nResult of S0 -> ",temp)
	val.append(int( temp[-2], 2) )
	val.append(int( temp[-1], 2) )

	temp = bin(  S1[int(str(data[4]) + str(data[7]), 2)] [int(str(data[5]) + str(data[6]), 2)] )
	#print("\nResult of S1 -> ",temp)
	temp = temp[2:]
	temp = '0'+temp
	#print("\nResult of S1 -> ",temp)
	val.append(int( temp[-2], 2) )
	val.append(int( temp[-1], 2) )

	data = val
	#print("\nIn F_func::Function After passing bits to S0 and S1 -->")
	#print("\nData = ",data)
	val = []
	"""Apply Permutation P4"""
	for i in P4:
		val.append(data[i-1])
	data = val
	#print("\nIn F_func::Function After P4 -->")
	#print("\nData = ",data)
	return data

def Fk_func(data, key):	#8 bits --> 8 bits
	count = 0
	L = []
	R = []
	for i in data:
		if count <= 3:
			L.append(i)
		else:
			R.append(i)
		count += 1
	f_return = F_func(R,key)
	#print("\nIn Fk_func::Function\nReturn DATA from F_func = ",f_return)
	count = 0
	L_tmp = []
	while(count <= 3):
		L_tmp.append(L[count] ^ f_return[count])
		count += 1
	L = L_tmp
	val = []
	for i in L:
		val.append(i)
	for i in R:
		val.append(i)
	return val
	#print("\nIn Fk_func::Function\nData = ",data)

def IP(data):
	P8 = [2, 6, 3, 1, 4, 8, 5, 7]
	val = []
	for i in P8:
		val.append(data[i-1])
	return val
def IP_Inverse(data):
	P8 = [4, 1, 3, 5, 7, 2, 8, 6]
	val = []
	for i in P8:
		val.append(data[i-1])
	return val
def SW(data):
	"""######### DEFINE THIS FUNCTION #########"""
	val = []
	for i in range(4,8):
		val.append(data[i])
	for i in range(0,4):
		val.append(data[i])
	#print("Data after SW :  ",val)
	return val

def Encrypt_Get_Data(DATA, KEY):
	DATA = []
	KEY = []
	print("\nEnter 8-bit Input [0/1]: ")
	"""for i in range(8):
		DATA.append(int(input()))"""
	print("\nEnter 10-bit Key  [0/1]: ")
	"""for i in range(10):
		KEY.append(int(input()))"""
	DATA = [1, 0, 1, 0, 0, 1, 0, 1]
	KEY  = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1]
	print("\nData = ",DATA,"\nKEY = ",KEY,"\n\n")
	return DATA, KEY
def Decrypt_Get_Data(DATA):
	DATA = []
	print("\nEnter 8-bit Input [0/1]: ")
	"""for i in range(8):
		DATA.append(int(input()))"""
	DATA = [0, 0, 1, 1, 0, 1, 1, 0]
	return DATA	

ch = 0
while ch != 3:
	print("\n***MENU***\n1. Encryption\n2. Decryption\n3. Exit\n   Enter your choice :  ")
	ch = int(input())
	if ch == 1:
		"""Encryption"""
		DATA, KEY = Encrypt_Get_Data(DATA, KEY)
		print("\nDATA [Plain] = ",DATA,"\nKEY = ",KEY)
		key1 = key(KEY)
		key1.permutation_P10()
		key1.LS1()
		key1.permutation_P8()

		key2 = key(KEY)
		key2.permutation_P10()
		key2.LS1()
		key2.LS2()
		key2.permutation_P8()

		DATA = IP(DATA)
		DATA = Fk_func(DATA, key1.key)
		DATA = SW(DATA)
		DATA = Fk_func(DATA, key2.key)
		DATA = IP_Inverse(DATA)
		print("\nEncrypted Data [Cipher Text] : ",DATA)
	elif ch == 2:
		"""Decryption"""
		print("\nDecryption: ")
		#print("\nDATA [Cipher] = ",DATA,"\nKEY = ",KEY)
		print("\nDATA [Cipher] = ",DATA,"\nKEY = ",KEY)
		DATA = Decrypt_Get_Data(DATA)
		DATA = IP(DATA)
		DATA = Fk_func(DATA, key2.key)
		DATA = SW(DATA)
		DATA = Fk_func(DATA, key1.key)
		DATA = IP_Inverse(DATA)
		print("\nDecrypted Data [Plain Text]  : ",DATA)
	elif ch == 3:
		print("Exiting...\n")
	else:
		print("Wrong choice.")

