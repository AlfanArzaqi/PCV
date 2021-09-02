# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 07:07:07 2021

@author: Alfan
"""

import cv2 as cv
import numpy as np

capture = cv.VideoCapture('vd.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroAllWindows