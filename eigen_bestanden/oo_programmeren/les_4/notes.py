codewoord = "Appel"
sleutel = 2


encode = []
for letter in codewoord:
    new_letter = chr(ord(letter) + 2)
    encode.append(new_letter)
print(encode)