import numpy as np

def dct(img):
    N = img.shape[0]

    F = np.zeros((N, N))
    for j in range(N):
        for i in range(N):

            for y in range(N):
                for x in range(N):
                    F[j, i] += img[y, x] * np.cos((np.pi * (2 * x + 1) * i) / (2 * N)) * np.cos \
                        ((np.pi * (2 * y + 1) * j) / (2 * N))

            alpha_i = np.sqrt( 1 /N) if i == 0 else np.sqrt( 2 /N)
            alpha_j = np.sqrt( 1 /N) if j == 0 else np.sqrt( 2 /N)
            F[j, i] *= alpha_i * alpha_j

    return F


def idct(F):
    N = F.shape[0]

    f = np.zeros((N, N))
    for y in range(N):
        for x in range(N):

            for j in range(N):
                for i in range(N):
                    alpha_i = np.sqrt( 1 /N) if i == 0 else np.sqrt( 2 /N)
                    alpha_j = np.sqrt( 1 /N) if j == 0 else np.sqrt( 2 /N)
                    f[y, x] += alpha_i * alpha_j * F[j, i] * np.cos((np.pi * (2 * x + 1) * i ) /(2 * N)) * np.cos \
                        ((np.pi * (2 * y + 1) * j) / (2 * N))

    return f


matrix3x3 = np.matrix([[1,1,1],[0,0,0],[2,2,2]])
DCT = dct(matrix3x3)
print(DCT)

IDCT = idct(DCT)
print('\n', IDCT)


