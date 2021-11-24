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

    points1 = []
    points2 = []

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click)

    point_counter = 0
    while True:
        cv2.imshow("Image", image_draw)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            points1 = points.copy()
            points = []
            break
        if len(points) > point_counter:
            point_counter = len(points)
            cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [0, 0, 255], -1)
        if key == ord("x"):
            points2 = points.copy()
            points = []
            break

    N = min(len(points1), len(points2))
    assert N >= 2, 'At least four points are required'

    pts1 = np.array(points1[:N])
    pts2 = np.array(points2[:N])

    cv2.line(image_draw, pts1, pts2, (255, 0, 0), thickness=3, lineType=2)
    cv2.imshow("Image", image_draw)
    cv2.waitKey(0)
