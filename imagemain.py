# Home Screen for Image Encryption/Decryption
"""
@author : Ankit Devani , Jeenal Shah , Meghna Kanade , Sarthak Bharad
"""

print("What do you wish to do?")
print("1 - Image Encryption ")
print("2 - Image Decryption")
j = int(input())
if j == 1:
    import imgencryption  # Calling the image Encryption file
elif j == 2:
    import imgdecryption  # Calling the image Decryption file
else:
    print("Please try again!!! Enter value 1 or 2")
