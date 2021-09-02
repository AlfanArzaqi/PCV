import cv2
from matplotlib.pyplot import close
import numpy as np

domino = cv2.imread('domino.jpg')
hsv_domino = cv2.cvtColor(domino, cv2.COLOR_BGR2HSV)
kernel = np.ones((3, 3), np.uint8)
# close_hsv_domino = cv2.morphologyEx(hsv_domino, cv2.MORPH_CLOSE, kernel);
light_red_1 = (0, 150, 50)
dark_red_1 = (10, 255, 255)
light_red_2 = (170, 150, 50)
dark_red_2 = (180, 255, 255)

while 1:
    mask1 = cv2.inRange(hsv_domino, light_red_1, dark_red_1)
    mask2 = cv2.inRange(hsv_domino, light_red_2, dark_red_2)
    mask = mask1 + mask2
    close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel);
    result = cv2.bitwise_and(domino, domino, mask=close_mask)
    contours, hierarchy = cv2.findContours(close_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(domino, contours, -1, (255, 255, 0), 1)
    cv2.imshow('result', result)
    cv2.imshow('result1', domino)

    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break