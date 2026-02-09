def caesar_encrypt(text, shift):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    for char in text:
        # Encrypt lowercase letters
        if char in lowercase:
            index = lowercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += lowercase[new_index]

        # Encrypt uppercase letters
        elif char in uppercase:
            index = uppercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += uppercase[new_index]

        # Keep other characters unchanged
        else:
            encrypted_text += char

    return encrypted_text


# Example usage
message = "Hello World"
shift = 3
print("Plain text:",message)
print("Encrypted message:", caesar_encrypt(message, shift))
