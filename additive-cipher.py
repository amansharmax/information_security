#function to encrypt
def encrypt(text,s):
    #formula used (text + s) mod 26
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#function to decrypt    
def decrypt(text,s):
    #formula used (text - s) mod 26
    result1 = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result1 += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result1 += chr((ord(char) - s - 97) % 26 + 97)
    return result1


text = "additivecipher"
s = 4
#print the result
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encypt Cipher: " + encrypt(text,s))
print("Decrypt Cipher: " + decrypt(encrypt(text,s),s))
