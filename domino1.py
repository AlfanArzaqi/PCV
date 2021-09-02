import cv2
import numpy as np

print(cv2.__version__)

def doNothing(x):
  pass

# window
cv2.namedWindow('Domino')

# Trackbar
cv2.createTrackbar('Low H', 'Domino', 0, 180, doNothing)
cv2.createTrackbar('High H', 'Domino', 180, 180, doNothing)
cv2.createTrackbar('Low S', 'Domino', 0, 255, doNothing)
cv2.createTrackbar('High S', 'Domino', 255, 255, doNothing)
cv2.createTrackbar('Low V', 'Domino', 0, 255, doNothing)
cv2.createTrackbar('High V', 'Domino', 255, 255, doNothing)

while True:
  LH = cv2.getTrackbarPos('Low H', 'Domino')
  HH = cv2.getTrackbarPos('High H', 'Domino')
  LS = cv2.getTrackbarPos('Low S', 'Domino')
  HS = cv2.getTrackbarPos('High S', 'Domino')
  LV = cv2.getTrackbarPos('Low V', 'Domino')
  HV = cv2.getTrackbarPos('High V', 'Domino')
  domino = cv2.imread("D:\Teknik Komputer\Semester 4\Kuliah\Pengolahan Citra dan Video\domino.jpg")
  frameHSV = cv2.cvtColor(domino, cv2.COLOR_BGR2HSV)
  frameSmooth = cv2.medianBlur(domino, 3)
  frameThreshold = cv2.inRange(frameSmooth, (LH, LS, LV), (HH, HS, HV))
  # frameThreshold = cv2.inRange(frameHSL, (99, 96, 0), (157, 180, 255))
  kernel = np.ones((10,10),np.uint8)
  closing = cv2.morphologyEx(frameThreshold, cv2.MORPH_CLOSE, kernel)
  
  contours, hier = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(domino, contours, -1, (255, 255, 0), 4)
  cv2.imshow('Domino', domino)
  key = cv2.waitKey(30)
  if key == ord('q') or key == 27:
      break
