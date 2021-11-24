import cv2
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
""" PUNTO 2 EXAMEN FINAL

    python color_filtering.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    # Hue histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])

    # Hue histogram max and location of max
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())

    # Peak mask
    lim_inf = (max_pos - 10, 0, 0)
    lim_sup = (max_pos + 10, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
    mask_not = cv2.bitwise_not(mask)

    # Extracción de tamaño imagen alto y ancho
    h, w = mask.shape

    # Creación de mascara y llenado de huecos para extraer objetos de interes y candidatos a posibles parasitos
    mask2 = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(mask, mask2, (0, 0), 255)
    imagen = cv2.bitwise_not(mask)

    canny = cv2.Canny(imagen, 50, 150)
    # Dectección de contornos
    contours, hierarchy = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_draw = image.copy()
    contar = 0
    for idx, cont in enumerate(contours):
        if len(contours[idx]) > 100:
            hull = cv2.convexHull(contours[idx])
            #cv2.drawContours(image_draw, contours, idx, (0, 255, 255), 2)
            #cv2.drawContours(image_draw, [hull], 0, (255, 0, 0), 2)
            M = cv2.moments(contours[idx])
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            area = M['m00']
            x, y, width, height = cv2.boundingRect(contours[idx])
            jugador = cv2.rectangle(image_draw, (x, y), (x + width, y + height), (0, 0, 255), 2)
            (x, y), radius = cv2.minEnclosingCircle(contours[idx])
            center = (int(x), int(y))
            radius = int(radius)
            contar=contar+1

    print("Se han encontrado {} jugadores/arbitro sobre el campo".format(contar))

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1280, 720)
    cv2.imshow("Image", image_draw)
    cv2.waitKey(0)



