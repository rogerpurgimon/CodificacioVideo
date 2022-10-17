def rgb_to_yuv(color):
    '''
    :param color is a vector containing the RED, GREEN and BLUE channels
    :return the color in the YUV colospace
    '''
    R = color[0]
    G = color[1]
    B = color[2]

    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = - 0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128

    return [Y,U,V]

R = input("Entra el valor de vermell(R) entre 0 i 255: ")
G = input("Entra el valor de verd(G) entre 0 i 255: ")
B = input("Entra el valor de blau(B) entre 0 i 255: ")
RGBcolor = [float(R),float(G),float(B)]
print('El color en RGB és ',RGBcolor)
YUVcolor = rgb_to_yuv(RGBcolor)
print('El color en el YUV space és ',YUVcolor)