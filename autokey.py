alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()

    # Create full key
    full_key = key + plaintext
    full_key = full_key[:len(plaintext)]

    ciphertext = ""

    for i in range(len(plaintext)):
        p = char_to_num(plaintext[i])
        k = char_to_num(full_key[i])

        c = (p + k) % 26
        ciphertext += num_to_char(c)

    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ""

    for i in range(len(ciphertext)):
        c = char_to_num(ciphertext[i])

        if i < len(key):
            k = char_to_num(key[i])
        else:
            k = char_to_num(plaintext[i - len(key)])

        p = (c - k + 26) % 26
        ch = num_to_char(p)

        plaintext += ch

    return plaintext

def mid_square_hash(text):
    
    num_str = ""
    for ch in text:
        num_str += str(ord(ch))

    num = int(num_str)

    square = num * num
    square_str = str(square)

    length = len(square_str)
    mid = length // 2

    start = max(mid - 2, 0)
    end = mid + 2

    hash_value = square_str[start:end]

    return hash_value


if __name__ == "__main__":
    while True:
        print("\n1. ENCRYPT")
        print("2. DECRYPT")
        print("3. ENCRYPT + MID-SQUARE HASH")
        print("4. EXIT")

        choice = input("ENTER CHOICE: ")

        if choice == '1':
            pt = input("ENTER PLAINTEXT: ")
            key = input("ENTER KEY: ")
            print("CIPHERTEXT:", encrypt(pt, key))

        elif choice == '2':
            ct = input("ENTER CIPHERTEXT: ")
            key = input("ENTER KEY: ")
            print("PLAINTEXT:", decrypt(ct, key))

        elif choice == '3':
            pt = input("ENTER PLAINTEXT: ")
            key = input("ENTER KEY: ")
            ct = encrypt(pt, key)
            print("CIPHERTEXT:", ct)
            print("HASH:", mid_square_hash(ct))

        elif choice == '4':
            break

        else:
            print("INVALID. TRY AGAIN!")
