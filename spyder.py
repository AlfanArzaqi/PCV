import cv2 as cv
import numpy as np

image = cv.imread('1.png')
new_image = np.zeros(image.shape, image.dtype)
 

print(' Basic Linear Transforms ')
print('-------------------------')

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            w = image[y,x,c] + 100
            new_image[y,x,c] = np.clip(w, 0, 255)
            
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
cv.waitKey(0)