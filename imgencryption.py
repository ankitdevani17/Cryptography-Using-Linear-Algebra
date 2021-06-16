# Image Encryption
"""
@author : Ankit Devani , Jeenal Shah , Meghna Kanade , Sarthak Bharad

"""
import imageio
import numpy as np

#Defining all the necessary functions
def Encryption():

    print("Enter the path of image")        #taking the image from the user
    img = input()
    img = imageio.imread(img)

    l = img.shape[0]                        #judging the number of rows and columns in the image
    w = img.shape[1]
    n = max(l, w)

    if n % 2:                               #checking if the image is square or not
        n = n + 1

    img2 = np.zeros((n, n, 3))
    img2[:l, :w, :] += img  # Making the picture to have square dimensions

    # Image is now ready for encyption
    # Generating the key for encrytion

    Mod = 256 #this is for judging the colour composition
    k = 23  # Key for Encryption

    d = np.random.randint(256, size=(int(n / 2), int(n / 2)))  # Arbitrary Matrix, should be saved as Key also
    u = int(n / 2)

    def identity(a):  # a is the dimension of the matrix required
        id = []
        k = 0
        for i in range(0, a):
            temp = []
            for j in range(0, a):
                if (j == k):
                    temp.append(1)
                else:
                    temp.append(0)
            id.append(temp)
            k = k + 1
        return id

    I = identity(u)                     #Generating an involutory matrix for key
    a = np.mod(-d, Mod)

    b = (k * ((I - a) % Mod))
    b=b%Mod
    k = (k**127)
    k=k%Mod

    c = (I + a) % Mod
    c = (c * k) % Mod

    A1 = np.concatenate((a, b), axis=1)
    A2 = np.concatenate((c, d), axis=1)
    A = np.concatenate((A1, A2), axis=0)

    Test = np.matmul(A % Mod, A % Mod) % Mod  # making sure that A is an involutory matrix, A*A = I

    # Saving key as an image
    key = np.zeros((n + 1, n))
    key[:n, :n] += A
    # Adding the dimension of the original image within the key
    # Elements of the matrix should be below 256

    key[-1][0] = int(l / Mod)
    key[-1][1] = l % Mod
    key[-1][2] = int(w / Mod)
    key[-1][3] = w % Mod

    imageio.imwrite("Key.png", key)

#-:ENCRYPTION:-
    '''We are using np.matmul function as below code is of o(n^3) 
       time complexity and hence our code was taking almost 6-7 MINUTES TO TERMINATE '''

    '''def multiply_mat(a,b):
        n=len(a)
        m=len(b[0])
        ans=zeroes(n,m)
        for i in range(0,n):
             for j in range(0,m):
                for k in range(0,len(b)):
                    ans[i][j] += a[i][k] * b[k][j]
        return ans
    '''
    # Apply the algorithm to R-G-B components separately

    enc_color1 = (np.matmul(A % Mod, img2[:, :, 0] % Mod))
    enc_color1=  enc_color1 % Mod

    enc_color2 = (np.matmul(A % Mod, img2[:, :, 1] % Mod))
    enc_color2 = enc_color2 % Mod

    enc_color3 = (np.matmul(A % Mod, img2[:, :, 2] % Mod))
    enc_color3 = enc_color3 % Mod

#Usage of np.resize is done as it's not a LA operation and is manipulating image

    enc_color1_shape=(enc_color1.shape[0], enc_color1.shape[1], 1)
    enc_color2_shape=(enc_color2.shape[0], enc_color2.shape[1], 1)
    enc_color3_shape=(enc_color3.shape[0], enc_color3.shape[1], 1)

    enc_color1 = np.resize(enc_color1,(enc_color1_shape) )
    enc_color2 = np.resize(enc_color2,(enc_color2_shape) )
    enc_color3 = np.resize(enc_color3,( enc_color3_shape) )

    # Enc = A * image  #combining the R-G-B components
    encrypt_full = np.concatenate((enc_color1, enc_color2, enc_color3), axis=2)

    imageio.imwrite('Encrypted.png', encrypt_full)
    print("Image encrypted successfully !!")

#main call
Encryption()