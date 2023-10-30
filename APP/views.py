from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

#CAESER CIPHER
def caeserCipher(request):
    return render(request, "caeserCipher.html")


#CAESER CIPHER ENCRYPTION
def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    
    return result

#CAESER CIPHER DECRYPTION
def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)


def caeserCipherEncryption(request):
    if request.method=="POST":
        pass
    return render(request, "caeserCipherEncryption.html")


def caeserCipherDecryption(request):
    if request.method=="POST":
        pass
    return render(request, "caeserCipherDecryption.html")

###########################################################################################################

#MONO ALPHABETIC CIPHER
def monoalphabeticCipher(request):
    return render(request,"monalphabeticCipher.html")

def create_monoalphabetic_cipher(key):
    if len(key) != 26:
        raise ValueError("Key must be 26 characters long")

    cipher = {}
    
    for i in range(26):
        cipher[chr(ord('a') + i)] = key[i]
    
    return cipher


def encrypt_monoalphabetic(plaintext, key):
    cipher = create_monoalphabetic_cipher(key)
    
    plaintext = plaintext.lower()
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            ciphertext += cipher[char]
        else:
            ciphertext += char
    
    return ciphertext

def decrypt_monoalphabetic(ciphertext, key):
    inverse_key = ''.join(sorted(key))  
    cipher = create_monoalphabetic_cipher(inverse_key)
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += cipher[char]
        else:
            plaintext += char
    
    return plaintext


def monoalphabeticCipherEncryption(request):
    #give key
    return render(request,"monoalphabeticCipherEncryption.html")


def monoalphabeticCipherDecryption(request):
    return render(request,"monoalphabeticCipherDecryption.html")
###########################################################################################################

#PLAY FAIR CIPHER
def playfairCipher(request):
    return render(request,"playfairCipher.html")

def create_playfair_matrix(key):
    key = key.replace("j", "i")  
    key = "".join(dict.fromkeys(key))  
    key_matrix = [[0] * 5 for _ in range(5)]
    key = key.replace("j", "i")  
    
    row, col = 0, 0
    for char in key:
        key_matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1
        alphabet = "abcdefghiklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in key:
            key_matrix[row][col] = char
            col += 1
            if col == 5:
                col = 0
                row += 1

    return key_matrix

def find_positions(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    
    plaintext = plaintext.replace("j", "i")  
    plaintext = plaintext.replace(" ", "")  
    plaintext = plaintext.lower()  
    plaintext = list(plaintext)
    
    for i in range(1, len(plaintext), 2):
        if plaintext[i] == plaintext[i - 1]:
            plaintext.insert(i, "x")
    if len(plaintext) % 2 != 0:
        plaintext.append("x")
    
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_positions(matrix, char1)
        row2, col2 = find_positions(matrix, char2)
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    
    ciphertext = ciphertext.lower()  
    ciphertext = list(ciphertext)
    
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_positions(matrix, char1)
        row2, col2 = find_positions(matrix, char2)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    
    return plaintext

def playfairCipherEncryption(request):
    # key = "keyword"
    # plaintext = "hello world"
    return render(request,"playfairCipherEncryption.html")


def playfairCipherDecryption(request):
    return render(request,"playfairCipherDecryption.html")
############################################################################################################

#HILL CIPHER
def hillCipher(request):
    return render(request,"hillCipher.html")

import numpy as np

def text_to_matrix(text, block_size):
    text = text.replace(" ", "") 
    text = text.upper()  
    while len(text) % block_size != 0:
        text += 'X' 
    matrix = []
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        matrix.append([ord(char) - ord('A') for char in block])
    return matrix

def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        text += ''.join([chr(char + ord('A')) for char in row])
    return text

def encrypt_hill_cipher(plaintext, key_matrix):
    block_size = len(key_matrix)
    plaintext_matrix = text_to_matrix(plaintext, block_size)
    encrypted_matrix = []
    
    for block in plaintext_matrix:
        block = np.array(block)
        result = np.dot(key_matrix, block) % 26
        encrypted_matrix.append(result)
    
    return matrix_to_text(encrypted_matrix)

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt_hill_cipher(ciphertext, key_matrix):
    block_size = len(key_matrix)
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    determinant_inv = mod_inverse(determinant, 26)
    
    if determinant_inv is None:
        raise ValueError("Key matrix is not invertible")

    key_matrix_inv = np.linalg.inv(key_matrix)
    key_matrix_adj = (key_matrix_inv * determinant) % 26
    
    decrypted_matrix = []
    
    ciphertext_matrix = text_to_matrix(ciphertext, block_size)
    
    for block in ciphertext_matrix:
        block = np.array(block)
        result = np.dot(key_matrix_adj, block) % 26
        decrypted_matrix.append(result)
    
    return matrix_to_text(decrypted_matrix)

def hillCipherEncryption(request):
    #key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  

    return render(request,"hillCipherEncryption.html")

def hillCipherDecryption(request):
    return render(request,"hillCipherDecryption.html")
###########################################################################################################

#POLYALPHABETIC CIPHER
def polyalphabeticCipher(request):
    return render(request,"polyalphabeticChiper.html")

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper()  
    key = key.upper()  
    encrypted_text = ""

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += plaintext[i]

    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper()  
    key = key.upper()  
    decrypted_text = ""

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            decrypted_char = chr(((ord(ciphertext[i]) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += ciphertext[i]

    return decrypted_text

def polyalphabeticCipherEncryption(request):
    return render(request,"polyalphabeticCipherEncryption.html")


def polyalphabeticCipherDecryption(request):
    return render(request,"polyalphabeticCipherDecryption.html")

############################################################################################################

 
#ONE TIME PAD
def onetimePad(request):
    return render(request,"onetimePad.html")

import random

def generate_one_time_pad(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def encrypt_one_time_pad(plaintext, one_time_pad):
    ciphertext = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        key = one_time_pad[i]
        encrypted_char = chr(ord(char) ^ ord(key))
        ciphertext += encrypted_char
    return ciphertext

def decrypt_one_time_pad(ciphertext, one_time_pad):
    return encrypt_one_time_pad(ciphertext, one_time_pad)  


def onetimePadEncryption(request):
    return render(request,"onetimePadEncryption.html")


def onetimePadDecryption(request):
    return render(request,"onetimePadDecryption.html")

#############################################################################################################
