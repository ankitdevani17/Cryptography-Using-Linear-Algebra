# Text Encryption and Decryption

'''
@author : Ankit Devani , Jeenal Shah , Meghna Kanade , Sarthak Bharad
'''

import numpy as np        #Install and import numpy
import sympy               #Install and import sympy
from sympy import Matrix

# Function to encrypt string s using key (Password)
def encrypt(s, password):
    n = len(s)
    # Generate plain text matrix
    plain_text = np.arange(n).reshape(n, 1)
    for i in range(0, n):
        plain_text[i][0] = ord(s[i]) - ord('a')

    # Generate key matrix
    key = np.arange(n * n).reshape(n, n)
    for i in range(0, n):
        for j in range(0, n):
            key[i][j] = ord(password[(n * i) + j]) - ord('a')

    # encrypted matrix

    encrypted_text = key.dot(plain_text)

    # generate encrypted string
    ans = ""
    for i in range(0, n):
        ans += chr((encrypted_text[i][0] % 26) + ord('a'))

    return ans


# Function to decrypt string s using key (Password)
def decrypt(s, password):
    n = len(s)

    # generate encrypted matrix
    encrypted_text = np.arange(n).reshape(n, 1)
    for i in range(0, n):
        encrypted_text[i][0] = ord(s[i]) - ord('a')

    # generate key matrix
    key = np.arange(n * n).reshape(n, n)
    for i in range(0, n):
        for j in range(0, n):
            key[i][j] = ord(password[(n * i) + j]) - ord('a')

    # inverse key matrix to inverse_key (for generating decryption key)
    def inv_mod(a, m):
        a = a % m;
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1

    inverse_key=Matrix(key).inv_mod(26)
    np.inverse_key = np.array(inverse_key)
    plain_text = inverse_key * encrypted_text

    # generate plaintext string
    ans = ""
    for i in range(0, n):
        ans += chr((plain_text[i] % 26) + ord('a'))

    return ans


# get choice
print("Enter 1 for encryption")
print("Enter 2 for decryption")
a = int(input())

if (a == 1):
    # Encryption BEGINS
    print("Enter string for encrypton(lowercase alphabtes):")
    s = str(input())                          #String to be encrypted
    n = len(s)

    print("Password should be " + str(n * n) + " letters long")
    print("Enter password(lowercase alphabtes): ")                 #Key/Password
    password = str(input())

    if (len(password) != n * n):
        print("Invalid length of string/password.")            #Error if password is not n*n letter long
        print("Password should be " + str(n * n) + " letters long")

    else:
        encrypted_string = encrypt(s, password)                #Calling the function to perform encryption
        print("The encrypted string is: " + encrypted_string)

if (a == 2):
    # Decryption BEGINS
    print("Enter string for decryption:")                      #String to be decrypted
    s = str(input())
    n = len(s)
    print("Enter password: ")                                 #Key/Password
    password = str(input())

    if (len(password) != n * n):
        print("Invalid length of string.Please try again")      #Error if password is not n*n letter long

    else:
        decrypted_string = decrypt(s, password)                 #Calling the function to perform decryption
        print("The decrypted string is " + decrypted_string)
