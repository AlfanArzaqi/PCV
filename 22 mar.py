import cv2 as cv
import numpy as np

citra = cv.imread ('naned.jpg')
gray = cv.imread ('naned.jpg', cv.IMREAD_GRAYSCALE)
citrabaru =  np.zeros (citra.shape, citra.dtype)
citraabu = np.zeros (citra.shape, citra.dtype)

print("\nDimensi CItra", citra.shape)

beta = 50
alpha = 1.5
for y in range (citra.shape[0]):
    for x in range (citra.shape[1]):
        for c in range (citra.shape[2]):
            w = alpha*citra[y,x,c] + beta
            citrabaru[y,x,c] = np.clip(w, 0, 255)
            
for y in range (citra.shape[0]):
    for x in range (citra.shape[1]):
        r = np.double (citra[y,x,0])
        g = np.double (citra[y,x,1])
        b = np.double (citra[y,x,2])
        w = (r+g+b)/3
        citraabu[y,x,0] = np.clip(w, 0, 255)
        citraabu[y,x,1] = np.clip(w, 0, 255)
        citraabu[y,x,2] = np.clip(w, 0, 255)
            
cv.imshow ('Citra Gray', gray)
cv.imshow ('Citra Asli', citra)
cv.imshow ('Citra Baru', citrabaru)
cv.imshow ('Citra Abu', citraabu)
cv.waitKey(0)
cv.destroyAllWindows()