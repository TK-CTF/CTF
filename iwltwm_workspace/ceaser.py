# encrypt 'str' into ciphertext by 'key'
def encrypt(str, key):
    ciphertext = ""

    for ch in list(str):
        if 'A' <= ch <= 'Z':
            ciphertext += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= ch <='z':
            ciphertext += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            ciphertext += ch

    return ciphertext

#deencrypt 'str' into plaintext by 'key'
def decrypt(str, key):
    return encrypt(str, -key)

if __name__ == "__main__": 
    mode = input("select mode from encrypt -> E, decrypt -> D: ")
    text = input("input text: ")
    key = input("input key: ")
    
    if mode == "E":
        encrypt(text, key) 
    elif mode == "D":
        decrypt(text, key)
    else: 
        print("The mode is invalid. Try again!")
