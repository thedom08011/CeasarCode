uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase= 'abcdefghijklmnopqrstuvwxyz'



def cesar_encrypt(clearText, step):
    cipherText =''

    for letter in clearText:
        if letter in uppercase:
            index = uppercase.index(letter)
            letterEncrypted = uppercase[(index + step) % 26]
            cipherText += letterEncrypted
        elif letter in lowercase:
            index = lowercase.index(letter)
            letterEncrypted = lowercase[(index + step) % 26]
            cipherText += letterEncrypted
        elif letter == ' ':
            cipherText += ' '

    return cipherText 

cipherText = cesar_encrypt('Le code Cesar es facile a dechiffrer', 12)
print(cipherText)

