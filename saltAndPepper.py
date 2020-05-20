
import cv2
import numpy as np

# Ez a program csak a k?pek zajterhel?s?re k?sz?lt

def addPointNoise(img, percentage, value):
    noise = np.copy(img)
    n = int(img.shape[0] * img.shape[1] * percentage)

    for k in range(1, n):
        i = np.random.randint(0, img.shape[1])
        j = np.random.randint(0, img.shape[0])

        if img.ndim == 2:
            noise[j, i] = value

        if img.ndim == 3:
            noise[j, i] = [value, value, value]

    return noise


def addSaltAndPepperNoise(img, percentage1, percentage2):
    n = addPointNoise(img, percentage1, 255) # Só
    n2 = addPointNoise(n, percentage2, 0) # Bors
    return n2


#             6             9               4               18
src = ["palcika1.jpg", "palcika2.jpg", "DSC_0340.JPG", "DSC_0339.JPG",
       "DSC_0338.JPG", "DSC_0343.JPG"]
#            18               7

for i in range(0, len(src)):
    img = cv2.imread("Palcikak_szamolasa_original/" + str(src[i]), cv2.IMREAD_COLOR)
    noise = addSaltAndPepperNoise(img, 0.003, 0.003)
    cv2.imwrite("Palcikak_szamolasa/" + str(src[i]), noise)
