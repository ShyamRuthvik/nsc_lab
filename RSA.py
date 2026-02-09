import math

# Step 1: Choose two prime numbers
p = 17
q = 11

# Step 2: Compute n
n = p * q

# Step 3: Compute phi(n)
phi = (p - 1) * (q - 1)

# Step 4: Choose public key e
e = 7   # must be coprime with phi

# Step 5: Compute private key d
d = pow(e, -1, phi)

# Encryption
def encrypt(message):
    return pow(message, e, n)

# Decryption
def decrypt(ciphertext):
    return pow(ciphertext, d, n)


# Example
message = 8
cipher = encrypt(message)
original = decrypt(cipher)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
print("Original Message:", message)
print("Encrypted Message:", cipher)
print("Decrypted Message:", original)
