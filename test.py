from autokey import encrypt, decrypt, mid_square_hash

plaintext = input("ENTER PLAINTEXT: ")
key = input("ENTER KEY: ")

cipher = encrypt(plaintext, key)
hash_value = mid_square_hash(cipher)
decrypted = decrypt(cipher, key)

print("\nRESULTS")
print("PLAINTEXT:", plaintext)
print("CIPHERTEXT:", cipher)
print("HASH      :", hash_value)
print("DECRYPTED :", decrypted)

