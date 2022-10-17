import numpy as np

def dct(img):
    N = img.shape[0]
    DCT = np.zeros((N, N)) #initialize the NxN matrix

    for j in range(N):
        for i in range(N):
            for y in range(N):
                for x in range(N):
                    #Aapply the DCT fucntion
                    DCT[j, i] += img[y, x] * np.cos((np.pi * (2 * x + 1) * i) / (2 * N)) * np.cos \
                        ((np.pi * (2 * y + 1) * j) / (2 * N))

            alpha_i = np.sqrt( 1 /N) if i == 0 else np.sqrt( 2 /N)
            alpha_j = np.sqrt( 1 /N) if j == 0 else np.sqrt( 2 /N)
            DCT[j, i] *= alpha_i * alpha_j

    return DCT


def idct(DCT):
    N = DCT.shape[0]
    #initilize the NxN matrix
    img = np.zeros((N, N))
    for y in range(N):
        for x in range(N):
            for j in range(N):
                for i in range(N):
                    alpha_i = np.sqrt( 1 /N) if i == 0 else np.sqrt( 2 /N)
                    alpha_j = np.sqrt( 1 /N) if j == 0 else np.sqrt( 2 /N)
                    img[y, x] += alpha_i * alpha_j * DCT[j, i] * np.cos((np.pi * (2 * x + 1) * i ) /(2 * N)) * np.cos \
                        ((np.pi * (2 * y + 1) * j) / (2 * N))

    return img


matrix3x3 = np.matrix([[1,1,1,1],[0,0,0,0]])
DCT = dct(matrix3x3)
print(DCT)

IDCT = idct(DCT)
print('\n', IDCT)


