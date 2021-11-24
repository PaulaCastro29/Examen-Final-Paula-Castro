import cv2
import sys
import os
import numpy as np

points = []


def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))


if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    imagen = cv2.imread(path_file)
    image_draw = np.copy(imagen)

    puntos=[]
    def dibujando(event, x, y, flags, param):
        # Imprimimos la información sobre los eventos que se estén realizando
        print('x=', x)
        print('y=', y)
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(imagen, (x, y), 20, (255, 255, 255), 2)
            puntos = [x, y]

        cv2.line(image_draw, (x,y) (x,y), (255, 0, 0), 3, 2)

    cv2.namedWindow('Imagen')
    cv2.setMouseCallback('Imagen', dibujando)
    while True:
        cv2.imshow('Imagen', imagen)
        k = cv2.waitKey(1) & 0xFF
    cv2.destroyAllWindows()
    #cv2.waitKey(0)



