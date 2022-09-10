# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# *******************************************************

import string
import math

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, password):
    encrypted_message = ''
    #password = math.ceil(len(message)/len(password))*password
    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        #ord_of_ch = ordinal_value[ch]
        message_ch = message[index]
        ord_of_message = ordinal_value[message_ch]
        shifted_ord_of_ch = (ord_of_message + key) % len(alphabet)
        encrypted_ch = alphabet[shifted_ord_of_ch]
        encrypted_message += encrypted_ch
    return encrypted_message

def decrypt(message, password):
    decrypted_message = ''
    for index, ch in enumerate(message):
        pass_ch = password[index % len(password)]
        key = ordinal_value[pass_ch]
        #ord_of_ch = ordinal_value[ch]
        message_ch = message[index]
        ord_of_message = ordinal_value[message_ch]
        shifted_ord_of_ch = (ord_of_message - key) % len(alphabet)
        decrypted_ch = alphabet[shifted_ord_of_ch]
        decrypted_message += decrypted_ch
    return decrypted_message

if __name__ == "__main__":
    print(encrypt("abcdefg", "bcde"))