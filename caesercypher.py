#Caesar Cipher - excercise from Hacking Cyphers

message = ""

#key used for encryption and decryption
key = 7

#set program to either encrypt or decrypt
mode = "encrypt"

#acceptable symbols to encrypt
letters = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

#empty string to store the encrypted or decrypted message
translated = ""

#capitalize message
message = message.upper()

#actual work or encryption or decryption happens here
for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
#what to do if num is larger than len(letters) or is less than 0.
        if num >= len(letters):
            num = num - len(letters)
        elif num < 0:
            num = num + len(letters)

#add encrypted or decrypted (or ignored) symbol to end of translated
        translated = translated + letters[num]

    else:
        translated = translated + symbol

#print string to screen
print(translated)
