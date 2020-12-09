# Main Home Screen
"""
@author : Ankit Devani , Jeenal Shah , Meghna Kanade , Sarthak Bharad
"""
from colorama import init  # install and import colorama library
from termcolor import colored  # install and import termcolor library

init()

print(colored("Welcome to the World of Crypto!!!", "red", "on_green"))
print("")
print(colored("What do you wish to do?", "red", "on_green"))
print("")
print(colored("1 - Text Encryption/Decryption", "red", "on_green"))
print("")
print(colored("2 - Image Encryption/Decryption", "red", "on_green"))


i = int(input())
if i == 1:
    import Text  # Calling the Text Encryption/Decryption file
elif i == 2:
    import imagemain  # Calling the main file for Image Encryption/Decryption file
else:
    print("Please try again!!! Enter value 1 or 2")
