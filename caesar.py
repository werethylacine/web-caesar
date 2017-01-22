def rotate_character(char, rot):
    if char.isalpha():
        if char.islower():
            newletter = chr(((ord(char) - 97 + rot) % 26) + 97)
        else:
            newletter = chr(((ord(char) - 65 + rot) % 26) + 65)
    else:
        newletter = char
    return newletter

def encrypt(text, rot):
    cryptid = []
    text = str(text)
    for letter in text:
        cryptid.append(rotate_character(letter, rot))
    return(''.join(cryptid))
