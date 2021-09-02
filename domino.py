import cv2
import numpy as np

def doNothing(x):
  pass

# window
cv2.namedWindow('Domino')

# Trackbar
cv2.createTrackbar('Low H', 'Domino', 99, 180, doNothing)
cv2.createTrackbar('High H', 'Domino', 157, 180, doNothing)
cv2.createTrackbar('Low L', 'Domino', 96, 255, doNothing)
cv2.createTrackbar('High L', 'Domino', 180, 255, doNothing)
cv2.createTrackbar('Low S', 'Domino', 0, 255, doNothing)
cv2.createTrackbar('High S', 'Domino', 19, 255, doNothing)

while True:
  LH = cv2.getTrackbarPos('Low H', 'Domino')
  HH = cv2.getTrackbarPos('High H', 'Domino')
  LL = cv2.getTrackbarPos('Low L', 'Domino')
  HL = cv2.getTrackbarPos('High L', 'Domino')
  LS = cv2.getTrackbarPos('Low S', 'Domino')
  HS = cv2.getTrackbarPos('High S', 'Domino')
  domino = cv2.imread("domino.jpg")
  frameSmooth = cv2.medianBlur(domino, 3)
  frameThreshold = cv2.inRange(frameSmooth, (LH, LL, LS), (HH, HL, HS))
#   frameThreshold = cv2.inRange(frameHSL, (99, 96, 0), (157, 180, 255))
  kernel = np.ones((10,10),np.uint8)
  closing = cv2.morphologyEx(frameThreshold, cv2.MORPH_CLOSE, kernel)
  
  contours, hier = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(domino, contours, -1, (255, 255, 0), 2)
  cv2.imshow('DominoS', frameSmooth)
  cv2.imshow('Domino', domino)
  key = cv2.waitKey(30)
  if key == ord('q') or key == 27:
  #if cv2.waitKey(20) & 0xFF==ord('d'):
      break