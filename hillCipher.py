import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def text_to_matrix(key):
    key = key.upper()
    size = int(len(key) ** 0.5)

    # Convert key text to matrix
    matrix = []
    k = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(alphabet.index(key[k]))
            k += 1
        matrix.append(row)

    return np.array(matrix)

def hill_encrypt(plaintext, key_text):
    plaintext = plaintext.upper().replace(" ", "")
    key_matrix = text_to_matrix(key_text)
    n = key_matrix.shape[0]

    # Padding with X
    while len(plaintext) % n != 0:
        plaintext += 'X'

    ciphertext = ""

    for i in range(0, len(plaintext), n):
        block = plaintext[i:i+n]

        # Convert letters to numbers
        numbers = [alphabet.index(char) for char in block]

        # Matrix multiplication
        result = np.dot(key_matrix, numbers) % 26

        # Convert back to letters
        for num in result:
            ciphertext += alphabet[num]

    return ciphertext


# Example usage
message = "HELLO"
key = "GYAD"   # 2x2 key matrix

encrypted = hill_encrypt(message, key)
print("Encrypted Message:", encrypted)
