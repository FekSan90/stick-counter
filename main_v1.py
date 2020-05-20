import cv2
import numpy as np

#             6             9               4               18
src = ["palcika1.jpg", "palcika2.jpg", "DSC_0340.JPG", "DSC_0339.JPG",
       "DSC_0338.JPG", "DSC_0343.JPG"]
#            18               7

for i in range(0, len(src)):
    print(str(src[i]))
    img = cv2.imread("Palcikak_szamolasa/" + str(src[i]))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)

    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 171, -20)
    # cv2.imshow('Color',thresh)
    # cv2.waitKey(0)
    layers = 4 * [0]
    for i in range(0, len(layers)):
        layers[i] = gray.copy()
        layers[i].fill(0)

    linesP = cv2.HoughLinesP(thresh, 1, np.pi / 180, 230, None, 300, 45)
    select = 0
    color = None
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            x = l[2] - l[0]
            y = l[1] - l[3]
            alfa = np.rad2deg(np.arctan2(y, x))
            if alfa < 0:
                alfa = 180 + alfa

            if alfa < 45 and alfa >= 0:
                color = (255, 0, 0)
                select = 0
            elif alfa > 45 and alfa <= 90:
                color = (0, 0, 255)
                select = 1
            elif alfa > 90 and alfa <= 135:
                color = (0, 255, 0)
                select = 2
            elif alfa > 135 and alfa <= 180:
                color = (0, 255, 255)
                select = 3
            cv2.line(layers[select], (l[0], l[1]), (l[2], l[3]), 255, 2, cv2.LINE_AA)
            cv2.line(img, (l[0], l[1]), (l[2], l[3]), color, 1, cv2.LINE_AA)

    kernel = np.ones((5, 5), np.uint8)
    contours = 4 * [None]
    sticks = 0
    for j in range(0, len(layers)):
        contours[j], _ = cv2.findContours(layers[j], cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        #         print("Layer " + str(i) + ": " + str(len(contours[i])))
        sticks += len(contours[j])

    print('    Pálcikák száma:', str(sticks))
    #    cv2.imshow('Color', img)
    #    cv2.waitKey(0)
    cv2.destroyAllWindows()
