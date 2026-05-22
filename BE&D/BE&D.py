def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        
        if char.isupper():

            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += shifted_char

        elif char.islower():

            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            ciphertext += shifted_char
        else:

            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):

    return caesar_encrypt(ciphertext, -shift)

def main():
    print("=== DecodeLabs Industrial Kit: Project 2 ===")
    print("Initialize: Cryptographic Phase - Data Confidentiality\n")
    

    user_text = input("Enter the plaintext message to secure: ")
    

    shift_key = 3 
    

    encrypted_text = caesar_encrypt(user_text, shift_key)
    decrypted_text = caesar_decrypt(encrypted_text, shift_key)
    

    print("-" * 50)
    print(f"Original Plaintext : {user_text}")
    print(f"Ciphertext (Secured): {encrypted_text}")
    print(f"Decrypted Plaintext: {decrypted_text}")
    print("-" * 50)

if __name__ == "__main__":
    main()