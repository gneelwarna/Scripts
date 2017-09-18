#Diffie-Hellman Key Exchange Algorithm
p = int(input("Enter Prime Number: "))
g  = int(input("Enter Base  Number: "))

print("\nAt Alice:")
a = int(input("Enter Alice's Secret Key: "))
A = (g**a) % p
print("Alice sends ",A," to Bob..")

print("\nAt Bob:")
b = int(input("Enter Bob's Secret Key: "))
B = (g**b) % p
print("Bob sends ",B," to Alice..")

s1 = (B**a) % p
print("\nAlice computes Secret Number: ",s1)
s2 = (A**b) % p
print("Bob   computes Secret Number: ",s2)
