import string

input = 'zadej jmeno souboru'
raw_input = input.replace(' ', '')
secret_dictionary = {}

def get_secret_dict(message, move):
    for index in range(0, len(message)):
        raw_letter = message[index]
        letter = raw_letter.lower()
        ascii_values = string.ascii_lowercase
        i = ascii_values.find(letter.lower())
        if i <= (26 - move - 1):
            secret_letter = ascii_values[i + move]
        else:
            secret_letter = ascii_values[i - 26 + move]

        secret_dictionary[letter] = secret_letter
    return secret_dictionary

secret_dictionary = get_secret_dict(raw_input, 3)
novy = []

def translate_message(message, secret_dictionary):
    for x in message:
        if x == " ":
            continue
        novy.append(secret_dictionary[x])
    print(novy)
    return message

translate_message(input, secret_dictionary)

#optimalizace kodu

import string
ascii_values = string.ascii_lowercase

input = 'Zadej nECco'

def encode_message(message, shift):
    secret_message = ''
    for i in message.lower():
        secret_message += translate_letter(i, shift)
    return secret_message

def translate_letter(i, shift):
    if i in (" ", string.digits):
        return i
    index = ascii_values.index(i)
    new_index = (index + shift) % len(ascii_values)
    return ascii_values[new_index]

print(encode_message(input, -2))  