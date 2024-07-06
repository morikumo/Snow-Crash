def decrypt_caesar(ciphertext, shift):
    decrypted = ""
    for c in ciphertext:
        # Vérifie si le caractère est une lettre
        if c.isalpha():
            # Décale le caractère
            offset = ord('a') if c.islower() else ord('A')
            decrypted += chr((ord(c) - offset - shift) % 26 + offset)
        else:
            decrypted += c
    return decrypted

# Texte à décrypter
ciphertext = "cdiiddwpgswtgt"

# Essayez tous les décalages de 1 à 25
for i in range(1, 26):
    decrypted_text = decrypt_caesar(ciphertext, i)
    print(f"Décalage de {-i % 26}: {decrypted_text}")
r