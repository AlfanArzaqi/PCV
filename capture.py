# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:30:19 2021

@author: Alfan
"""
import copy
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
n=0;
kernel = np.array([[1/9,1/9,1/9],
                   [1/9,1/9,1/9],
                   [1/9,1/9,1/9]])
while(True):
    
    ret, frame1 = cap.read()
    
    frame1 = np.double(cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY))/255;

    frame1 = cv2.filter2D(frame1,-1,kernel)
    if n==0:
        frame2=copy.copy(frame1);
        frame3=copy.copy(frame1);
        frame4=copy.copy(frame1);
        
    if n==0 :
        frame2=copy.copy(frame1)
        frame3=copy.copy(frame1)
        frame4=copy.copy(frame1)
    
    
    fr1=cv2.absdiff(frame1,frame2)
    fr2=cv2.absdiff(frame2,frame3)
    fr3=cv2.absdiff(frame3,frame4)
    fr =fr1+fr2+fr2
  #  fr[fr<0.2]=0
    
    n=1;
    
    frame4=copy.copy(frame3)
    frame3=copy.copy(frame2)
    frame2=copy.copy(frame1)
    # Display the resulting frame
    cv2.imshow('frame',fr)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()